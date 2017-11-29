#-------------------------------------------------------------------------------
# Name:        pyScraper
# Purpose:     Web scraping, supporting JavaScript, proxies and cookies.
#
# Author:      Akisato Kimura <akisato@ieee.org>
#
# Created:     April 24, 2014
# Updated:     November 29, 2017
# Copyright:   (c) Akisato Kimura 2014-
# Licence:     All rights reserved
#-------------------------------------------------------------------------------

from __future__ import print_function
import json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import codecs

def scraping(url, proxy_url, cookie_file, log_file, output_file):
    # Selenium settings
    phantomjs_args = []
    if proxy_url is not None:
        proxy_setting = '--proxy=' + proxy_url
        phantomjs_args.append(proxy_setting)
    if cookie_file is not None:
        cookie_setting = '--cookie_file={}'.format(cookie_file)
        phantomjs_args.append(cookie_setting)
    driver = webdriver.PhantomJS(service_args=phantomjs_args, service_log_path=log_file,
                                 executable_path='/usr/local/bin/phantomjs')
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
    description_content = description.attrs['content']
    # output
    print(isinstance(title, unicode))
    print(isinstance(description_content, unicode))
    output = {"title": title, "description": description_content}
    # write the output as a json file
    with codecs.open(output_file, 'w', 'utf-8') as fout:
        json.dump(output, fout, indent=4, sort_keys=True, ensure_ascii=False)
