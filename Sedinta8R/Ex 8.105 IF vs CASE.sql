
DROP PROCEDURE IF EXISTS PREMII;

DELIMITER $
CREATE PROCEDURE premii(participanti int(10), total INT)
deterministic
COMMENT 'calculeaza premiile cand sunt 3, 5 sau 10 premianti'

PREMII: BEGIN

	IF participanti BETWEEN 3 AND 10 THEN 

		BEGIN
    DECLARE M DECIMAL(5,2) DEFAULT 0.50;
    DECLARE N DECIMAL(5,2) DEFAULT 0.35;
    DECLARE O DECIMAL(5,2) DEFAULT 0.15;	
	SELECT 	M*total Locul1, 
			N*total Locul2, 
			O*total Locul3;
		END;

	ELSEIF participanti BETWEEN 11 AND 30 THEN 

		BEGIN
    DECLARE A DECIMAL(5,2) DEFAULT 0.40;
    DECLARE B DECIMAL(5,2) DEFAULT 0.30;
    DECLARE C DECIMAL(5,2) DEFAULT 0.13;
    DECLARE D DECIMAL(5,2) DEFAULT 0.10;
    DECLARE E DECIMAL(5,2) DEFAULT 0.07;
	SELECT 	A*total Locul1, 
			B*total Locul2, 
            C*total Locul3,
            D*total Locul4,
            E*total Locul5;
		END;

	ELSEIF participanti>30 THEN 

		BEGIN 
	DECLARE a,b,c,d,e,f,m,n,o DECIMAL(5,2);
    SET A=0.22, B=0.18, C=0.15, D=0.12, 
		E=0.09, M=0.07, N=0.05, O=0.04;
	SELECT 	A*total Locul1, 
			B*total Locul2, 
            C*total Locul3,
            D*total Locul4,
            E*total Locul5,
            M*total Locul6, 
			N*total Locul7, 
            O*total Locul8,
            O*total Locul9,
            O*total Locul10;
		END;

    ELSE SELECT 'Numar insuficient de jucatori' AS Anulat;

	END IF;

END $
DELIMITER ;

CALL premii(150, 30000);

DROP PROCEDURE IF EXISTS PREMII;