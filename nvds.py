import nvdlib


def nvdfind(name):

    r = nvdlib.searchCVE(keyword = name, limit=2, key='dd3fca30-10f7-4554-b717-305ac877d7aa')
    
    for eachCVE in r:

        i = eachCVE.id
        current = eachCVE.id
        x = nvdlib.getCVE(current,cpe_dict = True)
        p = x.v3severity
        s = x.score
        fin = str(i) + '\n'+ str(s) + '\n'+ str(p) + '\n'
        print(fin)
        return fin

