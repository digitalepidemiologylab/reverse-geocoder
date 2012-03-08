
#Here is an example of how to create one of the models from a shape file. 

python manage.py ogrinspect world/data/tiger_zcta_2010/tl_2010_us_zcta510.shp
ZipCode --srid=4326 --mapping --multi > models/zipcode.py
