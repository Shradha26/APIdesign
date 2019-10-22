#!/usr/bin/python3

import urllib.request
import json

HUSTON = 'http://api.open-notify.org/astros.json'

def main():
    groundctrl = urllib.request.urlopen(HUSTON)
    print(groundctrl)
    print(type(groundctrl))
    print(dir(groundctrl))
    shuttlecraft = groundctrl.read()
    shuttle = json.loads(shuttlecraft.decode('utf-8'))
    print(type(shuttle))
    print(shuttle)
    print(shuttle.get('people'))
    print(groundctrl.code) #status code

    for astro in shuttle.get('people'):
        print(astro.get('name'))

if __name__ == "__main__":
    main()
