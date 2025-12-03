import random

salajane_arv = random.randint(0, 100)

print("Arvu arvamise mäng!")
print("Arvuti mõtles välja arvu 0 kuni 100. Proovi ära arvata!")

while True:
    offer = int(input("Sinu pakkumine: "))

    if offer < salajane_arv:
        print("Liiga väike! Proovi suuremat arvu.")
    elif offer > salajane_arv:
        print("Liiga suur! Proovi väiksemat arvu.")
    else:
        print("Õige! Arv oli", salajane_arv)
        break
