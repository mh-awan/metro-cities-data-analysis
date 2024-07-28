#%%
import pandas as pd
from IPython.display import display;

#%%
pedestrian_data = pd.read_csv('data/pedestrian-counting-system-monthly-counts-per-hour.csv');
sensor_data = pd.read_csv('data/pedestrian-counting-system-sensor-locations.csv');

#%%
pedestrian_data

# first ten rows of pedestrian_data
pedestrian_data.head(10)
# first five rows of censor_data
sensor_data.head()

#%%
pedestrian_data.shape

#%%
print(sensor_data.shape);

#%%
print('dimensions of censor_data: ' + pedestrian_data.shape);
print('dimensions of censor_data: ' + pedestrian_data.shape);
print('**********');

#%%
display(sensor_data)
print('**********');
print('**********');
print('**********');
print(pedestrian_data, sensor_data);
print('**********');
print('**********');
print('**********');
# print(pedestrian_data.head(10), censor_data.head(10));
# print('dimensions of pedestrian_data: ', pedestrian_data.shape);

#%%
sensor_data.dtypes
sensor_data.info()

#%%
pedestrian_data.dtypes
pedestrian_data.info()

#%%
sensor_data.columns

sensor_data[['Sensor_Description', 'Latitude', 'Longitude']]

pedestrian_data.head(10)
pedestrian_data.head(-10)
pedestrian_data.tail(10)

pedestrian_data.sort_values(by = [''])

#%%
# 

print(pedestrian_data)
pedestrian_data.sort_values(by= ['Total_of_Directions'], ascending= True)


pedestrian_data[['Total_of_Directions']].sort_values(by= ['Total_of_Directions'], ascending= True)

print(len(sensor_data))
print(len(sensor_data.columns))

print(sensor_data['Location_Type'].unique())

#%%
sensor_data[sensor_data['Note'].notna()]
pedestrian_data[(pedestrian_data['Direction_1'] > 20) & (pedestrian_data['Direction_1'] > 15)]
pedestrian_data.columns

pedestrian_data[pedestrian_data['Sensor_Name'].isin(['Col700_T', 'BouHbr_T', 'WatCit_T', 'NewQ_T', 'SanBri_T'])]
#%%

condition = pedestrian_data['Total_of_Directions'] == pedestrian_data['Total_of_Directions'].max()
pedestrian_data[condition]

#%%

pedestrian_data.columns

df_grouped = pedestrian_data.groupby(['Sensor_Name', 'LocationID'])[['Direction_1', 'Direction_2', 'Total_of_Directions']].mean()
df_grouped = pedestrian_data.groupby(['Sensor_Name', 'LocationID'])[['Direction_1', 'Direction_2', 'Total_of_Directions']].agg(['min', 'max'])

sensor_data['Location_Type'].value_counts(normalize= True)
sensor_data['Location_Type'].value_counts(normalize= True, dropna = False)

#%%
df_grouped = pedestrian_data.groupby('Sensor_Name')['Total_of_Directions'].sum()
df_grouped = sensor_data['Direction_1'].value_counts()
df_grouped = sensor_data.groupby('Direction_1')['Sensor_Name'].agg(['count', 'nunique'])

# value counts works on series, 
# not on a dataframe so you can't use it in combination 
# with groupby
df_grouped = sensor_data['Direction_1'].value_counts(normalize=True)

#%%
df_inner_join = pedestrian_data.merge(sensor_data, how = 'inner', left_on='LocationID', right_on='Location_ID')
df_left_join = pedestrian_data.merge(sensor_data, how = 'left', left_on='LocationID', right_on='Location_ID')

#%%
all_data = pedestrian_data.merge(sensor_data, how = 'left', left_on='LocationID', right_on='Location_ID')
all_data = pedestrian_data.merge(sensor_data, how = 'left', left_on='LocationID', right_on='Location_ID', suffixes=['_Ped', '_Sens'])

#%%
display(len(sensor_data.Location_ID.unique()) == len(sensor_data))
duplication_predicate = sensor_data['Location_ID'].duplicated(keep=False)
sensor_data[duplication_predicate]['Location_ID'].unique
condition = (sensor_data['Location_ID']==44) & (sensor_data['Direction_2'].isin(['Out','South']))

sensor_data = sensor_data[~condition]

#%%
list_sensor_id = sensor_data.Location_ID.unique().tolist()
list_pedestrian_id = pedestrian_data.LocationID.unique().tolist()

list_diff_id = list(set(list_pedestrian_id) - set(list_sensor_id))

display(list_pedestrian_id)
display(list_sensor_id)
all_data = pedestrian_data.merge(sensor_data, how = 'left', left_on='LocationID', right_on='Location_ID', suffixes=['_Ped', '_Sens'])

#%%
renamed_columns = {
    'LocationID': 'Location_ID_Ped',
    'Location_ID': 'Location_ID_Sens',
    'SensingDateTime(Hour)': 'Sensing_Date_Time_Hour'
}
all_data.rename(columns = renamed_columns, inplace=True)

#%%
display(all_data[all_data['Sensor_Name_Ped'] != all_data['Sensor_Name_Ped']]['Sensor_Name_Ped'].unique())
display(all_data[all_data['Sensor_Name_Ped'] != all_data['Sensor_Name_Sens']]['Sensor_Name_Sens'].unique())

#%%
pedestrian_data[pedestrian_data.duplicated()]
all_data[all_data.duplicated()]

#%%
all_data.info()

#%%
all_data.astype({'Location_ID_Sens', 'int64'})

#%%
all_data.Sensing_Date_Time_Hour = pd.to_datetime(all_data['Sensing_Date_Time_Hour'], utc=True)
all_data['Year'] = all_data['Sensing_Date_Time_Hour'].dt.year
all_data['Weekday'] = all_data['Sensing_Date_Time_Hour'].dt.weekday
all_data['Month'] = all_data['Sensing_Date_Time_Hour'].dt.month
all_data['Day'] = all_data['Sensing_Date_Time_Hour'].dt.day
all_data['Hour'] = all_data['Sensing_Date_Time_Hour'].dt.hour

#%%
all_data.columns
columns_to_drop = ['Sensor_Name_Sens', 'Location_ID_Sens', 'Location_Sens', 'Note', 'Weekday']
columns_to_drop = ['Installation_Date', 'Status']
all_data.drop(columns=columns_to_drop, inplace=True)

processed_data = all_data.copy()
processed_data.to_csv('data/processed_pedestrian_sensor_data.csv')
