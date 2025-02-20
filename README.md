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
from RvLProMaster import types, bot, RunBOT
import asyncio

@RunBOT(always_run=True, save_polling=False) # Set True If You Want's Bot Always Run, But If You Set False BOT Only Run Just Once, If You Set save_polling into True Will saved polling, Default False (Not Saving Files)
async def MyBots():
    if types.text == "/start":
        await bot.Methods.sendMessage(types.chat_id, "*Hi I'm From `/start`*","MarkdownV2")

asyncio.run(MyBots())
