-- California Cities
-- select the cities where state_id is name "California"
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
