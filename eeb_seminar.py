#! /usr/bin/bash
from bs4 import BeautifulSoup
import os
import re
import pdp

open("seminar.txt", "a") as my file:
    myfile.write('Name\t')
    myfile.write('Date\n')
    for file in os.listdir('.'):
       soup= BeautifulSoup(open('797.html'))
       main= soup.find(class_= 'clear-fix right-wide-column') #don't attach find_all
       evo = main.find_all("strong")
       eco = re.search (r"\<p>(\w+\s\w+)<br", str(main))
       div= eco.find("div", class_"section)
           section = div.p 
#If "EcoEvoPub Series" is found
        if eeb_seminar == "EcoEvoPub Series":
#find the name of the speaker(s)	
            name = r"<p>([A-Za-z]* [A-Za-z]* ?[A-Za-z]?)<br/>" 
            pub = re.search(name, str(eco), re.I)
            name = mm.group(1)
#find date
            date = r"<h4>(.* .* .*) </h4>"
            pub2 = re.search(date, str(eco), re.I)
            date1 = mm2.group(1)
#write name + ", " + date to the file
            myfile.write(str(name + ", " + date + "\n"))
        #else: 
            #break
   
############################################   
    #else: print evo[0].string
#eco.group()
#date = re.search(r"<h4>(\w+\s\d+\s\d+)\s</h4>", str(main))
#date.group()

 #for name in main:
  #  div = find(div, class_="section")
   # section = div.a
    #print name
   
   #if print(evo[0].string == "EcoEvoPub Series"
      
