# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:47:34 2021

@author: tluen
"""

import pandas as pd
from serpapi import GoogleSearch
import time

# Set a list of locations for the Google to specify when seeking results
# This list causes the SerpAPI platform to iterate through different location urls
locations = ['USA','Japan','Germany','Sweden','Italy',
            'Paraguay','Brazil','Colombia','Guatemala','Mexico',
            'Nigeria','Kenya','Egypt','Morocco',
            'Indonesia','Bangladesh','India','Kazakhstan',
            'Israel','Oman','Russia']

# Set a list of queries for the search-bar to run through
queries = ['basmati rice 1 kg','loaf bread','coca cola 1 liter',
           'intel i7 10850k','steel shovel round point']

# Set an empty dataframe to store observations
dfg = pd.DataFrame()

# Begin for-loop
for location in locations:
    
    for query in queries:
        
        # Set an empty temporary dataframe to store observations
        df_temp = pd.DataFrame()
        
        # Set parameters for accessing the Google SerpAPI platform, running through each query and
        # location in their respective lists
        params = {
            "engine": "google",
            "q": query,
            "location_requested": location,
            "tbm": "shop",
            "api_key": "API_KEY"
        }
        
        # Run the API, for each query store the JSON results in a dictionary and keep the 
        # observation-section of the results
        search = GoogleSearch(params)
        results = search.get_dict()
        shopping_results = results['shopping_results']
        
        # Set the temporary dataframe to be the results from the API queries, and add today's date as 
        # a column vector
        df_temp = pd.DataFrame.from_dict(shopping_results)
        df_temp['query'] = query
        df_temp['location'] = location
        df_temp['date'] = pd.Timestamp("today").strftime("%m/%d/%Y")
        
        # Add the conditional statement to fill the original dataframe if empty, or append if there are
        # already observations contained in the dataframe.
        if dfg.empty == True:
            dfg = df_temp
        elif dfg.empty == False:
            dfg = dfg.append(df_temp, ignore_index=True)
            
dfg['category'] = dfg['query']
dfg.loc[(dfg.category == 'basmati rice 1 lb'), 'category'] = 'foods'
dfg.loc[(dfg.category == 'loaf bread'), 'category'] = 'foods'
dfg.loc[(dfg.category == 'coca cola 1 liter'), 'category'] = 'drinks'
dfg.loc[(dfg.category == 'intel i7 10850k'), 'category'] = 'electronics'
dfg.loc[(dfg.category == 'steel shovel round point'), 'category'] = 'home improvement'

# Set today's date and save the dataframe as a CSV and XLSX file using today's date.
todaysdate = time.strftime("%d-%m-%Y")
dfg.to_csv(r'~\World Bank\Data\Google Data\CSV Files\PPP data google api ' + 
           todaysdate + '.csv', index = False)
dfg.to_excel(r'~\World Bank\Data\Google Data\Excel Files\PPP data google api ' + 
             todaysdate + '.xlsx', index = False)