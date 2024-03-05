URL1 = 'https://www.twothousand.com/'
from Scrap_html import scrap_one_page
from TwoThousand_Toolkit import FindKeyLinkForTwoThousand,scrap_machine_item_info
from dict import dict
import json
kitchen_equitment = {}




def scrap_twothousand():
    #THE text data is in python dictionary format
    #This function retrieve data from a text file and modify it and store it back
    # FindkeylinkForTwoThousand and scrap_machine_item_info scrap the target web page and parse the wanted data and store it in the dictionary
    
    with open('data.txt') as f: 
        data = f.read() 
    dict = json.loads(data)
    FindKeyLinkForTwoThousand(dict)
    scrap_machine_item_info(dict=dict)
    with open('data.txt','w') as f:
        f.write(json.dumps(dict))

    #print(dict)
if __name__ == '__main__':
    scrap_twothousand()