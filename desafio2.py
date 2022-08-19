from bs4 import BeautifulSoup
import requests,random
for c in range(1, 51):
    links = []
    url = f'https://books.toscrape.com/catalogue/page-{c}.html'
    pagina = requests.get(url, verify=False)


    #raspagem dos links das imagens
    soup = BeautifulSoup(pagina.text, 'html.parser') 
    for item in soup.find_all('img'):
        links.append('https://books.toscrape.com/' + item['src']) 
    links = list(set(links))

    #download das imagens
    for item in links:
            try:
                img_data = requests.get(item, verify=False).content
                with open('{}.jpg'.format(random.randint(1,100000)), 'wb') as handler:
                    handler.write(img_data)
            except:
                pass