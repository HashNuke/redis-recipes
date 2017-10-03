class DummyRateLimiter:
    def __init__(self, name, **kwargs):
        self.name = name
        self.options = kwargs


    """
    Returns False if scope is "1".
    Just a test thing. No worries.
    """
    def can_allow(self, scope):
        if scope == "1":
            return False
        return True