# Creat a class Config that read configuration setting from a file and provide methods to access these settings.
class Config:
    def __init__(self, filename = "config.txt"):
        self.settings = {}
        try:
            with open(filename, "r", encoding = "utf-8") as f:
                for line in f:
                    if "=" in line:
                        key, value = line.strip().split("=")
                        self.settings[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"{filename} is not found and we can not access that ")
    
    def get(self, key):
        return self.settings.get(key)
    
config = Config()
database = config.get("database")
username = config.get("username")
if database and username:
    print("database  name:", database)
    print("user name :", username)
else:
    print("'database' settings is not found in config.txt")
    print("'username' settings is not found in config.txt")
    
