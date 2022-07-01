import os, sys
from Bio import SeqIO

# Para correr: python3 mapfile.py Pgenelist.txt PberProteinsList.csv

# Abre los 2 archivos que se ponen y los lee
seqtreelist = open(sys.argv[1], "r").readlines()
listaespecie = open(sys.argv[2], "r").readlines()

# Le doy una variable a cada item en una fila separados por comas
for linea in seqtreelist:
	gfname = (linea.split(",")[0]).strip()
	seqname = (linea.split(",")[1]).strip()
	
	# Defino la especie (código de 10) y el nombre de la proteina a partir de seqname
	especie = (seqname[:10]).strip()
	proteina = (seqname[11:]).strip()

# 	print(proteina + ", " + gfname)

# Le doy una variable a cada item en una fila separados por comas 
	for rec in listaespecie:
		chromosome = (rec.split(",")[0]).strip()
		start_locus = (rec.split(",")[1]).strip()
		end_locus = (rec.split(",")[2]).strip()			
		tag_locus = (rec.split(",")[3]).strip()
				
# Creé un diccionario con gfname y proteina (No logré hacerlo funcionar con esto tampoco)
		seqtree_dic = {}
		for i in seqtreelist:
			seqtree_dic[proteina] = gfname		
		
		newlist_dic = {}
		notree_dic = {}
		for a in listaespecie:
			if tag_locus not in seqtree_dic.keys():
				notree_dic[tag_locus] = "no_tree"
# 		
# 		for key, value in seqtree_dic.items():
# 			print(key, ", ", value)
		for k, v in notree_dic.items():
			print(k, ", ", v)
		
		
# 		# Para que solo analice las proteinas de Plasmodium berghei
# 		if especie == "Ap_ca_Pber":
# 			
# 			# Si tag_locus es igual a proteina que imprima "tag_locus, gfname"
# 			# Si corro este if sin el "else", funciona
# 			if tag_locus == proteina:
# 				print(tag_locus + "," + gfname)	
# 			
# 			# Si tag_locus no coincide con proteina que imprima "tag_locus has no tree"
# 			else:
# 				print(tag_locus + ", no_tree")


# Lo de abajo es para generar el mapping file con las columnas que son 
# Lo estoy probando con lo de arriba para asegurarme de que funcione primero				

# 					if chromosome == "chromosome 1":
# 						print("chrI" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 2":
# 						print("chrII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 3":
# 						print("chrIII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 4":
# 						print("chrIV" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 5":
# 						print("chrV" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 6":
# 						print("chrVI" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 7":
# 						print("chrVII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 8":
# 						print("chrVIII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 9":
# 						print("chrIX" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 10":
# 						print("chrX" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 11":
# 						print("chrXI" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 12":
# 						print("chrXII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 13":
# 						print("chrXIII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					if chromosome == "chromosome 14":
# 						print("chrXIV" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + gfname)
# 					continue
					
# 				if proteina != tag_locus:
# 					if chromosome == "chromosome 1":
# 						print("chrI" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 2":
# 						print("chrII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 3":
# 						print("chrIII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 4":
# 						print("chrIV" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 5":
# 						print("chrV" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 6":
# 						print("chrVI" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 7":
# 						print("chrVII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 8":
# 						print("chrVIII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 9":
# 						print("chrIX" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 10":
# 						print("chrX" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 11":
# 						print("chrXI" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 12":
# 						print("chrXII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 13":
# 						print("chrXIII" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")
# 					if chromosome == "chromosome 14":
# 						print("chrXIV" + "," + start_locus + "," + end_locus + "," + tag_locus + "," + "no_tree")	
