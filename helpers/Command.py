class Command:
    def __init__(self, name, func, args=()):
        self.name = name
        self.func = func
        self.args = args

    def exec(self):
        if len(self.args) > 0:
            self.func(*self.args)
        else:
            self.func()