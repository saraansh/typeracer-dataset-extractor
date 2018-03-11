# -*- coding: utf-8 -*-
"""
Updated on Sun Mar 11 13:53:37 2018

@author: Hopeless
"""

import pandas as pd
import numpy as np
import lxml.html
#import time

# Function to save user profile
def save_csv(user,link):
	# Extract profile data
	page = lxml.html.parse(link)
	tables = page.xpath('//table')
	# Extract user stats
	content = tables[2].xpath('.//tr/td//text()')
	rows = int(len(content)/6)
	stats = np.array(content).reshape(rows,6)
	# Export profile data
	df = pd.DataFrame(stats)
	df.to_csv(user + ".csv", header=None, index=None)

# Function to set parameters
def set_parameters(user):
	header = "http://www.typeracerdata.com/profile?"
	para1 = "username=" + user
	# Extract number of races
	tags = lxml.html.parse(header+para1).xpath("//td")
	races = tags[0].text_content()
	para2 = "&last=" + races
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
	save_csv(user,link)
	print (user+".csv saved!" + "\n\n")
	#time.sleep(2)