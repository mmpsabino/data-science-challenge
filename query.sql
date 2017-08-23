
create temporary table aux on commit drop as(
select *, "Amount USD"/numdays as daily
	from(
		select *, 
			case
			when "Start Date" is null then 1
			else ("End Date" - "Start Date")+1
			end as numdays
			from (
				select * 
				from companyx 
				where ("Status"!='overdue' AND "Status"!='voided')) as foo) as cons);

update aux
set "Start Date" = "Created at", "End Date" = "Created at"
where "Start Date" is null;


do $$
declare d record;
declare counter int := 0;

begin
	for d in 
		select "Transaction-ID", "Start Date", numdays, daily from aux order by "Start Date"
		
		loop
			counter :=1;

			loop
				insert into aux ("Transaction-ID", "Start Date", daily) values (d."Transaction-ID", d."Start Date" + counter, d.daily);
				counter := counter + 1;
				exit when counter >= d.numdays;

			end loop;
			
		end loop;


end $$;

select "Start Date" as day, sum(daily) as revenue from aux
where ('2016-12-31' < "Start Date" AND "Start Date" < '2018-01-01')
group by "Start Date"
order by day;