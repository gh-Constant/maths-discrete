import numpy as np
import matplotlib.pyplot as plt
from math import isinf, isnan

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

def graphique(suite, nmin, nmax, pas):
    
    x = list(range(nmin, nmax + 1, pas))
    y = [suite(n) for n in x]
    
    plt.figure(figsize=(12, 8))
    
    plt.scatter(x, y, marker='o', color='#2E86C1', alpha=0.6, s=50)

    plt.xlabel('n', fontsize=12, fontweight='bold')
    plt.ylabel('u(n)', fontsize=12, fontweight='bold')
    plt.title('Évolution de la suite u₁', fontsize=14, pad=15)
    

    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    
    plt.show()

def f(x):
  return 0.5 * x + 2123.56

def random_color():
    return '#{:06x}'.format(random.randint(0, 0xFFFFFF))


def convergence(fonction_f, x0, rang, xmin, xmax, pas):
    # Create x values strictly within the specified range
    tabx = []
    x = xmin
    while x <= xmax:
        tabx.append(x)
        x += pas
    
    plt.plot(tabx, tabx, 'r--', label='y=x')
    
    taby = [fonction_f(x) for x in tabx]
    plt.plot(tabx, taby, 'b-', label='f(x)')
    
    points_x = [x0]
    points_y = [0] 
    current_x = x0
    
    for i in range(rang):
        points_x.extend([current_x, current_x])
        next_y = fonction_f(current_x)
        points_y.extend([points_y[-1], next_y])
        
        next_x = next_y 
        points_x.extend([current_x, next_x])
        points_y.extend([next_y, next_y])
        
        current_x = next_x
    
    plt.plot(points_x, points_y, 'g-', label='Iterations')
    
    plt.legend()
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Convergence Analysis')

    
    plt.show()


def graphique_multiple(suites, nmin, nmax, pas):
    x = list(range(nmin, nmax + 1, pas))
    
    plt.figure(figsize=(12, 8))
    
    for i, suite in enumerate(suites):
        y = [suite(n) for n in x]
        color = random_color()
        plt.scatter(x, y, marker='o', alpha=0.6, s=50, label=f'u{i+1}(n)', color=color)

    plt.xlabel('n', fontsize=12, fontweight='bold')
    plt.ylabel('u(n)', fontsize=12, fontweight='bold')
    plt.title('Comparaison des suites', fontsize=14, pad=15)
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    
    plt.show()

def funcF(x):
    return x * (1 - x)

def u2_iteratif(n):
  u = 2.56453
  for i in range(n):
    u = 0.9972 * u + i ** 2
  return u

def f(x):
  return 0.5 * x + 2123.56


def convergence(f, u0, rang, xmin, xmax, pas):
    tabx = []
    taby = []
    x = xmin
    while x < xmax:
        tabx.append(x)
        x += pas
    plt.plot(tabx, tabx)
    for x in tabx:
        taby.append(f(x))
    plt.plot(tabx, taby)
    tabx = []
    taby = []
    u = u0
    for i in range(rang):
        tabx.append(u)
        taby.append(f(u))
        tabx.append(f(u))
        taby.append(f(u))
        u = f(u)
    plt.plot(tabx, taby)
    plt.grid()
    plt.show()

convergence(f, 0, 100, 0, 5000, 100)