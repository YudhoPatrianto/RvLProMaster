import os
import time
import sys
from dotenv import load_dotenv

load_dotenv()

class Configs:
    def __init__(self):
        self.checkConfiguration()
        self.token = os.getenv("token")
        self.url = os.getenv("endpoint")
        self.endpoint = f"{self.url}{self.token}"
    
    def checkConfiguration(self):
        try:
            if os.path.isfile("RvLProMaster/config/.env"):
                pass
            else:
                print("No .env File Found\nCreating .env File")
                time.sleep(2)
                token = input("Enter Your Bot Token: ")
                ask_endpoint = input("Are You Want's To Add Endpoint From https://github.com/tdlib/telegram-bot-api or You Want's To Use https://api.telegram.org? (y/N): ")
                if ask_endpoint == "y" or ask_endpoint == "Y":  # Custom Endpoint
                    custom_endpoint = input("Enter Your Custom Endpoint From https://github.com/tdlib/telegram-bot-api: \nExample: http://127.0.0.1/bot")
                    if sys.platform == "linux":
                        with open(r'.env', "w") as f: 
                            f.write(f'token = "{token}"\nendpoint = "https://api.telegram.org/bot"')
                            print(f"Configuration Saved!")
                    if sys.platform == "win32":
                        with open(r'.env', "w") as f: 
                            f.write(f'token = "{token}"\nendpoint = "https://api.telegram.org/bot"')
                            print(f"Configuration Saved!")
                else:  # Default Endpoint https://api.telegram.org
                    if sys.platform == "linux":
                        with open(r'RvLProMaster/config/.env', "w") as f:
                            f.write(f'token = "{token}"\nendpoint = "https://api.telegram.org/bot"')
                            print(f"Configuration Saved!")
                    elif sys.platform == "win32":
                        with open(r'RvLProMaster\config\.env', "w") as f:
                            f.write(f'token = "{token}"\nendpoint = "https://api.telegram.org/bot"')
                            print(f"Configuration Saved!")
        except KeyboardInterrupt:
            print(f"\nCanceling Configuration")
            sys.exit(1)

# Create Object    
Config = Configs()

# Pull Out Information
endpoint = Config.endpoint
token = Config.token
