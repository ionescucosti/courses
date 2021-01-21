	/* Instructiuni decizionale CASE 1 */

DROP PROCEDURE IF EXISTS PREMII;

DELIMITER $
CREATE PROCEDURE premii(premianti ENUM('3','4','5'), total INT)
	deterministic
	COMMENT 'calculeaza premiile cand sunt 3, 4 sau 5 premianti'

PREMII: BEGIN
	CASE premianti

	WHEN 3 THEN 

        Trei: BEGIN
    
			DECLARE M DECIMAL(5,2) DEFAULT 0.50;
			DECLARE N DECIMAL(5,2) DEFAULT 0.35;
			DECLARE O DECIMAL(5,2) DEFAULT 0.15;
			SELECT 	M*total AS Locul1, 
					N*total AS Locul2, 
					O*total AS Locul3;
		END Trei;	
	
	WHEN 4 THEN 

		patru: BEGIN
			DECLARE A, B, C, D DECIMAL(5,2);
    
			SET A=.40, B=.30, C=.20, D=.10;
    
			SELECT 	A*total AS Locul1, 
					B*total AS Locul2, 
					C*total AS Locul3,
					D*total AS Locul4;
		END patru;    
    
    
	WHEN 5 THEN 

		Cinci: BEGIN
			DECLARE A, B, C, D, E DECIMAL(5,2);
    
			SET A=.40, B=.30, C=.13, D=.10, E=.07;
    
			SELECT 	A*total AS Locul1, 
					B*total AS Locul2, 
					C*total AS Locul3,
					D*total AS Locul4,
					E*total AS Locul5;
		END Cinci;
	
    END CASE;

END $
DELIMITER ;

CALL premii('3', 100000);

DROP PROCEDURE IF EXISTS PREMII;