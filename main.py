#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Testing the package pyScraper
#
# Author:      Akisato Kimura <akisato@ieee.org>
#
# Created:     May 13, 2016
# Copyright:   (c) Akisato Kimura 2016-
# Licence:     All rights reserved
#-------------------------------------------------------------------------------

import os.path
import pyScraper

if __name__ == '__main__':
    # arguments
    url = 'http://www.mainichi.jp'
#    proxy_url = 'proxy.server.no.basho:0000'
    proxy_url = None
#    cookie_file = 'cookie.txt'
    cookie_file = None
    log_file = 'log.txt'
#    log_file = os.path.devnull
    output_file = 'output.json'
    # main
    pyScraper.scraping(url=url, proxy_url=proxy_url, cookie_file=cookie_file, log_file=log_file, output_file=output_file)
