DROP DATABASE IF EXISTS `uebung`;
CREATE DATABASE IF NOT EXISTS `uebung`;
USE `uebung`;

CREATE TABLE personen (
	ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	Nachname VARCHAR(64) NOT NULL,
	Vorname VARCHAR(64) NOT NULL,
	LAND INT,
	SPRACHE INT
);

CREATE TABLE laender (
	ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	Name VARCHAR(64) NOT NULL
);

CREATE TABLE sprachen (
	ID INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	Name VARCHAR(64) NOT NULL
);

ALTER TABLE `personen` 
ADD CONSTRAINT FOREIGN KEY (`LAND`)
REFERENCES `laender` (`ID`)
ON DELETE SET NULL
ON UPDATE CASCADE;

ALTER TABLE `personen` 
ADD CONSTRAINT FOREIGN KEY (`SPRACHE`)
REFERENCES `sprachen` (`ID`)
ON DELETE SET NULL
ON UPDATE CASCADE;

-- ----------------------------------------------
-- Einfügen von Ländern
-- ----------------------------------------------
INSERT INTO laender ( ID, Name ) VALUES ( 1, 'Österreich' );
INSERT INTO laender ( ID, Name ) VALUES ( 2, 'Deutschland' );
INSERT INTO laender ( ID, Name ) VALUES ( 3, 'Schweiz' );

-- ----------------------------------------------
-- Einfügen von Sprachen
-- ----------------------------------------------
INSERT INTO sprachen ( ID, Name ) VALUES ( 1, 'Deutsch' );
INSERT INTO sprachen ( ID, Name ) VALUES ( 2, 'Englisch' );
INSERT INTO sprachen ( ID, Name ) VALUES ( 3, 'Italienisch' );

-- ----------------------------------------------
-- Einfügen von Personen
-- ----------------------------------------------
INSERT INTO personen ( ID, Nachname, Vorname, LAND, SPRACHE ) VALUES ( 1, 'Brenneis', 'Jan', 1, 1 );
INSERT INTO personen ( ID, Nachname, Vorname, LAND, SPRACHE ) VALUES ( 2, 'Bruckmoser', 'Desiree', 1, 1 );
INSERT INTO personen ( ID, Nachname, Vorname, LAND, SPRACHE ) VALUES ( 3, 'Eder', 'Thomas', 1, 1 );
INSERT INTO personen ( ID, Nachname, Vorname, LAND, SPRACHE ) VALUES ( 4, 'Kreuzer', 'Christoph', 1, 1 );
INSERT INTO personen ( ID, Nachname, Vorname, LAND, SPRACHE ) VALUES ( 5, 'Löschke', 'Simon', 1, 1 );
INSERT INTO personen ( ID, Nachname, Vorname, LAND, SPRACHE ) VALUES ( 6, 'Pollheimer', 'Lukas', 1, 1 );
INSERT INTO personen ( ID, Nachname, Vorname, LAND, SPRACHE ) VALUES ( 7, 'Renner', 'Daniel', 1, 1 );
INSERT INTO personen ( ID, Nachname, Vorname, LAND, SPRACHE ) VALUES ( 8, 'Samardzic', 'Amir', 1, 1 );
INSERT INTO personen ( ID, Nachname, Vorname, LAND, SPRACHE ) VALUES ( 9, 'Topal', 'Florian', 1, 1 );
INSERT INTO personen ( ID, Nachname, Vorname, LAND, SPRACHE ) VALUES ( 10, 'Trivunovic', 'Dejan', 1, 1 );
