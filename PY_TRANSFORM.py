import pandas as pd

pd.set_option("display.max")

file_path= "AB_NYC_2019 -ascii (2).csv"

# EXTRACT--- LOAD


#LOAD INTO DATA

rawdf_df = pd.read_csv(file_path)

# Check for erroes, check data quality
#TODO: FILL NA OF REVIEWS PER MONTH-1
rawdf_df['last_review']= rawdf_df['last_review'].fillna('1900-01-01')

#TODO: FILL NA OF REVIEWS PER MONTH WITH-1
rawdf_df['last_review']= rawdf_df['last_review'].fillna('1900-01-01')

#change data type of last review to date


print(rawdf_df.describe())


# Transform into insights
# filter data set for manhattan

print(rawdf_df[rawdf_df['neighbourhood_group']=='Manhattan'])
high_value_manhattan=manhattan_df[manhattan_df]['price']> 150

print(len(high_value_manhattan))

print(rawdf_df[(rawdf_df['neighbourhood_group']== 'Brroklyn') & (raw_df['price'] > 150)])




# Case Statements
# if price between 0-100 "cheap"
#if price between 100-150 "moderate"
# if price is between 150-200 "average"
#if price is between 200+ "expensive"
rawdf_df.loc[(rawdf_df['price'] <=100) , "price_group"] = "cheap"
rawdf_df.loc[(rawdf_df['price'] >=200) , "price_group"] = "expensive"


# drop/add Columns
# remove column "host_name"
selected_cols=rawdf_df[['host_name' , 'price_group ' , 'price' , 'room_type' , ' neighbourhood_group']]

print(selected_cols.head)
# perform Joins
# Aggregates = Group By
# WHats the average price by room type by neighbourhood
selected_cols.groupby(['neighbourhood_group' , 'room_type']) ['price'].mean()
#---- Pivots 
# LOAD
# write the data to a table, or a view