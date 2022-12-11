import time
from bs4 import BeautifulSoup
from autocode.gui.finalEval import *

def predict_gui(path):
    # time.sleep(1)
    op_path = runShell(path)
    print(op_path)
    print("Loading...")
    soup = BeautifulSoup(open(op_path, encoding="utf8"), "html.parser")
    return soup.prettify()  