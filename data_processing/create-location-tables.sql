DROP TABLE IF EXISTS states;

CREATE TABLE states (
	name text NOT NULL,
	fips_code int(10) NOT NULL,
	population int(15),
	two_letter_code varchar(2),
	PRIMARY KEY(fips_code), 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE INDEX state_two ON states (state_two_letter);

DROP TABLE IF EXISTS `counties`;

CREATE TABLE counties (
	name text,
	fips_code int(25) NOT NULL,
	population int(15),
	state_two_letter varchar(2),
	KEY `state_two_letter` (`state_two_letter`),
	CONSTRAINT `cnties_stat_fk1` FOREIGN_KEY (`state_two_letter`) REFERENCES `states` (`two_letter_code`),
	PRIMARY KEY (fips_code),
	UNIQUE KEY name (name)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


DROP TABLE IF EXISTS places;

CREATE TABLE places (
	name text NOT NULL,
	area_type_code varchar(3), 
	fips_code int(10) NOT NULL
	PRIMARY KEY(fips_code),
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS metros;

CREATE TABLE metros (
	name text NOT NULL, 
	code int(20),
	PRIMARY KEY(code)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

DROP TABLE IF EXISTS zctas;

CREATE TABLE zctas (
	zipcode int(5),
	state_two_letter VARCHAR(2),
	KEY `state_two_letter` (`state_two_letter`),
	CONSTRAINT `zctas_stat_fk1` FOREIGN_KEY (`state_two_letter`) REFERENCES `states` (`two_letter_code`),
	PRIMARY KEY(zipcode)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
