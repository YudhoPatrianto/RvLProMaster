from dotenv import load_dotenv
import os
import glob
import sys

class Configs:
    def __init__(self) -> None:
        self.result = ''
        self.findEnv()
        load_dotenv(self.result)

        self.token = os.getenv("token")
        self.url = os.getenv("endpoint")
        self.endpoint = f"{self.url}{self.token}"
        self.gemini_api_key = os.getenv("gemini_api_key")
        self.github_pat = os.getenv("github_pat")

        if os.path.isfile(self.result):
            load_dotenv(self.result)
        else:
            print("No Authentication File Found, Creating")
            self.CreateAuth()
            self.clearScreen()
            print("Configuration Success")
            self.load_env_again()

    def clearScreen(self):
        os.system("clear" if sys.platform == "linux" else "cls")

    def findEnv(self, dir="."):
        for find_env in glob.iglob(f"{dir}/**/.env", recursive=True):
            self.result = os.path.abspath(find_env)
            return  
        print("Authentication File Not Found.")

    def CreateAuth(self):
        try:
            token = input("Please Input Your Token: ")
            selector_endpoint = int(input(
                "Please Choose Your Endpoint:\n"
                "1. (Default) https://api.telegram.org/bot\n"
                "2. (Custom) http://localhost/bot\n\n"
                "Enter Your Choice: "
            ))

            endpoint = "https://api.telegram.org/bot" if selector_endpoint == 1 else input("Enter Custom Endpoint: ")

            with open(".env", "w") as f:
                f.write(f"token = '{token}'\nendpoint = '{endpoint}'\n")

            print("Configuration Success!")

        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

    def load_env_again(self):
        """ Reloads environment variables after creating .env """
        self.findEnv()
        load_dotenv(self.result)
        
        self.token = os.getenv("token")
        self.url = os.getenv("endpoint")
        self.endpoint = f"{self.url}{self.token}"
        self.gemini_api_key = os.getenv("gemini_api_key")
        self.github_pat = os.getenv("github_pat")

        if os.path.isfile(self.result):
            load_dotenv(self.result)

# Create Object    
Config = Configs()

# Pull Out Information
endpoint = Config.endpoint
token = Config.token
gemini_api_key = Config.gemini_api_key
github_pat = Config.github_pat
