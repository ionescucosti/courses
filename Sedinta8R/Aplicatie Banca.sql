
	/* creare tabele */

drop database IF EXISTS d;
create database d;
USE d;

CREATE TABLE IF NOT EXISTS `client`
(idcl int unique auto_increment primary key,
nume VARCHAR(50),
prenume VARCHAR(50),
adresa VARCHAR(50));

CREATE TABLE IF NOT EXISTS `cont`
(idco int unique auto_increment primary key,
client_id int,
cod int,
valoare DECIMAL(30,2),
FOREIGN KEY (client_id) REFERENCES client(idcl));

CREATE TABLE IF NOT EXISTS tip_operatiune
(idop int unique auto_increment primary key,
numeop VARCHAR(40));

CREATE TABLE IF NOT EXISTS operatiune_cont
(idtr int unique auto_increment primary key,
cont_sursa_id int,
cont_destinatie_id int,
tip int,
data date,
timp time,
valoare DECIMAL(30,2),
detaliu VARCHAR(50),
FOREIGN KEY (cont_sursa_id) REFERENCES cont(idco),
FOREIGN KEY (cont_destinatie_id) REFERENCES cont(idco),
FOREIGN KEY (tip) REFERENCES tip_operatiune(idop));


	/* creare triggere 

	Trigger inainte de insert in tabela client
	Utilizat pentru a adauga automat un cont pentru un client nou */
    
delimiter $

CREATE TRIGGER insert_contcl AFTER INSERT ON client
	FOR EACH ROW 
BEGIN
    INSERT INTO cont (client_id, cod, valoare) VALUES(new.idcl, new.idcl * 10001, 0.00);
END $
delimiter ;

	/* Trigger AFTER INSERT tabela cont utilizat pentru a adauga o 
    inregistrare pentru creearea contului, in operatiune_cont */

delimiter $
CREATE TRIGGER insert_conttr AFTER INSERT ON cont
  FOR EACH ROW BEGIN
    INSERT INTO  operatiune_cont 
    (cont_sursa_id, cont_destinatie_id,tip, data, timp, valoare) VALUES 
    (NEW.idco, NEW.idco, 
    (SELECT idop from tip_operatiune WHERE numeop = 'Deschidere cont'),
     CURRENT_DATE(), NOW(),0.00);
  END $
delimiter ;


/* populare tabelele de client, tip_operatiune */

 
insert into tip_operatiune(numeop)
	VALUES
	('Deschidere cont'),
	('Inchidere cont'),
	('Transfer intre conturi'),
	('Depunere ghiseu'),
	('Depunere ATM'),
	('Extragere ghiseu'),
	('Extragere ATM'),
	('Balanta cont'),
	('Istoric tranzactii'),
	('EROARE: cont creditor insuficient');
 
INSERT INTO client(nume, prenume, adresa) VALUES('Georgescu', 'Ion', 'Str Frumoasa Otopeni'),
('Ionescu', 	'Maria',  'Blvd. Aviatorilor, Bucuresti'),
('Andrei', 	'Vasile', 'Str. Logofat Udriste, Bucuresti'),
('Marinescu', 	'Emanuel', 'Str. Sapantei, Oradea'),
('Popescu', 	'Micsunica', 'Str. Dumbravii, Sibiu'),
('Firea', 	'Cristian', 'Calea Calarasilor, Bucuresti'),
('Mirea', 	'Marian', 'Str. Rozelor, Bucuresti'),
('Udrea', 	'Traian', 'Str. Stupilor, Bucuresti'),
('Dinu', 	'Gheorghe', 'Calea Bucuresti, Pitesti');

	/* Creare procedura Alimentare cont */

delimiter $

CREATE PROCEDURE ALIMENTARE_CONT(cont_destinatie_cod int, valoare_depunere DECIMAL(30,2))   

  BEGIN
    START TRANSACTION;
       SET @DEST = NULL, @VAL = NULL, @TIP = NULL;
       SELECT @DEST := idco FROM cont WHERE cod = cont_destinatie_cod;
       SELECT @VAL := valoare FROM cont WHERE idco = @DEST;
       SELECT @TIP := idop FROM tip_operatiune WHERE numeop = 'Depunere ghiseu';

       IF(@DEST IS NOT NULL) THEN 	
	 BEGIN
	   INSERT INTO operatiune_cont
	    (cont_sursa_id, cont_destinatie_id, valoare, tip, data, timp,detaliu)
	    VALUES
	    (NULL, @DEST, valoare_depunere, @TIP, CURRENT_DATE(), NOW(),'Depunere ghiseu');

	    UPDATE cont SET valoare = valoare + valoare_depunere WHERE idco = @DEST;	
			
	   COMMIT;
         END;

	ELSE ROLLBACK;
    	END IF;
  END$
