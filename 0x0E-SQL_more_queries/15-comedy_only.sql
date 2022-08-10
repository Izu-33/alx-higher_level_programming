-- Lists all Comedy shows in the database hbtn_0d_tvshows
SELECT s.`title`
  FROM `tv_shows` AS s
       INNER JOIN `tv_show_genres` AS t
       ON s.`id` = t.`show_id`

       INNER JOIN `tv_genres` AS g
       ON g.`id` = t.`genre_id`
       WHERE g.`name` = "Comedy"
 ORDER BY s.`title`;
