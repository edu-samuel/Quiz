#1-hälsning
namn=input("Hej vad heter du?")
print(f"Hej {namn} och vällkommen till spelet")

import random
hemligt_tal= random.randint(1,10)
gissning=int(input("Gissa ett tal mellan 1 och 10:"))
if gissning==hemligt_tal:
    print("Din gissning är rätt")
else:
    print(f"tyvärr, det var {hemligt_tal}")
