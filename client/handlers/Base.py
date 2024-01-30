class Base:
    def __init__(self, id, default_value):
        self.id = id
        self.value = default_value

    def get_config(self):
        return {
            "id": self.id,
            "value": self.value
        }

    def execute(self, value):
        self.value = value
        print(f"Handler {self.id} executed with {self.value}")