# Write your MySQL query statement below
SELECT id, COUNT(*) AS num
FROM (  SELECT ra.requester_id AS id FROM RequestAccepted ra
        UNION ALL
        SELECT ra2.accepter_id AS id FROM RequestAccepted ra2
    
) AS combined
GROUP BY id
ORDER BY num DESC
LIMIT 1;