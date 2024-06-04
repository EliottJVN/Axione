import openpyxl

# Nom du fichier Excel (ajustez selon le nom réel de votre fichier)
file_name = 'exc_file.xlsx'

# Chargement du classeur
workbook = openpyxl.load_workbook(file_name)

# Sélection de la feuille active (vous pouvez également sélectionner une feuille spécifique)
sheet = workbook.active

# Lecture de la valeur de la cellule A2
cell_value = sheet['A2'].value

# Affichage de la valeur
print(f"La valeur de la cellule A2 est : {cell_value}")
