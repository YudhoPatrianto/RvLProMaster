# Load Library
from RvLProMaster import endpoint
from httpx import AsyncClient

@staticmethod
async def clear_log():
    async with AsyncClient() as client:
        r = await client.get(f'{endpoint}/getUpdates')
        d = r.json()
        if d['result']:
            l = max(update['update_id'] for update in d['result'])
            payload = {'offset': l + 1}
            await client.get(f"{endpoint}/getUpdates", params=payload)
        else:
            print("No Polling Cleared, Skipping!")
            pass