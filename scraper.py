from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv


START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("C:/Users/HP/Downloads/chromedriver_win32/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date", "hyperlink", "planet_type", "planet_radius", "orbital_radius", "orbital_period", "eccentricity"]
    planet_data = []
    for i in range(1,5):
       soup = BeautifulSoup(browser.page_source, "html.parser")      
      
       currentpageno=int(soup.find_all("input",attrs={"class","page_num"})[0].get("value"))
       if currentpageno<i:
            browser.find_element(By.XPATH(value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a')).click()
       elif currentpageno>i:
             browser.find_element(By.XPATH(value='//*[@id="primary_column"]/footer/div/div/div/nav/span[1]/a')).click()





       for ul_tag in soup.find_all("ul", attrs={"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
               if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
               else:
                   try:
                        temp_list.append(li_tag.contents[0])
                   except:
                       temp_list.append("")
            hyperlink_li_tag=li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov"+hyperlink_li_tag.find_all("a", href=True)[0]["href"])
            planet_data.append(temp_list)

            
       browser.find_element(By.XPATH,value="//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()")
       print(f"page {i} scrape completed")
    

scrape()
newplanetdata=[]
def scrapemoredata(hyperlink):
     try:
          page=requests.get(hyperlink)
          soup=BeautifulSoup(page.content,"html.parser")
          temp_list=[]
          for tr_tag in soup.find_all("tr", attrs={"class", "fact_row"}):
            td_tags = tr_tag.find_all("td")
            
            for td_tag in enumerate(td_tags):
               
               try:
                    temp_list.append(tr_tag.find_all("div",attrs={"class":"value"})[0].contents[0])
               except:
                    temp_list.append("")

          newplanetdata.append(temp_list)
     except:
          time.sleep(1)
          scrapemoredata(hyperlink)

for index,data in ennumerate(planet_data):
     scrapemoredata(data[5])
     print(f"scraping@hyperlink {index+1} is completed")

print(newplanetdata[0:10])
finalplanetdata=[]
for index, data in enumerate(planets_data):
      newplanetdata_element = newplanetdata[index] 
      newplanetdata_element = [elem.replace("\n", "") for elem in newplanetdata_element] newplanetdata_element = newplanetdata_element[:7] 
      finalplanetdata.append(data + newplanetdataelement)

with open("./final.csv", "w") as f:
       csvwriter = csv.writer(f)
       csvwriter.writerow(headers)
       csvwriter.writerows(newplanetdata)

    
