	/* Instructiuni repetitive: LOOP */

USE test;
DROP PROCEDURE IF EXISTS CUMPARA;

DELIMITER $
CREATE PROCEDURE CUMPARA(limita INT UNSIGNED, pret DECIMAL(8,2) UNSIGNED)
COMMENT 'cumpara maxim ''Numar'' actiuni la pretul de ''Pret'' lei, in total maxim ''Limita'' lei'

BEGIN 

	DECLARE numar INT UNSIGNED DEFAULT 0;
    DECLARE total INT UNSIGNED DEFAULT 0;

    bucla: LOOP
		        
        SET Numar = Numar + 1;
        SET Total = Numar * Pret;
        
			IF Total>= Limita THEN LEAVE bucla;
			END IF;
	END LOOP;
        
	SELECT Numar;
END $
DELIMITER ;

CALL cumpara(80000,2.25);

DROP PROCEDURE IF EXISTS cumpara;
        
        