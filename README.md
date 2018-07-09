
# SQL Join Tables Lab

In this lab we will integrate join tables into our SQL queries.  The join table creates a "many-to-many" relationship between two sets of data.

## Objectives

1.  Use `JOIN`s to answer questions about data having a "many-to-many" relationship
2.  Combine `JOIN` statements with grouping and sorting methods like `ORDER BY` and `GROUP BY`

## Superheroes and Superpowers

In the previous lab, we worked with a table containing superheroes and a table containing superhero teams.  Many of the superheroes "belonged to" one of these superhero teams through the `squad_id` foreign key.  Superheroes also had a `name`, a `real_identity`, a `superpower`, and a `weakness`.

However, can't superheroes have more than one `superpower`?  In the previous superheroes table, Superman had only one power, *superstrength*.  Superman has other superpowers, though, like the ability to *fly*, the ability to *breathe in space*, and *x-ray vision*.

Furthermore, multiple superheroes might possess the same `superpower`.  For instance, both Superman and Thor ought to possess *superstrength*.  How can we express these relationships programmatically?  We can use a join table to track `hero_id`s and `power_id`s!



## Tables

We created a separate `powers` table and removed the `superpower` column from the previous superheroes.  We also created a join table called `hero_powers` to make the appropriate "many-to-many" association between `heroes` and `powers`.  All database tables are shown below:

`heroes`:

id  |name           |real_identity        |weakness          |squad_id
----|---------------|---------------------|-------------------------------
1   |Batman         |Bruce Wayne          |mortal human      |2
2   |Superman       |Clark Kent           |kryptonite        |2
3   |Thor           |Thor Odinson         |ego               |1
4   |Iron Man       |Tony Stark           |mortal human      |1
5   |Wonder Woman   |Diana Prince         |broken bracelets  |2
6   |Captain America|Steve Rogers         |mortal human      |1
7   |Aquaman        |Arthur Curry         |needs water nearby|2
8   |Black Panther  |T'Challa             |mortal human      |1
9   |Black Widow    |Natasha Romanoff     |mortal human      |1
10  |Hulk           |Bruce Banner         |rage              |1
11  |Cyborg         |Victor Stone         |hackers           |2
12  |Megaman        |NULL                 |hackers           |NULL
13  |StretcherFlex  |Jean-Claude Van Damme|mortal human      |NULL
14  |Goku           |Kakarot              |myopia            |NULL
15  |Green Lantern  |Alan Scott           |the color yellow  |2

`powers`:

id |type                   |damage_points|
---|-----------------------|-------------|
1  |works hard             |5            |
2  |superstrength          |20           |
3  |flight                 |10           |
4  |summons lightning      |10           |
5  |ultra smart            |20           |
6  |unlimited financing    |5            |
7  |breathes underwater    |5            |
8  |enhanced speed         |10           |
9  |enhanced agility       |10           |
10 |expert martial artist  |15           |
11 |rage                   |10           |
12 |technorganic physiology|10           |
13 |enhanced flexibility   |10           |
14 |magic ring             |1            |
15 |advanced weaponry      |10           |
16 |breathes in outer space|10           |
17 |x-ray vision           |10           |


`hero_powers`:

|hero_id|power_id
|-------|--------
|1      |1
|1      |6
|1      |10
|1      |15
|2      |2
|2      |3
|2      |8
|2      |9
|2      |13
|2      |16
|2      |17
|3      |4
|3      |2
|3      |16
|4      |1
|4      |5
|4      |6
|4      |15
|5      |2
|5      |8
|5      |9
|5      |15
|6      |1
|6      |2
|6      |8
|6      |9
|6      |15
|7      |7
|8      |8
|8      |9
|8      |13
|8      |15
|9      |5
|9      |10
|9      |13
|9      |9
|10     |2
|10     |11
|11     |2
|11     |15
|11     |12
|12     |7
|12     |12
|12     |17
|13     |13
|14     |1
|14     |2
|14     |3
|14     |8
|14     |9
|14     |10
|14     |16
|15     |14


`squads`:

id  |name
----|--------
1   |Avengers
2   |Justice League
3   |The Illuminati

Thanks to the `hero_powers` join table, now each `hero` can have many `powers`, and every `power` can be associated with multiple `heroes`.

## Queries

Write your SQL queries inside the strings found in the functions already provided in the `sql_queries.py` file to get the tests to pass.  If you wish to write your query in multiple lines, make sure to wrap it inside triple quotation marks.

* `select_expert_martial_artists_using_id`

> Write a query that joins the `heroes` table and the `hero_powers` table to select the names of all heroes that have a `power.id` of 10.  

* `select_all_power_types_for_batman`

> Write a query that returns all of Batman's power types.

Although it is easy for a computer to remember heroes and powers based upon their id numbers, we human beings struggle remembering all this information.  From here to the end of the lab, we will write queries that join the `heroes`, `hero_powers`, and `powers` tables to work with data we can easily interpret.

* `select_total_damage_points_for_wonder_woman`

> Write a query that adds the damage points for all of Wonder Woman's powers.

* `list_iron_mans_powers_and_respective_damage_points`

> Write a query that lists all of Iron Man's power types and respective damage points.

* `total_power_of_only_humans`

> Write a query that returns the total damage points of all human superheroes.  We know that all human superheroes have a weakness of "mortal human".

* `list_heroes_and_their_num_of_powers_ordered_by_hero_name_alphabetically`

> This query returns names of all heroes and counts their total number of powers aliased as `num_of_powers`.


* `select_heroes_name_and_sum_damage_points_ordered_by_most_damage_to_least`

> Write a query that orders all superheroes based upon their total number of damage points.  A hero's total number of damage points should be aliased as `total_damage`.  

* `all_star_team`

> Write a query that determines which superheroes should be part of a "Superhero All-Star Team".  Heroes belong on the team if their total damage points (again aliased as `total_damage`) are greater than 45.

## Summary

Great work! In this lab we practiced writing SQL queries on tables with a many to many relationship. We used JOIN statements to query results across tables and select only instances that met the requirements
