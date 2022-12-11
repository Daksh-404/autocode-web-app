import os

def runShell(path):
    run_command = "python Predict.py bin Code-Automaton {} output greedy".format(path)
    with open("runfile.bat",'w') as r:
        r.write(run_command)
    os.system("runfile.bat", )

runShell("C:/Users/hp/Desktop/autocode-web-app/application/autocode/gui/0E172E7D-AEB2-4C5D-9F78-DE2168678986.png")