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

INSERT INTO Pozice VALUES('elektrik��',200);
INSERT INTO Pozice VALUES('analytik',150);
INSERT INTO Pozice VALUES('brig�dn�k',70);
INSERT INTO Pozice VALUES('datab�zov� n�vrh��',350);
INSERT INTO Pozice VALUES('program�tor',250);
INSERT INTO Pozice VALUES('��etn�',200);

INSERT INTO Zamestnanec VALUES('Alice','Nov�kov�','elektrik��');
INSERT INTO Zamestnanec VALUES('Jitka','Smutn�','datab�zov� n�vrh��');
INSERT INTO Zamestnanec VALUES('Franti�ek','Bl�ha','datab�zov� n�vrh��');
INSERT INTO Zamestnanec VALUES('David','Skoupil','analytik');
INSERT INTO Zamestnanec VALUES('Jana','R�mov�','analytik');
INSERT INTO Zamestnanec VALUES('V�clav','Kr�sa','program�tor');
INSERT INTO Zamestnanec VALUES('Marie','Aloisov�','program�tor');
INSERT INTO Zamestnanec VALUES('Roman','Koubsk�','��etn�');
INSERT INTO Zamestnanec VALUES('Jan','V�clav','��etn�');
INSERT INTO Zamestnanec VALUES('Jakub','Frommer','brig�dn�k');



INSERT INTO Projekt VALUES('Amber','14.8.2014');
INSERT INTO Projekt VALUES('Evergreen','15.1.2014');
INSERT INTO Projekt VALUES('Rosmary','10.7.2014');
INSERT INTO Projekt VALUES('Starflight','1.1.2015');


INSERT INTO Prace_na_projektu VALUES('Jana','R�mov�','Rosmary',23);
INSERT INTO Prace_na_projektu VALUES('Jana','R�mov�','Amber',19);
INSERT INTO Prace_na_projektu VALUES('Jana','R�mov�','Starflight',23);
INSERT INTO Prace_na_projektu VALUES('Jana','R�mov�','Evergreen',23);
INSERT INTO Prace_na_projektu VALUES('Roman','Koubsk�','Starflight',24);
INSERT INTO Prace_na_projektu VALUES('Roman','Koubsk�','Amber',45);
INSERT INTO Prace_na_projektu VALUES('Roman','Koubsk�','Rosmary',44);
INSERT INTO Prace_na_projektu VALUES('Jakub','Fromer','Evergreen',64);
INSERT INTO Prace_na_projektu VALUES('Jakub','Fromer','Starflight',48);
INSERT INTO Prace_na_projektu VALUES('Jakub','Fromer','Rosmary',23);
INSERT INTO Prace_na_projektu VALUES('Jakub','Fromer','Amber',27);
INSERT INTO Prace_na_projektu VALUES('Jitka','Smutn�','Amber',24);
INSERT INTO Prace_na_projektu VALUES('Alice','Nov�kov�','Amber',45);
INSERT INTO Prace_na_projektu VALUES('Alice','Nov�kov�','Rosmary',56);
INSERT INTO Prace_na_projektu VALUES('Alice','Nov�kov�','Evergreen',33);
INSERT INTO Prace_na_projektu VALUES('Alice','Nov�kov�','Starflight',23);