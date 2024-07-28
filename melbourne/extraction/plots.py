#%%
import pandas as pd
import matplotlib.pyplot as plt

#%%
# timezone fixes to the data
data = pd.read_csv('processed_pedestrian_sensor_data.csv')

data['Sensing_Date_Time_Hour_Local'] = pd.DatetimeIndex(data['Sensing_Date_Time_Hour']).tz_convert('Australia/Melbourne')

data['Year'] = data['Sensing_Date_Time_Hour_Local'].dt.year
data['Month'] = data['Sensing_Date_Time_Hour_Local'].dt.month
data['Day'] = data['Sensing_Date_Time_Hour_Local'].dt.day
data['Hour'] = data['Sensing_Date_Time_Hour_Local'].dt.hour
data['WeekDay'] = data['Sensing_Date_Time_Hour_Local'].dt.day_name()


#%%
condition = data['Sensor_Description'].isin(['Flinders St (South)', 'Melbourne Central'])

data.columns

df_bar_plot = data[['Total_of_Directions', 'Sensor_Description']][condition]

df_bar_plot = df_bar_plot.groupby('Sensor_Description')['Total_of_Directions'].agg(['sum']).reset_index()

plt.bar(df_bar_plot['Sensor_Description'], df_bar_plot['sum'])

#%%
plt.barh(df_bar_plot['Sensor_Description'], df_bar_plot['sum'], color = 'red')
plt.show()

#%%
plt.barh(df_bar_plot['Sensor_Description'], df_bar_plot['sum'], color = 'brown')

plt.x

plt.ylabel('Number of pedestrians')
plt.xlabel('Locations')
plt.title('Number of pedestrians in chosen locations in the last year')
plt.ticklabel_format(style='plain')

plt.ylim(2000000, 10000000)

plt.show()

#%%
df_bar_plot = data[['Sensor_Description', 'Total_of_Directions']]
df_bar_plot = df_bar_plot[df_bar_plot['Sensor_Description'].notna()]
df_grouped = df_bar_plot.groupby('Sensor_Description')['Total_of_Directions'].agg(['sum'])

condition = data['Sensor_Description'].isin(['Flinders La-Swanston St (West)', 'Town Hall (West)', 'Melbourne Central', 'Elizabeth St - Flinders St (East) - New footpath', 'State Library - New'])

df_bar_plot = data[['Total_of_Directions', 'Sensor_Description']][condition]
df_bar_plot = df_bar_plot.groupby('Sensor_Description')['Total_of_Directions'].agg(['sum']).reset_index()

plt.barh(df_bar_plot['Sensor_Description'], df_bar_plot['sum'], color = 'brown')

plt.ylabel('Number of pedestrians')
plt.xlabel('Locations')
plt.title('Number of pedestrians in chosen locations in the last year')
# plt.ticklabel_format(style='plain')

# plt.ylim(2000000, 10000000)

plt.show()

#%%
df_scatter_plot = data[data['Sensor_Description'] == 'Melbourne Central']
df_scatter_plot = df_scatter_plot[df_scatter_plot['Year'] == 2023]

df_scatter_plot = df_scatter_plot[['Total_of_Directions', 'Month']]

df_scatter_plot = df_scatter_plot.groupby('Month')['Total_of_Directions'].agg(['mean']).reset_index()

x = df_scatter_plot['Month']
y = df_scatter_plot['mean']

plt.xlabel('Month')
plt.ylabel('Number of pedestrians')
plt.scatter(x, y, color='purple')
plt.show()

#%%
df_scatter_plot = data[data['Sensor_Description'] == 'Melbourne Central']
df_scatter_plot = df_scatter_plot[df_scatter_plot['Year'] == 2023]

df_scatter_plot = df_scatter_plot[['Total_of_Directions', 'WeekDay']]

df_scatter_plot = df_scatter_plot.groupby('WeekDay')['Total_of_Directions'].agg(['mean']).reset_index()

x = df_scatter_plot['WeekDay']
y = df_scatter_plot['mean']

plt.xlabel('WeekDay')
plt.ylabel('Number of pedestrians')
plt.scatter(x, y, color='purple')
plt.show()

# question for self: how do people cognize and perceive visualizations when they view them? how do our evolutionary-instinctive attenuations process them?

#%%
df_line_plot = data[data['Sensor_Description'] == 'Elizabeth St - Flinders St (East) - New footpath']
df_line_plot = df_line_plot[df_line_plot['Year'] == 2023]
df_line_plot = df_line_plot[['Total_of_Directions', 'Hour']]

df_line_plot = df_line_plot.groupby('Hour')['Total_of_Directions'].agg(['mean']).reset_index()

x = df_line_plot['Hour']
y = df_line_plot['mean']

plt.xlabel('Hour')
plt.ylabel('Number of pedestrians')
plt.plot(x, y, color = 'pink')
plt.show()


#%%
df_histogram = data.copy()
df_histogram = df_histogram[(df_histogram['Sensor_Description'] == 'State Library - New') & (df_histogram['Year'] == 2023)]

plt.hist(df_histogram['Total_of_Directions'], bins=8)
plt.show()

