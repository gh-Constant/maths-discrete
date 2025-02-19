import matplotlib.pyplot as plt
import seaborn as sns  # Add this import at the top
import random
import math
def u1_iteratif(n): # F
  u = 2.56453
  for i in range(n):
    u = 0.9972 * u + 2123.56
  return u

def u2_iteratif(n):
  u = 2.56453
  for i in range(n):
    u = 0.9972 * u + i ** 2
  return u

def u3_iteratif(n):
   if n == 0:
      return 0
   a,b = 0,1
   for i in range(n-1):
      c = a+b
      a = b
      b = c
   return b

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
    
    # Plot each suite with a different color
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

def v(x):
    return math.cos(x)

def w(x):
    return -x**2 + 4

def z(x):
    return 3 / (x**2 + 1)

if __name__ == "__main__":
    #graphique(u1_iteratif, 0, 12000, 150)   
    # Le graphique suggère une divergence exponentielle

    #graphique(u2_iteratif, 0, 30000, 600)
    # Le graphique suggère une divergence quadratique

    #graphique(u3_iteratif, 0, 25, 1)
    # Le graphique suggère une divergence exponentielle

    #graphique_multiple([u1_iteratif, u2_iteratif, u3_iteratif], 0, 25, 1)  

    #convergence(f, 4500, 50, 0, 10000, 100)  # Adjusted parameters for better visibility
    # Si u0 est inférieur à 4247.12, la suite converge vers 4247.12 et est strictement croissante
    # Si u0 est supérieur à 4247.12, la suite converge vers 4247.12 et est strictement décroissante

    #convergence(v, 50, 200, 0, 1, 0.01)  # Modifié pour zoomer sur la zone d'intérêt
    # Si v0 = 0,74 alors v converge vers 0,7390851332151607
    # Sinon v converge en oscillant (oscillations)``

    #convergence(w, 0.0, 3, -3, 3, 0.01)
    # Si w0 = -1 + sqrt(17) / 2 alors w converge vers -1 + sqrt(17) / 2
    # Sinon w converge vers 1.75 en oscillant

    #convergence(z, 0, 100, 0, 10, 0.5)
    # Si z0 = 1.2134 alors z est constante
    # Sinon z converge vers 1.6 en oscillant, z se dirige vers un régime d'oscillations stables
    
    g = 0
    for i in range(100):
        g = z(g)
    print(g)
    
    