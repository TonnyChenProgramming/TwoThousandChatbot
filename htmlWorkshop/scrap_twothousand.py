URL1 = 'https://www.twothousand.com/'
from Scrap_html import scrap_one_page
from TwoThousand_Toolkit import FindKeyLinkForTwoThousand,scrap_machine_item_info
from dict import dict
import json
kitchen_equitment = {}




def scrap_twothousand():
    
    #FindKeyLinkForTwoThousand(dict = kitchen_equitment)
    with open('data.txt') as f: 
        data = f.read() 
    dict = json.loads(data)
    scrap_machine_item_info(dict=dict)
    with open('data.txt','w') as f:
        f.write(json.dumps(dict))

    #print(dict)
if __name__ == '__main__':
    scrap_twothousand()