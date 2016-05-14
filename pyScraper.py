#-------------------------------------------------------------------------------
# Name:        pyScraper
# Purpose:     Web scraping, supporting JavaScript, proxies and cookies.
#
# Author:      Akisato Kimura <akisato@ieee.org>
#
# Created:     April 24, 2014
# Copyright:   (c) Akisato Kimura 2014-
# Licence:     All rights reserved
#-------------------------------------------------------------------------------

import json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

def scraping(url, proxy_url, cookie_file, log_file, output_file):
    # Selenium settings
    phantomjs_args = []
    if proxy_setting is not None:
        proxy_setting = '--proxy=' + proxy_url
        phantomjs_args.append(proxy_setting)
    if cookie_setting is not None:
        cookie_setting = '--cookie_file={}'.format(cookie_file)
        phantomjs_args.append(cookie_setting)
    driver = webdriver.PhantomJS(service_args=phantomjs_args, service_log_path=log_file)
    # get a HTML response
    driver.get(url)
    html = driver.page_source.encode('utf-8')  # more sophisticated methods may be available
    # parse the response
    soup = BeautifulSoup(html, 'lxml')

    ##### You have to modify the following part according to your objectives. #####
    ##### Here, we extract
    #####   1. Texts between <head> ... <title> and </title> ... </head>
    #####   2. Texts in <meta name="description"> between <head> and </head>
    # extract
    ## title
    header = soup.find("head")
    title = header.find("title").text
    ## description
    description = header.find("meta", attrs={"name": "description"})
    description_content = description.attrs['content'].text
    # output
    output = {"title": title, "description": description_content}
    # write the output as a json file
    with open(output_name, "w") as fout:
        json = json.dump(output, fout, indent=4, sort_keys=True)
