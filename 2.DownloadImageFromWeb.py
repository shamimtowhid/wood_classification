# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests,bs4,csv
import re

def DownloadHTML(parameter):
    file = requests.get('http://www.wood-database.com/'+parameter)
    file.raise_for_status()
    soupOb = bs4.BeautifulSoup(file.text,"lxml")
    elems=soupOb.find_all('a',href=True)
    return elems[6]['href']
    
def downloadimage(url,name):
#    urllib.urlretrieve(url, "./images/"+name+".jpg")
    f = open('./images/'+name+'.jpg','wb')
    f.write(requests.get(url).content)
    f.close()


if __name__=="__main__":
#    link= DownloadHTML('abura/')
#    downloadimage(link,"abura")
#        input("Press Enter to continue...")
    file = open("woodname.csv")
    reader=csv.reader(file)
    for row in reader:
        trimmed_val=re.sub(' {2,}','',str(row))
        lower_case_str=trimmed_val.lower()
        search_string=lower_case_str.replace(" ","-")
        try:
            print('now processing ',str(search_string))
            link=DownloadHTML(str(search_string)+'/')
            print('link: ',link)
            downloadimage(link,str(search_string))
            print('download done')
        except Exception:
            print('Error Occured for ',search_string)
            continue
