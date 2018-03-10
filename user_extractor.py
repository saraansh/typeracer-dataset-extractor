# -*- coding: utf-8 -*-
"""
Updated on Sun Mar 11 03:27:44 2017

@author: Hopeless
"""

import lxml.html

# Set the parameters to load user list

header = "http://www.typeracerdata.com/leaders?"
para1 = "min_races=100&min_texts=100"
para2 = "&sort=wpm_textbests"
para3 = "&rank_start=1&rank_end=100"

# Load the page and extract all links

page = header + para1 + para2 + para3
parsed_page = lxml.html.parse(page)
links = parsed_page.xpath("//a/@href");

# Extract usernames and profile links

users = ['saraansh']
user_links = ['/profile?username=saraansh']
for link in links:
	if(link[0:9]=='/profile?'):
		users.append(link[18:])
		user_links.append(link)

# Saving usernames to user_list

with open('user_list.txt','w+') as f:
	for user in users:
		f.write(user + "\n")

"""
Usernames or profile links can be used
interchangeably to generate each other.
Pick either to be saved for future use.
""" 