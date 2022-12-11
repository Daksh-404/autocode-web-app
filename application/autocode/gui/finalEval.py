import os
from autocode.gui.compiler.webCompiler import *
from autocode.gui.Predict import *
import time

def runShell(path):
    path = path.replace("\\",'/')
    # run_command = "python autocode/gui/Predict.py autocode/gui/bin Code-Automaton {} autocode/gui/output greedy".format(path)
    # with open("autocode/gui/runfile.bat",'w') as r:
    #     r.write(run_command)
    # os.system("autocode/gui/runfile.bat")
    # png_filename = os.path.basename(path)
    # sample_id = png_filename[:png_filename.find('.png')]
    # gui_path = "autocode/gui/output/{}.gui".format(sample_id)
    # compileHTML(gui_path)
    # return "autocode/gui/output/" + sample_id + ".html"
    predictGUI(path)
    png_filename = os.path.basename(path)
    sample_id = png_filename[:png_filename.find('.png')]
    gui_path = "autocode/gui/output/{}.gui".format(sample_id)
    compileHTML(gui_path)
    return "autocode/gui/output/" + sample_id + ".html"
    

# runShell("C:/Users/hp/Desktop/autocode-web-app/application/autocode/gui/0E172E7D-AEB2-4C5D-9F78-DE2168678986.png")