PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE person (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(256) NOT NULL,
    AGE INTEGER NOT NULL
);
INSERT INTO person VALUES(1,	'Bolt Crank',	-1);
INSERT INTO person VALUES(2,	'Iwakura Lain',	14);
INSERT INTO person VALUES(3,	'Koji Kabuto',	17);
INSERT INTO person VALUES(4,	'Mamiya Otaru',	18);
INSERT INTO person VALUES(5,	'Ban Midou',	21);
INSERT INTO person VALUES(6,	'Nada',	34);
INSERT INTO person VALUES(7,	'Ellen Ripley',	30);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('person',7);
COMMIT;
