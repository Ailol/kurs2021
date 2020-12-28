import random as rand

def hent_bruker_input(tekst):
	return int(input(tekst))

def randomiser_tall(n1, n2):
	return rand.randint(n1,n2)

def print_resultat(g1,g2,g3):
	print("\n")
	print("Du traff, tallet var: " , g1)
	print("Ditt tall: " , g2)
	print("Antall forsøk: ",g3) 
	print("\n")


def andregradsligning(a, b, c, x):
    return a*x**2 + b*x + c
    
