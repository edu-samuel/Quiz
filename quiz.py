namn=input("Hej vad heter du?")
print(f"Hej {namn} och vällkommen till spelet")

import random
hemligt_tal1 = random.randint(1, 10)
for försök in range(1,4):
    gissnings_tal = int(input(f"Försök {försök}: Gissa ett tal mellan 1 och 10: "))
    
    if gissnings_tal == hemligt_tal1:
        print("Din gissning är rätt!")
        break
    else:
        print("Det är fel")
else:
    print(f"Tyvärr, det var {hemligt_tal1}")