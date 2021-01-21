	/* TRIGGER-E */ 

USE test;

drop table if exists oameni3;

CREATE TABLE oameni3 LIKE paul.people1;

select * from paul.people1 limit 1;

INSERT INTO oameni3 SELECT * FROM paul.people1 order by rand() LIMIT 5000;

SELECT * FROM oameni3;

TRUNCATE OAMENI3;

DELIMITER /
CREATE TRIGGER oameni3_BI BEFORE INSERT 
	ON oameni3 FOR EACH ROW
BEGIN
	IF NEW.inaltime < 165 
		THEN SET NEW.inaltime = 165;
	ELSEIF NEW.inaltime > 200
		THEN SET NEW.inaltime = 200;
    END IF;
    
    IF NEW.greutate < 70 
		THEN SET NEW.greutate = 70;
	ELSEIF NEW.greutate > 120
		THEN SET NEW.greutate = 120;
    END IF;
    
END /
DELIMITER ;

INSERT INTO oameni3 SELECT * FROM paul.people1 order by rand() LIMIT 5000;

SELECT * FROM oameni3;

truncate oameni3;


	/* EXEMPLUL 2 */
    
CREATE TABLE vizite(
	nume text, 
    prenume text,
    data_vizitei datetime);
    
DELIMITER /
CREATE TRIGGER vizite_BI BEFORE INSERT 
	ON vizite FOR EACH ROW
BEGIN
	IF NEW.data_vizitei IS NULL
		THEN SET NEW.data_vizitei=now();
	END IF;
END /
DELIMITER ;

INSERT INTO vizite(nume, prenume) VALUES ('Vasile', 'Vasile');
INSERT INTO vizite(nume, prenume) VALUES ('Ion', 'Ion');
INSERT INTO vizite(nume, prenume) VALUES ('Marin', 'Marin');
    
select * from vizite;

SHOW TRIGGERS;
SHOW CREATE TRIGGER vizite_BI;


	/* EXEMPLUL 3 */

drop table if exists oameni5;
Create Table oameni5(
	nume text,
    pren text,
    data date,
    lunan tinyint);
    
DROP TRIGGER IF EXISTS oameni5_BI;

INSERT INTO oameni5 VALUES
		('Georgescu', 'Vasile', '1978-09-15', 3),
        ('Patraru', 'Ciprian', '1993-08-5', 7),
        ('Cozma', 'George', '1966-12-31', 13);

DELIMITER /
CREATE TRIGGER oameni5_BI BEFORE INSERT 
	ON oameni5 FOR EACH ROW
BEGIN
	IF new.lunan <> month(NEW.data) 
		THEN SET new.lunan = month(NEW.data);
	END IF;
END /
DELIMITER ;

TRUNCATE oameni5;

INSERT INTO oameni5 VALUES
		('Georgescu', 'Vasile', '1978-09-15', 3),
        ('Patraru', 'Ciprian', '1993-08-5', 7),
        ('Cozma', 'George', '1966-12-31', 13);

SELECT * FROM oameni5;

DROP TABLE IF EXISTS oameni3;
DROP TABLE IF EXISTS oameni5;
drop table if exists vizite;    

drop TRIGGER oameni3_bi;
