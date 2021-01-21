
drop procedure if exists paml;

delimiter $

create procedure paml()

begin

declare lu int default 1;

drop temporary table if exists luna;
create temporary table luna(
	luna enum('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Iun', 'Iul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'),
    nume text,
    nr_apel tinyint
	);

while lu<=12 do

select count(*), month(apel), fullname from c5 
	where month(apel) = lu
	group by month(apel), fullname
    order by count(*) desc limit 1 into @nr, @lu, @fn;

insert ignore into luna values(@lu, @fn, @nr);
    
set lu = lu + 1;

set @lu=0, @fn=0, @nr=0;

end while;

select * from luna where nr_apel >0 order by luna;
  
end$
 
delimiter ;

call paml;