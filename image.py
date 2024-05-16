import requests
from bs4 import BeautifulSoup

# URL de la page web que tu souhaites récupérer
url = 'https://dossier.parcoursup.fr/Candidats/public/fiches/afficherFicheFormation?g_ta_cod=24728'

def get_ecole_link(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        link_ecole = soup.find('a', id='lien-site-internet-etab-2')
        return link_ecole['href'] if link_ecole else None
    else:
        return None

print(get_ecole_link(url))