LOAD DATA LOCAL INFILE '/opt/code/reverse-geocoder/data_processing/sql/census-places.txt'
INTO TABLE places FIELDS TERMINATED BY '\t'
(fips_code, name) 
