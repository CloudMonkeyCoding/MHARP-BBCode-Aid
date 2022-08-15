import requests
from bs4 import BeautifulSoup

def find_technique(technique, character_url):
    r = requests.get(character_url)
    s = BeautifulSoup(r.text, "html.parser")

    first_post = s.find('div', class_ = "cbrpost")
    spoilers = first_post.find_all('div', class_ = "spoiler")
    for spoiler in spoilers:
        if spoiler.find('div').string == "Techniques":
            techniques = spoiler
            break
        
    return str(techniques).find(technique)