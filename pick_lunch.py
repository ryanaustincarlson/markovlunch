#!/usr/bin/env python

import sys, os

from LunchPlace import LunchPlace
from LunchEvent import LunchEvent
from LuncherPreferences import LuncherPreferences

def read_places(filename):
    places = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue

            fields = line.split(',')
            name = fields[0]
            tags = fields[1:]
            place = LunchPlace(name)
            for tag in tags:
                place.add_tag(tag)
            places.append(place)
    return places

def read_history(filename):
    history = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue

            name, date = line.split(',')
            event = LunchEvent(name, date)
            history.append(event)
    return history

def read_luncher_prefs(filenames):
    lunchers_preferences = []
    for filename in filenames:
        name = os.path.basename(filename).replace(".prefs", "")
        prefs = LuncherPreferences(name)
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line.startswith('#'):
                    continue

                name, weight = line.split(',')
                prefs.update_preference(name, weight)
        lunchers_preferences.append(prefs)
    return lunchers_preferences
    

def load_files(places_filename, history_filename, luncher_prefs_filenames):
    places = read_places(places_filename)
    history = read_history(history_filename)
    lunchers_preferences = read_luncher_prefs(luncher_prefs_filenames)

    # check that places in the history and user prefs are known PLACES
    # otherwise bad things could happen
    places_dict = {}
    for place in places: 
        places_dict[place.name] = True
    for event in history:
        assert(event.place in places_dict)
    for prefs in lunchers_preferences:
        for place in prefs.preferences:
            assert(place in places_dict)
    return (places, history, lunchers_preferences)

def main(args):
    if len(args[1:]) < 3:
        sys.stderr.write("usage: %s <places> <history> <user-preferences>+\n" % args[0])
        sys.stderr.write("You must have 1 or more user preferences!\n")
        return 1

    places_filename = args[1]
    history_filename = args[2]
    luncher_prefs_filenames = args[3:]

    places, history, lunchers_prefs = load_files(places_filename, history_filename, luncher_prefs_filenames)

    # TODO: pick a place based on history and preferences
    #       assign each place a probability
    #       choose from the distribution


    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
