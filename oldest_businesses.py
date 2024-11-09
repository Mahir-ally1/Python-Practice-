# Data Sources and Credits - https://projects.datacamp.com/projects/2510



import pandas as pd

# Load the data
businesses = pd.read_csv("data/businesses.csv")
new_businesses = pd.read_csv("data/new_businesses.csv")
countries = pd.read_csv("data/countries.csv")
categories = pd.read_csv("data/categories.csv")




business_with_continent = businesses.merge(countries, how = 'inner', on = 'country_code')

old_business = business_with_continent.groupby(['continent'])['year_founded'].min().reset_index()

oldest_business_continent = old_business.merge(business_with_continent, how = 'inner', on = ['continent','year_founded'])[['continent','country','business','year_founded']]

oldest_business_continent.head()




all_business = pd.concat([new_businesses, businesses])

all_business_with_continent = all_business.merge(countries, on='country_code', how = 'outer', indicator = True)
                                                 
missing_countries = all_business_with_continent[all_business_with_continent['_merge']!="both"]
                                                 
count_missing = missing_countries.groupby("continent").agg({"country":"count"})
count_missing.columns = ["count_missing"]



business_with_continent_category = business_with_continent.merge(categories, on='category_code', how = 'inner')

oldest_by_continent_category = business_with_continent_category.groupby(['continent','category'])['year_founded'].min().reset_index()

oldest_by_continent_category.head()
