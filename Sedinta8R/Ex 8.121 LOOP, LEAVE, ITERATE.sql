	/* Instructiuni repetitive: LOOP */

USE test;

drop procedure if exists people;

DELIMITER $

CREATE PROCEDURE people() DETERMINISTIC
	COMMENT 'Returneaza persoanele cu id divizibil la 100, fullname si varsta'
    
BEGIN

	DECLARE var1 INT UNSIGNED DEFAULT 0;

    bucla: LOOP
        
		SET var1 = var1 +1;
        
        IF var1 = (SELECT MAX(id) + 1 FROM paul.people1) THEN LEAVE bucla;
        END IF;
        
        IF var1 MOD 100 = 0 THEN 
			INSERT INTO t8 SELECT id, CONCAT_WS(' ', prenumele, numele), VARSTA(DATAN) 
				FROM paul.people1
                WHERE id = var1;
        END IF;
        
	END LOOP;	
    
END$

DELIMITER ;

CREATE TABLE t8(	id int3, 
					Fullname varchar(70), 
                    varsta int1);
truncate t8;
 
CALL people();


select * from t8;

select * from paul.people1;

