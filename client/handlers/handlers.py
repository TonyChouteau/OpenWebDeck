from handlers.Base import Base

class SwitchBranch(Base):
    def __init__(self):
        super().__init__("switch_branch", "debian11")

    def get_config(self):
        return {
            **super().get_config(),
            "name": "Switch branch",
            "sub-cells": [{
                "name": "Debian11",
                "value": "debian11"
            }, {
                "name": "Dev",
                "value": "dev"
            }, {
                "name": "Tony",
                "value": "tony"
            }, {
                "name": "Tony2",
                "value": "tony2"
            }, {
                "name": "Maxime",
                "value": "maxime"
            }, {
                "name": "Lucas",
                "value": "lucas"
            }]
        }


config = [
    SwitchBranch()
]