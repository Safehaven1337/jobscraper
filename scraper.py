import requests
from bs4 import BeautifulSoup

# Our testing URL to see if we get an error code
url = "https://www.arbeitsagentur.de/jobsuche/suche?angebotsart=4&was=Fachinformatiker%2Fin%20Anwendungsentwicklung&wo=93142%20Maxh%C3%BCtte-Haidhof&umkreis=25"


# Masking our user to not trigger any anti-script blockers
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

print(f"Versuche {url} aufzurufen...")



# If .get is successfull we parse the html with soup and print the title of the webpage
try:
    response = requests.get(url, headers=user_agent)
    if response.status_code == 200:
        print("OK!")

        soup = BeautifulSoup(response.text, "html.parser")

        print(f"Seitentitel: {soup.title.string}")
    
    else:
        print(f"FEHLER Code: {response.status_code}")

except Exception as e:
    print(f"Irgendwas ist schief gelaufen: {e}")



