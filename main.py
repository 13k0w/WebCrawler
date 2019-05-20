import urllib.request # https://pythonprogramming.net/urllib-tutorial-python-3/
import bs4 as bs # https://www.pythonforbeginners.com/beautifulsoup/beautifulsoup-4-python

URL = "http://quotes.toscrape.com/page/{}/" # zaso na kraj pomegu dvete / ima {} -> https://www.geeksforgeeks.org/python-format-function/
                                            # posle dole koristemo format

req = urllib.request.urlopen(URL.format(1)) # praves http request do stranata i ona ti vraka odgovor, kojsto se zacuvue u req
soup = bs.BeautifulSoup(req, "lxml") # lxml (u slucaj da te interesira) -> https://lxml.de/
                                     # bs e skraeno od BeautifulSoup i se koriste za da mozemo polsno da trazemo elementi na stranata

if(req.code == 200): # https://www.restapitutorial.com/httpstatuscodes.html
    print("Success")
else:
    print("Error")

#LEKOV UTRE SUM SLOBODEN MOZE DA SI PROGRAMIRAME DA SI SIMULIRAME
# Помини ти овиа работи што ти ги напиша погоре и прашај што не ти е јасно :D
