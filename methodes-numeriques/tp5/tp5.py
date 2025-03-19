from math import *
import matplotlib.pyplot as plt
import numpy as np

def funcF(x):
    return x**5 - 3*x**4 + 2*x**3 + 5*x**2 - 7*x + 2

def g(x):
    return x * sin(x)

def h(x):
    return sin(1/x)

def z(x):
    return exp(-(x - 5.456454)**2 / 2) + exp(-(x - 58.34523)**2 / 2)

def find_zero(f, xmin, xmax):
    compteur = 0
    seuil = 0.000000000001
    x = 0
    
    while xmax - xmin > seuil:
        x = (xmax + xmin) / 2
        compteur += 1
        if np.sign(f(x)) == np.sign(f(xmin)):
            xmin = x
        else:
            xmax = x
    
    return x



def max(f, xmin, xmax):
    def df(x):
        h = 0.000000001
        return (f(x + h) - f(x)) / h
    x = find_zero(df, xmin, xmax)
    return x, f(x)

def test(x):
    return x * (1 - x)    



def affiche(f, xmin, xmax, pas):

    x = np.arange(xmin, xmax, pas)
    
    y = []
    for xi in x:
        try:
            yi = f(xi)
            if not (isinf(yi) or isnan(yi)):  
                y.append(yi)
            else:
                y.append(None)
        except:
            y.append(None)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'b-', label=f.__name__)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Graph of function {f.__name__}')
    plt.legend()
    plt.show()

#def test(x):
 #   return (x**2)-2



# t,b = zero(f, -5, 0)
# t2,b2 = zero(f, 0, 0.75)
# t3,b3 = zero(f, 0.75, 1.5)
# print(f(1))

print(max(funcF, -1.5, -0.5))
print(max(funcF, 0, 1)) 
print(max(funcF, 1.5, 2))

# (-0.8794637798810072, 8.342244045234905) maximum
# (0.6967907957396164, -0.31626933671486945) MINImum

# print(f"La première racine de f est approximativement {t} (trouvée en {b} itérations)")
# print(f"La deuxième racine de f est approximativement {t2} (trouvée en {b2} itérations)")
# print(f"La troisième racine de f est approximativement {t3} (trouvée en {b3} itérations)")



#affiche(f, -1.5, 2, 0.1)
# Resultat (coupe 3 fois en 0) 
# [fGraphTP5.png]

# affiche(g, -250, 250, 2.5)
# Resultat (coupe 2 fois en 0) 
# [gGraphTP5.png]

# affiche(h, -0.01, 0.01, 0.000000001)
# Oscille de plus en plus en arriant à 0 
# [hGraphTP5_1.png] 
# [hGraphTP5_2.png]

#affiche(z, -10, 63, 0.01)
# Resultat (Affiche 2 pics de gaus) 
# [zGraphTP5_2.png]

