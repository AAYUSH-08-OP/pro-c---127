#I tried doing this but it is only scraping the headers

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("Users/DELL/OneDrive/Desktop/chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Brown Dwarf", "Distance", "Mass", "Radius"]
    dwarf_data = []
    for i in range(0, 100):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "Field brown dwarfs"}):
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
                hyperlink_li_tag = li_tags[0]
                temp_list.append("https://en.wikipedia.org/wiki/List_of_brown_dwarfs"+hyperlink_li_tag.find_all("a", href = True)[0]["href"])
                dwarf_data.append(temp_list)
            browser.find_element_by_xpath("Users/DELL/OneDrive/Documents/white-hat-python/apps-softwares/chromedriver.exe")
    with open("dwarf_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(dwarf_data)

scrape()

