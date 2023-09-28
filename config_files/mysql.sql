CREATE SCHEMA IF NOT EXISTS dlaas;
USE dlaas;
CREATE TABLE person (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
);
INSERT INTO `person` VALUES ('João'), ('Maria'), ('José');