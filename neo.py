#!/usr/bin/python3
"""Shradha Shankar NEO"""

import requests
import argparse

def main():
    """Run time code"""

    #define our url
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
    startdate = 'start_date=' + args.start
    enddate = '&end_date=END_DATE'
    
    with open('/users/shradsha/nasa.creds') as creds:
        myapikey = creds.read().rstrip('\n')
   
    myapikey = '&api_key=' + myapikey
    neourl += startdate  + myapikey

    neow = requests.get(neourl)
    print(neow.json())
    #prompt user for start date

    #prompt user for end date

    #make our API request

    #parse out json



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', help='provide a start date')
    args = parser.parse_args()
    main()