DELIMITER ;


	/*  Transfer intre conturi */
    
delimiter $

CREATE PROCEDURE 
   TRANSFER(cont_sursa_cod int, cont_destinatie_cod int,  
   			valoare_transfer DECIMAL(30,2), detaliu_transfer VARCHAR(50))   
	
  BEGIN
    START TRANSACTION; 
    	    SET @SURSA = NULL, @DEST = NULL, @VAL = NULL, @TIP1 = NULL, @TIP2 = NULL;
    	    SELECT @SURSA := idco FROM cont WHERE cod = cont_sursa_cod;
    	    SELECT @DEST := idco FROM cont WHERE cod = cont_destinatie_cod;
    	    SELECT @VAL := valoare FROM cont WHERE idco = @SURSA;
    	    SELECT @TIP1 := idop FROM tip_operatiune WHERE numeop = 'Transfer intre conturi';
    	    SELECT @TIP2 := idop FROM tip_operatiune WHERE numeop = 'EROARE: cont creditor insuficient';

    	    IF (@VAL < valoare_transfer) THEN 	
		    BEGIN
			INSERT INTO operatiune_cont
			    (cont_sursa_id, cont_destinatie_id, valoare, tip, data, timp, detaliu)
			    VALUES
			    (@SURSA, @DEST, 0, @TIP2, CURRENT_DATE(), NOW(), detaliu_transfer);
		    	COMMIT;
		    END;
	    ELSEIF (@SURSA IS NOT NULL AND @DEST IS NOT NULL) THEN 	
		    BEGIN
			INSERT INTO operatiune_cont
			    (cont_sursa_id, cont_destinatie_id, valoare, tip, data, timp,detaliu)
			    VALUES
			    (@SURSA, @DEST, valoare_transfer, @TIP1, CURRENT_DATE(), NOW(), detaliu_transfer);
			    
			UPDATE cont SET valoare = valoare - valoare_transfer WHERE idco = @SURSA;
			
   			UPDATE cont SET valoare = valoare + valoare_transfer WHERE idco = @DEST;
   			
			COMMIT;
		    END;

	   ELSE ROLLBACK;
    	   END IF;
  END$
DELIMITER;


	/* Extragere de la ATM */
    
delimiter $

CREATE PROCEDURE EXT_NUM(cont_sursa_cod int, valoare_extragere DECIMAL(30,2))   

  BEGIN
    START TRANSACTION; 
       	    SET @SURSA = NULL, @VAL = NULL, @TIP1 = NULL, @TIP2 = NULL;
    	    SELECT @SURSA := idco FROM cont WHERE cod = cont_sursa_cod;
    	    SELECT @VAL := valoare FROM cont WHERE idco = @SURSA;
    	    SELECT @TIP1 := idop FROM tip_operatiune WHERE numeop = 'Extragere ATM';
    	    SELECT @TIP2 := idop FROM tip_operatiune WHERE numeop = 'EROARE: cont creditor insuficient';

    	    IF (@SURSA IS NOT NULL AND @VAL < valoare_extragere) THEN 	
		    BEGIN
			INSERT INTO operatiune_cont
			    (cont_sursa_id, cont_destinatie_id, valoare, tip, data, timp,detaliu)
			    VALUES
			    (@SURSA, NULL, 0, @TIP2, CURRENT_DATE(), NOW(),'Extragere ATM esuata');
		    	COMMIT;
		    END;
	    ELSEIF (@SURSA IS NOT NULL) THEN 	
		    BEGIN
			INSERT INTO operatiune_cont
			    (cont_sursa_id, cont_destinatie_id, valoare, tip, data, timp,detaliu)
			    VALUES
			    (@SURSA, NULL, valoare_extragere, @TIP1, CURRENT_DATE(), NOW(),'Extragere ATM reusita');
			    
			UPDATE cont SET valoare = valoare - valoare_extragere WHERE idco = @SURSA;	
			
			COMMIT;
		    END;

	   ELSE ROLLBACK;
    	   END IF;
  END$
DELIMITER ;

	/* Procedura istoric tranzactii */
    

delimiter $

