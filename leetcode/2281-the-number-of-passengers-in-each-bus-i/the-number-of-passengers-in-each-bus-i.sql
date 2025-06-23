# Write your MySQL query statement below
SELECT b.bus_id, 
       (SELECT COUNT(*)
        FROM Passengers p
        WHERE p.arrival_time <= b.arrival_time
          AND NOT EXISTS (
              SELECT 1 
              FROM Buses b2
              WHERE p.arrival_time <= b2.arrival_time
                AND b2.arrival_time < b.arrival_time
          )) AS passengers_cnt
FROM Buses b
ORDER BY b.bus_id;