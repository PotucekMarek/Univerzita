CREATE TABLE prace_na_projektu
(
cislo_projektu INTEGER,
jmeno_projektu VARCHAR(20),
cislo_zamestnance INTEGER,
jmeno_zamestnance VARCHAR(50),
pozice VARCHAR(20),
hodinova_mzda INTEGER,
hodiny numeric(5),
vyplata INTEGER
);


INSERT INTO prace_na_projektu VALUES (15,'Evergreen',103,'Alice Nováková','Elektrikář',200,23.8,4760),
(15,'Evergreen',101,'František Bláha','Databázový návrhář',350,19.4,6790),
(15,'Evergreen',105,'Jitka Smutná','Databázový návrhář',350,35.7,12495),
(15,'Evergreen',106,'Václav Krása','Programátor',150,12.6,1890),
(15,'Evergreen',102,'David Skoupil','Analytik',300,23.8,7140),
(18,'Amber',114,'Anna Jánská','Návrhář aplikace',120,24.6,2952),
(18,'Amber',118,'Jakub Frommer','Brigádník',70,45.3,3171),
(18,'Amber',104,'Jana Rámová','Analytik',300,32.4,9720),
(18,'Amber',112,'Darina Sladká','Analytik DSS',225,44,9900),
(22,'Rosmary',105,'Jitka Smutná','Databázový návrhář',350,64.7,22645),
(22,'Rosmary',104,'Jana Rámová','Analytik',300,48.4,14520),
(22,'Rosmary',113,'Daniel John','Návrhář aplikace',120,23.6,2832),
(22,'Rosmary',111,'Jan Václav','Účetní',130,22,2860),
(22,'Rosmary',106,'Václav Krása','Programátor',150,12.8,1920),
(25,'Starflight',107,'Marie Aloisová','Programátor',150,24.6,3690),
(25,'Starflight',115,'Tomáš Vidím','Analytik',300,45.8,13740),
(25,'Starflight',101,'František Bláha','Databázový návrhář',350,56.3,19705),
(25,'Starflight',114,'Anna Jánská','Návrhář aplikace',120,33.1,3972),
(25,'Starflight',108,'Roman Koubský','Analytik',300,23.6,7080),
(25,'Starflight',118,'Jakub Frommer','Brigádník',70,30.5,2135),
(25,'Starflight',112,'Darina Sladká','Analytik DSS',225,41.4,9315);

