call tabele();

load data local infile 'C:\\wt\\ls.txt' into table ls
	fields terminated by ';'
    lines terminated by '\r\n'
    ignore 1 lines
    (Judet , Localitate , Ua , Prod_sfecla_t , Prod_oua_miibuc)
    ;

drop procedure if exists POP_TAB_cursor;

DELIMITER $

CREATE PROCEDURE POP_TAB_cursor()

BEGIN

	declare jud, loc, unita  varchar(50);
    declare sfecla, oua int;
    declare idjud, iduadm, idloc int;
	declare stop_cursor condition for 1329;
    declare pop_tab cursor for select * from ls;
	declare exit handler for stop_cursor -- definire handler de tip exit 
		begin
		end;

	set foreign_key_checks = 0;

open pop_tab;

loop 

	fetch pop_tab into jud, loc, unita, sfecla, oua;
    
    insert ignore into judete(judet) values(jud);
    
		select idj from judete where judet = jud into idjud;
		
	insert ignore into unitadm(ua) values(unita);	
    
		select idua from unitadm where ua = unita into iduadm;
		
    INSERT ignore INTO localitati(localitate,idju,iduad) 
		values(loc, idjud, iduadm); 
        
        select idl from localitati where loc = localitate and idjud = idju 
        and iduadm = iduad into idloc;
    
    INSERT INTO Prod_sfecla(idl, cant_t) VALUES(idloc, sfecla);								 
	
    INSERT INTO Prod_oua(idl, cant_miibuc) VALUES(idloc, oua);								

	set foreign_key_checks = 1;
    
end loop;

close pop_tab;
    
END$

DELIMITER ;

call POP_TAB_cursor();

call rapoarte()