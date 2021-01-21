	/* Instructiuni repetitive: LOOP */

USE paul;

drop procedure if exists people8;

create table if not exists a_g(
	id int3 auto_increment key,
    nume text,
    prenume text,
    datan date
    );
    
create table if not exists h_m(
	id int3 auto_increment key,
    nume text,
    prenume text,
    datan date
    );

create table if not exists n_s(
	id int3 auto_increment key,
    nume text,
    prenume text,
    datan date
    );
    
create table if not exists t_w(
	id int3 auto_increment key,
    nume text,
    prenume text,
    datan date
    );

DELIMITER $

CREATE PROCEDURE paul.people8() DETERMINISTIC
	COMMENT 'Distribuie persoanele din tabela data in alte tabele dupa '
    
BEGIN

	DECLARE var1 INT UNSIGNED DEFAULT 1;
    
    
    bucla: LOOP
                
        IF var1 = (SELECT MAX(id) + 1 FROM paul.people1) THEN LEAVE bucla;
        END IF;
        
        IF  people1.numele like 'a%' OR 
			 'b%' OR 
            'c%' OR 
            'd%' OR 
            'e%' OR 
			'f%' OR 
            'g%' THEN 
			INSERT INTO a_g(nume, prenume, datan) 
            SELECT numele, prenumele, datan FROM paul.people1 WHERE id = var1;
	/*	ELSEIF paul.people1.numele like 'h%' OR 'i%' OR 'j%' OR 'k%' OR 'l%' OR 'm%' THEN 
			INSERT INTO h_m(nume, prenume, datan) 
            SELECT numele, prenumele, datan FROM paul.people1 WHERE id = var1;
		ELSEIF paul.people1.numele like 'n%' OR 'o%' OR 'p%' OR 'q%' OR 'r%' OR 's%' THEN 
			INSERT INTO n_s(nume, prenume, datan) 
            SELECT numele, prenumele, datan FROM paul.people1 WHERE id = var1;
		ELSE 
			INSERT INTO h_m(nume, prenume, datan) 
            SELECT numele, prenumele, datan FROM paul.people1 WHERE id = var1;	*/
        END IF;	
        
        SET var1 = var1 +1;
        
	END LOOP;

  
END$

DELIMITER ;

    
    truncate a_g; 
    truncate h_m;
    truncate n_s;
    truncate t_w;
 
CALL people8(); 
