-- lists number of records with same score
-- sql query syntax
SELECT score, COUNT(*) as number
FROM second_table
GROUP BY score
ORDER BY number DESC;
