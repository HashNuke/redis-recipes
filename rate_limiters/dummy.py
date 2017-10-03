class DummyRateLimiter:
    def __init__(self, name, **kwargs):
        self.name = name
        self.options = kwargs

    def can_allow(self, scope):
        if scope == "1":
          return False
        else:
          return True