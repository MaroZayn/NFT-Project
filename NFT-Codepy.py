import re
import requests  
from bs4 import BeautifulSoup  
import csv                     


page = requests.get("https://howrare.is/drops")

def main(page):  

    src = page.content  
    soup = BeautifulSoup(src, "lxml")

    project_details = [] #a liste of dictionnary

    date = soup.find_all("div", {'class':'table_wrap'}) 
    
    def get_project_info(date):

        date_details = date.contents[1].text.strip()
        
        all_projects = date.contents[3].find_all('tr')            #all project is a liste 
        
        all_project = all_projects[1:]
        #print(len(all_project))
        number_of_projects = len(all_project)
        
        for i in range(number_of_projects):
            
            # get projects names
            projects_names = all_project[i].find('div',{'class': 'tab_collection'}).text.strip()
            # get Twitter username
            projects_link = all_project[i].find('div',{'class': 'links'})
            for link in projects_link.find_all('a'):
                link = link.get('href')
                if 'twitter' in link:
                    twitter = str(link)[20:]
            # get project details        
            details = all_project[i].find_all('td')
            # get the supply
            count = details[1].text.strip()
            # get the price
            price = details[2].text.strip() 
            # add project info to the var project_details
            project_details.append({"    day     ":date_details,"   project name    ":projects_names,"    price    ":price,"   supply     ":count," Twitter Username":twitter})
            
            
            #print(project_details)
            
    for i in range(len(date)):
        (get_project_info(date[i]))
    keys = project_details[0].keys() 
    
    with open('D:/Work/denart.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(project_details)
    print('file created')
main(page)
