import ast
handle=open("assemble_output.txt","r")
in_map=False
for line in handle:
	line=line.strip()
	#find the line that records the em map
	if line.find(".mrc")!=-1:
		current_map = line
		in_map = True
		sorted_dict = {}
	elif line.find("[")!=-1:
		current_group = line
		new_dict={}
	elif line.find("{")!=-1:
		dict_vol= ast.literal_eval(line)
		lst_vol = dict_vol.values()
		lst_vol=list(lst_vol)
		lst_vol.sort()
		lst_vol.reverse()
		if lst_vol!=[]:
			count=0
			last_vol=lst_vol[0]
			for vol in lst_vol:
				if count<3:
					for item in dict_vol:
						if dict_vol[item]==vol:
							new_dict[item]=vol
				count+=1
				last_vol=vol
				if count>3 and vol!=last_vol:
					break
		#delete groups that are impossible to make up target volume
		if new_dict!={}:
			sorted_dict[current_group]=new_dict

	elif line=="" or line=="end":
		print(current_map)
		print(sorted_dict)


		

handle.close()