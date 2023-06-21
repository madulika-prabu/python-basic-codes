#modules--> google, beautifulsoup4
'''pip install google
pip install beautifulsoup4'''

#functions and parameter
# fn=search(query,tld,num,stop,pause)
'''
query-->string that we want to search for
tld-->top level domain-->search our result in google.com or google.in or in any domain
num-->no of result we want
stop-->last result to retrieve-->use None to keep searching forever
pause-->lapse to wait between HTTP request
'''

try:
    from googlesearch import search
except ImportError:
    print("module not found")
query=input('Enter a query \n')
for i in search(query,tld='com',num=10,stop=10,pause=2):
    print(i)
