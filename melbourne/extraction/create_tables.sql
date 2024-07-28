CREATE TABLE melbourne_data.employment_per_block(

Census_year integer,
Block_ID integer,
CLUE_small_area varchar,
Accommodation integer,
Admin_and_Support_Services integer,
Agriculture_and_Mining integer,
Arts_and_Recreation_Services integer,
Business_Services integer,
Construction integer,
Education_and_Training integer,
Electricity_Gas_Water_and_Waste_Services integer,
Finance_and_Insurance integer,
Food_and_Beverage_Services integer,
Health_Care_and_Social_Assistance integer,
Information_Media_and_Telecommunications integer,
Manufacturing integer,
Other_Services integer,
Public_Administration_and_Safety integer,
Real_Estate_Services integer,
Rental_and_Hiring_Services integer,
Retail_Trade integer,
Transport_Postal_and_Storage integer,
Wholesale_Trade integer,
Total_jobs_in_block integer
);

CREATE TABLE melbourne_data.cafes_and_restaurants(

Census_year integer,
Block_ID integer,
Property_ID integer,
Base_property_ID integer,
Street_address varchar,
CLUE_small_area varchar,
Trading_name varchar,
Business_address varchar,
Industry_ANZSIC4_code varchar,
Industry_ANZSIC4_description varchar,
Seating_type varchar,
Number_of_seats numeric,
x_coordinate numeric,
y_coordinate numeric,
Location varchar
);

CREATE TABLE melbourne_data.building_access_bikes_space(

Census_year integer,
Block_ID integer,
Property_ID integer,
Base_property_ID integer,
Building_name varchar,
Street_address varchar,
CLUE_small_area varchar,
Construction_year numeric,
Refurbished_year numeric,
Number_of_floors_above_ground numeric,
Predominant_space_use varchar,
Accessibility_type varchar,
Accessibility_type_description varchar,
Accessibility_rating numeric,
Bicycle_spaces numeric,
Has_showers varchar,
x_coordinate numeric,
y_coordinate numeric,
Location varchar
);
