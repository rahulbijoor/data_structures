# Write your MySQL query statement below
WITH normalized AS (
  -- Home team stats
  SELECT
    home_team_id AS team_id,
    home_team_goals AS goals_for,
    away_team_goals AS goals_against,
    CASE
      WHEN home_team_goals > away_team_goals THEN 3
      WHEN home_team_goals = away_team_goals THEN 1
      ELSE 0
    END AS points,
    1 AS matches_played
  FROM Matches

  UNION ALL

  -- Away team stats
  SELECT
    away_team_id AS team_id,
    away_team_goals AS goals_for,
    home_team_goals AS goals_against,
    CASE
      WHEN away_team_goals > home_team_goals THEN 3
      WHEN away_team_goals = home_team_goals THEN 1
      ELSE 0
    END AS points,
    1 AS matches_played
  FROM Matches
),
aggregated AS (
  SELECT
    team_id,
    SUM(matches_played) AS matches_played,
    SUM(points) AS points,
    SUM(goals_for) AS goal_for,
    SUM(goals_against) AS goal_against,
    SUM(goals_for) - SUM(goals_against) AS goal_diff
  FROM normalized
  GROUP BY team_id
)
SELECT
  t.team_name,
  a.matches_played,
  a.points,
  a.goal_for,
  a.goal_against,
  a.goal_diff
FROM aggregated a
JOIN Teams t ON a.team_id = t.team_id
ORDER BY
  a.points DESC,
  a.goal_diff DESC,
  t.team_name ASC;
