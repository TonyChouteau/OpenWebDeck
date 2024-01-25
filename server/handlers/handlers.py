class Base:
    def __init__(self, id, default_value):
        self.id = id
        self.value = default_value

    def get_config(self):
        return {
            "id": self.id,
            "value": self.value
        }

    def get_value(self):
        print(f"Handler {self.id} return value {self.value}")
        return self.value

    def execute(self):
        print(f"Handler {self.id} executed with {self.value}")
        return 0

    def set_value(self, new_value):
        print(f"Handler {self.id} get a new value {new_value}")
        self.value = new_value


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