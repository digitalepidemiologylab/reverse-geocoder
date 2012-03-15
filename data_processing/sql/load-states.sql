LOAD DATA LOCAL INFILE '/opt/code/reverse-geocoder/data_processing/sql/census-states.txt'
INTO TABLE states 
(name, fips_code, two_letter_code)
