	/* Incheierea fortata a executiei unui bloc: LEAVE */
    

USE test;
DROP PROCEDURE IF EXISTS test5;

DELIMITER /

CREATE PROCEDURE test5(x int, y int) -- DETERMINISTIC

UNU: BEGIN 

	DECLARE a,b int UNSIGNED;
    set @iter = 0; -- numaram cate iteratii s-au facut

    IF x < 1 OR y < 1 OR x = y THEN
		SELECT 'Parametrii trebuie sa fie diferiti si mari ca zero' AS EROARE;
        LEAVE UNU;
	ELSE SET a = x, b = y;
	END IF;

    DOI: REPEAT
		SET a = a * 3 + 1;
        SET b = b * 2 + 1;
		set @iter = @iter +1;
		UNTIL b >=200 OR a >=100 
	
    END REPEAT DOI;

SELECT a, b, @iter;
    
END/
DELIMITER ;

call test5(0,100);
CALL test5(10, 0);
CALL test5(15, 15);
CALL test5(5,110);
CALL test5(5,6);

DROP PROCEDURE IF EXISTS blok;