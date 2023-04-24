# -*- coding: utf-8 -*-
"""
Created on Sat May  8 13:10:34 2021

@author: tluen
"""

import pandas as pd
from serpapi import GoogleSearch
import time

# Set a list of queries for the search-bar to run through
queries = ['basmati rice 1 lb','loaf bread','oreos','soup','pot pie','eggs','top sirloin',
           'chicken breast','coca cola 1 liter','milk','creamer','1 pound coffee','apple juice',
           '1 gallon water','gatorade','red bull','cold brew','capri sun','steel shovel round point',
           'power drill','rug','vinyl flooring','caulk','hammer','3 shelf bookcase','chair','desk',
           'table','washing machine','sauce pan','spatula','toaster','kitchen aide',
           'barbie','settlers of catan','soccer ball','lego','ticket to ride','magic the gathering',
           'bicycle','vtech','nerf','monopoly','paper towels','trash bags',
           'plastic utensils','toilet paper','intel i7 10850k','apple watch','chromebook','go pro',
           'graphics card','1 tb hard drive','airpods pro','google nest','tshirt','shorts','pants',
           'sandals','jeans','baseball cap','ibuprofen','acetaminophen','bandage','thermometer',
           'vitamin d3','diapers','hardcover book','softcover book','bluray','nintendo switch','playstation',
           'binder','notepad','pens','pencils','scissors']

# Set a list of pages for the search-bar to run through
pages = ["1","2"]

# Set an empty dataframe to store observations
dfwx = pd.DataFrame()

# Begin for-loop

for query in queries:

    # Set an empty temporary dataframe to store observations
    dfw_temp = pd.DataFrame()

    # Set parameters for accessing the Google SerpAPI platform, running through each query in the queries list
    params = {
        "engine": "walmart",
        "query": query,
        "api_key": "API_KEY"
    }

    # Run the API, for each query store the JSON results in a dictionary and keep the observation-
    # section of the results
    search = GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results['organic_results']

    # Set the temporary dataframe to be the results from the API queries, and add today's date as a column vector
    dfw_temp = pd.DataFrame.from_dict(shopping_results)
    dfw_temp['query'] = query
    dfw_temp['date'] = pd.Timestamp("today").strftime("%m/%d/%Y")


    # Add the conditional statement to fill the original dataframe if empty, or append if there are
    # already observations contained in the dataframe.
    if dfwx.empty == True:
        dfwx = dfw_temp
    elif dfwx.empty == False:
        dfwx = dfwx.append(dfw_temp, ignore_index=True)
        
# Extract prices from 'primary_offer' dictionary-column
# Average min/max/offer price to normalize prices
dfwx = dfwx[dfwx['primary_offer'].notnull()]
dfwx_p = pd.json_normalize(dfwx['primary_offer'])
dfwx = pd.concat([dfwx,dfwx_p], axis=1)
dfwx['avg_price'] = dfwx[['min_price','max_price','offer_price']].mean(axis=1)
        
