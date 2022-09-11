#!/usr/bin/python3
"""Displays all cities of a given state from the
states table of the database hbtn_0e_4_usa.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` as `c` \
                 INNER JOIN `states` as `s` \
                 ON `c`.`state_id` = `s`.`id` \
                 ORDER BY `c`.`id`")
    states = [city[2] for city in c.fetchall() if city[4] == sys.argv[4]]
    print(", ".join(states))
