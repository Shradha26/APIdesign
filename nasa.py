#!/usr/bin/python3
"""shradha.shankar@gmail.com || Shradha Shankar
Harvest astronomical picture of the day from NASA"""

import requests

## define URL as global
NASA_URL = 'https://api.nasa.gov/planetary/apod?api_key='

def main():
    """Code to talk to NASA APOD"""
    ## read in our nasa api key
    with open("/users/shradsha/nasa.creds", "r") as ncreds:
        my_api_key = ncreds.read().rstrip('\n')
    ## make an API request
    apod = requests.get(NASA_URL + my_api_key)
    ## parse out json
    apod = apod.json()
    ## print out date
    apod_date = apod.get('date')
    print(apod_date)
    ## print out explanation
    apod_exp = apod.get('explanation')
    print(apod_exp)
    ## print out URL
    apod_url = apod.get('hdurl')
    print(apod_url)

if __name__ == "__main__":
    main()
