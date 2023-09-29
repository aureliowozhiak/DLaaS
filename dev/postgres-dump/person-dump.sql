-- Adminer 4.8.1 PostgreSQL 16.0 (Debian 16.0-1.pgdg120+1) dump

\connect "dlaas";

DROP TABLE IF EXISTS "person";
DROP SEQUENCE IF EXISTS "person_ID_seq";
CREATE SEQUENCE "person_ID_seq" INCREMENT  MINVALUE  MAXVALUE  CACHE ;

CREATE TABLE "public"."person" (
    "id" integer DEFAULT nextval('"person_ID_seq"') NOT NULL,
    "name" character varying(256) NOT NULL,
    "age" integer NOT NULL,
    CONSTRAINT "person_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

INSERT INTO "person" ("id", "name", "age") VALUES
(1,	'Bolt Crank',	-1),
(2,	'Iwakura Lain',	14),
(3,	'Koji Kabuto',	17),
(4,	'Mamiya Otaru',	18),
(5,	'Ban Midou',	21),
(6,	'Nada',	34),
(7,	'Ellen Ripley',	30);

-- 2023-09-28 00:18:47.113708+00
