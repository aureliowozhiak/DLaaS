-- Adminer 4.8.1 MySQL 8.1.0 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `dlaas` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dlaas`;

DROP TABLE IF EXISTS `person`;
CREATE TABLE `person` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NAME` varchar(256) NOT NULL,
  `AGE` int NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `person` (`ID`, `NAME`, `AGE`) VALUES
(1,	'Bolt Crank',	-1),
(2,	'Iwakura Lain',	14),
(3,	'Koji Kabuto',	17),
(4,	'Mamiya Otaru',	18),
(5,	'Ban Midou',	21),
(6,	'Nada',	34),
(7,	'Ellen Ripley',	30);

-- 2023-09-27 23:54:25