#!/usr/bin/python3

import json

def main():
    #data 
    hitchhikers = [{"name":"Zaphod Beeblebrox", "species":"Betelgeusian"}, {"name":"Arthur Dent", "species":"Human"}]
    for character in hitchhikers:
        print(character.get("name"))
    hitchhikers.append({"name":None, "species":"Human"})

    with open("galaxyguide.json", "w") as jfile:
        json.dump(hitchhikers, jfile)

    jsonstring = json.dumps(hitchhikers)
    print(jsonstring)

    with open("datacenter.json", "r") as dfile:
        datacenterstr = dfile.read()
        print(type(datacenterstr))
    print(datacenterstr)
    datacenterdecoded = json.loads(datacenterstr)
    print(type(datacenterdecoded))
    print(datacenterdecoded)

if __name__ == "__main__":
    main()
