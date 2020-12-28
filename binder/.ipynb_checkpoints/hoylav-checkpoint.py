import random

riktig_tall  = random.randint(1,2)

antall_gjett = 0

while True:

    gjettet_tall = int(input("Gjett et tall: "))
    antall_gjett += 1
    
    if gjettet_tall < riktig_tall:
        print("høyere")

    if gjettet_tall > riktig_tall:
        print("lavere")
    
    else:
    	break

    
print("Du traff, tallet var: " , riktig_tall)
print("Ditt tall: " , gjettet_tall)
print("Antall forsøk: ",antall_gjett) 


