
from __future__ import annotations

import yaml


def main():
    '''Main entry point for generating a configuration file.'''
    
    # open the example configuration file
    with open("example.config.yaml", "r") as file:
        data = yaml.safe_load(file)
    
    
if __name__ == "__main__":
    main()