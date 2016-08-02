#!/usr/bin/env python

from pogom.pgoapi.utilities import get_pos_by_name
import sys
import csv
lat_dist = 0.004
lon_dist = 0.0137

def up_right(pos):
    return (pos[0] + lat_dist, pos[1] + lon_dist, 0.0)

def up(pos):
    return (pos[0] + 2* lat_dist, pos[1], 0.0)

def down(pos):
    return (pos[0] - 2*lat_dist, pos[1], 0.0)

def up_left(pos):
    return (pos[0] + lat_dist, pos[1] - lon_dist, 0.0)

def down_left(pos):
    return (pos[0] - lat_dist, pos[1] - lon_dist, 0.0)

def down_right(pos):
    return (pos[0] - lat_dist, pos[1] + lon_dist, 0.0)

def right(pos):
    return (pos[0], pos[1] + 1.5 * lon_dist, 0.0)

def left(pos):
    return (pos[0], pos[1] - 1.5 * lon_dist, 0.0)

def get_next_pos(loc):
    yield loc
    yield down_right(loc)
    yield down(loc)
    yield down_left(loc)
    yield up_left(loc)
    yield up(loc)
    yield up_right(loc)

def load_accounts(file_name):
    accounts = []
    with open(file_name) as accs:
        reader = csv.DictReader(accs, delimiter=';')
        for row in reader:
            accounts.append(row)
    return accounts

def create_envs(accounts, location):
    location_generator = get_next_pos(location)
    for i, acc in enumerate(accounts, 1):
        loc = location_generator.next()
        create_env(acc, loc, 'bot{}.env'.format(i))
    create_env(accounts[0], location, filename='server.env')

def create_env(acc, loc, filename):
    with open(filename, 'w') as f:
        f.write('POKE_USER={}\n'.format(acc['user']))
        f.write('POKE_PASS={}\n'.format(acc['pass']))
        f.write('POKE_LOCATION={}, {}\n'.format(loc[0], loc[1]))
        f.write('POKE_MAPSKEY={}\n'.format(acc['key']))

def setup_bots(location):
    print("Searching Coordinates for {}".format(location))
    pos = get_pos_by_name(location)
    print("Coordinates are: {}, {}").format(pos[0], pos[1])
    accs = load_accounts('accounts.csv')
    create_envs(accs, pos)

if __name__ == "__main__":
    if sys.argv[1]:
        location = sys.argv[1]
        setup_bots(location)
    else:
        print("supply a location as argument!")

