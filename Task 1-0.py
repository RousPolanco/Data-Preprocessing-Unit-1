import csv

def import_csv (filename):
    with open (filename, 'r') as file:
        reader = csv.DictReader (file)
        data = [row for row in reader]
    return data

student_data = import_csv ('C:/Users/cesar/OneDrive/Documents/Arturo/3rd Quarter/Proof CSV')
print (student_data)