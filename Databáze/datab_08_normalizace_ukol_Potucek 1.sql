CREATE TABLE knihovna
(
ISBN VARCHAR(20),
nazev_knihy VARCHAR(255),
nakladatel VARCHAR(20),
rok_vydani INTEGER,
pocet_stran INTEGER,
autor VARCHAR(60),
datum_narozeni DATE,
datum_umrti DATE
);

INSERT INTO knihovna VALUES ('K001','�ivot, vesm�r a v�bec','MF',1987,256,'Douglas Adams','11.03.1952','11.05.2001'),
('K002','Sbohem a d�k za ty ryby','MF',1990,237,'Douglas Adams','11.03.1952','11.05.2001'),
('K003','Stopa��v pr�vodce po galaxii','MF',1985,214,'Douglas Adams','11.03.1952','11.05.2001'),
('K025','Barva kouzel','Tallpress',1989,250,'Terry Pratchet','1948.04.28','12.03.2015'),
('K026','Str�e! Str�e!','Tallpress',2000,302,'Terry Pratchet','1948.04.28','12.03.2015'),
('K027','Lehk� fantasti�no','Tallpress',1999,248,'Terry Pratchet','1948.04.28','12.03.2015'),
('K028','Velk� j�zda','Tallpress',2001,264,'Terry Pratchet','1948.04.28','12.03.2015'),
('K029','Sek��','Tallpress',2002,258,'Terry Pratchet','1948.04.28','12.03.2015'),
('K030','Pohybliv� obr�zky','Tallpress',2003,325,'Terry Pratchet','1948.04.28','12.03.2015'),
( 'K031','Erik','Tallpress',2005,189,'Terry Pratchet','1948.04.28','12.03.2015'),
('K032','Soudn� sestry','Tallpress',2008,179,'Terry Pratchet','1948.04.28','12.03.2015'),
('K043','Hobit','MF',1950,325,'JohnRonaldReuel Tolkien','3.1.1892','02.09.1973'),
('K044','P�n prsten� - Spole�enstvo prstenu','MF',1946,312,'JohnRonaldReuel Tolkien','3.1.1892','02.09.1973'),
('K045','P�n prsten� - Dv� v�e','MF',1948,365,'JohnRonaldReuel Tolkien','3.1.1892','02.09.1973'),
('K046','P�n prsten� - N�vrat kr�le','MF',1952,325,'JohnRonaldReuel Tolkien','3.1.1892','02.09.1973'),
('K051','Kedrigern a hlas pro princeznu','Odeon',1996,214,'John Morresy','08.12.1930','2006.03.20'),
('K054','Kedrigern a kouzeln� p�r','Odeon',1998,215,'John Morresy','08.12.1930','2006.03.20'),
('K059','Den trifid�','Odeon',1945,289,'John Wyndham','10.07.1903','11.03.1969');

ALTER TABLE knihovna
ADD CONSTRAINT knihovna_isbn_pkey PRIMARY KEY
(isbn);

ALTER TABLE knihovna
ADD COLUMN prijmeni_autora VARCHAR(40);

ALTER TABLE knihovna
ADD COLUMN jmeno_autora VARCHAR(40);

UPDATE knihovna SET jmeno_autora=left(autor,
position(' ' in autor)-1), 
prijmeni_autora=right(autor,char_length(autor
)-position(' ' in autor));

ALTER TABLE knihovna
DROP COLUMN autor;

CREATE TABLE kniha
(
isbn VARCHAR(20),
nakladatel VARCHAR(40),
rok_vydani INTEGER,
pocet_stran INTEGER,
CONSTRAINT isbn_pkey PRIMARY KEY (isbn)
);

INSERT INTO kniha SELECT DISTINCT isbn, nakladatel, rok_vydani, pocet_stran FROM knihovna;

ALTER TABLE knihovna
DROP COLUMN nakladatel;

ALTER TABLE knihovna
DROP COLUMN rok_vydani;

ALTER TABLE knihovna
DROP COLUMN pocet_stran;

CREATE TABLE autor
(
jmeno_autora VARCHAR(40),
datum_narozeni DATE,
datum_umrti DATE,
CONSTRAINT pkey PRIMARY KEY (datum_narozeni)
);

INSERT INTO autor SELECT DISTINCT jmeno_autora, datum_narozeni, datum_umrti FROM knihovna


ALTER TABLE knihovna
DROP COLUMN jmeno_autora;

ALTER TABLE knihovna
DROP COLUMN datum_narozeni;

ALTER TABLE knihovna
DROP COLUMN datum_umrti;


