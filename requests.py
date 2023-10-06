import requests
from unidecode import unidecode
from requests.exceptions import HTTPError, ConnectionError

def moeda(site):
    cur = list(site['currencies'].values())[0]
    print("Moeda: {} ({})".format(cur['name'], cur['symbol']))
def capital(site):
    print("Capital(is): " + ', '.join(site['capital']))
def lingua(site):
    print("Língua(s): " + ', '.join(site['languages'].values()))
def population(site):
    print("Populaçâo: " + str(site['population']))
def continente(site):
    print("Continente: " + site['continents'][0])
def tudo(site):
    moeda(site)
    capital(site)
    lingua(site)
    population(site)
    continente(site)
    
while True:
    print("Argumentos:")
    print("\tMoeda")
    print("\tCapital")
    print("\tLíngua")
    print("\tPopulação")
    print("\tContinente")
    print("\tTudo")
    print("\tSair")
    pais = input("Digite um país: ").lower()
    if pais == "sair":
        break
    args = unidecode(input("Digite um argumento: ").lower())
    if args == "sair":
        break

    try:
        url = "https://restcountries.com/v3.1/translation/"+pais+"?fields=currencies,capital,name,languages,population,continents"
        site = requests.get(url)
        site.raise_for_status()
        site = site.json()[0]
        
        if args == "moeda":
            moeda(site)
        elif args == "capital":
            capital(site)
        elif args == "lingua":
            lingua(site)
        elif args == "populacao":
            population(site)
        elif args == "continente":
            continente(site)
        elif args == "tudo":
            tudo(site)
        else: 
            raise Exception("Informação inválida.")
 
    except Exception as error:
        if type(error) == ConnectionError:
            print("Sem internet.")
        elif type(error) == HTTPError:
            print("País inválido.")
        else:
            print(error)
