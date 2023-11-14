delimiter |
create trigger cctruecheck
before insert on clientcoaches
for each row
begin
if (select count(*) from clientcoaches where clientID=new.clientID and request=true group by clientID)=1 or (select count(*) from clientcoaches where clientID=new.clientID and coachexpID=new.coachexpID group by clientID)>=1  then
signal sqlstate'45000';
end if;

end
|