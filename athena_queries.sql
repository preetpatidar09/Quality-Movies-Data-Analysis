CREATE DATABASE IF NOT EXISTS transformed_movie_db;

drop TABLE IF EXISTS transformed_movie_db.movies_cleaned;

CREATE EXTERNAL TABLE IF NOT EXISTS transformed_movie_db.movies_cleaned (
  title string,
  genre string,
  rating double,
  revenue bigint,
  budget bigint,
  profit bigint
)
STORED AS PARQUET
LOCATION 's3://movies-transformed-data/';


SELECT title, rating
FROM transformed_movie_db.movies_cleaned
ORDER BY rating DESC
LIMIT 10;


SELECT title,original_language
FROM transformed_movie_db.movies_cleaned
where original_language = "en"
ORDER BY rating DESC
LIMIT 5;


SELECT title,overview, rating
FROM transformed_movie_db.movies_cleaned
ORDER BY rating DESC
LIMIT 10;



