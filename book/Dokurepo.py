from bs4 import BeautifulSoup
import re
import os

def main():
    
    hon_list = []
    dir_pleace = os.getcwd()
#    target_dir = r"{}\book\reports.html".format(dir_pleace)
    target_dir = r"{}\toshi0923.pythonanywhere.com\book\reports.html".format(dir_pleace)
    
    with open(target_dir, encoding="utf-8") as f:
        html = f.read()
        
    soup = BeautifulSoup(html,"lxml")
    
    for i in soup.find_all('h1'):
        hon_list.append(i.text)
    
    hon = "".join(hon_list)
    hon = re.split("[「」#]",hon)
    hon = [x for x in hon if x]
    for i in hon:
        if i == "none":
            i.replace("none", "test")
    hon = [hon[i:i+3] for i in range(0,len(hon),3)]
    
    return hon
    
#    frame = pd.DataFrame([hon[0::3],hon[1::3],hon[2::3]]).T
#    frame.columns = columns
        

