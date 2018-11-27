from bs4 import BeautifulSoup
import requests

def dictionary(string):
	page_link ='https://dictionary.com/browse/' + string
# fetch the content from url
	page_response = requests.get(page_link, timeout=5)
# parse html
	page_content = BeautifulSoup(page_response.content, "html.parser")

# extract all html elements where price is stored
# prices has a form:
#[<div class="main_price">Price: $66.68</div>,
# <div class="main_price">Price: $56.68</div>]

# you can also access the main_price class by specifying the tag of the class
	prices = page_content.find_all('span', attrs={'class':'luna-pos'})
	print(prices[0].text)

while True:
	dictionary(input())