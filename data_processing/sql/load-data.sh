echo "loading states"
mysql -u root -p localtweets < load-states.sql
echo "loading counties"
mysql -u root -p localtweets < load-counties.sql
echo "loading zipcodes"
mysql -u root -p localtweets < load-zips.sql
echo "loading metros"
mysql -u root -p localtweets < load-metros.sql
echo "loading places"
mysql -u root -p localtweets < load-places.sql
