import itertools
#determine the minimum key value pair of a dictionary
def min_dict(dict_input, output_type):
	key_list=list(dict_input)
	first_key = key_list[0]
	first_value = dict_input[first_key]
	min_val = first_value
	min_key = first_key
	for key in dict_input:
		if dict_input[key]< min_val:
			min_val = dict_input[key]
			min_key = key

	if output_type == "key":
		return min_key
	elif output_type == "value":
		return min_val
	return

#this is the composition where there's the most smallest subunits
def max_comp(volume_data, vol_limit, output_type):
	min_subunit = min_dict(volume_data,"key")
	min_subunit_vol = min_dict(volume_data,"value")
	rest_subunit_vol = sum(volume_data.values()) - min_subunit_vol
	flag = False
	count = 0
	while flag == False:
		count += 1
		total_vol= rest_subunit_vol + count*(min_subunit_vol)
		if total_vol > vol_limit:
			flag = True
			count-=1
		elif total_vol == vol_limit:
			flag = True

	if output_type == "comp":
		min_composition = {}
		for key in volume_data:
			if key != min_subunit:
				min_composition[key]=1
			elif key == min_subunit:
				min_composition[key]=count
		return min_composition
	elif output_type == "vol":
		return rest_subunit_vol + min_subunit_vol*count
	elif output_type == "num":
		return count+len(volume_data.keys())-1


def main():
	protein_groups= [["A","B"], ["C","D"], ["E","F","G"], ["H","I","J","K","L"]]
	em_volume = {"EM1":10, "EM2":12, "EM3":17, "EM4":25}
	subunit_volume = {"A":4, "B":2, "C":7, "D":5, "E":3, "F":1, "G":8, "H":0.5, "I":1.5, "J":6, "K":3.5, "L":4.5}

	#determine order of em map by acsending order
	lst_em_vol = list(em_volume.values())
	lst_em_vol.sort()
	lst_em_vol.reverse()
	lst_em =[]
	#fix this such that if em_volume have two em map with the same volume, it will still work
	for vol in lst_em_vol:
		for key in em_volume:
			if em_volume[key] == vol:
				lst_em.append(key)


	#determine all possible combination for the largest em volume
	combo_cache={}
	largest_em = lst_em[0]
	em_map_vol = em_volume[largest_em]
	for current_group in protein_groups:

		max_total=max_comp(subunit_volume,em_map_vol,"num")
		max_total=max_total-len(current_group)+1

		iter1 = itertools.product(range(max_total),repeat=len(current_group))
		tup_iter=tuple(iter1)
		lst_tup = []
		for tup in tup_iter:
			flag=True
			for num in tup:
				if num == 0:
					flag = False
			if flag == True:
				lst_tup.append(tup)
			else:
				flag = True

		new_dict= {}
		for t in lst_tup:
			tup_new=tuple(itertools.permutations(t,len(current_group)))
			for k in tup_new:
				if k not in new_dict:
					total=0
					for index in range(len(k)):
						curr_subunit = current_group[index]
						total+= k[index]*subunit_volume[curr_subunit]
					if total<= em_map_vol:
						new_dict[k] = total
		combo_cache[str(current_group)]=new_dict
	
	print(largest_em)
	for key in combo_cache:
		print(key)
		keys = combo_cache[key]
		print(keys)
		#for value in keys:
		#	print(value, ":" ,keys[value])	
		print()
	#print(combo_cache)


	for i in range(len(lst_em)-1,0,-1):
		curr_em_map = lst_em[i]
		curr_em_vol= em_volume[curr_em_map]
		print(curr_em_map)
		for group in combo_cache:
			print(group)
			new_dict2={}
			combo_pair = combo_cache[group]
			#print(combo_pair)
			for combo in combo_pair:
				#print(combo)
				vol = combo_pair[combo]
				if vol <= curr_em_vol:
					new_dict2[str(combo)]=vol
				else:
					next
			print(new_dict2)
			print()
		print()
		print()
	
	



			


main()






