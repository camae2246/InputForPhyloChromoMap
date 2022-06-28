f = open("/Users/camae/Thesis/All_Results/Database/NewSGDtrees/newDtrees_info.txt", "r").readlines()
fn = open("/Users/camae/Thesis/All_Results/Database/NewSGDtrees/improvisando", "w")
for i in f:
	i = i.strip()
	codigo = i.split("\t")[0]
	nombres = (i.split("\t")[1]).split(",")
	for nombre in nombres:
		print(codigo + "," + (nombre.split(":")[0]).replace("(", ""))
		
	