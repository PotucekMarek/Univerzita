CREATE TABLE Pozice
(
Nazev_Pozice VARCHAR(20),
HodinovaMzda INTEGER,
UNIQUE(Nazev_Pozice)
);

CREATE TABLE Zamestnanec
(
Jmeno VARCHAR(20),
Prijmeni VARCHAR(30),
Nazev_Pozice VARCHAR(20),
UNIQUE(Jmeno,Prijmeni)
);

CREATE TABLE Projekt
(
Nazev_Projektu VARCHAR(30),
Zahajeno DATE,
UNIQUE(Nazev_Projektu)
);

CREATE TABLE Prace_na_projektu
(
Jmeno VARCHAR(20),
Prijmeni VARCHAR(30),
Nazev_Projektu VARCHAR(30),
OdpracovaneHodiny INTEGER,
UNIQUE (Jmeno,Prijmeni,Nazev_Projektu)
);

INSERT INTO Pozice VALUES('elektrikáø',200);
INSERT INTO Pozice VALUES('analytik',150);
INSERT INTO Pozice VALUES('brigádník',70);
INSERT INTO Pozice VALUES('databázový návrháø',350);
INSERT INTO Pozice VALUES('programátor',250);
INSERT INTO Pozice VALUES('úèetní',200);

INSERT INTO Zamestnanec VALUES('Alice','Nováková','elektrikáø');
INSERT INTO Zamestnanec VALUES('Jitka','Smutná','databázový návrháø');
INSERT INTO Zamestnanec VALUES('František','Bláha','databázový návrháø');
INSERT INTO Zamestnanec VALUES('David','Skoupil','analytik');
INSERT INTO Zamestnanec VALUES('Jana','Rámová','analytik');
INSERT INTO Zamestnanec VALUES('Václav','Krása','programátor');
INSERT INTO Zamestnanec VALUES('Marie','Aloisová','programátor');
INSERT INTO Zamestnanec VALUES('Roman','Koubský','úèetní');
INSERT INTO Zamestnanec VALUES('Jan','Václav','úèetní');
INSERT INTO Zamestnanec VALUES('Jakub','Frommer','brigádník');



INSERT INTO Projekt VALUES('Amber','14.8.2014');
INSERT INTO Projekt VALUES('Evergreen','15.1.2014');
INSERT INTO Projekt VALUES('Rosmary','10.7.2014');
INSERT INTO Projekt VALUES('Starflight','1.1.2015');


INSERT INTO Prace_na_projektu VALUES('Jana','Rámová','Rosmary',23);
INSERT INTO Prace_na_projektu VALUES('Jana','Rámová','Amber',19);
INSERT INTO Prace_na_projektu VALUES('Jana','Rámová','Starflight',23);
INSERT INTO Prace_na_projektu VALUES('Jana','Rámová','Evergreen',23);
INSERT INTO Prace_na_projektu VALUES('Roman','Koubský','Starflight',24);
INSERT INTO Prace_na_projektu VALUES('Roman','Koubský','Amber',45);
INSERT INTO Prace_na_projektu VALUES('Roman','Koubský','Rosmary',44);
INSERT INTO Prace_na_projektu VALUES('Jakub','Fromer','Evergreen',64);
INSERT INTO Prace_na_projektu VALUES('Jakub','Fromer','Starflight',48);
INSERT INTO Prace_na_projektu VALUES('Jakub','Fromer','Rosmary',23);
INSERT INTO Prace_na_projektu VALUES('Jakub','Fromer','Amber',27);
INSERT INTO Prace_na_projektu VALUES('Jitka','Smutná','Amber',24);
INSERT INTO Prace_na_projektu VALUES('Alice','Nováková','Amber',45);
INSERT INTO Prace_na_projektu VALUES('Alice','Nováková','Rosmary',56);
INSERT INTO Prace_na_projektu VALUES('Alice','Nováková','Evergreen',33);
INSERT INTO Prace_na_projektu VALUES('Alice','Nováková','Starflight',23);