# Set a category column vector and set categories based on query
dfwx['category'] = dfwx['query']
dfwx.loc[(dfwx.category == 'basmati rice 1 lb'), 'category'] = 'foods'
dfwx.loc[(dfwx.category == 'loaf bread'), 'category'] = 'foods'
dfwx.loc[(dfwx.category == 'oreos'), 'category'] = 'foods'
dfwx.loc[(dfwx.category == 'soup'), 'category'] = 'foods'
dfwx.loc[(dfwx.category == 'pot pie'), 'category'] = 'foods'
dfwx.loc[(dfwx.category == 'eggs'), 'category'] = 'foods'
dfwx.loc[(dfwx.category == 'top sirloin'), 'category'] = 'foods'
dfwx.loc[(dfwx.category == 'chicken breast'), 'category'] = 'foods'
dfwx.loc[(dfwx.category == 'coca cola 1 liter'), 'category'] = 'drinks'
dfwx.loc[(dfwx.category == 'milk'), 'category'] = 'drinks'
dfwx.loc[(dfwx.category == 'creamer'), 'category'] = 'drinks'
dfwx.loc[(dfwx.category == '1 pound coffee'), 'category'] = 'drinks'
dfwx.loc[(dfwx.category == 'apple juice'), 'category'] = 'drinks'
dfwx.loc[(dfwx.category == '1 gallon water'), 'category'] = 'drinks'
dfwx.loc[(dfwx.category == 'gatorade'), 'category'] = 'drinks'
dfwx.loc[(dfwx.category == 'red bull'), 'category'] = 'drinks'
dfwx.loc[(dfwx.category == 'cold brew'), 'category'] = 'drinks'
dfwx.loc[(dfwx.category == 'capri sun'), 'category'] = 'drinks'
dfwx.loc[(dfwx.category == 'steel shovel round point'), 'category'] = 'home improvement'
dfwx.loc[(dfwx.category == 'power drill'), 'category'] = 'home improvement'
dfwx.loc[(dfwx.category == 'rug'), 'category'] = 'home improvement'
dfwx.loc[(dfwx.category == 'vinyl flooring'), 'category'] = 'home improvement'
dfwx.loc[(dfwx.category == 'caulk'), 'category'] = 'home improvement'
dfwx.loc[(dfwx.category == 'hammer'), 'category'] = 'home improvement'
dfwx.loc[(dfwx.category == '3 shelf bookcase'), 'category'] = 'home and furniture'
dfwx.loc[(dfwx.category == 'chair'), 'category'] = 'home and furniture'
dfwx.loc[(dfwx.category == 'desk'), 'category'] = 'home and furniture'
dfwx.loc[(dfwx.category == 'table'), 'category'] = 'home and furniture'
dfwx.loc[(dfwx.category == 'washing machine'), 'category'] = 'home and furniture'
dfwx.loc[(dfwx.category == 'sauce pan'), 'category'] = 'home and furniture'
dfwx.loc[(dfwx.category == 'spatula'), 'category'] = 'home and furniture'
dfwx.loc[(dfwx.category == 'toaster'), 'category'] = 'home and furniture'
dfwx.loc[(dfwx.category == 'kitchen aide'), 'category'] = 'home and furniture'
dfwx.loc[(dfwx.category == 'barbie'), 'category'] = 'toys and games'
dfwx.loc[(dfwx.category == 'settlers of catan'), 'category'] = 'toys and games'
dfwx.loc[(dfwx.category == 'soccer ball'), 'category'] = 'toys and games'
dfwx.loc[(dfwx.category == 'lego'), 'category'] = 'toys and games'
dfwx.loc[(dfwx.category == 'ticket to ride'), 'category'] = 'toys and games'
dfwx.loc[(dfwx.category == 'magic the gathering'), 'category'] = 'toys and games'
dfwx.loc[(dfwx.category == 'bicycle'), 'category'] = 'toys and games'
dfwx.loc[(dfwx.category == 'vtech'), 'category'] = 'toys and games'
dfwx.loc[(dfwx.category == 'nerf'), 'category'] = 'toys and games'
dfwx.loc[(dfwx.category == 'monopoly'), 'category'] = 'toys and games'
dfwx.loc[(dfwx.category == 'paper towels'), 'category'] = 'dry goods'
dfwx.loc[(dfwx.category == 'paper plates'), 'category'] = 'dry goods'
dfwx.loc[(dfwx.category == 'trash bags'), 'category'] = 'dry goods'
dfwx.loc[(dfwx.category == 'plastic utensils'), 'category'] = 'dry goods'
dfwx.loc[(dfwx.category == 'toilet paper'), 'category'] = 'dry goods'
dfwx.loc[(dfwx.category == 'intel i7 10850k'), 'category'] = 'electronics'
dfwx.loc[(dfwx.category == 'apple watch'), 'category'] = 'electronics'
dfwx.loc[(dfwx.category == 'chromebook'), 'category'] = 'electronics'
dfwx.loc[(dfwx.category == 'go pro'), 'category'] = 'electronics'
dfwx.loc[(dfwx.category == 'graphics card'), 'category'] = 'electronics'
dfwx.loc[(dfwx.category == '1 tb hard drive'), 'category'] = 'electronics'
dfwx.loc[(dfwx.category == 'airpods pro'), 'category'] = 'electronics'
dfwx.loc[(dfwx.category == 'google nest'), 'category'] = 'electronics'
dfwx.loc[(dfwx.category == 'tshirt'), 'category'] = 'clothing and accessories'
dfwx.loc[(dfwx.category == 'shorts'), 'category'] = 'clothing and accessories'
dfwx.loc[(dfwx.category == 'pants'), 'category'] = 'clothing and accessories'
dfwx.loc[(dfwx.category == 'sandals'), 'category'] = 'clothing and accessories'
dfwx.loc[(dfwx.category == 'jeans'), 'category'] = 'clothing and accessories'
dfwx.loc[(dfwx.category == 'baseball cap'), 'category'] = 'clothing and accessories'
dfwx.loc[(dfwx.category == 'ibuprofen'), 'category'] = 'health'
dfwx.loc[(dfwx.category == 'acetaminophen'), 'category'] = 'health'
dfwx.loc[(dfwx.category == 'bandage'), 'category'] = 'health'
dfwx.loc[(dfwx.category == 'thermometer'), 'category'] = 'health'
dfwx.loc[(dfwx.category == 'vitamin d3'), 'category'] = 'health'
dfwx.loc[(dfwx.category == 'diapers'), 'category'] = 'health'
dfwx.loc[(dfwx.category == 'hardcover book'), 'category'] = 'entertainment'
dfwx.loc[(dfwx.category == 'softcover book'), 'category'] = 'entertainment'
dfwx.loc[(dfwx.category == 'bluray'), 'category'] = 'entertainment'
dfwx.loc[(dfwx.category == 'nintendo switch'), 'category'] = 'entertainment'
dfwx.loc[(dfwx.category == 'playstation'), 'category'] = 'entertainment'
dfwx.loc[(dfwx.category == 'binder'), 'category'] = 'school and office'
dfwx.loc[(dfwx.category == 'notepad'), 'category'] = 'school and office'
dfwx.loc[(dfwx.category == 'pens'), 'category'] = 'school and office'
dfwx.loc[(dfwx.category == 'pencils'), 'category'] = 'school and office'
dfwx.loc[(dfwx.category == 'scissors'), 'category'] = 'school and office'

# Set today's date and save the dataframe as a CSV and XLSX file using today's date.
todaysdate = time.strftime("%d-%m-%Y")
dfwx.to_csv(r'~\World Bank\Data\Walmart Data\CSV Files\PPP data walmart api ' + 
           todaysdate + ' expanded.csv', index = False)
dfwx.to_excel(r'~\World Bank\Data\Walmart Data\Excel Files\PPP data walmart api ' + 
           todaysdate + ' expanded.xlsx', index = False)