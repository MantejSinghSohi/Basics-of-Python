import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# experiment 1
dataframe = pd.read_csv('sales_data.csv')
# When you read a CSV file using pd.read_csv() from the Pandas library in Python, the data is typically stored as a Pandas DataFrame.

dataframe.head(8)
# .head() function is used in pandas to print first few rows of a dataframe. By default it prints 5.

# experiment 2
# i am using isnull() function here. will create a dataframe of same dim as original. True-> empty position. False-> value exists
checker= dataframe.isnull()
# print(checker) # wherever the entry is true that means missing value

# go column by columnn in the checker dataframe to calculte the number of null vals and tabulate them
counter= list()
col_list= list()
for column_name in checker.columns:
  a= checker[column_name].sum()
  counter.append(a)
  col_list.append(column_name)


m= len(counter)
data= {
    'Column Name' : col_list,
    'No. of missing values' : counter,
}
df_missing= pd.DataFrame(data)
df_missing.head(m)

# using df.mean and df.fillna to meet the required purpose
mean_series= dataframe.mean(axis=0, skipna= True, numeric_only= True)# used numeric only true because it was giving a warning. now it will not try to calcuate mean for the columns which are invalid
dataframe= dataframe.fillna(mean_series)

# experiment 3
# creating a list named revenue containing the revenue values
revenue = []
for i in range (len(dataframe['Date'])):
  revenue.append(dataframe.loc[i, 'Quantity']*dataframe.loc[i, 'Price'])

# print(revenue)
# plotting
plt.plot(dataframe['Date'], revenue, label='plot line',color='green', linewidth= 5)
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=90) # rotated the label to avoid clutering
plt.title("Revenue vs Date ")
plt.legend(loc= 'upper center')
plt.show()

# experiment 4
tot_rev = 0
for i in range (len(revenue)):
  tot_rev = tot_rev + revenue[i]

tot_or = dataframe['Quantity'].sum()

print(f"Total number of Orders = {tot_or}")
print(f"Total revenue = {tot_rev}")

# experiment 5
# calculation of prices
revenue_A= 0
revenue_B= 0
revenue_C= 0
sale_A= 0
sale_B= 0
sale_C= 0
m= len(dataframe['Product'])
for i in range (m):
  if dataframe.loc[i,'Product']=='Product_A':
    revenue_A = revenue_A + (dataframe.loc[i, 'Quantity']*dataframe.loc[i, 'Price'])
    sale_A = sale_A + (dataframe.loc[i, 'Quantity'])
  elif dataframe.loc[i,'Product']=='Product_B':
    revenue_B = revenue_B + (dataframe.loc[i, 'Quantity']*dataframe.loc[i, 'Price'])
    sale_B = sale_B + (dataframe.loc[i, 'Quantity'])
  else:
    revenue_C = revenue_C + (dataframe.loc[i, 'Quantity']*dataframe.loc[i, 'Price'])
    sale_C = sale_C + (dataframe.loc[i, 'Quantity'])

avg_A = revenue_A/ sale_A
avg_B = revenue_B/ sale_B
avg_C = revenue_C/ sale_C
prod= ['Product_A', 'Product_B', 'Product_C']
avg= [avg_A, avg_B, avg_C]

# Plotting
plt.bar(prod, avg)
plt.xlabel('Product Types')
plt.ylabel('Average Price')
plt.title('Average Prices of different products')
plt.show()


print("\n")
# Finding the most sold product
maximum = max(sale_A, sale_B, sale_C)
if maximum== sale_A:
  print("Top Sold Product is A")

if maximum== sale_B:
  print("Top Sold Product is B")

if maximum== sale_C:
  print("Top Sold Product is C")