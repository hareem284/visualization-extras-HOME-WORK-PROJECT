#importing matplotlib
import matplotlib.pyplot as plt
#importing pandas as pd
import pandas as pd
#importing statistics
import statistics as st
#importing seaborn
import seaborn as sns
#reading dataframe
df=pd.read_csv("FuelConsumption (7).csv")
print(df.info())
#checking for any null values
df.isnull().any()
#just leaving a space to organize my work
meanfueltype=st.mean(df['FUELTYPE'])
print("the mean of fuel type is na na na na!!!!" , meanfueltype)
#creating a barplot on fueltype
sns.set_color_codes('blue')
sns.set_style('darkgrid')
sns.set_theme('poster')
sns.barplot(df,x='FUELTYPE',palette='viridis')