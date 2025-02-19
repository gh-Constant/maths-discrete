from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import json
import pandas as pd
import os
import time
from dotenv import load_dotenv

def scrape_csgo_skins():
    # Configuration de Selenium
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    try:
        print("Initialisation du navigateur...")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://csfloat.com/search")

        # Attendre que la page charge
        print("Attente du chargement de la page...")
        wait = WebDriverWait(driver, 20)
        items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "item-card")))

        results = []
        print(f"Nombre d'items trouvés: {len(items)}")

        # Limiter à 10 items pour le test
        for item in items[:10]:
            try:
                # Attendre que les éléments soient chargés
                time.sleep(1)  # Petit délai pour éviter la détection

                # Extraire les informations
                skin_info = {
                    "Skin": item.get_attribute("data-name") if item.get_attribute("data-name") else "N/A",
                    "Type_skin": item.get_attribute("data-weapon") if item.get_attribute("data-weapon") else "N/A",
                    "Usure": item.get_attribute("data-wear") if item.get_attribute("data-wear") else "N/A",
                    "Spécial": "Normal",  # Par défaut
                    "Patterne": item.get_attribute("data-float") if item.get_attribute("data-float") else "N/A",
                    "Prix": item.get_attribute("data-price") if item.get_attribute("data-price") else "N/A",
                    "photo": item.find_element(By.TAG_NAME, "img").get_attribute("src") if item.find_elements(By.TAG_NAME, "img") else "N/A"
                }

                # Vérifier les attributs spéciaux
                if "StatTrak" in item.text:
                    skin_info["Spécial"] = "StatTrak"
                elif "Souvenir" in item.text:
                    skin_info["Spécial"] = "Souvenir"

                results.append(skin_info)
                print(f"Item scrapé: {skin_info['Type_skin']} | {skin_info['Skin']}")

            except Exception as e:
                print(f"Erreur lors du scraping d'un item: {str(e)}")
                continue

        # Sauvegarder les résultats
        if results:
            # Conversion en DataFrame
            df = pd.DataFrame(results)
            
            # Sauvegarde en CSV
            df.to_csv('csgo_skins.csv', index=False, encoding='utf-8')
            print(f"\nScraping réussi pour {len(results)} items")
            
            # Sauvegarde en JSON
            with open('csgo_skins.json', 'w', encoding='utf-8') as f:
                json.dump(results, f, indent=2, ensure_ascii=False)
        else:
            print("Aucun résultat trouvé")

    except Exception as e:
        print(f"Une erreur est survenue: {str(e)}")
    
    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    scrape_csgo_skins()