import csv

passwords = {}

with open('correct.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for line in csv_reader:
        passwd = line[0]
        user = line[1]
        passwords[user] = passwd
file.close()

with open('correct.txt', 'w') as file:
    for key in passwords:
        file.write("%s:%s\n"%(key, passwords[key]))
