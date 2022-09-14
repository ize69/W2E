from lib2to3.pgen2.token import NEWLINE
from operator import contains, indexOf
from xml.etree.ElementInclude import include
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from io import BytesIO
from array import *
def main(Local_name):
    url = 'https://www.rit.edu/fa/diningservices/places-to-eat/hours'
    source_html = requests.get(url)
    soup = BeautifulSoup(source_html.content,'html.parser')
    open_hours = 0
    dinlocal = 0
    #prints the dinning locations found
    for i in soup.find_all('div', class_="hours-title"):  
        dinlocal = dinlocal + 1
    dinName = [[0 for i in range(12)] for j in range(dinlocal)]
    print(dinlocal)
    dinlocal = 0
    for i in soup.find_all('div', class_="hours-title"):    
        dinName[dinlocal][0] = ((i.get_text()).replace('\n',''))
        dinlocal = dinlocal + 1
    #prints all dinning locations 
    
    currentLocation = 0 
    k=0
    
    for i in soup.find_all('div', class_="container-fluid location-box panel panel-default hours-all-panel"):
        k=k+1
        #print(i.get_text())
        #print(k)
        
        #check for edge cases 
        if k == 17:
            currentLocation = currentLocation+1
        if "Close" in str(i.get_text()):
            print("edge case : closed")
            currentLocation = currentLocation + 1
        elif   "Breakfast" in str(i.get_text()):
            print("edge case : Breakfast")
            #get the sub string containg the hours of opporation
            temp = (i.get_text()).index("m - ")
            print((i.get_text())[temp-6:len(str(i.get_text()))-1])
            dinName[currentLocation][2] = ((i.get_text())[temp-6:temp+1]).replace(' ','')
            dinName[currentLocation][3] = ((i.get_text())[temp+4:len(str(i.get_text()))-1]).replace(' ','')
        elif "Lunch"     in str(i.get_text()):
            print("edge case : lunch")
            if "Closed" in str(i.get_text()):
                print("edge case : closed")
            else:
                temp = (i.get_text()).index("m - ")
                print((i.get_text())[temp-6:len(str(i.get_text()))-1])
                dinName[currentLocation][4] = ((i.get_text())[temp-6:temp+1]).replace(' ','')
                dinName[currentLocation][5] = ((i.get_text())[temp+4:len(str(i.get_text()))-1]).replace(' ','')
            if "Dinner" not in str(soup.find_all('div', class_="container-fluid location-box panel panel-default hours-all-panel")[k]) and "Salsarita" not in str(soup.find_all('div', class_="container-fluid location-box panel panel-default hours-all-panel")[k]):
                print("end of location hours")
                print((i.next).get_text())
                currentLocation = currentLocation + 1
        elif "Dinner" in str(i.get_text()):
            print("edge case : dinner")
            if "Closed" in str(i.get_text()):
                print("edge case : closed")
            else:
                temp = (i.get_text()).index("m - ")
                print((i.get_text())[temp-6:len(str(i.get_text()))-1])
                dinName[currentLocation][6] = ((i.get_text())[temp-6:temp+1]).replace(' ','')
                dinName[currentLocation][7] = ((i.get_text())[temp+4:len(str(i.get_text()))-1]).replace(' ','')
            currentLocation = currentLocation + 1
        elif "Salsarita's" in str(i.get_text()):
            print("edge case : Salsarita's")
            temp = (i.get_text()).index("m - ")
            print((i.get_text())[temp-6:len(str(i.get_text()))-1])
            dinName[currentLocation][8] = ((i.get_text())[temp-6:temp+1]).replace(' ','')
            dinName[currentLocation][9] = ((i.get_text())[temp+4:len(str(i.get_text()))-1]).replace(' ','')
        else:
            temp = (i.get_text()).index("m -")
            print((i.get_text())[temp-6:len((i.get_text()))-1])
            try:
                dinName[currentLocation][2] = ((i.get_text())[temp-6:temp+1]).replace(' ','')
                dinName[currentLocation][3] = ((i.get_text())[temp+4:len((i.get_text()))-1]).replace(' ','')
            except:
                print("")
            currentLocation = currentLocation + 1
    return dinName

#main(5)
