mysql -u root -p localtweets < table-schema.sql
mysql -u root -p localtweets < create-location-tables.sql
mysql -u root -p localtweets < alter-tweets-add-locs.sql
