# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 03:32:18 2018

@author: Hopeless
"""

import lxml.html
import time

# Function to save user profile
def save_csv(user,link):
	with open(user+".csv") as f:
		dfs = []

# Function to set parameters
def set_parameters(user):
	header = "http://www.typeracerdata.com/profile?"
	para1 = "username=" + user
	# Extract number of races
	tags = lxml.html.parse(header+para1).xpath("//td")
	para2 = "&last=" + tags[0].text_content()
	# Return the new link
	return (header + para1 + para2)


# Load the user list

users = []
with open('user_list.txt') as f:
	users = f.read().splitlines()

# Extract profile for each user

for user in users:
	link = set_parameters(user)
	print ("Received Link -> " + link + "\n")
	#time.sleep(1)
	#save_csv(user,link)
	#print (user+".csv saved!" + "\n\n")