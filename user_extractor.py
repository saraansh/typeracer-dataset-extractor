# -*- coding: utf-8 -*-
"""
Updated on Sun Mar 11 02:53:02 2017

@author: Hopeless
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import lxml.html

# Set the parameters to load user list

header = "http://www.typeracerdata.com/leaders?"
para1 = "min_races=100&min_texts=100"
para2 = "&sort=wpm_textbests"
para3 = "&rank_start=1&rank_end=100"

# Load the page and extract profile links

page = header + para1 + para2 + para3
parsed_page = lxml.html.parse(page)
links = parsed_page.xpath("//a/@href")

# Print the links

for link in links:
	print(link)