from bs4 import BeautifulSoup
import requests



def to_dict(param):
    return [i.get_text() for i in param]

def makert_list_to_json():
    r = requests.get('https://www.americanas.com.br/produto/134217467/smartphone-samsung-galaxy-s10-128gb-dual-chip-android-tela-6-1-octa-core-4g-camera-tripla-traseira-12mp-12mp-16mp-branco?pfm_carac=celular%20samsung%20s10&pfm_index=0&pfm_page=search&pfm_pos=grid&pfm_type=search_page%20&sellerId=00776574000660')

    main = {}
    v = {}

    bs = BeautifulSoup(r.content, 'html.parser')

    soup = bs.find('section')

    title = soup.find('h1')
    img = soup.find('div', attrs={'class': 'image-gallery-image'})
    vendor = soup.find_all('div', attrs={'class': 'seller-name-content'})
    tax = soup.find('p', attrs={'class': 'payment-option'})
    price = soup.find('span', attrs={'class': 'sales-price'})

    
    v.update({'markets': to_dict(vendor)})

    main.update({
        'imagem': img.find('img')['src'],
        'titulo': title.get_text(),
        'valor': price.get_text(),
        'taxa': tax.get_text(),
        'vendedor': v
    })

    return main