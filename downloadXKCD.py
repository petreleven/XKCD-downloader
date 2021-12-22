import bs4
import requests
import os

url='http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
print(os.getcwd())
while not url.endswith('#'):
    print('Downloading page %s...'%(url))
    res=requests.get(url)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text,'html.parser')
    comic_Elem=soup.select('#comic img')
    if comic_Elem==[]:
        print('No image found')
    else:
        print(comic_Elem[0].get('src'))
        comicUrl='http:'+comic_Elem[0].get('src')
        print('Downloading image...')
        res=requests.get(comicUrl)
        res.raise_for_status()
        
        imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        prevLink=soup.select('a[rel=prev]')
        url='https://xkcd.com/'+prevLink[0].get('href')

print('Done')
print(os.getcwd())