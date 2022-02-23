#!/usr/bin/env python
# coding: utf-8

# **Import Packages**
import pandas as pd
from requests import get
from bs4 import BeautifulSoup
import requests
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
chrome_options = Options()
chrome_options.add_argument('--headless')# servers don't provide the visulazation
chrome_options.add_argument('--no-sandbox')# operate at the highest authority
chrome_options.add_argument('--disable-dev-shm-usage')#increase the RAM of chrome to load the page
path = "chromedriver" #path to chromedriver


# **Define cities job links on craiglists**
citiesLink = ['https://chicago.craigslist.org/d/jobs/search/jjj', 'https://newyork.craigslist.org/d/jobs/search/jjj',
              'https://newjersey.craigslist.org/d/jobs/search/jjj', 'https://indianapolis.craigslist.org/d/jobs/search/jjj',
             'https://columbus.craigslist.org/d/jobs/search/jjj', 'https://sfbay.craigslist.org/d/jobs/search/jjj',
              'https://seattle.craigslist.org/d/jobs/search/jjj','https://austin.craigslist.org/d/jobs/search/jjj',
             'https://houston.craigslist.org/d/jobs/search/jjj', 'https://lasvegas.craigslist.org/d/jobs/search/jjj']


# **Function to extract all the job posting links on the first page**
def getjobLinks(citiesLink):
    try:
        cityjoblink = {}
        for link in citiesLink:
            city = link[8:link.find('.')]
            cityjoblink[city] = []
            response = get(link)
            soup = BeautifulSoup(response.text, 'html.parser')
            for a in soup.find_all("a", class_="result-title hdrlnk"):
                cityjoblink[city].append(a.get('href'))
        return cityjoblink

    except Exception as e:
            print(e)


# **Function to parse the data of a job posting**
def getjobData():
    try:
        driver = webdriver.Chrome(path, options = chrome_options)
        cityjoblinkDict = getjobLinks(citiesLink)
        cityList=[]
        linkList=[]
        titleList=[]
        descriptionList=[]

        for key in cityjoblinkDict:
            jobLinks = cityjoblinkDict[key]
            for link in jobLinks:
                time.sleep(2)
                try:
                    response = get(link)
                    #print(link)
                    driver.get(link)
                    title = driver.find_element_by_class_name('postingtitletext').text.strip()
                    description = driver.find_element_by_xpath('//html/body/section/section/section/section').text.strip()
                    cityList.append(key)
                    linkList.append(link)
                    titleList.append(title)
                    descriptionList.append(description)
                except Exception as e:
                    print(e)
                finally:
                    continue
        driver.quit()
        return cityList, linkList, titleList, descriptionList
    except Exception as e:
        print(e)


# **Define a dataframe to store extracted job data**
cityList, linkList, titleList, descriptionList = getjobData()
df = pd.DataFrame({'location': cityList,'URL': linkList,'title':titleList, 'description': descriptionList})

# **Write the dataframe to a csv**
df['fradulent'] = ''
df.to_csv('scraped_data.csv', index = False)