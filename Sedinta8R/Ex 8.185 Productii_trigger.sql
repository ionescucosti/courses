drop database if exists localitati;
create database localitati;
use localitati;

delimiter //

create procedure tabele()

BEGIN

set foreign_key_checks = 0;

	drop table if exists ls;
    
create table ls (
	Judet varchar(30),
    Localitate varchar(30),
    Ua varchar(10),
    Prod_sfecla_t int,
    Prod_oua_miibuc int
    );

	drop table if exists judete;

create table judete(
    idj int auto_increment primary key,
    judet varchar(100) not null unique
	);

	drop table if exists unitadm;

create table unitadm(
    idua int auto_increment primary key,
    ua varchar(100) not null unique
	);

	drop table if exists localitati;

create table localitati(
    idl int auto_increment primary key,
    localitate varchar(100) not null,
    idju int,
    iduad int,
	foreign key (idju) references judete(idj) ON delete SET NULL on update CASCADE,
    foreign key (iduad) references unitadm(idua) ON delete SET NULL on update CASCADE,
    index (idju),
    index(iduad)
	);

	drop table if exists Prod_sfecla;

create table Prod_sfecla(
    id int auto_increment primary key,
    idl int,
    cant_t decimal(20,2),
    foreign key (idl) references localitati(idl) ON delete SET NULL on update CASCADE,
    index (idl)
	);

	drop table if exists Prod_oua;

create table Prod_oua(
    id int auto_increment primary key,
    idl int ,
    cant_miibuc decimal(20,2),
    foreign key (idl) references localitati(idl) ON delete SET NULL on update CASCADE,
    index (idl)
    );
    
set foreign_key_checks = 1;

END//

DELIMITER ;    

call tabele();

drop trigger if exists pop_tab_bi;

DELIMITER $

CREATE trigger POP_TAB_BI before insert
	on ls
	for each row

BEGIN

	declare ij, ia, il, dublare int;
	declare dublare_inreg condition for 1062;
	declare continue handler for dublare_inreg -- definire handler de tip continue 
		begin
			set dublare = 0;	-- handler seteaza valoarea 0 daca insertul a generat eroarea 1062
		end;
    set dublare = 1;
	
    set foreign_key_checks = 0;

	insert into judete(judet) values(new.judet);		# slide 27	
		
		set ij = last_insert_id();
        if dublare = 0 then
			select distinct idj from judete where judet = new.judet into ij;
            set dublare = 1;
         
		end if;
        
	insert into unitadm(ua) values(new.ua);				# slide 28	
		
        set ia = last_insert_id();
        if dublare = 0 then
			select distinct idua from unitadm where ua =new.ua into ia;
            set dublare = 1;
            
		end if;
    
        -- populare localitati prin preluarea trinomului (localitate, id judet, id unitate administrativa) 		#slide 29
	
    INSERT INTO localitati(localitate,idju,iduad) 
		values(new.localitate, ij, ia); 
        
        set il = last_insert_id();
        
        if dublare = 0 then
			select distinct idl from localitati 
				join ls using(localitate)
                join judete on idj = idju
                join unitadm on idua = iduad
				where localitati.localitate = new.localitate 
					into il;
			set dublare = 1;
           
		end if;
		
    
    INSERT INTO Prod_sfecla(idl, cant_t) VALUES(
		il, new.Prod_sfecla_t 
		);								# slide 30
	
    INSERT INTO Prod_oua(idl, cant_miibuc) VALUES(
		il, new.Prod_oua_miibuc 
		);								# slide 30

	set foreign_key_checks = 1;
    
END$


DELIMITER ;

load data local infile 'C:\\wt\\ls.txt' into table ls
	fields terminated by ';'
    lines terminated by '\r\n'
    ignore 1 lines
    (Judet , Localitate , Ua , Prod_sfecla_t , Prod_oua_miibuc)
    ;

use localitati;
    
SELECT * FROM ls;


select * from localitati;

select * from judete;

select * from unitadm;

select * from prod_oua;

select * from prod_sfecla;

CREATE OR REPLACE VIEW Reg_Agricol AS SELECT judet, localitate,  ua,
	Prod_sfecla.cant_t as Sfecla_tone, Prod_oua.cant_miibuc as Oua_miibuc 
	FROM judete
    left join localitati on judete.idj = localitati.idju
    left join unitadm on localitati.iduad = unitadm.idua
    left join Prod_sfecla on Prod_sfecla.idl = localitati.idl
    left join Prod_oua on localitati.idl = Prod_oua.idl;

select * from Reg_Agricol; 
select * from ls;


delimiter #

create procedure rapoarte()

begin

-- verificare 1: productia Sebesului la sfecla

SELECT localitate, judet, Sfecla_tone from Reg_Agricol 
	where localitate = 'Sebes';

-- verificare 2: productia de oua a unei localitati cu nume duplicat

select localitate, judet, Oua_miibuc from Reg_Agricol
	where localitate = 'Stefanesti';

-- Cate oua s-au produs in judetul Maramures?

select judet, sum(Oua_miibuc) AS Prod_oua_judet 
	from Reg_Agricol 
    group by judet
    having judet = 'Maramures';
    
-- Sa se listeze toate produsele din judetul Alba

SELECT * from Reg_Agricol WHERE judet = 'Alba' ORDER BY localitate;

-- productia de sfecla realizata pe judete descrescator
select judet, sum(Sfecla_tone) AS Prod_sfecla_judet 
	from Reg_Agricol 
    group by judet 
    order by Prod_sfecla_judet desc;

-- productia de oua realizata pe judete descrescator
select judet, sum(Oua_miibuc) AS Prod_oua_judet 
	from Reg_Agricol 
    group by judet 
    order by Prod_oua_judet desc;

-- ce localitati au inregistrat cea mai mare productie pentru fiecare din productii?
(select judet, localitate, Sfecla_tone, Oua_miibuc 
	from Reg_Agricol 
	order by Sfecla_tone DESC
    limit 1)
		UNION
(select judet, localitate, Sfecla_tone, Oua_miibuc 
	from Reg_Agricol 
	order by Oua_miibuc DESC
    limit 1);

-- productia de oua realizata pe judete si unitati administrative
select judet, ua, sum(Oua_miibuc) AS Cant 
	from Reg_Agricol 
    group by judet, ua 
    order by judet, Cant desc;

-- care sunt localitatile fara productie de oua / sfecla?

SELECT localitate, judet, Oua_miibuc FROM Reg_Agricol 
	WHERE Oua_miibuc = 0 
    OR Oua_miibuc IS NULL;

SELECT localitate, judet, Sfecla_tone FROM Reg_Agricol 
	WHERE Sfecla_tone = 0 OR Sfecla_tone IS NULL;
    
-- Care sunt municipiile care au productie de sfecla?

SELECT localitate, judet, Sfecla_tone FROM  Reg_Agricol 
	WHERE Sfecla_tone > 0 AND ua = 'Municipiu';
    
-- Sa se afle productia pentru sfecla si oua pentru localitatile din exemplul scurt (slide-uri)

SELECT * FROM reg_agricol WHERE 
	localitate in(
	'Pitesti',
	'Campulung',
	'Albestii de Muscel',
	'Targoviste',
	'Pucioasa',
	'Bezdead',
	'Sibiu',
	'Rasinari',
	'Jina') AND JUDET IN('ARGES','DiMBOVITA','SIBIU');
    
end #

delimiter ;

call rapoarte()