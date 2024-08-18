
/*
Creating the table and loading the dataset
*/
DROP TABLE IF EXISTS ratings;
CREATE TABLE ratings (userid INT, temp1 VARCHAR(10),  movieid INT , temp3 VARCHAR(10),  rating REAL, temp5 VARCHAR(10), timestamp INT);
COPY ratings FROM 'test_data.txt' DELIMITER ':';
ALTER TABLE ratings DROP COLUMN temp1, DROP COLUMN temp3, DROP COLUMN temp5, DROP COLUMN timestamp;

-- Do not change the above code except the path to the dataset.
-- make sure to change the path back to default provided path before you submit it.

-- Part A
/* Write the queries for Part A*/
DROP VIEW IF EXISTS best;
SELECT * FROM ratings;
SELECT userid, rating FROM ratings;
SELECT userid, movieid FROM ratings WHERE rating>4.0;
SELECT userid, movieid FROM ratings WHERE rating>4.0 AND rating<2.0;
CREATE VIEW best AS
    SELECT userid, movieid
    FROM ratings
    WHERE rating>4.5;


-- Part B
/* Create the fragmentations for Part B1 */
DROP TABLE IF EXISTS bad_movies;
CREATE TABLE bad_movies AS
    SELECT * FROM ratings
    WHERE rating<2.0;
SELECT * FROM bad_movies;

DROP TABLE IF EXISTS good_movies;
CREATE TABLE good_movies AS
    SELECT * FROM ratings
    WHERE rating>=2.0;
SELECT * FROM good_movies;

DROP TABLE IF EXISTS top_movies;
CREATE TABLE top_movies AS
    SELECT * FROM ratings
    WHERE rating>=4.5;
SELECT * FROM top_movies;

-- Proof to show that the fragemetns are not disjoint, the intersection rows will be not null
SELECT * FROM good_movies
INTERSECT
SELECT * FROM top_movies;

/* reconstruction query/queries for Part B1 */
DROP TABLE IF EXISTS ratings_reconstructed;
CREATE TABLE ratings_reconstructed AS
    SELECT * FROM bad_movies
    UNION
    SELECT * FROM good_movies
    UNION
    SELECT * FROM top_movies;

SELECT * FROM ratings_reconstructed;

SELECT * FROM ratings
INTERSECT
SELECT * FROM ratings_reconstructed;

/* The above fragmentations as Part of B1 satisfies reconstruction and completeness
 *  but not disjointness because there are common rows present in fragements good_movies and top_movies.
 *  The completeness and reconstruction is proved by the above step, where we created the table ratings_reconstructed,
 *  and compared it with the ratings table, and all the rows were present.
*/


/* fragmentations for Part B2 */
DROP TABLE IF EXISTS users;
CREATE TABLE users AS
    SELECT userid from ratings;
SELECT * FROM users;

DROP TABLE IF EXISTS movies;
CREATE TABLE movies AS
    SELECT movieid from ratings;
SELECT * FROM movies;

DROP TABLE IF EXISTS user_rating;
CREATE TABLE user_rating AS
    SELECT userid, rating from ratings;
SELECT * FROM user_rating;

/* The above fragements as Part of B2 satisfies completeness and disjointness but not reconstruction.
 *  Here I have chossen user_id to be the primary_key, so inorder to recreate the table from the fragements,
 *  the primary key should be part of all the fragments, but as we can see that the fragement movies doesnot have 
 *  the user_id, so we will not able to map the userid, rating and movieid. Hence, we cannot satisfy reconstruction.
*/

/* fragmentations for Part B3 */
DROP TABLE IF EXISTS f1 cascade;
CREATE TABLE f1 AS
    SELECT * FROM ratings
    WHERE rating<2.0;
SELECT * FROM f1;

DROP TABLE IF EXISTS f2 cascade;
CREATE TABLE f2 AS
    SELECT * FROM ratings
    WHERE rating>=2.0 and rating<4.5;
SELECT * FROM f2;

DROP TABLE IF EXISTS f3 cascade;
CREATE TABLE f3 AS
    SELECT * FROM ratings
    WHERE rating>=4.5;
SELECT * FROM f3;

-- Proof to show that the fragemetns are disjoint, the intersection will be null
SELECT * FROM f2
INTERSECT
SELECT * FROM f3;

/*reconstruction query/queries for Part B3 */
DROP TABLE IF EXISTS ratings_disjoint_reconstructed;
CREATE TABLE ratings_disjoint_reconstructed AS
    SELECT * FROM f1
    UNION
    SELECT * FROM f2
    UNION
    SELECT * FROM f3;
SELECT * FROM ratings_disjoint_reconstructed;

SELECT * FROM ratings
INTERSECT
SELECT * FROM ratings_disjoint_reconstructed;


/* The above fragmentations as Part of B3 satisfies reconstruction, disjointness and completeness
 *  The completeness and reconstruction is proved by the above step, where we created the table ratings_reconstructed,
 *  and compared it with the ratings table, and all the rows were present. And, the disjointness is proved by the step
 *  where we did use INTERSECT to find the common rows, but the result was null/0 rows.
*/


-- Part C

SELECT * FROM f1;
SELECT userid, rating FROM f1;
SELECT userid, movieid FROM f1 WHERE rating>4.0;
SELECT userid, movieid FROM f1 WHERE rating>4.0 AND rating<2.0;
CREATE VIEW best_f1 AS
    SELECT userid, movieid
    FROM f1
    WHERE rating>4.5;

SELECT * FROM f2;
SELECT userid, rating FROM f2;
SELECT userid, movieid FROM f2 WHERE rating>4.0;
SELECT userid, movieid FROM f2 WHERE rating>4.0 AND rating<2.0;
CREATE VIEW best_f2 AS
    SELECT userid, movieid
    FROM ratings
    WHERE rating>4.5;

SELECT * FROM f3;
SELECT userid, rating FROM f3;
SELECT userid, movieid FROM f3 WHERE rating>4.0;
SELECT userid, movieid FROM f3 WHERE rating>4.0 AND rating<2.0;
CREATE VIEW best_f3 AS
    SELECT userid, movieid
    FROM f3
    WHERE rating>4.5;
