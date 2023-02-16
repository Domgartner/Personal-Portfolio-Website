DROP DATABASE IF EXISTS ARTMUSEUM;
CREATE DATABASE ARTMUSEUM;
USE ARTMUSEUM;

DROP TABLE IF EXISTS Art_Objects;
CREATE TABLE Art_Objects(
	Artist				varchar(40),
    Artist_ID			INT NOT NULL,
    Title				varchar(50),
    Descriptions 		varchar(60),
    Collection_name		varchar(40),
    Culture_origin		varchar(15),
    Year_created		INT,
    Epoch				varchar(15),
    ID_number			INT not null,
    
	primary key(ID_number, Artist_ID, Collection_name)
);

INSERT INTO Art_Objects (Artist, Artist_ID, Title, Collection_name, descriptions, Culture_origin, Year_created, Epoch, ID_number)
VALUES
('Guillim Scrots', '5000', 'Edward VI', 'European Paintings', 'Portrait of King Edward VI', 'English',1547, 'Tudor', '1000'),  																																-- Edward VI
('Quentin Metsys', '5001', 'Elizabeth I', 'European Paintings', 'Portrait of Queen Elizabeth I', 'Netherlands', 1583, 'Elizabethan era', '1001'), 																			-- Elizabeth I ("The Sieve Portrait")
('Edgefield District potter', 5002, 'Face Cup', 'The American Wing', 'Alkaline glazed stoneware', 'American', 1850, 'Merchant era', '1002'),  																									-- Face Cup
('Manufactory Tournai', 5003, 'Coffeepot', 'European Sculpture and Decorative Arts', 'Coffeepot made of soft-paste porcelain', 'Belgian',1780, 'Georgian Era', '1003'),																				-- Coffeepot
('Pablo Picasso', 5004, 'The Absinthe Glass', 'European Sculpture and Decorative Arts', 'Rendering of a glass of alcohol','Spanish',1914,'Cubism','1004'),      																							-- The Absinthe Glass
('Benedetto da Rovezzano', 5005, 'Candelabrum', 'European Sculpture and Decorative Arts', 'Candle Holder','English', 1500, 'Middle Ages', '1005'),						 																					-- Candelabrum
('Benedetto da Rovezzano', 5005, 'Angel Bearing Candlestick', 'European Sculpture and Decorative Arts', 'Designed for the tomb of Cardinal Thomas Wolsey','English',1524,'Renaissance',1006),		 													-- Angle bearing candlestick
('Pietro Torrigiano', 5006, 'Portrait of John Fisher', 'European Sculpture and Decorative Arts', 'Bishop of Rochester','English',1510,'Renaissance',1007),	-- Portrait Bust of John Fisher, Bishop of Rochester
('David Drake', 5007, 'Storage Jar', 'The American Wing', 'By enslaved African American potter and poet David Drake', 'American', 1858, 'Modern', 1008);																						-- Storage Jar

ALTER TABLE Art_Objects ADD INDEX (Artist_ID);
ALTER TABLE Art_Objects ADD INDEX (Collection_name);


DROP TABLE IF EXISTS Artist;
CREATE TABLE Artist(
	Artist_name			varchar(40),
    Artist_ID			INT NOT NULL,
    Date_born			INT,
    Date_died			INT,
    Epoch				varchar(15),
    Country_origin		varchar(15),
    Main_style			varchar(20),
    Descriptions		varchar(120),
    
    foreign key(Artist_ID) references Art_Objects(Artist_ID) ON DELETE CASCADE
);

INSERT INTO Artist (Artist_name, Artist_ID, Date_born, Date_died, Epoch, Country_origin, Main_style, Descriptions)
VALUES
('Guillim Scrots', 5000, 1537, 1553, 'Tudor', 'England', "Mannerist", "William (or Guillim) Scrots was an English painter of the Tudor Court"), -- Edward VI
('Quentin Metsys', 5001, 1543, 1589, 'Tudor', 'Belgium', NULL, 'Flemish Renaissance painter, active as artists of the Tudor court in the reign of Elizabeth I of England'),   -- Elizabeth I ("The Sieve Portrait")
('Manufactory Tournai', 5003, Null, Null, Null, Null, Null, Null),	-- Facecup
('Edgefield District Potter', 5002, Null, Null, Null, Null, Null, Null),	-- Coffeepot
('Pablo Picasso', 5004, 1881, 1973,'Cubism','Spain','Cubsim',"Spanish painter, sculptor, ceramicist considered one of the greatest and most influential artists of the 20th century"), -- The Absinthe Glass
('Benedetto da Rovezzano', 5005, 1474, 1552,'Middle Ages','Italy', 'Renaissance', 'Italian architect and sculptor who worked mainly in Florence'),	-- Candelabrum
-- ('Benedetto da Rovezzano', 5005, 1474, 1554,'Reniassance', 'Italy','Angelic Work','Benedetto Grazzini, best known as Benedetto da Rovezzano (1474 – 1552) was an Italian architect and sculptor'), -- Anglebearing candle stick
('Pietro Torrigiano', 5006, 1472, 1528,'Reniassance','Italy', 'Realism','This man had a splendid person and a most arrogant spirit, with the air of a great soldier more than a sculptor'), -- Portrait Bust of John Fisher, Bishop of Rochester
('David Drake', 5007, 1800, 1865, 'Victorian Era', 'America', NULL, 'Enslaved African American potter and poet'); -- Storage Jar



