ALTER TABLE tweets DROP CONSTRAINT `tweets_ibfk_1`;
ALTER TABLE tweets ADD FOREIGN KEY (county_fips) REFERENCES `counties` (`fips_code`);
ALTER TABLE tweets ADD FOREIGN KEY (place_fips) REFERENCES places (fips_code);
ALTER TABLE tweets ADD FOREIGN KEY (metro_code) REFERENCES metros (code);
ALTER TABLE tweets ADD FOREIGN KEY (state_fips) REFERENCES states (fips_code);
ALTER TABLE tweets ADD FOREIGN KEY (zcta) REFERENCES zctas (zipcode);
