CREATE TABLE Autor
(
Jmeno VARCHAR(30),
Prijmeni VARCHAR(50),
UNIQUE(Jmeno,Prijmeni)
);

CREATE TABLE Kniha
(
ISBN VARCHAR(20),
Nazev VARCHAR(255),
JmenoAutora VARCHAR(30),
PrijmeniAutora VARCHAR(50),
UNIQUE(ISBN)  
);

CREATE TABLE Ctenar
(
Cislo INTEGER,
Jmeno VARCHAR(255),
Prijmeni VARCHAR(255),
Telefon VARCHAR(15),
UNIQUE(Cislo)
);

CREATE TABLE Vypujcka
(
Kniha VARCHAR(20),
Cislo INTEGER,
DatumVypujceni DATE,
Vraceno BOOLEAN
);

INSERT INTO Autor VALUES('Terry','Prattchet');
INSERT INTO Autor VALUES('Douglas','Adams');

INSERT INTO Kniha VALUES('9781529046137','Stopaøùv prùvodce po galaxii','Terry','Prattchet');
INSERT INTO Kniha VALUES('80-85609-28-2','Barva kouzel','Douglas','Adams');

INSERT INTO Ctenar VALUES(1,'Jan','Bumba','758 475 487');
INSERT INTO Ctenar VALUES(2,'Alice','Novotna','654 789 512');
INSERT INTO Ctenar VALUES(3,'Jitka','Pokorna','745 548 457');
INSERT INTO Ctenar VALUES(4,'Martin','Ferenc','214 758 469');

INSERT INTO Vypujcka VALUES ('9781529046137',1,'2001.3.17',True);
INSERT INTO Vypujcka VALUES ('9781529046137',2,'2002.6.20',False);
INSERT INTO Vypujcka VALUES ('80-85609-28-2',3,'2002.8.27',False);
INSERT INTO Vypujcka VALUES ('80-85609-28-2',4,'2001.1.1',True);


-- 1
SELECT ct.jmeno as jmeno, ct.prijmeni as prijmeni, vy.datumvypujceni as datumvypujceni from (TABLE ctenar) as ct NATURAL JOIN (table vypujcka) as vy where datumvypujceni BETWEEN '2000.12.31' and '2002.1.1'

-- 2
SELECT DISTINCT kniha.nazev FROM vypujcka, kniha, ctenar where (kniha.jmenoautora='Douglas')AND(ctenar.cislo=vypujcka.cislo)AND(ctenar.jmeno='Jan')and(ctenar.prijmeni='Bumba')

-- 3
select kn.nazev as nazev, ct.jmeno as jmeno, ct.prijmeni as prijmeni, vy.datumvypujceni as datumvypujceni from(TABLE ctenar) as ct NATURAL JOIN(table kniha) as kn NATURAL JOIN(table vypujcka) as vy where (vy.vraceno=False)and(kn.isbn=vy.kniha)

-- Potucek Marek