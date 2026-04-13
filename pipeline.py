class Job:
    def __init__(self, name, dependencies=None, func=None, retries=2):
        self.name = name
        self.dependencies = dependencies or []
        self.func = func
        self.completed = False
        self.failed = False
        self.retries = retries

    def run(self):
        attempt = 0
        while attempt <= self.retries:
            try:
                if self.func:
                    self.func()
                self.completed = True
                return
            except Exception as e:
                attempt += 1
                print(f"{self.name} failed (attempt {attempt}): {e}")

        self.failed = True