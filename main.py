import yaml

FILE = "config.yaml"

def parse_config():
    with open(FILE, "r") as f:
        return yaml.safe_load(f)

def main():
    thing = parse_config()
    print(thing['ODE'])

if __name__ == '__main__':
    main()