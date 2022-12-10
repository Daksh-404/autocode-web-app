import time
from bs4 import BeautifulSoup

def predict_wireframe(path):
    time.sleep(1)
    print("Loading...")
    soup = BeautifulSoup(open("/Users/daksh_mac/Desktop/everything/Dev/gitRepos/autocode-web-app/application/autocode/sample2.html", encoding="utf8"), "html.parser")
    return soup.prettify()  