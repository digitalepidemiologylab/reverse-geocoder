ALTER TABLE zctas ADD FOREIGN KEY (state_two_letter) REFERENCES states (two_letter_code);
ALTER TABLE counties ADD FOREIGN KEY (state_two_letter) REFERENCES states (two_letter_code);

ALTER TABLE tweets ADD COLUMN county_fips int (25);
ALTER TABLE tweets ADD FOREIGN KEY (county_fips) REFERENCES `counties` (`fips_code`);

ALTER TABLE tweets ADD COLUMN place_fips int (25);
ALTER TABLE tweets ADD FOREIGN KEY (place_fips) REFERENCES places (fips_code);

ALTER TABLE tweets ADD COLUMN metro_code int(20);
ALTER TABLE tweets ADD FOREIGN KEY (metro_code) REFERENCES metros (code);

ALTER TABLE tweets ADD COLUMN state_fips int (10);
ALTER TABLE tweets ADD FOREIGN KEY (state_fips) REFERENCES states (fips_code);

ALTER TABLE tweets ADD COLUMN zcta int(5);
ALTER TABLE tweets ADD FOREIGN KEY (zcta) REFERENCES zctas (zipcode);
