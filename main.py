import json

filename='cities.json'
file=open(filename, 'r')
json_data=json.load(file)
cities_list=[city['city'] for city in json_data]

eco_cities={
   "clean":[], #no oil, no mining
   "semi_clean":[], #1 oil or mining
   "dirty":[], #more than 1 oil or mining
}

for i in json_data:
	# print('i - ', i)
	count=0
	for j in i['company']:
		if j['industry']=='Mining' or j['industry']=='Gas/Oil':
			count+=1
	if count==0:
		eco_cities['clean'].append(i['city'])
	elif count==1:
		eco_cities['semi_clean'].append(i['city'])
	else:
		eco_cities['dirty'].append(i['city'])

industrial_cities={
   "many_companies":[i['city'] for i in json_data if len(i['company'])>4 ], # more than 4 companie
   "mid_companies": [i['city'] for i in json_data if len(i['company']) in range(2,5)], #from 2 to 5 companies in a city
   "small_companies":[i['city'] for i in json_data if len(i['company'])<2], #"less than 2"
}

pub_cities={
   "good":[i['city'] for i in json_data if len(i['bars'])==5], #contains a lot of different chains
   "normal": [i['city'] for i in json_data if len(i['bars']) in range(2,5)], #contains at least 2 chains
   "bad":[i['city'] for i in json_data if len(i['bars'])<2], #others
}

print('\n'*2, ' ---  ind cities ---  ', '\n',industrial_cities)
print('\n'*2, '---  eco_cities ---  ','\n', eco_cities)
print('\n'*2, '---  pub_cities ---  ','\n', pub_cities)


file.close()