import sys
import os

# tri nacina da se programu daju neki ulazni podaci

# 1 - kroz standardni ulaz (komandnu liniju)

'''path = input("unesite putanju do fajla:")
print(path)'''

# 2 - kroz parametre u komandnoj liniji
# da bi ovo radilo, udjes u folder gde je ovaj fajl
# i ukucas python env.py neki_parametar
print(len(sys.argv))

if len(sys.argv) > 1:
    print(sys.argv[0])  # env.py
    print(sys.argv)  # prvi parametar
    # itd
else:
    print("Niste zadali parametre")

# 3 - environment variables

path_env = os.environ["BAKIR_CAR"]
print(path_env)

# 4 - cuvas sve u fajlu, pa citas iz fajla
# domaci
