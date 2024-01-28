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