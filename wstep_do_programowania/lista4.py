#zad 1
def shift(list1, step):
    for i in range(0, step%len(list1)):
        temp = list1.pop(0)
        list1.append(temp)

list1 = [1, 2, 3, 4, 5, 6]
step = 3
shift(list1, step)
print("zad1:\n",list1)

#zad2
print("zad2:\nWieksze od K: ")
list2=["Bednarski", "Wojciechowski", "Pyka", "Wiench", "Adamiak"]
for i in range(0, len(list2)):
    if list2[i][0] > "K":
        print(list2[i])

print("Dluzsze niz 5: ")
for i in range(0, len(list2)):
    if len(list2[i]) > 5:
        print(sorted(list2)[i])

#zad3
waznosc_mleka=(8,5,2021)
karton_mleka={}
karton_mleka["data_waznosci"]=waznosc_mleka
karton_mleka["waga"]=2
karton_mleka["koszt"]=3
karton_mleka["marka"]="Laciate"
print("Data waznosci:", karton_mleka["data_waznosci"], "waga:", karton_mleka["waga"], "koszt:", karton_mleka["koszt"], "marka:", karton_mleka["marka"])
print("Koszt 6 kartonow mleka wynosi: ", karton_mleka["koszt"] * 6)

