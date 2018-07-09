# Write your SQL queries inside the strings below.  If you choose to write your queries on multiple lines, make sure to wrap your query inside """triple quotes""".  Use "single quotes" if your query fits on one line.


def select_expert_martial_artists_using_id():
    return """SELECT heroes.name FROM hero_powers LEFT JOIN heroes ON hero_powers.hero_id = heroes.id WHERE hero_powers.power_id = 10;"""

def select_all_power_types_for_batman():
    return """SELECT A.type FROM heroes INNER JOIN (SELECT powers.type, hero_powers.hero_id FROM powers INNER JOIN hero_powers ON hero_powers.power_id = powers.id) AS A ON A.hero_id = heroes.id WHERE heroes.name = 'Batman';"""

def select_total_damage_points_for_wonder_woman():
    return """SELECT SUM(A.damage_points) FROM heroes INNER JOIN (SELECT powers.damage_points, hero_powers.hero_id FROM powers INNER JOIN hero_powers ON hero_powers.power_id = powers.id) AS A ON A.hero_id = heroes.id WHERE heroes.name = 'Wonder Woman';"""

def list_iron_mans_powers_and_respective_damage_points():
    return """SELECT A.type, A.damage_points FROM heroes INNER JOIN (SELECT powers.type, powers.damage_points, hero_powers.hero_id FROM powers INNER JOIN hero_powers ON hero_powers.power_id = powers.id) AS A ON A.hero_id = heroes.id WHERE heroes.name = 'Iron Man';"""

def total_power_of_only_humans():
    return """SELECT SUM(A.damage_points) FROM heroes INNER JOIN (SELECT powers.damage_points, hero_powers.hero_id FROM powers INNER JOIN hero_powers ON hero_powers.power_id = powers.id) AS A ON A.hero_id = heroes.id WHERE heroes.weakness = 'mortal human';"""

def list_heroes_and_their_num_of_powers_ordered_by_hero_name_alphabetically():
    return """SELECT heroes.name, COUNT(heroes.name) AS num_of_powers FROM heroes INNER JOIN (SELECT * FROM powers INNER JOIN hero_powers ON hero_powers.power_id = powers.id) AS A ON A.hero_id = heroes.id GROUP BY heroes.name ORDER BY heroes.name;"""

def select_heroes_name_and_sum_damage_points_ordered_by_most_damage_to_least():
    return """SELECT heroes.name, SUM(A.damage_points) AS total_damage FROM heroes INNER JOIN (SELECT * FROM powers INNER JOIN hero_powers ON hero_powers.power_id = powers.id) AS A ON A.hero_id = heroes.id GROUP BY heroes.name ORDER BY SUM(A.damage_points) DESC;"""

def all_star_team():
    #I can't use WHERE. Look up HAVING
    return """SELECT heroes.name, SUM(A.damage_points) AS total_damage FROM heroes INNER JOIN (SELECT * FROM powers INNER JOIN hero_powers ON hero_powers.power_id = powers.id) AS A ON A.hero_id = heroes.id GROUP BY heroes.name HAVING total_damage > 45;"""
