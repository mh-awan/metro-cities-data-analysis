-- rename melbourne_data to whatever is in local setup
SET search_path = my_schema, "$user", melbourne_data;

SELECT * FROM building_access_bikes_space LIMIT 5;
SELECT * FROM employment_per_block LIMIT 5;
SELECT * FROM cafes_and_restaurants LIMIT 5;
SET search_path = my_schema, "$user", melbourne_data;
select block_id, census_year from employment_per_block;

select * from cafes_and_restaurants;
select block_id, clue_small_area from cafes_and_restaurants;

select * from cafes_and_restaurants limit 5;
select block_id from building_access_bikes_space limit 10;

select COUNT(*) as total_count from building_access_bikes_space;

select COUNT(block_id) as total_count from cafes_and_restaurants;
select COUNT(*) as total_count from employment_per_block;

select distinct(clue_small_area) from cafes_and_restaurants;
select distinct(clue_small_area) from employment_per_block;
select distinct(clue_small_area) from building_access_bikes_space;

select * from cafes_and_restaurants LIMIT 1;
select count(distinct(clue_small_area)) from cafes_and_restaurants;
select count(distinct(block_id)) from cafes_and_restaurants;
select count(distinct(base_property_id)) from cafes_and_restaurants;
select count(distinct(property_id)) from cafes_and_restaurants;

select count(distinct(clue_small_area)) from employment_per_block;
select count(distinct(block_id)) from employment_per_block;

select distinct(clue_small_area) as suburbs
from cafes_and_restaurants
order by suburbs desc;

SELECT * FROM building_access_bikes_space LIMIT 5;

select distinct(accessibility_type) as unique_accessibility_type
from building_access_bikes_space
order by unique_accessibility_type;

select distinct(census_year)
from cafes_and_restaurants
order by census_year desc;

select distinct(clue_small_area) as suburbs
from cafes_and_restaurants
order by suburbs;

select * from cafes_and_restaurants where block_id = '5';

select * from cafes_and_restaurants where clue_small_area = 'North Melbourne';

select * from building_access_bikes_space LIMIT 1;
select * from building_access_bikes_space where bicycle_spaces < 50;

select * from cafes_and_restaurants where industry_anzsic4_description = 'Takeaway Food Services';
select trading_name from cafes_and_restaurants where number_of_seats > 50 and clue_small_area = 'Carlton';


select * from cafes_and_restaurants where clue_small_area != 'Southbank';

select distinct(street_address) from cafes_and_restaurants where clue_small_area = 'Southbank' and (industry_anzsic4_description != 'accommodation' or industry_anzsic4_description != 'common areas'); 


select count(distinct(trading_name)) from cafes_and_restaurants where census_year >= 2022;

select * from cafes_and_restaurants where clue_small_area not in ('Melbourne', 'South Yarra');

select street_address, clue_small_area from building_access_bikes_space where clue_small_area in ('North Melbourne', 'Kensington', 'Carlton');

select trading_name from cafes_and_restaurants where number_of_seats between 50 and 100;


select accessibility_type, * from building_access_bikes_space where accessibility_type like '%accessibility%';

select block_id, building_name, street_address, clue_small_area from building_access_bikes_space where building_name is not null;
select count(*) from building_access_bikes_space where refurbished_year is not null;
select count(distinct(block_id)) from building_access_bikes_space where refurbished_year is not null;



select count(distinct(trading_name)) from cafes_and_restaurants where census_year = 2022 and trading_name is not null;
select count(distinct(property_id)) from cafes_and_restaurants where census_year = 2022 and trading_name is not null;

select * from employment_per_block;
select count(distinct(block_id)) from employment_per_block 
where census_year = 2022 and block_id is not null and business_services > 200;

select count(distinct(property_id)) as total, clue_small_area from cafes_and_restaurants group by clue_small_area;
select count(distinct(property_id)) as total, block_id from cafes_and_restaurants group by block_id;

select count(distinct(block_id)) as total, clue_small_area from cafes_and_restaurants group by clue_small_area;

select count(distinct(block_id)) as total, clue_small_area from employment_per_block group by clue_small_area;
select count(distinct(census_year)) as total, block_id from employment_per_block group by block_id;

