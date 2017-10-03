class DummyRateLimiter:
    def __init__(self, name, **kwargs):
        self.name = name
        self.options = kwargs

    def can_allow(self, scope):
        # Returns False if scope is "1".
        # Just a test thing. No worries.
        if scope == "1":
          return False
        return True