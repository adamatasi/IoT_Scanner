import nvdlib


def nvdfind(name):
	
	r = nvdlib.searchCVE(keyword = name, limit=2, key='dd3fca30-10f7-4554-b717-305ac877d7aa')
	
	cve = {}
	
	for eachCVE in r:
		
		i = eachCVE.id
		print(i)
		
		x = nvdlib.getCVE(i, key='dd3fca30-10f7-4554-b717-305ac877d7aa', cpe_dict=True)
		print(x.score)
		s = x.score
		cve.update({i: s})
	
	return str(cve).strip("'}{")
