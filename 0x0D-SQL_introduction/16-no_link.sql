-- lists records in second_table
-- sql query syntax 
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
