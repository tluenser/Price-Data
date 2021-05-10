# Price-Data
Methods of using Google SerpAPI to collect price data and other relevant information for analyzing prices over time.

*********************************************************************
* Data for "GSE 580 World Bank Project title Purchasing Power Parity"
* Authors:
  - Ian Donovan
	- Brendan Hoang
	- Trevor Luenser
	- Russel McIntosh
* Date: 05/08/2021
*********************************************************************

INSTRUCTIONS

- 	This data zip contains the raw data for replicating the above paper.
	To replicate the paper you should:
a)	Change file paths from ~ to XXX, where XXX is your working directory
b)	Execute the scripts in this order:
	1)	table_2_stats.py
c)	The scripts will output the following data that are used in Section
   4 of the paper.
	1)	Replication of Table 2 in "Scraped Data and Sticky Prices" (Cavallo, 2015)

DATA COLLECTION REPLICATION INSTRUCTIONS

-	To replicate the process of data acquisition, perform the following steps:
a)	Use pip-install to load the Google SerpAPI package into Python:
	1)	pip install google-search-results
b)	Replace API_KEY, located under param in the API codes to your own API key for Google SerpAPI
c)	Execute the following files to perform the data collection:
	1) 	google_api.py			    # To replicate the Google Shopping data collection
	2) 	walmart_api_abbr.py		# To replicate the abbreviated Walmart data collection
	3)	walmart_api_exp.py		  # To replicate the expanded Walmart data collection
d)	Execute the following file to concatenate your datasets
	1)	data_concat.py
   
DATA DICTIONARY

- The raw data files are in both .csv and .xslx formats.
- Below is the file structure and purpose of each file.

GSE 580 World Bank Project title Purchasing Power Parity
data_requirements.txt				      # Dependencies for running data collection
model_requirements.txt				    # Dependencies for running models
collect_concat_walkthrough.txt		# Documentation of steps for data collection and concatenation of data files
variable_information.txt			    # Information about data variables
data_config.py						        # Configuration files for running data collection code (see DATA COLLECTION REPLICATION INSTRUCTIONS above)
model_config.py						        # Configuration files for running models
ADD YOUR FILE NAMES AND DESCRIPTIONS HERE!!!

FILE STRUCTURE

~World Bank/
|--- read_me.txt
|--- data_requirements.txt
|--- model_requirements.txt
|--- variable_information.txt
|---| Data/
	|--- collect_concat_walkthrough.txt
	|--- data_config.py
	|--- google_shopping_api.py
	|--- walmart_api_abbr.py
	|--- walmart_api_exp.py
	|--- google_shopping_concat.py
	|--- walmart_abbr_concat.py
	|--- walmart_exp_concat.py
	|---| Google Data/
		|--- google_data_full.csv
		|--- google_data_full.xslx
		|---| CSV Files/
			|--- PPP data google api 28-04-2021.csv
			|--- ...
			|--- PPP data google api nn-05-2021.csv
		|---| Excel Files/
			|--- PPP data google api 28-04-2021.xslx
			|--- ...
			|--- PPP data google api nn-05-2021.xslx
	|---| Google Data/
		|--- walmart_abbr_full.csv
		|--- walmart_abbr_full.xslx
		|--- walmart_exp_full.csv
		|--- walmart_exp_full.xslx
		|---| Walmart Abbreviated/
			|---| CSV Files/
				|--- PPP data walmart api 28-04-2021.csv
				|--- ...
				|--- PPP data walmart api nn-05-2021.csv
			|---| Excel Files/
				|--- PPP data walmart api 28-04-2021.xslx
				|--- ...
				|--- PPP data walmart api nn-05-2021.xslx
		|---| Walmart Expanded/
			|---| CSV Files/
				|--- PPP data walmart api 04-05-2021 expanded.csv
				|--- ...
				|--- PPP data walmart api nn-05-2021 expanded.csv
			|---| Excel Files/
				|--- PPP data walmart api 28-04-2021 expanded.xslx
				|--- ...
				|--- PPP data walmart api nn-05-2021 expanded.xslx
|---| Model/
	|--- model_walkthrough.txt
	|--- model_config.ipynb
	|--- CONTINUE WITH YOUR FILE NAMES AND PATHS HERE!!!
	|---|Cavallo Replication/
	    |--- table_2_stats.py
