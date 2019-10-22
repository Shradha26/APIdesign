#!/usr/bin/python3

import requests

HUSTON = "http://api.open-notify.org/astros.json"

def main():
    astros = requests.get(HUSTON)
    print(astros)
    print(type(astros))

    decodedastros = astros.json()
    print(decodedastros)
    print(type(decodedastros))

    for astro in astros.json().get('people'):
        print(astro.get('name'))
if __name__ == "__main__":
    main()
