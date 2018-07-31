from bs4 import BeautifulSoup
import requests
import webbrowser


movie_name = input("what movie would you like? ")

url = "https://thepiratebay.org/search/" + movie_name + "/0/99/0"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

magnet_links = soup.find_all(title="Download this torrent using magnet")


def open_avi_links():
    for link in magnet_links:
        link = str(link)
        if 'xvid' in link.lower():
            link = link[9:-121]
            webbrowser.open(link)

open_avi_links()