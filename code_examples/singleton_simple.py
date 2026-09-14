class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.debug = True
            cls._instance.database_url = "localhost"
        return cls._instance

config1 = Config()
config2 = Config()

print(config1 is config2)