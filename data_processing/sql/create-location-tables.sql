ALTER TABLE tweets DROP FOREIGN KEY `tweets_ibfk_1`;
ALTER TABLE tweets DROP COLUMN county_id;
DROP TABLE IF EXISTS counties;
DROP TABLE IF EXISTS zctas;
DROP TABLE IF EXISTS states;

CREATE TABLE states (
	name text NOT NULL,
	fips_code int(10) NOT NULL,
	population int(15),
	two_letter_code varchar(2),
	PRIMARY KEY(fips_code) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE INDEX state_two ON states (two_letter_code);


CREATE TABLE counties (
	name text NOT NULL,
	fips_code int(25) NOT NULL,
	population int(15),
	state_two_letter varchar(2),
	PRIMARY KEY (fips_code)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS places;

CREATE TABLE places (
	name text NOT NULL,
	area_type_code varchar(3), 
	fips_code int(25) NOT NULL,
	PRIMARY KEY(fips_code)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS metros;

CREATE TABLE metros (
	name text NOT NULL, 
	code int(20),
	PRIMARY KEY(code)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


CREATE TABLE zctas (
	zipcode int(5),
	state_two_letter VARCHAR(2),
	PRIMARY KEY(zipcode)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
