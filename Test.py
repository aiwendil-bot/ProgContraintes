from recherche_k_dicho import recherche_dicho
import os
import csv

nbAretes = 500

files = os.listdir("Instances")
os.remove("results.csv")
fichier = open("results.csv", "x")
writer = csv.writer(fichier)

for filename in files:
    file = open("Instances/"+filename, "r")
    file.readline()
    str = file.readline()
    #print(str)
    str = str.split()
    file.close()
    if int(str[2])<nbAretes:
        print("Execution de "+filename+"\n")
        k = recherche_dicho("Instances/"+filename)
        writer.writerow([filename , k])

fichier.close()




