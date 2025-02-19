import math

# ----- Question 1 : u1 -----

printu1 = {
   "print1": False,
   "print2": False,
   "print3": False,
   "print4": False,
   "print5": False,
   "print6": False,
   "print7": False,
   "print8": True,
   "print9": False, 
   "print10": False,
}

def u1_iteratif(n):
  u = 2.56453
  for i in range(n):
    u = 0.9972 * u + 2123.56
  return u

def u1_recursif(n):
  if n == 0:
    return 2.56453
  return 0.9972 + u1_recursif(n - 1) + 2123.56

# Test de la question 1

if printu1["print1"] == True:
    # Test de la valeur initiale

    print(u1_iteratif(0)) # 2.56453
    print(u1_recursif(0)) # 2.56453

    print(u1_iteratif(1)) # 2127.12173
    print(u1_recursif(1)) # 2127.12173

    print(u1_iteratif(2)) # 4251.67893
    print(u1_recursif(2)) # 4251.67893

    print(u1_iteratif(3)) # 6376.236129999999
    print(u1_recursif(3)) # 6376.236129999999
    
if printu1["print2"] == True:
   # Test croissance

    for i in range(101):
        print("Rang ", i, " : ", u1_iteratif(i))

    # On constate que la suite semble être strictement croissante de 0 à 100 (demarrage trés rapide) (2.56453 -> 212458.2845300002)

if printu1["print3"] == True:
    # Test de la convergence

    i = 11000
    while (u1_iteratif(i) != u1_iteratif(i+1)):
        i += 1
    print("Rang ", i, " : ", u1_iteratif(i))

    # Rang  11096  :  758414.2857142782


def u2_iteratif(n):
  u = 2.56453
  for i in range(1, n+1):
    u = 0.9972 * u + i ** 2
  return u

def u2_recursif(n):
  if n == 0:
    return 2.56453
  return 0.9972 * u2_recursif(n - 1) + (n)** 2

def u3_iteratif(n):
   if n == 0:
      return 0
   a,b = 0,1
   for i in range(n-1):
      c = a+b
      a = b
      b = c
   return b

# TODO : JAMAIS DE RECURSION DOUBLE
def u3_recursif(n):
   
   def u3_fainter(n):
      if(n == 1):
         return 0,1
      else:
         a,b = u3_fainter(n-1)
         return b, a+b
   if n == 0:
      return 0
   if n == 1: 
      return 1
   return u3_fainter(n)[1]

def uv_iteratif(n):
   u,v = 1000000000,1
   if n == 0:
      return u,v
   for i in range(n):
      lastu = u
      u = (lastu + v) / 2
      v = 2*lastu*v/(lastu+v)
   return u,v

def uv_recursif(n):
   if n == 0:
      return 2,1
   else:
      u,v = uv_recursif(n-1)
      return (u+v)/2, 2*u*v/(u+v)

if printu1["print4"] == True:
    # Test de la valeur initiale

    print(u2_iteratif(0)) # 2.56453
    print(u2_recursif(0))
    
    print(u2_iteratif(1)) # 2.56453
    print(u2_recursif(1))

    print(u2_iteratif(2)) # 2.56453$
    print(u2_recursif(2))

    print(u2_iteratif(3))

    # Rang  0  :  0
    # Rang  1  :  1
    # Rang  2  :  1
    # Rang  3  :  2
    # Rang  4  :  3
    # Rang  5  :  5
    # Rang  6  :  8
    # Rang  7  :  13

    print(u2_recursif(2))

if printu1["print5"] == True:
   
   for i in range(0, 100):
      print("Rang ", i, " : ", u2_iteratif(i))

    ## strictement croissante aprés le terme 1 

if printu1["print6"] == True:
    for i in range(0, 8):
        print("Rang ", i, " : ", u3_iteratif(i))

    for i in range(0, 800):
        print("Rang ", i, " : ", u3_recursif(i))

if printu1["print7"] == True:

    for i in range(0, 100):
        print("Rang ", i, " : ", uv_iteratif(i))

    # Rang  0  :  (2, 1)
    # Rang  1  :  (1.5, 1.3333333333333333)
    # Rang  2  :  (1.4166666666666665, 1.411764705882353)

    for i in range(0, 100):
      print("Rang ", i, " : ", uv_recursif(i))


    # Rang  0  :  (2, 1)
    # Rang  1  :  (1.5, 1.3333333333333333)
    # Rang  2  :  (1.4166666666666665, 1.411764705882353)

    # On constate que le u est strictement décroissant et le v est strictement croissant et ils convergent vers la même valeur au 5eme terme

    #https://fr.wikipedia.org/wiki/Algorithme_de_calcul_de_la_racine_n-i%C3%A8me

if printu1["print8"] == True:
   
   # Converge vers le nombre d'or aprés 40 itérations

   for i in range(0, 100):
      if i == 0:
         print("0")
      else:
         print("Rang ", i, " : ", u3_iteratif(i+1) / u3_iteratif(i))

