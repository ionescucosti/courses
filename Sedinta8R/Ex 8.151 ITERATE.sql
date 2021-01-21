	/* Intreruperea iteratiei curente */

DELIMITER /
CREATE PROCEDURE test_iterate()

begin

	DECLARE i INT DEFAULT 0;

    bucla: WHILE i<10 do
		SET i=i+1;

       IF i in(1,3,5,7,9) THEN ITERATE bucla;
       end if;

        SELECT i;

        END WHILE;

END /
DELIMITER ;

CALL test_ITERATE;

DROP PROCEDURE IF EXISTS test_iterate;