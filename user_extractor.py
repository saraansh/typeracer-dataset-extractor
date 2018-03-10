# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 16:25:01 2017

@author: Hopeless
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from http.client import IncompleteRead

# Set the parameters to load user list

header = "http://www.typeracerdata.com/leaders?"
para1 = "min_races=100&min_texts=100"
para2 = "&sort=wpm_textbests"
para3 = "&rank_start=1&rank_end=100"

# Load the page and parse html

try:
	page = urlopen(header + para1 + para2 + para3).read()
except IncompleteRead as e:
	page = e.partial

soup = bs(page, "html.parser")

# Find all profile links

print([tag.attrMap['href'] for tag in soup.findAll('a', {'href': True})])