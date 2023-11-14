delimiter |
create event ccCheck
on schedule every 20 minute
do begin
set test=0;
delete from clientcoaches where request=false;

end |