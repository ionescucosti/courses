	/* Declararea conditiilor si handlerelor */

DROP TABLE IF EXISTS catalog;
DROP PROCEDURE IF EXISTS handtest;

CREATE TABLE catalog(
	Nume VARCHAR(100) UNIQUE,
	Nota INT(2)
    );

CREATE TABLE logs(
		Moment DATETIME,
        Coment TEXT);
    
INSERT INTO catalog(Nume, Nota) VALUES 
	('Vasile',5),
	('Maria',10),
	('Ion',8),
	('George',7);
    
delimiter /
CREATE PROCEDURE handtest(Nu text, No int)

BEGIN 

	DECLARE dublare CONDITION FOR 1062;

    DECLARE CONTINUE handler for dublare
    hand: begin
    INSERT INTO logs VALUES(NOW(), 
    nu);
    end hand;

	INSERT INTO catalog VALUES (Nu, No);
	
END /
DELIMITER ;
        
CALL handtest('Vasile', 5);
CALL handtest('Maria', 10);
CALL handtest('Ion', 8);
CALL handtest('Costica', 7);

SELECT * FROM CATALOG;
SELECT * FROM logs;

DROP TABLE IF EXISTS catalog;
DROP TABLE IF EXISTS logs;
DROP PROCEDURE IF EXISTS handtest;
