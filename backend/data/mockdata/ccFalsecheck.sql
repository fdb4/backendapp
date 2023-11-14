delimiter |
CREATE TRIGGER ccfalsecheck 
BEFORE UPDATE ON clientcoaches 
FOR EACH ROW begin
if (select count(*) from clientcoaches where clientID=new.clientID and request=true group by clientID)=1 and new.request=true then
signal sqlstate '45000';
end if;

end
|