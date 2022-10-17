# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.

def getFruits(letter, listNames):
    listFruits = []
    for i, values in enumerate(listNames):
        if str.upper(letter) == str.upper(listNames[i][0]):
            listFruits.append(listNames[i])
    return listFruits   
    
firstLetter = input("Введите первую букву названия фрукта: ")

with open("fruits.txt", "r") as f:
    namesOfFruits = f.read()
listNames = namesOfFruits.split(", ")

print(getFruits(firstLetter, listNames))

