from utils import randomiser_tall, print_resultat, hent_bruker_input

riktig_tall  = randomiser_tall(1,10)
antall_gjett = 0

while True:

    gjettet_tall = hent_bruker_input("Gjett et tall mellom 1,10")
    antall_gjett = antall_gjett + 1
    
    if gjettet_tall < riktig_tall:
        print("høyere")

    if gjettet_tall > riktig_tall:
        print("lavere")
        
    if gjettet_tall == riktig_tall:
    	break

print_resultat(riktig_tall, gjettet_tall, antall_gjett)