#%%
'''
high number of pedestrians

Index(['Unnamed: 0', 'Sensor_Name_Ped', 'Sensing_Date_Time_Hour',
       'Location_ID_Ped', 'Direction_1_Ped', 'Direction_2_Ped',
       'Total_of_Directions', 'Location_Ped', 'Sensor_Description',
       'Location_Type', 'Direction_1_Sens', 'Direction_2_Sens', 'Latitude',
       'Longitude', 'Year', 'Month', 'Day', 'Hour', 'WeekDay'],
      dtype='object')

'''

df_bar_plot = data[['Sensor_Description', 'Total_of_Directions']]
df_bar_plot = data[data['Total_of_Directions'] > 500]
df_bar_plot = data[data['Total_of_Directions'] > 1000]
df_bar_plot = data[data['Total_of_Directions'] > 2000]
df_bar_plot = data[data['Total_of_Directions'] > 3000]
df_bar_plot = data[data['Total_of_Directions'] > 4000]
df_bar_plot = data[data['Total_of_Directions'] > 5500]
df_bar_plot = data[data['Total_of_Directions'] > 6700]
df_bar_plot = data[data['Total_of_Directions'] > 7700]

df_bar_plot = df_bar_plot.groupby('Sensor_Description')['Total_of_Directions'].agg(['sum']).reset_index()

plt.bar(df_bar_plot['Sensor_Description'], df_bar_plot['sum'])
plt.xlabel('Locations')
plt.ylabel('Number of pedestrians')

plt.show()

#%%
'''
2. Hours of day with highest pedestrian count

Index(['Unnamed: 0', 'Sensor_Name_Ped', 'Sensing_Date_Time_Hour',
       'Location_ID_Ped', 'Direction_1_Ped', 'Direction_2_Ped',
       'Total_of_Directions', 'Location_Ped', 'Sensor_Description',
       'Location_Type', 'Direction_1_Sens', 'Direction_2_Sens', 'Latitude',
       'Longitude', 'Year', 'Month', 'Day', 'Hour', 'WeekDay'],
      dtype='object')

'''

df_line_plot = data[data['Sensor_Description'] == 'Southbank']
df_line_plot = df_line_plot[['Total_of_Directions', 'Hour']]
df_line_plot = df_line_plot.groupby('Hour')['Total_of_Directions'].agg(['mean']).reset_index()


x = df_line_plot['Hour']
y = df_line_plot['mean']

plt.xlabel('Hour')
plt.ylabel('Number of pedestrians')
plt.plot(x, y, color = 'pink')
plt.show()

plt.scatter(x, y, color='purple')
plt.show()

#%%
'''
1. Days of week with highest pedestrian count

Index(['Unnamed: 0', 'Sensor_Name_Ped', 'Sensing_Date_Time_Hour',
       'Location_ID_Ped', 'Direction_1_Ped', 'Direction_2_Ped',
       'Total_of_Directions', 'Location_Ped', 'Sensor_Description',
       'Location_Type', 'Direction_1_Sens', 'Direction_2_Sens', 'Latitude',
       'Longitude', 'Year', 'Month', 'Day', 'Hour', 'WeekDay'],
      dtype='object')

'''

df_line_plot = data[data['Sensor_Description'] == 'Southbank']
df_line_plot = df_line_plot[['Total_of_Directions', 'WeekDay']]
df_line_plot = df_line_plot.groupby('WeekDay')['Total_of_Directions'].agg(['mean']).reset_index()


x = df_line_plot['WeekDay']
y = df_line_plot['mean']

plt.xlabel('WeekDay')
plt.ylabel('Number of pedestrians')
plt.plot(x, y, color = 'pink')
plt.show()

plt.scatter(x, y, color='purple')
plt.show()


#%%
'''
Trends for the last few months for Southbank

Index(['Unnamed: 0', 'Sensor_Name_Ped', 'Sensing_Date_Time_Hour',
       'Location_ID_Ped', 'Direction_1_Ped', 'Direction_2_Ped',
       'Total_of_Directions', 'Location_Ped', 'Sensor_Description',
       'Location_Type', 'Direction_1_Sens', 'Direction_2_Sens', 'Latitude',
       'Longitude', 'Year', 'Month', 'Day', 'Hour', 'WeekDay'],
      dtype='object')

'''

df_line_plot = data[data['Sensor_Description'] == 'Southbank']
df_line_plot = data[data['Year'] == 2023]
df_line_plot = df_line_plot[['Total_of_Directions', 'Month']]
df_line_plot = df_line_plot.groupby('Month')['Total_of_Directions'].agg(['mean']).reset_index()


x = df_line_plot['Month']
y = df_line_plot['mean']

plt.xlabel('Month')
plt.ylabel('Number of pedestrians')
plt.plot(x, y, color = 'pink')
plt.show()

plt.plot(x, y, color='purple')
plt.show()

#%%
df_histogram = data.copy()
df_histogram = df_histogram[(df_histogram['Sensor_Description'] == 'Southbank') & (df_histogram['Year'] == 2023) & (df_histogram['Month'] == 7)]

plt.hist(df_histogram['Total_of_Directions'], bins=8)
plt.show()
