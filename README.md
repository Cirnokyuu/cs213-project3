# cs213-project3

The entire my_movies.sql is too large to upload, so I only uploaded the first 50,000 rows.

To get my_movies.sql, you should download title.basics.tsv.gz and title.ratings.tsv.gz from [imdb](https://datasets.imdbws.com/), import it into both openGauss and Postgres, and run the code below:

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

## data import

Use [j.py](https://github.com/Cirnokyuu/cs213-project3/blob/main/j.py) to monitor server resource usage, and output it into files, which is written in the code:

```python
filename = 'log.txt'
```

You only need to change this line of code to set the output file name.

I have already exported my_movies_xw.sql to import directly.

Use [paint.py](https://github.com/Cirnokyuu/cs213-project3/blob/main/paint.py) to draw a diagram of CPU and memory usage for a specified file.

Use [paint2.py](https://github.com/Cirnokyuu/cs213-project3/blob/main/paint2.py) to draw a diagram of the relationship between CPU and memory usage and efficiency and data size for the specified file.

## other parts

I have explained the detailed operation procedures of other parts in the report.
