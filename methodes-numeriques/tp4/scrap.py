import requests
from bs4 import BeautifulSoup
import json
import os
import asyncio
import aiohttp
from typing import List, Dict, TypedDict, Set
import async_timeout
from pathlib import Path
import time

SEDNA_BASE = 'https://sedna.univ-fcomte.fr/jsp/custom/ufc'
MAIN_URL = f'{SEDNA_BASE}/mselect.jsp'
SCRIPT_DIR = Path(__file__).parent
OUTPUT_FILE = SCRIPT_DIR / 'output.ts'
STOP_TEXT = "Note : Vous pouvez mettre cette page en signet pour un accès direct ultérieur"
MAX_RETRIES = 3
RETRY_DELAY = 1  # seconds

class SednaPage(TypedDict):
    name: str
    url: str
    subpages: List['SednaPage']

async def get_soup(session: aiohttp.ClientSession, url: str, retry_count: int = 0) -> BeautifulSoup:
    """Make async request and return BeautifulSoup object with retry logic"""
    try:
        async with async_timeout.timeout(10):
            async with session.get(url) as response:
                if response.status == 200:
                    html = await response.text()
                    return BeautifulSoup(html, 'html.parser')
                elif retry_count < MAX_RETRIES:
                    print(f"Request failed with status {response.status}, retrying in {RETRY_DELAY} seconds...")
                    await asyncio.sleep(RETRY_DELAY)
                    return await get_soup(session, url, retry_count + 1)
                else:
                    print(f"Failed to fetch {url} after {MAX_RETRIES} retries")
                    return None
    except Exception as e:
        if retry_count < MAX_RETRIES:
            print(f"Error fetching {url}: {str(e)}, retrying in {RETRY_DELAY} seconds...")
            await asyncio.sleep(RETRY_DELAY)
            return await get_soup(session, url, retry_count + 1)
        print(f"Error fetching {url}: {str(e)} after {MAX_RETRIES} retries")
        return None

def save_as_typescript(data: List[SednaPage]):
    """Save data as TypeScript interface and constant"""
    try:
        typescript_content = """// Generated by scraping script
export interface SednaPage {
    name: string;
    url: string;
    subpages: SednaPage[];
}

export const sednaData: SednaPage[] = """

        # Convert to TypeScript-compatible JSON
        json_str = json.dumps(data, ensure_ascii=False, indent=2)
        typescript_content += f"{json_str};\n"
        
        with OUTPUT_FILE.open('w', encoding='utf-8') as f:
            f.write(typescript_content)
            print(f"Saved TypeScript data to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error saving TypeScript file: {str(e)}")

async def scrape_page(session: aiohttp.ClientSession, url: str, depth: int = 0, processed_urls: Set[str] = None) -> List[SednaPage]:
    """
    Scrape a page and its subpages recursively
    Returns a list of dictionaries containing page info and their subpages
    """
    if processed_urls is None:
        processed_urls = set()
    
    print(f"{'  ' * depth}Scraping: {url}")
    
    soup = await get_soup(session, url)
    if not soup:
        return []
    
    pages = []
    tasks = []
    
    if STOP_TEXT in soup.text:
        print(f"{'  ' * depth}Found stop text, skipping further scraping")
        return []
    
    for link in soup.find_all('a', href=True):
        href = link['href']
        text = link.text.strip()
        
        # Skip unwanted links
        if text == 'Retour' or not text:
            continue
            
        if href.startswith(('mplanif.jsp?id=', 'mselect.jsp?id=', 'mselect.jsp')):
            # Handle root level links without id parameter
            if href == 'mselect.jsp':
                full_url = f'{SEDNA_BASE}/{href}'
            else:
                full_url = f'{SEDNA_BASE}/{href}'
                
            print(f"{'  ' * depth}Found: {text}")
            
            page_info: SednaPage = {
                'name': text,
                'url': full_url,
                'subpages': []
            }
            pages.append(page_info)
            
            # Create task for scraping subpages - now we scrape everything
            # We'll process URLs even if we've seen them before
            task = asyncio.create_task(scrape_page(session, full_url, depth + 1, processed_urls))
            tasks.append((page_info, task))
            processed_urls.add(full_url)
    
    # Wait for all subpage scraping tasks to complete
    for page_info, task in tasks:
        try:
            page_info['subpages'] = await task
        except Exception as e:
            print(f"Error in subpage task: {str(e)}")
            page_info['subpages'] = []
    
    # Save progress after each main category
    if depth == 0:
        save_as_typescript(pages)
    
    return pages

async def main_async():
    try:
        print('Starting Sedna hierarchical scraping from main page...')
        
        # Use connection pooling and keep-alive with increased limits
        conn = aiohttp.TCPConnector(limit=5)  # Reduced concurrent connections to avoid overwhelming server
        timeout = aiohttp.ClientTimeout(total=120)  # Increased timeout for deeper scraping
        async with aiohttp.ClientSession(connector=conn, timeout=timeout) as session:
            # Start scraping from main page
            hierarchy = await scrape_page(session, MAIN_URL)
            
            # Final save
            save_as_typescript(hierarchy)
        
        print(f'\nScraping completed. Data saved to {OUTPUT_FILE}')
        
    except Exception as e:
        print(f'Error occurred: {str(e)}')

def main():
    asyncio.run(main_async())

if __name__ == '__main__':
    main()