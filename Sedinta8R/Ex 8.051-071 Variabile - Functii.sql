		/* 8.051	Variabile locale */

DELIMITER $
CREATE PROCEDURE premii(Val INT)
COMMENT 'calculeaza premiile cand sunt 3 premianti'

BEGIN

	DECLARE M DECIMAL(5,2) DEFAULT 0.50; 
    DECLARE N DECIMAL(5,2) DEFAULT 0.35;
    DECLARE O DECIMAL(5,2) DEFAULT 0.15;
-- sau	 declare M,N,O DECIMAL(5,2);	SET M=0.50, N=0.35, O=0.15

    SELECT 	M * Val AS Locul1, 
			N * Val AS Locul2, 
            O * Val AS Locul3;

END $
DELIMITER ;

CALL premii(10110);

SELECT M,N,O; -- Nu sunt vizibile in afara procedurii
    
DROP PROCEDURE IF EXISTS premii;


		
        /* 8.052	Variabile locale SELECT ...INTO */	-- ACASA

DELIMITER $
CREATE PROCEDURE premii(IN Premiu INT)
COMMENT 'calculeaza premiile cand sunt 3 premianti'

BEGIN

	DECLARE M DECIMAL(5,2) DEFAULT 0.50 /* declarare individuala */;
    DECLARE N DECIMAL(5,2) DEFAULT 0.35;
    DECLARE O DECIMAL(5,2) DEFAULT 0.15;
    DECLARE Tax1, Tax2, Tax3 DECIMAL (10,2) /* declarare multipla */;
	
    SELECT 	M * Premiu Locul1, 
			N * Premiu Locul2, 
			O * Premiu Locul3 
		INTO @I, @II, @III;			-- premii brute
    
    SELECT @I*0.16, @II*0.16,@III*0.16   INTO 	Tax1, Tax2, Tax3;	-- impozite aferente premiilor
    
    SET @I = @I - Tax1, 			-- calculam premiile nete si total impozit de plata
					@II = @II - Tax2, 
											@III = @III - Tax3, 
																@Tax = Tax1 + Tax2 + Tax3;
        
        SELECT @I, @II, @III, @Tax;		-- vizualizam rezultatul

END $
DELIMITER ;

CALL premii(80000);
    


		/* 8.053	Restrictii coloane/randuri la SELECT ...INTO ...*/	-- ACASA

DROP TABLE IF EXISTS produse;

CREATE TABLE produse(
	Id int,
    Denumire VARCHAR(100),
    Cant DECIMAL(10,2),
    Pret DECIMAL(10,2)
    );

INSERT INTO produse VALUES
	(1, 'caise', 5, 4), 
	(2, 'mere', 120, 2.5), 
	(3, 'pere', 30, 3.8),
    (4, 'struguri', 10, 8);

SELECT Denumire, Pret 
	FROM produse WHERE Denumire LIKE '%er%' LIMIT 1,1 
    into @Produs, @Pret, @Cantitate;
    -- Eroare - difera numarul coloanelor

SELECT Denumire, Pret 
	FROM produse WHERE Denumire LIKE '%er%' 
    into @Produs, @Pret ; 
     -- Eroare - numarul randurilor > 1
     
select @produs, @pret;


     
     
		/* 8.061	Functii */

DROP FUNCTION IF EXISTS varsta;

DELIMITER $
CREATE FUNCTION Varsta(data_nasterii date)
	RETURNS INT
    DETERMINISTIC
    COMMENT 'Returneaza varsta in ani'

BEGIN 
	
	IF MONTH(NOW()) > MONTH(data_nasterii) or 
		MONTH(NOW()) = MONTH(data_nasterii) AND DAY(NOW()) >= DAY(data_nasterii)THEN 
			RETURN YEAR(NOW())-YEAR(data_nasterii);
	ELSE RETURN YEAR(NOW())-YEAR(data_nasterii) - 1;
    end if;
END $
DELIMITER ;

select varsta('1977-06-11');

select numele, DATAN, varsta(datan) from paul.people1;


		/* 8.071	Vizualizarea rutinelor */


SHOW PROCEDURE STATUS;

SHOW FUNCTION STATUS;

SHOW CREATE PROCEDURE premii;

SHOW CREATE FUNCTION varsta;

SELECT * FROM information_schema.ROUTINES
	WHERE ROUTINE_SCHEMA = 'TEST';

DROP PROCEDURE IF EXISTS premii;

    