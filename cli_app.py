import argparse

def add_rating(name, stars):
    with open('films.csv', 'a') as f:
        f.write(f"{name},{stars}\n")

parser = argparse.ArgumentParser(description='Submit a film rating.')
parser.add_argument('--film-name', help='The name of the film you\'re rating', dest="film_name")
parser.add_argument('--stars', help='The star rating of the film', dest="stars")
args = parser.parse_args()
add_rating(args.film_name, args.stars)

