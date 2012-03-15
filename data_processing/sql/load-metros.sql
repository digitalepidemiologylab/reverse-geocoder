LOAD DATA LOCAL INFILE '/opt/code/reverse-geocoder/data_processing/sql/census-metros.txt'
INTO TABLE metros FIELDS TERMINATED BY '\t'
(code, name) 
