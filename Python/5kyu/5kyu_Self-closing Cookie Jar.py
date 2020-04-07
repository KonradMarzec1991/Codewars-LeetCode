class SelfClosing:
    def __init__(self, cookie_jar):
        self.jar = cookie_jar

    def __enter__(self):
        self.jar.open_jar()
        return self.jar

    def __exit__(self, exc_type, exc_val, exc_t):
        self.jar.close_jar()