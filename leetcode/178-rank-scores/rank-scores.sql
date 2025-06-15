SELECT score, 
    (SELECT COUNT(DISTINCT score)
     FROM Scores AS s
     Where s.score >= Scores.score) AS 'rank'
FROM Scores 
ORDER BY score DESC;