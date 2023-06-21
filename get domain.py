pip install python-whois
#modules-->python-whois
#pip install python-whois
import whois

def domain_info(link):
  domain=whois.whois(url)
  print(f'server:{domain.whois_server}')
  print(f'expiration:{domain.expiration_date}')
  print(f'name:{domain.name}')
  print(f'organisation:{domain.org}')
  print(f'state:{domain.state}')
  print(f'city:{domain.city}')
  print(f'country:{domain.country}')

url=input('enter URL \n')

try:
  domain=whois.whois(url)
except:
  print('this domain is available')
else:
  print('this domain is already purchased')
  print('domain information \n')
  domain_info(url)
