	/* Instructiuni repetitive : REPEAT */
    
	USE test;
	/* Instructiuni repetitive : REPEAT */
    
	USE test;
DROP PROCEDURE IF EXISTS EXEMPLU_REP;

DROP TABLE IF EXISTS sumaNnumere;

create table sumaNnumere(numarul int, suma int);

DELIMITER $
CREATE PROCEDURE EXEMPLU_REP(n int)
COMMENT 'returneaza suma tuturor numerelor de la 1 la n, numarul lor (n) si media aritmetica'

BEGIN 

	DECLARE suma INT UNSIGNED DEFAULT 0;		-- initializam o variabila pentru suma
    DECLARE numarul INT UNSIGNED DEFAULT 0;		-- initializam o variabila pentru numararea iteratiilor
	truncate sumaNnumere;
    
	REPEAT
		
        SET numarul = numarul + 1, 		-- numaram iteratiile (practic, cate numere adunam) pana la n numere
			suma = suma + numarul;  	-- suma numerelor
            
        insert into sumaNnumere VALUES(numarul, suma);		-- insereaza rezultatul fiecarei iteratii in tabel
        
	UNTIL numarul = n					-- cand ajunge la numarul n iese din bucla

	END REPEAT;
        
	SELECT Numarul, suma, suma / numarul AS media;		-- extragem rezultatul
    SELECT * FROM sumaNnumere;
    
END $
DELIMITER ;

CALL EXEMPLU_REP(17);

select * from sumannumere;

DROP PROCEDURE IF EXISTS EXEMPLU_REP;