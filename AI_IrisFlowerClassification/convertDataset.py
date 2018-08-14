import csv

new_dataset = []

# Loading the original dataset
dataset = open('datasetOriginal.csv', 'r')
reader = csv.reader(dataset)
for row in reader:
    del row[0]
    print(row)
    new_dataset.append(row)
dataset.close()

# Creating new dataset
dataset2 = open('datasetNew.csv', 'w', newline='')
writer = csv.writer(dataset2)
writer.writerows(new_dataset)
dataset2.close()
