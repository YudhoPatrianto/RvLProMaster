#### Create Virtual Environment
```bash
python3 -m venv .venv
```
#### Linux Users
```bash
source .venv/bin/activate
```
#### Windows Users (CMD)
```bat
\.venv\bin\activate.bat
```
#### Upgrade Pip To Latest Version
```bash
pip install --upgrade pip
```
#### Install Needed Library 
```bash
pip install -r requirements.txt
```
#### Run The Bots
```bash
python3 main.py
```

#### Usage:
```python
from RvLProMaster import Types, bot
import asyncio

async def MyBots():
    while True: # Add This If Your Bot Still Want's Running
        types = Types.RunBOT()
        if types.text == "/start":
            await bot.Methods.sendMessage(types.chat_id, "*Hi I'm From `/start`*","MarkdownV2")

asyncio.run(MyBots())
