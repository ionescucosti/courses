	/* Cursoare */
    
DROP PROCEDURE IF EXISTS selectie;
drop table if exists NumeSupergrei;

DELIMITER /
CREATE PROCEDURE Selectie() 

BEGIN

	DECLARE n VARCHAR(100);
    DECLARE h, g INT;
	DECLARE supergreii CURSOR FOR 				-- declaram cursorul
		SELECT Numele, Inaltime, Greutate FROM paul.people1
        WHERE Greutate>100 LIMIT 500;
	DECLARE EXIT HANDLER FOR 1329 BEGIN END;	-- declaram handler specific erorii de terminarea cursorului

OPEN supergreii;								-- deschidem cursorul
	
bucla: LOOP

FETCH supergreii INTO n, h, g;					-- apelam fiecare inregistrare din result set
	IF h <170 or h > 190  THEN ITERATE bucla;	-- ducem valorile inregistrarii in variabilele n, h, g
    END IF;										-- cu exceptia celor cu h , 170	

INSERT INTO NumeSupergrei VALUES(n, h, g);		-- valorile fiecarei inregistrari sunt prelucrate
    
END LOOP;

CLOSE supergreii;								-- inchidem cursorul

END /    
DELIMITER ;

CREATE TABLE NumeSupergrei(`name` text,
	Inaltime INT, Greutate INT);

CALL selectie;

SELECT * FROM NUMESUPERGREI;

TRUNCATE TABLE NUMESUPERGREI;

	
    /* ALTERNATIV */		-- ACASA

DROP PROCEDURE IF EXISTS selectie;
drop table if exists NumeSupergrei;

DELIMITER /

CREATE PROCEDURE Selectie() BEGIN
	DECLARE n VARCHAR(100);
    DECLARE P VARCHAR(100);
    DECLARE h, gata INT;

DECLARE supergreii CURSOR FOR 
		SELECT Numele, Prenumele, Inaltime FROM paul.people1
        WHERE Greutate>100 LIMIT 100;
	DECLARE CONTINUE HANDLER FOR 1329 BEGIN SET gata=1; 
    END;

OPEN supergreii;
	bucla: LOOP

FETCH supergreii INTO n, p, h;
	IF gata=1 THEN LEAVE bucla;
    end IF;
	IF h <180 THEN ITERATE bucla;
    END IF;

INSERT INTO NumeSupergrei VALUES(n, p, h);
    END LOOP;

CLOSE supergreii;
	SELECT * FROM NUMESUPERGREI;

END /    
DELIMITER ;

CREATE TABLE IF NOT EXISTS NumeSupergrei(
	Numele text,
    Prenumele text,
	Inaltime INT);

CALL selectie;