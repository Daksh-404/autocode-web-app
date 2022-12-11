import time
from bs4 import BeautifulSoup
from autocode.wireframe.finalEval import *

def predict_wireframe(path):
    # time.sleep(1)
    op_path = runCode(path)
    print("Loading...")
    soup = BeautifulSoup(open(op_path, encoding="utf8"), "html.parser")
    return soup.prettify()  