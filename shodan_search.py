import shodan
from nvds import nvdfind
SHODAN_API_KEY = "fTQg75ovS20N6DK0wTbtC0dBa2VXr9of"

api = shodan.Shodan(SHODAN_API_KEY)

v = []
def search(ip):
    seen = []
    
    try:
        # Search Shodan
        stype = 'Alternate IP Address: '
        if ip != 'bluetooth':
            results = api.search(stype+ip)
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            current = result['product']
    
            if current not in seen:
                seen.append(current)
    
        for l in seen:
            f = open('results.txt', 'a')
            x = ('\n'+'\n'+'product ' + l + '\n')
            print(x)
            v.append(x)
            f.write(x)
            if nvdfind(l) != None: 
                f.write(nvdfind(l))
                f.write('\n')
                v.append(nvdfind(l))
            f.close()

    
    except shodan.APIError:
        print('Error: {}')


