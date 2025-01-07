# cs213-project3

The entire my_movies.sql is too large to upload, so I only uploaded the first 50,000 rows.

To get my_movies.sql, you should download title.basics.tsv.gz and title.ratings.tsv.gz from [imdb](https://datasets.imdbws.com/), and run the code below:

```sql
CREATE TABLE movie_id AS
 SELECT
 title_basics.tconst::varchar(10) as movieid,
 titletype::varchar,
 primarytitle::varchar,
 originaltitle::varchar,
 startyear::integer,
 string_to_array(genres,',','\N') as genres,
 averagerating::double precision,
 numvotes::integer
 FROM title_basics
 INNER JOIN title_ratings
 ON title_basics.tconst = title_ratings.tconst;
 ALTER TABLE my_movies ADD CONSTRAINT id PRIMARY KEY (tid);
```
