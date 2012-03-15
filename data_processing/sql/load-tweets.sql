LOAD DATA LOCAL INFILE '/opt/code/reverse-geocoder/data_processing/sql/tweets.txt' 
INTO TABLE tweets FIELDS TERMINATED BY '\t' OPTIONALLY ENCLOSED BY '"' LINES TERMINATED BY '\n'
