from Scrap_html import scrap_one_page
import re
from bs4 import BeautifulSoup
def FindKeyLinkForTwoThousand(dict):
    #TwoThousand Machinery company's products can be divided in these categories stated in the keywords variable.
    #This function will go over each of the categories and store the machine name and machine url(subpage) in to the dictionary
    keywords = ['food-preparation','refrigeration-equipment','baking-equipment','cooking-equipment','stainless-steel-equipment','industry-and-food-service-equipments',]
    #for item in keywords:
    for item in keywords:
        try:
            url = 'https://www.twothousand.com/'+ item
            text = scrap_one_page(url = url)
            #filter out desired chunck of content for efficiency
            filtered = re.search('<div class="listing-catalogimg-grid catalogimg-listing">(.*?)<div class="need_help_form">',text,re.S)
            # I need a name and a link 
            machines =re.findall('<a href="(.*?)" title="(.*?)" class="product-image">',filtered.group())
            # add each item to dictionary kitchen equitment
            for machine in machines:
                dict[machine[1]] ={
                    'name':machine[1],
                    'url':machine[0],
                }
        except:
            print("error")
        

def description_append(text):
    # this function recevie an html piece and return text, it the text doesn't exist, it return ''
    data = ''
    try:
        data += text.string
    except:
        try:
            data+=text.span.strong.a.span.string
            data+=text.span.nextSibling
        except: 
            data = None
    if data is None:
        data = ''
    return data
def parse_description(text):
    soup = BeautifulSoup(text,'lxml')
    description = ''
    description_div = soup.find_all(name ='div',attrs={'class':'category-description'})
    for item in description_div:
        description_spans = item.find_all(name = 'span')
        for span in description_spans:
            description+= description_append(span)
    return description
def parse_items(text):
    soup = BeautifulSoup(text,'lxml')
    # name & link 
    items = {}
    item_list = soup.select('.category-products .category_right .products-grid .item .product-info .product-name')
    for item in item_list:
        link = item.a.attrs['href']
        name = item.string
        items[name] ={
                    'name':name,
                    'link':link,
                }
    return items
def parse_item_data(text):
    #this function parse model html string
    try:
        soup = BeautifulSoup(text,'lxml')
    except:
        return ''
    data = ''

    description= soup.select('.product-collateral .tab-content .std')
    description_list = description[0].find_all(name = 'span')
    for item in description_list:
        try:
            data += (item.string +' ')
        except:
            data +=''
    additional_info = soup.select('.tab-container .tab-content .data-table')
    data += ' addtional information: '
    info_list = additional_info[0].find_all(name='tr')
    for piece in info_list:
        data += ' '+piece.th.string+':'
        data += ' '+piece.td.string+' '
    return data
def scrap_machine_item_info(dict):
    # a product have many models, for example, a green color mixer and a blue color mixer.
    #This function will scrape and pass the key information for each model listed on the company wesbite
    #The dict is being updated 
    

    #for machine in dict:
        #text =scrap_one_page(url=dict[machine]['url']) 
        #dict[machine]['description'] = parse_description(text=text)
    # scrap item link 
    #for machine in dict:
        #text =scrap_one_page(url=dict[machine]['url']) 
        #dict[machine]['items'] = parse_items(text=text)
    # scrap item information     
    for machine in dict: 
        for item in dict[machine]['items']:
            dict[machine]['items'][item]
            text =scrap_one_page(url=dict[machine]['items'][item]['link'])
            dict[machine]['items'][item]['data'] = parse_item_data(text)