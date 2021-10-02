import yaml


class Config:

    def __init__(self):
        with open('config.yml', 'r') as yml:
            self.config = yaml.load(yml)

    def get_string(self, node: str):
        if self.config.__contains__(node):
            return self.config[node]
        return None

    def get_integer(self, node: str):
        if self.config.__contains__(node):
            num = self.config[node]
            if str.isdigit(num):
                return int(num)
        return None
