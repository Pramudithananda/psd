import requests
from bs4 import BeautifulSoup
import pandas as pd

amazon_url = "https://www.amazon.in/Samsung-Graygreen-Storage-Additional-Exchange/dp/B0B8S8NT22/ref=mp_s_a_1_3?crid=2779GFJS54RGO&keywords=samsung+galaxy+fold+4&qid=1680988379&sprefix=Samsung+Galaxy+Fold%2Caps%2C686&sr=8-3"

onshopdeals_url = "https://onshopdeals.com/original-new-samsung-galaxy-fold-smartphone-tablet-2-in-1-4-6-or-7-3-display-12g-ram-512g-storage-android-12mp-triple-rear-camera/"

headers = {"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36/8mqMlPuL-96'}
#amazon
page = requests.get(url=amazon_url, headers=headers) 
soup = BeautifulSoup(page.content,"html.parser") 

price = soup.find('span', class_ = "a-offscreen")
product = soup.find('title')
amazon_price = ((price.get_text()).strip()).replace("₹" , "")
print('Amazon price is :\n\n ',product, '\n₹', amazon_price)


#On Shop
page = requests.get(url=onshopdeals_url, headers=headers) 
soup = BeautifulSoup(page.content,'html.parser') 
product = soup.find("title")
price = soup.find('span',class_ = "price price--withTax price--main")
onshop_price = ((price.get_text()).strip()).replace("₹" , "")
print('\nOn Shop Price is :\n\n',product, '\n₹', onshop_price )

website_list = ['Amazon' , 'On Shop Deals' ]
price_list = [amazon_price, onshop_price]
url_list = [amazon_url,onshopdeals_url]
#Creating lists for each of the details

data = pd.DataFrame({"Website" :website_list , "Price" : price_list , "URL" : url_list})
data = data.set_index("Website")
data.Price.min() 
#will print the minimum value from the Price column from the dataframe

#data.Price == data.Price.min() 

#data[data.Price == data.Price.min()] 

#data.plot.bar()