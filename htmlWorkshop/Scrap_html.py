import requests
from requests.exceptions import RequestException 

def scrap_one_page(url):
    #This function visit the target website and return the html content of the website in string, if it fail it, return none
    #input: 
    #  url(string): the url of a website page 
    #expected return:
    #  response : the html of the website page
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'  
        }

        response = requests.get(url=url,headers=header)

        if response.status_code == 200:
            return response.text
        return None 
    
    except RequestException:
        return None