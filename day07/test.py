#!/usr/bin/env python
import yaml

if __name__ == '__main__':
    #with open('config.yaml', encoding='UTF-8') as config_file:
    with open('guy.yaml', encoding='UTF-8') as config_file:
        config = yaml.safe_load(config_file)
        print(config)
