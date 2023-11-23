-- List all genres and the number of shows linked to each
SELECT genres.name AS genre, COUNT(show_genres.show_id) AS number_of_shows
FROM genres
LEFT JOIN show_genres ON genres.id = show_genres.genre_id
GROUP BY genres.id
HAVING COUNT(show_genres.show_id) > 0
ORDER BY COUNT(show_genres.show_id) DESC;