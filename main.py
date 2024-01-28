import names
import random
from tqdm import tqdm

classeListe = range(1, 6)
groupeListe = ['1A', '1B', '2A', '2B', '3A', '3B', '4A', '4B']

if __name__ == "__main__":
    inputNumber = input("Combien d'éléments voulez vous créer ? : ")
    fileName = input("Nom du fichier final : ")
    data = ""
    for i in tqdm(range(int(inputNumber))):
        firstName = names.get_first_name()
        lastName = names.get_last_name()
        classe = random.choice(classeListe)
        groupe = random.choice(groupeListe)
        data += lastName + "," + firstName + \
            "," + str(classe) + "," + groupe + "\n"

    f = open(fileName+".csv", "w")
    f.write(data)
    f.close()
