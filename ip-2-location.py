import requests
from bs4 import BeautifulSoup

# Grab into from user or file.

def db2location():
    file = input("Please enter the file name:")
    
def ip2Location():
    # Initializing URL.
    ip = input("Enter the IP Address:")
    url = "https://www.geodatatool.com/en/?ip="+ip
    
    # Getting site's data in plain text..
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText,features="lxml")
    
    data_items = soup.select('div.sidebar-data div.data-item')
    targets = ['Country:','City:','Region:']
    for item in data_items:
        if item.select('span.bold')[0].text in targets:
            print(item.select('span.bold')[0].text, item.select('span')[1].text.strip())        
        
    
     
def main():
    ip2Location()

if __name__ == "__main__":
    main()
     
