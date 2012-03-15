LOAD DATA LOCAL INFILE '/opt/code/reverse-geocoder/data_processing/sql/census-counties.txt'
INTO TABLE counties FIELDS TERMINATED BY '\t'
(fips_code, name,state_fips) 