DROP TABLE IF EXISTS Collections;
CREATE TABLE Collections (
	Col_name			varchar(40),
    Col_type			varchar(50),
    Descriptions		varchar(100),
    Curr_contact		varchar(40),
    Phone				integer,
    Address				varchar(40),
    
    foreign key (Col_name) references Art_Objects(Collection_name) ON DELETE CASCADE
);

INSERT INTO Collections (Col_name, Col_type, Descriptions, Curr_contact, Phone, Address)
VALUES
('European Paintings', 'Museum', 'Collection of European paintings from the thirteenth through the early twentieth century','The Met Fifth Avenue', 2125357710, '1000 Fifth Avenue New York'),					#Edward VI
-- ('The Met Collection', 'European Paintings', 'Collection of European paintings from the thirteenth through the early twentieth century','The Met Fifth Avenue', 2125357710, '1000 Fifth Avenue New York'),					#Elizabeth I ("The Sieve Portrait")
( 'The American Wing', 'Personal','Collection of works by African American, Euro American, Native American, and Latin American artists', 'The Met Fifth Avenue', 2125357710, '1000 Fifth Avenue New York'),		#Facecup
('European Sculpture and Decorative Arts', 'Museum','Museums comprehensive collection of European sculpture and decorative arts', 'The Met Fifth Avenue', 2125357710, '1000 Fifth Avenue New York');			#Coffeepot
-- ('The Met Collection', 'European Sculpture and Decorative Arts',' Museums comprehensive collection of European sculpture and decorative arts', 'The Met Fifth Avenue', 2125357710, '1000 Fifth Avenue New York'),			#The Absinthe Glass
-- ('The Met Collection', 'European Sculpture and Decorative Arts',' Museums comprehensive collection of European sculpture and decorative arts', 'The Met Fifth Avenue', 2125357710, '1000 Fifth Avenue New York'),			#Candelabrum
-- ('The Met Collection', 'European Sculpture and Decorative Arts',' Museums comprehensive collection of European sculpture and decorative arts', 'The Met Fifth Avenue', 2125357710, '1000 Fifth Avenue New York'),			#Anglebearing candle stick
-- ('The Met Collection', 'European Sculpture and Decorative Arts',' Museums comprehensive collection of European sculpture and decorative arts', 'The Met Fifth Avenue', 2125357710, '1000 Fifth Avenue New York'),			#Portrait Bust of John Fisher, Bishop of Rochester
-- ('The Met Collection', 'The American Wing', 'Collection of works by African American, Euro American, Native American, and Latin American artists', 'The Met Fifth Avenue', 2125357710, '1000 Fifth Avenue New York');		#Storage Jar



DROP TABLE IF EXISTS Exhibition;
CREATE TABLE Exhibition (
	Exhibition_name		varchar(80),
    Start_date			DATE,
    End_date			DATE,
	Object_ID			INT,
    
    foreign key(Object_ID) references Art_Objects(ID_number) ON DELETE CASCADE
);

INSERT INTO Exhibition (Exhibition_name, Start_date, End_date, Object_ID)
VALUES
('The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08', 1000),					-- Edward VI
('The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08', 1001),				-- Elizabeth I ("The Sieve Portrait")
('Cubism: The Leonard A. Lauder Collection','2014-09-20', '2015-02-16', 1004), 							-- The Absinthe Glass
('The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08', 1005), 				-- caldembrum
('The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08', 1006), 				-- Angle bearing candle stick
('The Tudors: Art and Majesty in Renaissance England', '2022-10-10', '2023-01-08', 1007), 				-- Portrait Bust of John Fisher, Bishop of Rochester
('Hear Me Now: The Black Potters of Old Edgefield, South Carolina', '2022-09-09', '2023-02-05', 1002),		-- face Cup
('Cubism and the Trompe l’Oeil Tradition', '2022-10-20', '2023-01-22', 1003), 								-- Coffeepot
('Hear Me Now: The Black Potters of Old Edgefield, South Carolina', '2022-09-09', '2023-02-05', 1008);		-- storage Jar


DROP TABLE IF EXISTS Painting;
CREATE TABLE Painting (
	Drawn_on		varchar(10),
    Style			varchar(15),
    Paint_type		varchar(15),
    ID_number		INT NOT NULL,
    
    foreign key(ID_number) references Art_Objects(ID_number) ON DELETE CASCADE
);

INSERT INTO Painting (Drawn_on, Style, Paint_type, ID_number)
VALUES
('Panel','anamorphosis' ,'Oil', 1000),	-- Edward VI
('Canvas','Netherlandish', 'Oil', 1001);	-- Elizabeth I ("The Sieve Portrait")


