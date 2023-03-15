# _SQL - More queries_

_task 0_ -  Lists all privileges of the users user_0d_1 and user_0d_2.
_task 1_ - Creates the user user_0d_1 with all privileges.
_task 2_ - Creates the database hbtn_0d_2 and the user user_0d_2
_task 3_ - Creates the table force_name
_task 4_ - Creates the table id_not_null
_task 5_ - Creates the table unique_id.
_task 6_ - script that creates the database hbtn_0d_usa and the table states with id INT unique, auto generated, can’t be null and is a primary key and name VARCHAR(256) can’t be null
_task 7_ - script that creates the database hbtn_0d_usa and the table cities with id INT unique, auto generated, can’t be null and is a primary key; state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table; and name VARCHAR(256) can’t be null
_task 8_ - script that lists all the cities of California that can be found in the database hbtn_0d_usa
            states table contains only one record where name = California
_task 9_ -  script that lists all cities contained in the database hbtn_0d_usa.

Each record should display: cities.id - cities.name - states.name
Results must be sorted in ascending order by cities.id
_task 10_ - Import the database dump from hbtn_0d_tvshows (https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)
script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

Each record should display: tv_shows.title - tv_show_genres.genre_id
Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
_task 11_ - Import the database dump from hbtn_0d_tvshows (https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)
script that lists all shows contained in the database hbtn_0d_tvshows.

Each record should display: tv_shows.title - tv_show_genres.genre_id
Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
If a show doesn’t have a genre, display NULL
_task 12_ - Import the database dump from hbtn_0d_tvshows (https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)
script that lists all shows contained in hbtn_0d_tvshows without a genre linked.

Each record should display: tv_shows.title - tv_show_genres.genre_id
_task 13_ - Import the database dump from hbtn_0d_tvshows (https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)
script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.

Each record should display: <TV Show genre> - <Number of shows linked to this genre>
First column must be called genre
Second column must be called number_of_shows
Don’t display a genre that doesn’t have any shows linked
Results must be sorted in descending order by the number of shows linked
_task 14_ - Import the database dump from hbtn_0d_tvshows (https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)
script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

The tv_shows table contains only one record where title = Dexter (but the id can be different)
Each record should display: tv_genres.name
Results must be sorted in ascending order by the genre name
_task 15_ - Import the database dump from hbtn_0d_tvshows (https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)
script that lists all Comedy shows in the database hbtn_0d_tvshows.

The tv_genres table contains only one record where name = Comedy (but the id can be different)
Each record should display: tv_shows.title
Results must be sorted in ascending order by the show title
_task 16_ - Import the database dump from hbtn_0d_tvshows (https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)
script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

If a show doesn’t have a genre, display NULL in the genre column
Each record should display: tv_shows.title - tv_genres.name
Results must be sorted in ascending order by the show title and genre name
_task 100_ - script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

The tv_shows table contains only one record where title = Dexter (but the id can be different)
Each record should display: tv_genres.name
Results must be sorted in ascending order by the genre name
_task 101_ - script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

The tv_genres table contains only one record where name = Comedy (but the id can be different)
Each record should display: tv_shows.title
Results must be sorted in ascending order by the show title
_task 102_ - script that lists all shows from hbtn_0d_tvshows_rate by their rating.

Each record should display: tv_shows.title - rating sum
Results must be sorted in descending order by the rating
_task 103_ - script that lists all shows from hbtn_0d_tvshows_rate by their rating.

Each record should display: tv_shows.title - rating sum
Results must be sorted in descending order by the rating