	/* Instructiuni decizionale CASE 2 */

use test;
drop function if exists Perioada;

DELIMITER /
CREATE FUNCTION Perioada(Varsta INT)
	RETURNS text
    deterministic
	comment 'Exprima perioada din viata a unui om'
begin	

	CASE 
		WHEN varsta BETWEEN 0 AND 12 THEN RETURN 'Copil';
        WHEN varsta BETWEEN 13 AND 22 THEN RETURN 'Adolescent';
		WHEN varsta BETWEEN 23 AND 45 THEN RETURN 'Tanar';
        WHEN varsta BETWEEN 46 AND 65 THEN RETURN 'Matur';
        WHEN varsta BETWEEN 66 AND 85 THEN RETURN 'In varsta';
        WHEN varsta > 85 THEN RETURN 'Norocos sau ghinionist';
	END CASE;

 END /       
 DELIMITER ;

select perioada(71);

select *, Perioada(varsta(datan)) AS starea 
	from paul.people1
    order by numele; 