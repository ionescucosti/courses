	/* Instructiuni repetitive : WHILE */

USE test;
DELIMITER $
CREATE PROCEDURE test_while(param1 DATE)
	COMMENT 'Returneaza tote datele din intervalul param1 pana in data curenta'

BEGIN 

	DECLARE d date DEFAULT param1;
        
    w: WHILE d <= curdate() DO
		               
        INSERT INTO t9 values(d);
        SET d = d + INTERVAL 1 DAY;
        
	END WHILE;
  END $
DELIMITER ;

CREATE TABLE t9 (data date);

call test_while(curdate()- interval 6 day);

select * from t9;

drop procedure if exists test_while;
drop table if exists t9;