CREATE PROCEDURE IST_TRANZ(cod_cont int, data_initiala date, data_finala date, stocheaza int) 

  BEGIN
  	IF(stocheaza = 1) THEN
  	BEGIN
  	    
	    START TRANSACTION;
	    
		SET @ID = NULL;
		SELECT @ID := idco FROM cont WHERE cod = cod_cont;

		INSERT INTO operatiune_cont
		(cont_sursa_id, tip, data, timp,detaliu) 
		VALUES
		(@ID,(SELECT idop from tip_operatiune WHERE numeop = 'Istoric tranzactii'), 
		CURRENT_DATE(), NOW(),'Consultare tranzactii');
	    COMMIT;	
	END;
	END IF; 
	
	SELECT cont_sursa_id AS Sursa, cont_destinatie_id AS Destinatie, 
	operatiune_cont.valoare AS Valoare,  tip_operatiune.numeop AS Operatiune, data AS Data, timp AS Timp,
	detaliu as Detaliu
	FROM operatiune_cont, tip_operatiune, cont, client
	WHERE operatiune_cont.tip = tip_operatiune.idop
	AND ( cont.idco = cont_sursa_id OR cont.idco = cont_destinatie_id)
	AND  client.idcl = cont.idco
	AND cont.cod = cod_cont
	AND data BETWEEN data_initiala AND  data_finala
	ORDER BY Data, Timp;
	
  END$
DELIMITER ;

	/* Balanta cont */ 
    
delimiter $

CREATE PROCEDURE BAL_CONT(cont_cod int, data_balanta date, ora_balanta time)   

  BEGIN
    SET @ID = NULL, @TIP = NULL;
    SELECT @ID := idco FROM cont WHERE cod = cont_cod;
    SELECT @TIP := idop FROM tip_operatiune WHERE numeop = 'Balanta cont';

    IF(@ID IS NOT NULL) THEN 	
    	BEGIN
		SELECT @Credit:= SUM(valoare) 
		FROM operatiune_cont
		WHERE (data < data_balanta OR (data = data_balanta AND timp <= ora_balanta))
		GROUP BY cont_destinatie_id
		HAVING operatiune_cont.cont_destinatie_id = @ID;	

		SELECT @Debit:= SUM(valoare) 
		FROM operatiune_cont
		WHERE (data < data_balanta OR (data = data_balanta AND timp <= ora_balanta))
		GROUP BY cont_sursa_id
		HAVING operatiune_cont.cont_sursa_id = @ID;

		SELECT cont_cod AS Cont, ROUND((@Credit - @Debit),2) AS Balanta, 
		data_balanta AS Data, ora_balanta As Ora;
	
	END;
   END IF;
  END$
DELIMITER ;


CALL ALIMENTARE_CONT(10001,2000);
CALL ALIMENTARE_CONT(20002,1000);
CALL ALIMENTARE_CONT(30003,2000);
CALL ALIMENTARE_CONT(40004,4500);
CALL ALIMENTARE_CONT(50005,6000);
CALL ALIMENTARE_CONT(60006,7000);
CALL ALIMENTARE_CONT(70007,100000);
CALL ALIMENTARE_CONT(80008,200000);
CALL ALIMENTARE_CONT(90009,2500);


CALL IST_TRANZ(10001, CURRENT_DATE(), CURRENT_DATE(),1);
CALL TRANSFER(10001,20002,100,'Ramburs imprumut');
CALL TRANSFER(70007,10001,1000,'Plata salariu');
CALL TRANSFER(10001,80008,120,'Plata utilitati');
CALL IST_TRANZ(10001, CURRENT_DATE(), CURRENT_DATE(),1);


CALL TRANSFER(10001,40004,450,'Cumparaturi diverse');
CALL TRANSFER(10001,40004,4500,'Plata imprumut');
CALL IST_TRANZ(10001, CURRENT_DATE(), CURRENT_DATE(),1);

CALL IST_TRANZ(20002, CURRENT_DATE(), CURRENT_DATE(),0);
CALL TRANSFER(20002,30003,200,'Cadou');
CALL IST_TRANZ(20002, CURRENT_DATE(), CURRENT_DATE(),1);


CALL IST_TRANZ(10001, CURRENT_DATE(), CURRENT_DATE(),1);
CALL EXT_NUM(10001, 500);
CALL EXT_NUM(10001, 500);
CALL EXT_NUM(10001, 30000);
CALL EXT_NUM(10009, 300);
CALL IST_TRANZ(10009, CURRENT_DATE(), CURRENT_DATE(),0);



CALL BAL_CONT(10001, CURRENT_DATE(), NOW());
CALL IST_TRANZ(10001, CURRENT_DATE(), CURRENT_DATE(),0);
CALL BAL_CONT(10001, CURRENT_DATE(), '12:09');

use d;

CALL IST_TRANZ(10001, '2008-12-14', '2008-12-14',1);

CALL BAL_CONT(10001, CURRENT_DATE(), NOW());
CALL BAL_CONT(10001, '2008-12-14', '22:10');
