CREATE TABLE Osoby
(
osCislo VARCHAR(7),
jmeno VARCHAR(20),
prijmeni VARCHAR(30),
stav VARCHAR(20),
obor VARCHAR(30),
rocnik SMALLINT,
email VARCHAR(50),
pohlavi VARCHAR(4),
datum_zahajeni_studia DATE,
datum_ukonceni_studia DATE,
kredity SMALLINT
);

INSERT INTO Osoby VALUES
('R1245','Jan','Novák','studuje','MATAP',2,'jan.novak06@upol.cz','muž','1.9.2017',null,12),
('R1246',null,null,'studuje','MMA',1,'anna.valkova01@upol.cz','žena','1.9.2018',null,10),
('R1247','Pavel','Holík','nestuduje','KMI',2,'pavel.holik02@upol.cz','muž','1.9.2017','31.7.2016',34),
('R1248','Pavel','Mareš','studuje','KMI',3,'pavel.mares02@upol.cz','muž','1.9.2016',null,67),
('R1249','Hana','Holíková','studuje','KMI',1,'hana.holikova03@upol.cz','žena','1.9.2016',null,40),
('R1250','Karel','Dlabal','nestuduje',null,1,null,'muž','1.9.2017',null,-5),
('R1251','Marie','Novotná','studuje',null,3,null,'žena','1.9.2017',null,null),
('R1251','Jan','Kinský','nestuduje',null,1,null,'muž','1.9.2017',null,null);

CREATE TABLE Predmety
(
id INT,
nazev VARCHAR(30),
katedra VARCHAR(4),
zkratka VARCHAR(6),
ucitel VARCHAR(30),
rok SMALLINT,
kapacita SMALLINT,
budova VARCHAR(4),
mistnost VARCHAR(6),
datum_od DATE,
datum_do DATE,
kredity SMALLINT,
CONSTRAINT id_pkey PRIMARY KEY(id)
)

INSERT INTO Predmety VALUES(402,	'Databáze',	'KMI',	'DB',	'Jiří Zacpal',	2018,56,	'LP',	'5006',	'12.2.2019',	'7.5.2019',5),
(543,	'Základní software',	'KMI',	'ZSW',	'Jiří Zacpal',	2018,36,	'LP',	'5002',	'18.9.2018',	'11.12.2018',4),
(224,	'Základy práce s PC L',	'KMI',	'ZPPCL',	'Jiří Zacpal',	2018,18,	'LP',	'5003',	'13.2.2019',	'8.5.2019',3),
(403,	'Algoritmy 1',	'KMI',	'ALG1',	'Arnošt Večerka',	2019,25,	'LP',	'5002',	'13.2.2020',	'8.5.2020',3);

