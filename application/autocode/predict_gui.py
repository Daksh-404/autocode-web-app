import time
from bs4 import BeautifulSoup
from lxml import html, etree
from io import StringIO 

def predict_gui(path):
    time.sleep(1)
    print("Loading...")
    soup = BeautifulSoup(open("/Users/daksh_mac/Desktop/everything/Dev/gitRepos/autocode-web-app/application/autocode/sample.html", encoding="utf8"), "html.parser")
    return soup.prettify()  