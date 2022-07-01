import os, sys
from Bio import SeqIO

# Para correr: python3 mapfile.py Genelist.txt ProteinList.csv

# Abre los 2 archivos que se ponen y los lee
listagenes = open(sys.argv[1], "r").readlines()
listaespecie = open(sys.argv[2], "r").readlines()


gene_list_dir = {} # MACR - esta variable se declara antes de que inicies el loop. De lo contrario, cada que agregue un valor se re-inicia
# Le doy una variable a cada item en una fila separados por comas
for linea in listagenes:
# Para que solo analice las proteinas de Plasmodium berghei
	gfname = (linea.split(",")[0]).strip()
	seqname = (linea.split(",")[1]).strip()			
	# Defino la especie (código de 10) y el nombre de la proteina a partir de seqname
	especie = (seqname[:10]).strip()
	proteina = (seqname[11:]).strip()
	# Creo un diccionario con proteina as keys and gfname as values 		
	gene_list_dir[proteina] = gfname


especies_list_dir = {} # MACR -- Acá puedes hacer lo mismo, pero con el otro archivo
# Le doy una variable a cada item en una fila separados por comas --- MACR: Este es el archivo que tienes que iterar 
for rec in listaespecie:
	chromosome = (rec.split(",")[0]).strip()
	start_locus = (rec.split(",")[1]).strip()
	end_locus = (rec.split(",")[2]).strip()			
	tag_locus = (rec.split(",")[3]).strip()			
	
	# Si tag_locus es igual a proteina que imprima "tag_locus, gfname"
	if tag_locus in gene_list_dir.keys():
# 		print(chromosome + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])	# MACR ---- Imprime más completo

		if chromosome == "1":
			print("chr1" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "2":
			print("chr2" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "3":
			print("chr3" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "4":
			print("chr4" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "5":
			print("chr5" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "6":
			print("chr6" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "7":				
			print("chr7" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "8":
			print("chr8" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "9":
			print("chr9" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "10":
			print("chr10" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "11":
			print("chr11" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "12":
			print("chr12" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "13":
			print("chr13" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "14":
			print("chr14" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])
		if chromosome == "Not Assigned":
			print("no_chr" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gene_list_dir[tag_locus])


	# Si tag_locus no coincide con proteina que imprima "tag_locus has no tree"
	else:
# 		print(chromosome + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")   # MACR --- Imprime más completo
				
		if chromosome == "1":
			print("chr1" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "2":
			print("chr2" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "3":
			print("chr3" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "4":
			print("chr4" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "5":
			print("chr5" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "6":
			print("chr6" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "7":				
			print("chr7" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "8":
			print("chr8" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "9":
			print("chr9" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "10":
			print("chr10" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "11":
			print("chr11" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "12":
			print("chr12" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "13":
			print("chr13" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "14":
			print("chr14" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
		if chromosome == "Not Assigned":
			print("no_chr" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
