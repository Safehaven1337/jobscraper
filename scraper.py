import requests
from bs4 import BeautifulSoup
import time


# Our testing URLs to see if we get an error code
urls = ["https://www.arbeitsagentur.de/jobsuche/suche?angebotsart=4&was=Fachinformatiker%2Fin%20Anwendungsentwicklung&wo=93142%20Maxh%C3%BCtte-Haidhof&umkreis=25",
        "https://www.stepstone.de/jobs/fachinformatiker-anwendungsentwicklung-ausbildung/in-93142?radius=30&searchOrigin=Resultlist_top-search&whatType=autosuggest",
        "https://de.indeed.com/jobs?q=Ausbildung+Fachinformatiker+Anwendungsentwicklung&l=Regensburg%2C+Bayern&fromage=last&radius=35&from=searchOnDesktopSerp&vjk=19adac4ddfdaea9f",
        "https://www.stepstone.de/jobs/fachinformatiker-in-anwendungsentwicklung/in-93142-maxh%c3%bctte-haidhof?radius=30&searchOrigin=membersarea&whereType=autosuggest&whatType=autosuggest&q=Fachinformatiker%2Fin%20Anwendungsentwicklung"]

# Masking our user to bypass script blockers
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer": "https://www.google.com/"
}

# We loop through our list of urls. If .get is successfull we parse the html with soup and print the title of the webpage. If it is not successful we output the error code and/or
# if we suspect anti-script measures

for url in urls:
    try:
        print(f"Versuche URL zu fetchen: {url}")
        response = requests.get(url, headers=user_agent)
        if response.status_code == 200:
            print("OK!")

            soup = BeautifulSoup(response.text, "html.parser")
            print(f"Seitentitel: {soup.title.string}")
            print("----------------")
        
        else:
            if response.status_code == 403:
                print(f"Access denied - Wahrscheinlich anti-script. Fehlercode: {response.status_code}")
                print("----------------")
            else:
                print(f"Fehler {response.status_code}")
                print("----------------")
    
    except Exception as e:
        print(f"Irgenwas ist schief gelaufen: {e}")

# Short snooze for not spamming pings
    time.sleep(1)






