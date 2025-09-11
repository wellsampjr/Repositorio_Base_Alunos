import csv

with open('lista_de_compras.tsv', 'w', newline='', encoding='utf-8') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter='\t', lineterminator='\n')

    csvWriter.writerow(['Maças','Bananas','Morangos'])
    csvWriter.writerow(['Leite','Iogurte','Queijo'])
    csvWriter.writerow(['Sabão','Detergente','Amaciante'])