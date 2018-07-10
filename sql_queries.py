# Write your SQL queries inside the strings below.  If you choose to write your queries on multiple lines, make sure to wrap your query inside """triple quotes""".  Use "single quotes" if your query fits on one line.


def select_expert_martial_artists_using_id():
    return """SELECT heroes.name FROM heroes
                JOIN hero_powers ON heroes.id = hero_powers.hero_id
                WHERE hero_powers.power_id = 10"""

def select_all_power_types_for_batman():
    return """SELECT powers.type FROM powers
                JOIN hero_powers ON powers.id = hero_powers.power_id
                JOIN heroes ON hero_powers.hero_id = heroes.id
                WHERE heroes.name = 'Batman'"""

def select_total_damage_points_for_wonder_woman():
    return """SELECT SUM(powers.damage_points) FROM powers
                JOIN hero_powers ON powers.id = hero_powers.power_id
                JOIN heroes ON hero_powers.hero_id = heroes.id
                WHERE heroes.name = 'Wonder Woman'"""

def list_iron_mans_powers_and_respective_damage_points():
    return """SELECT powers.type, powers.damage_points FROM powers
                JOIN hero_powers ON powers.id = hero_powers.power_id
                JOIN heroes ON hero_powers.hero_id = heroes.id
                WHERE heroes.name = 'Iron Man'"""

def total_power_of_only_humans():
    return """SELECT SUM(powers.damage_points) FROM powers
                JOIN hero_powers ON powers.id = hero_powers.power_id
                JOIN heroes ON hero_powers.hero_id = heroes.id
                WHERE heroes.weakness = 'mortal human'"""

def list_heroes_and_their_num_of_powers_ordered_by_hero_name_alphabetically():
    return """SELECT heroes.name, count(hero_powers.power_id) FROM heroes
                JOIN hero_powers ON heroes.id = hero_powers.hero_id
                GROUP BY heroes.name"""

def select_heroes_name_and_sum_damage_points_ordered_by_most_damage_to_least():
    return """SELECT heroes.name, SUM(powers.damage_points) AS total_damage FROM powers
                JOIN hero_powers ON powers.id = hero_powers.power_id
                JOIN heroes ON hero_powers.hero_id = heroes.id
                GROUP BY heroes.name
                ORDER BY total_damage DESC"""

def all_star_team():
    return """SELECT heroes.name, SUM(powers.damage_points) AS total_damage FROM powers
                JOIN hero_powers ON powers.id = hero_powers.power_id
                JOIN heroes ON hero_powers.hero_id = heroes.id
                GROUP BY heroes.name
                HAVING total_damage > 45"""
