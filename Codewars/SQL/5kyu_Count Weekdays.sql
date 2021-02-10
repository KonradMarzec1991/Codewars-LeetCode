-- Replace with your code
CREATE OR REPLACE FUNCTION weekdays(date, date)
RETURNS int AS  $$
    declare
        greater_date date := greatest($1, $2);
        lower_date date := least($1, $2);
        counter integer := 0;
    begin
        while greater_date >= lower_date loop
            if extract(isodow FROM lower_date) <= 5 then
                counter = counter + 1;
            end if;
            lower_date = lower_date + interval '1 day';
        end loop;

        return counter;
    end;
    $$ LANGUAGE 'plpgsql';