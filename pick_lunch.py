#!/usr/bin/env python

import sys, os, random

from pprint import pprint

from LunchPlace import LunchPlace
from LunchVisit import LunchVisit
from LuncherPreferences import LuncherPreferences

def read_places(filename):
    placenames = {}
    places = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line.startswith('#'):
                continue

            fields = line.split(',')
            name = fields[0]
            tags = fields[1:]

            if name in placenames:
                continue
            placenames[name] = True

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

            date, name = line.split(',')
            visit = LunchVisit(name, date)
            history.append(visit)
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

                weight, name = line.split(',')
                prefs.update(name, weight)
        prefs.normalize()
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
    for visit in history:
        assert(visit.place in places_dict)
    for prefs in lunchers_preferences:
        for place in prefs.preferences:
            assert(place in places_dict)
    return (places, history, lunchers_preferences)

def pick_my_lunch(place_probs):
    # got this code here http://eli.thegreenplace.net/2010/01/22/weighted-random-generation-in-python/
    totals = []
    running_total = 0
    for place,prob in place_probs.items():
        running_total += prob
        totals.append((place, running_total))

    rnd = random.random() * running_total
    for i, place_total in enumerate(totals):
        place, total = place_total
        if rnd < total:
            return place

def main(args):
    if len(args[1:]) < 3:
        sys.stderr.write("usage: %s <places> <history> <user-preferences>+\n" % args[0])
        sys.stderr.write("You must have 1 or more user preferences!\n")
        return 1

    places_filename = args[1]
    history_filename = args[2]
    luncher_prefs_filenames = args[3:]

    places, history, lunchers_prefs = load_files(places_filename, history_filename, luncher_prefs_filenames)
    total_preference_weight = 0
    for luncher_pref in lunchers_prefs:
        total_preference_weight += sum(luncher_pref.preferences.values())

    # TODO: pick a place based on history and preferences
    #       assign each place a probability
    #       choose from the distribution
    probabilities = {}
    for place in places:
        place_total_weight = 0
        for luncher_prefs in lunchers_prefs:
            if place.name in luncher_prefs.preferences:
                place_total_weight += luncher_prefs.preferences[place.name]
        probabilities[place.name] = place_total_weight / total_preference_weight
        
        most_recent_visit = None
        for visit in history:
            if visit.place != place.name: continue
            if most_recent_visit is None or most_recent_visit < visit.date:
                most_recent_visit = visit
        if most_recent_visit is not None:
            probabilities[place.name] *= most_recent_visit.discount

    # normalize back to actual probabilities, just for fun
    total_unnormalized_probs = sum(probabilities.values())
    for place in probabilities:
        probabilities[place] = probabilities[place] * 100 / total_unnormalized_probs


    # time to pick lunch!
    print pick_my_lunch(probabilities)
    
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
