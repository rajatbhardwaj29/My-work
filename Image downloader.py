#image downloader
import bs4
import urllib.request as url
path="https://www.cricbuzz.com/"
response=url.urlopen(path)
page=bs4.BeautifulSoup(response,'lxml')
div=page.find('div',class_="cb-col cb-hm-mid cb-bg-white cb-hmpage")
new_path=div.findAll('img')['src']
pic_url=path+new_path
url.urlretrieve(pic_url,'Crickbuz1.jpg')

