LOAD DATA LOCAL INFILE '/opt/code/reverse-geocoder/data_processing/sql/census-counties.txt'
INTO TABLE zctas 
(zipcode)
