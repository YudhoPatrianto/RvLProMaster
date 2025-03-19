import os
import time
import sys
from typing import Any

class access_list:
    def __init__(self):
        self.username = ''
        self.file_path = "RvLProMaster/admin_utils/list_access.txt"

    def CheckFile(self, username: Any):
        try:
            self.username = username
            if os.path.exists("list_access.txt"):
                pass
            else:
                print(f"File list_access.txt Not Found Creating...")
                time.sleep(2)
                with open(self.file_path, "w") as f:
                    f.write(f"{self.username}\n")
                    f.close()
        except KeyboardInterrupt:
            print(f"Canceling...")
            time.sleep(2)
            sys.exit(1)
            
    def CheckAccess(self, username: Any):
        self.username = username
        with open(self.file_path, 'r') as f:
            get_list = f.read().split()
            return get_list
    
    def AddAccess(self, username: Any):
        self.username = username
        with open(self.file_path, 'a') as f:
            f.write(f"{self.username}\n")
            f.close()
        
AccessManager = access_list()