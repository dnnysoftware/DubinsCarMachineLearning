import yaml
import graph

FILE = "config.yaml"

def parse_config():
    with open(FILE, "r") as f:
        return yaml.safe_load(f)

def main():
    config = parse_config()
    s0 = config['USER']['START']
    sf_prime = config['USER']['FINISH']
    population_size = config['USER']['POP_SIZE']
    plot = graph.create_plot()


if __name__ == '__main__':
    main()