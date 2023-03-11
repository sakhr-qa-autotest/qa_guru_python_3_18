from dataclasses import dataclass


@dataclass
class Hosts:
    demoqa: str
    reqres: str

    def __init__(self, env):
        self.demoqa = {
            'local': 'https://demowebshop.tricentis.com',
            'prod': 'https://demowebshop.tricentis.com',
        }[env]
        self.reqres = {
            'local': 'https://demowebshop.tricentis.com',
            'prod': 'https://reqres.in/api/',
        }[env]
