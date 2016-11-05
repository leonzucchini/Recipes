import json

def id_generator(this_dict):
    for k, v in this_dict.items():
        if k == "dir":
            yield v
        elif isinstance(v, dict):
            for id_val in id_generator(v):
                yield id_val

def main():
    filepath = "linkscraping_preferences.json"
    with open(filepath, "r") as f:
        prefs = json.load(f)
    # print json.dumps(prefs, indent=4, sort_keys=True)
    
    for _ in id_generator(prefs):
        print(_)

if __name__ == '__main__':
    main()