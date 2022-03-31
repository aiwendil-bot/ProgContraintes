from recherche_k_dicho import recherche_dicho
import os
import csv
import time
from Modele_1 import satisfiabilite_model1
from Modele_2 import satisfiabilite_model2
from Modele_3 import satisfiabilite_model3
from parser import parser




nbAretes = 500

files = os.listdir("Instances")
os.remove("results.csv")
fichier = open("results.csv", "x")
writer = csv.writer(fichier)

for filename in files:
    file = open("Instances/"+filename, "r")
    file.readline()
    string = file.readline()
    #print(str)
    string = string.split()
    file.close()
    if int(string[2])<nbAretes:
        print("Execution de "+filename)
        print("Modele 1")
        ############MODELE 1####################
        start_time = time.time()
        satisfiabilite_model1("Instances/" + filename,"180")
        end_time = time.time()
        tempsM1 = end_time - start_time
        print("Modele 2")
        ############MODELE 2####################
        start_time = time.time()
        satisfiabilite_model2("Instances/"+filename,int((int(string[1])+1)/2),"180")
        end_time = time.time()
        tempsM2 = end_time - start_time
        print("Modele 3")
        ############MODELE 3####################
        start_time = time.time()
        satisfiabilite_model3("Instances/"+filename,int((int(string[1])+1)/2),"180")
        end_time = time.time()
        tempsM3 = end_time - start_time
        writer.writerow([filename , tempsM1, tempsM2, tempsM3 ])

fichier.close()







# files = os.listdir("Instances")
# os.remove("results.csv")
# fichier = open("results.csv", "x")
# writer = csv.writer(fichier)
#
# for filename in files:
#     file = open("Instances/"+filename, "r")
#     file.readline()
#     string = file.readline()
#     #print(str)
#     string = string.split()
#     file.close()
#     if int(string[2])<nbAretes:
#         print("Execution de "+filename+"\n")
#         start_time = time.time()
#         satisfiabilite_model2("Instances/"+filename,int(string[1])/2,"300")
#         end_time = time.time()
#         temps = end_time - start_time
#         print(temps)
#         temps = int(temps) + 5
#         print(temps)
#         temps = str(temps)
#         print(temps)
#         start_time_dicho = time.time()
#         k = recherche_dicho("Instances/"+filename, temps)
#         end_time_dicho = time.time()
#         temps_dicho = end_time_dicho - start_time_dicho
#         writer.writerow([filename , k, temps_dicho ])
#
# fichier.close()