DROP TABLE IF EXISTS Sculpture;
CREATE TABLE Sculpture (
	Height_in		integer,
    Weight_kg		integer,	
    Style			varchar(15),
    Material		varchar(20),
    ID_number		INT NOT NULL,
    
    foreign key(ID_number) references Art_Objects(ID_number) ON DELETE CASCADE

);

INSERT INTO Sculpture (Height_in, Weight_kg, Style, Material, ID_number)
VALUES
(8.87, NULL, "liberalism", "Bronze", 1004),		-- The Absinthe Glass
(133.85, 622, "Royal", "Bronze", 1005); 		-- Candelabrum



DROP TABLE IF EXISTS Statue;
CREATE TABLE Statue (
	Height_ft		integer,
    Weight_kg		integer,	
    Style			varchar(15),
    Material		varchar(30),
    ID_number		INT NOT NULL,
    
    foreign key(ID_number) references Art_Objects(ID_number) ON DELETE CASCADE
    
);

INSERT INTO Statue (Height_ft, Weight_kg, Style, Material, ID_number)
VALUES
(40.56,177.5,"Drapery","Bronze", 1006), 					   		-- Angel Bearing Candlestick
(24.25,28.1,"Portrait"," Polychrome terracotta", 1007); 			-- Portrait Bust of John Fisher, Bishop of Rochester



DROP TABLE IF EXISTS Other;
CREATE TABLE Other (    
	Other_type			varchar(15),
	Style				varchar(15),
    ID_number			INT NOT NULL,
    
    foreign key(ID_number) references Art_Objects(ID_number) ON DELETE CASCADE
);

INSERT INTO Other (Other_type, Style, ID_number)
VALUES
('Pottery', 'stoneware', 1002),     -- Face Cup
('Ceramics', 'Modern', 1003), 		-- Coffeepot
('Pottery', 'stoneware', 1008);		-- Storage Jar


DROP TABLE IF EXISTS Borrowed;
CREATE TABLE Borrowed (
	Date_borrowed		Date,
    Date_returned		date,
    ID_number			INT NOT NULL,
    Collection_from		varchar(40),
    
    foreign key(ID_number) references Art_Objects(ID_number) ON DELETE CASCADE,
    foreign key(Collection_from) references Collections(Col_name) ON DELETE CASCADE
);


INSERT INTO Borrowed (Date_borrowed, Date_returned, Collection_from, ID_number)
VALUES
('2022-10-10', '2023-01-08', 'European Paintings', 1000),							-- Edward VI
('2022-10-10', '2023-01-08', 'European Paintings', 1001),							-- Elizabeth I ("The Sieve Portrait")
('2022-10-10', '2023-01-08', 'The American Wing', 1002),							-- Face Cup
('2014-09-20', '2015-02-16', 'European Sculpture and Decorative Arts', 1004), 		-- The Absinthe Glass
('2022-10-10', '2023-01-08', 'European Sculpture and Decorative Arts', 1006),		-- Angle bearing candle stick
('2022-10-10', '2023-01-08', 'European Sculpture and Decorative Arts', 1005);		-- Candlebraum


DROP TABLE IF EXISTS Permanent_collection;
CREATE TABLE Permanent_collection (
	Permanent_Status		varchar(15),		
    Date_acquired			Varchar(20),
    Cost_CDN				INT,
    ID_number				INT NOT NULL,
    
    Foreign Key (ID_number) references Art_Objects(ID_number) ON DELETE CASCADE
);

INSERT INTO Permanent_collection (Permanent_status, Date_acquired, Cost_CDN, ID_number)
VALUES
('On Display', '2010-08-09', 1890, 1003),		-- Coffeepot
('On Display', '2008-06-11', 420, 1008),		-- Storage Jar
('On Display', '2005-01-18', 650, 1007);		-- Portrait Bust of John Fisher, Bishop of Rochester


DROP TABLE IF EXISTS users;
CREATE TABLE users (
	username 		VARCHAR(40) NOT NULL UNIQUE,
    user_role		VARCHAR(20) NOT NULL
);

INSERT INTO users (username, user_role)
VALUES
('user1', 'Admin');

DROP ROLE IF EXISTS db_admin@localhost, read_access@localhost;
CREATE ROLE db_admin@localhost, read_access@localhost;
GRANT ALL PRIVILEGES ON Artmuseum.* TO db_admin@localhost;
GRANT Select ON Artmuseum.* TO read_access@localhost;

DROP USER IF EXISTS mk@localhost;
DROP USER IF EXISTS guest@localhost;

CREATE USER mk@localhost IDENTIFIED WITH mysql_native_password BY 'Password';
CREATE USER guest@localhost;
GRANT db_admin@localhost TO mk@localhost;
GRANT read_access@localhost TO guest@localhost;
SET DEFAULT ROLE ALL TO mk@localhost;
SET DEFAULT ROLE ALL TO guest@localhost;
