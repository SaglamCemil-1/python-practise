import csv

name = input("name: ")
home = input("home: ")

with open("csv1.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name,home])