select * from cafes_and_restaurants limit 5;

select 
min(number_of_seats) as min_seats, round(avg(number_of_seats), 2), max(number_of_seats), clue_small_area, seating_type 
	from cafes_and_restaurants group by clue_small_area, seating_type order by clue_small_area;

select count(distinct(block_id)), clue_small_area 
from cafes_and_restaurants 
where census_year = 2022
group by clue_small_area

select property_id, count(distinct(trading_name)) as unq_trading_name
from cafes_and_restaurants
group by property_id
having count(distinct(trading_name)) > 1
order by unq_trading_name desc;

select clue_small_area, count(distinct(block_id)) as unique_blocks
from cafes_and_restaurants
group by clue_small_area
having count(distinct(block_id)) < 20;

select b.block_id, b.census_year, trading_name  
from cafes_and_restaurants c
inner join building_access_bikes_space b
on c.block_id = b.block_id
and c.census_year = b.census_year
inner join employment_per_block e
on e.block_id = b.block_id
and e.census_year = b.census_year;

select b.block_id, b.census_year, trading_name  
from cafes_and_restaurants c
left join building_access_bikes_space b
on c.block_id = b.block_id
and c.census_year = b.census_year
left join employment_per_block e
on c.block_id = e.block_id
and c.census_year = e.census_year;

select b.accessibility_type, trading_name
from cafes_and_restaurants c
left join building_access_bikes_space b
on c.block_id = b.block_id
and c.census_year = b.census_year
and c.property_id = b.property_id
where accessibility_type = 'High level of accessibility';

select *, concat(trading_name, ' , ', street_address) from cafes_and_restaurants limit 10;

select count(business_services)::float / count(accommodation)::float, clue_small_area 
from employment_per_block where census_year = 2022
group by clue_small_area;

select
    case
        when construction_year >= 1940 and construction_year <= 1980 then 'moderately old'
        when construction_year >= 1800 and construction_year <= 1939 then 'very old'
        when construction_year >= 1980 and construction_year <= 2022 then 'fairly new'
    else
        'unknown'
    end as bicycle_space_category, *
from building_access_bikes_space

select * from employment_per_block
where block_id in
    (
        select block_id from building_access_bikes_space where clue_small_area = 'Carlton'
    );

select trading_name from cafes_and_restaurants 
    where block_id in (
        select block_id from employment_per_block where business_services > 200
    );

with 
	moderate_access as (
	    select * from building_access_bikes_space 
        where accessibility_type in ('Moderate level of accessibility', 'High level of accessibility')
        and census_year = 2022
),
	accommodation_50 as (
        select * from employment_per_block where accommodation >= 50 and census_year = 2022;
),
	restaurants_2022 as (
        select * from cafes_and_restaurants where census_year = 2022;
)

select trading_name
from restaurants_2022 a
left join accommodation_50 b
on a.block_id = b.block_id
left join moderate_access c
on a.block_id = c.block_id
and a.property_id = c.property_id

create table cafes_and_restaurants_test_table as
    select * from cafes_and_restaurants where census_year = 2022

create table employment_per_block_test_table as
    select * from employment_per_block where census_year = 2022

create table building_access_bikes_space_test_table as
    select * from building_access_bikes_space where census_year = 2022

select * from cafes_and_restaurants where census_year = 2022;
select * from employment_per_block where business_services > 200 and accommodation > 100 and census_year = 2022;

select * from building_access_bikes_space;

with 
restaurants as (
    select * from cafes_and_restaurants 
    where census_year = 2022 
    and industry_anzsic4_description like '%Accommodation%'
    and seating_type = 'Seats - Indoor'
    and number_of_seats >= 100
),
req_space as (
    select * from employment_per_block 
    where business_services > 200 and (accommodation > 100 or retail_trade > 100) and census_year = 2022
),
moderate_access as (
    select * from building_access_bikes_space 
    where accessibility_type in ('Moderate level of accessibility', 'High level of accessibility')
    and 
    and census_year = 2022
),
select distinct(a.block_id)
from restaurants a
inner join req_space b
on a.block_id = b.block_id
inner join moderate_access c
on a.block_id = c.block_id;

