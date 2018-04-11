from bs4 import BeautifulSoup as bSoup
import requests

class Pokeball:

    name = ""
    kdex = ""
    ndex = ""
    types = None

    def __init__(self, name, kdex, ndex, types):

        self.name = name
        self.kdex = kdex
        self.ndex = ndex
        self.types = types


url = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pokémon_by_National_Pokédex_number"

html = requests.get(url)
page = bSoup(html.content, 'html')

#print(page)

tables = page.find_all("table", attrs={"align":"center"})
pokeList = []
pokeDex = {}

for table in tables:
    pokeList.append(table.find_all("tr", attrs={"style":"background:#FFF"}))

for gen in pokeList:
    for tempPoke in gen:

        kdex = tempPoke.find_all("td", attrs={"style":"font-family:monospace"})[0].contents[0]

        ndex = tempPoke.find_all("td", attrs={"style":"font-family:monospace"})[1].contents[0]
        ndex = int(ndex.strip(" #"))


        name = tempPoke.find_all("td")[3].find("a").contents[0]

        type = []
        numOfTypes = len(tempPoke.find_all("td"))-4

        type.append(tempPoke.find_all("td")[4].find("a").find("span").contents[0])

        if numOfTypes == 2:

            type.append(tempPoke.find_all("td")[5].find("a").find("span").contents[0])

        pokemon = Pokeball(name, kdex, ndex, type)

        if pokemon.ndex not in pokeDex:
            pokeDex[pokemon.ndex] = pokemon

print(pokeDex[1].name)


