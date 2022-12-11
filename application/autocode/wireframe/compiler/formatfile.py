import os

def formatGUI(path):
    with open(path, 'r') as r:
        text = r.read()
        # print(text)
    text = text.split(' ')
    # print(text)
    text = text[1:len(text)-1]
    # print(text)
    s = ' '.join(text)
    # print(s)

    ans = ""
    for token in text:
        if token == "}":
            ans += "\n"
        ans = ans + token + " "
        if token == "{":
            ans += "\n"
        if token == "}":
            ans += "\n"
    
    ans = os.linesep.join([s for s in ans.splitlines() if s])
    ans = ans.split('\n')
    with open(path, 'w', encoding="utf-8") as r:
        r.writelines(ans)