select * from cafes_and_restaurants where industry_anzsic4_description like '%Accommodation%' and census_year = 2022;

select * from building_access_bikes_space limit 5;

select
    case
        when construction_year >= 1980 and construction_year <= 2022 then 'fairly new'
        when construction_year >= 1940 and construction_year <= 1980 then 'moderately old'
        when construction_year >= 1800 and construction_year <= 1939 then 'very old'
    else
        'unknown'
    end as bicycle_space_category, *
from building_access_bikes_space;

select * from employment_per_block
where block_id in
    (
        select block_id from building_access_bikes_space where clue_small_area = 'Carlton'
    );

select trading_name from cafes_and_restaurants 
    where block_id in (
        select block_id from employment_per_block where business_services > 200
    );

select * from cafes_and_restaurants where census_year = 2022;
select * from employment_per_block where accommodation >= 50;
select distinct(accessibility_type) from building_access_bikes_space ;

with 
	restaurants_2022 as (
        select * from cafes_and_restaurants where census_year = 2022
),
	accommodation_50 as (
        select * from employment_per_block where accommodation >= 50 and census_year = 2022
),
	moderate_access as (
	    select * from building_access_bikes_space 
        where accessibility_type in ('Moderate level of accessibility', 'High level of accessibility')
        and census_year = 2022
)

select distinct(trading_name)
from restaurants_2022 a
inner join accommodation_50 b
on a.block_id = b.block_id
inner join moderate_access c
on a.block_id = c.block_id
and a.property_id = c.property_id;

select * from information_schema.columns where table_schema = 'melbourne_data';

select * from information_schema.columns where table_schema = 'melbourne_data' and column_name like '%rating%';


select table_name, count(column_name) as column_name_count from information_schema.columns where table_schema = 'melbourne_data' group by table_name;

select distinct(seating_type) from cafes_and_restaurants where census_year = 2022;

select * from employment_per_block where business_services > 200;

select * from employment_per_block where business_services > 200 and accommodation > 100;

select * from building_access_bikes_space;

with 
restaurants as (
    select * from cafes_and_restaurants where census_year = 2022
),
req_space as (
    select * from employment_per_block 
    where business_services > 200 
	and (accommodation > 100 or retail_trade > 100)
	and census_year = 2022
	and food_and_beverage_services is not null
)
select distinct(a.block_id)
from restaurants a
inner join req_space b
on a.block_id = b.block_id;


select * from information_schema.columns where table_schema = 'melbourne_data' and column_name like '%anz%';

select food_and_beverage_services from employment_per_block where food_and_beverage_services is null;
select distinct(industry_anzsic4_description) from cafes_and_restaurants where industry_anzsic4_description like '%f%';

select * from cafes_and_restaurants where industry_anzsic4_description like '%Accommodation%' and census_year = 2022;

with 
restaurants as (
    select * from cafes_and_restaurants 
    where census_year = 2022 
    and industry_anzsic4_description like '%Accommodation%'
),
req_space as (
    select * from employment_per_block 
    where business_services > 200 and (accommodation > 100 or retail_trade > 100) and census_year = 2022
)
select distinct(a.block_id)
from restaurants a
inner join req_space b
on a.block_id = b.block_id;


select * from information_schema.columns where table_schema = 'melbourne_data' and column_name like '%seat%';

with 
restaurants as (
    select * from cafes_and_restaurants 
    where census_year = 2022 
    and industry_anzsic4_description like '%Accommodation%'
    and seating_type = 'Seats - Indoor'
    and number_of_seats >= 100
),
req_space as (
    select * from employment_per_block 
    where business_services > 200 and (accommodation > 100 or retail_trade > 100) and census_year = 2022
),
moderate_access as (
    select * from building_access_bikes_space 
    where accessibility_type in ('Moderate level of accessibility', 'High level of accessibility')
    and census_year = 2022
)
select distinct(a.block_id), a.property_id, trading_name, concat(trading_name, '-', a.street_address)
from restaurants a
inner join req_space b
on a.block_id = b.block_id
inner join moderate_access c
on a.block_id = c.block_id;


select count(*) as year_count, census_year
	from melbourne_data.cafes_and_restaurants
group by census_year
order by year_count desc;
