import os
from dotenv import load_dotenv

load_dotenv()


class Configs:
    def __init__(self):
        self.token = os.getenv("token")
        self.url = os.getenv("endpoint")
        self.endpoint = f"{self.url}{self.token}"
    
# Create Object    
Config = Configs()

# Pull Out Information
endpoint = Config.endpoint
token = Config.token
