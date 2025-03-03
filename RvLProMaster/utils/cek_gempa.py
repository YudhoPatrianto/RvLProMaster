from httpx import AsyncClient
from functools import wraps
import asyncio

class checkGempa:
    def __init__(self):
        self.url = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"

        # Data Gempa
        self.tanggal = None
        self.jam = None
        self.datetime = None
        self.coordinates = None
        self.lintang = None
        self.bujur = None
        self.magnitude = None
        self.kedalaman = None
        self.wilayah = None
        self.potensi = None
        self.dirasakan = None
        self.shakemap = None
        
    async def GetInformation(self):
        async with AsyncClient() as client:
            r = await client.get(self.url)
            r_data = r.json()
            
            # Pull Out Data Gempa
            self.tanggal = r_data["Infogempa"]["gempa"].get('Tanggal', '')
            self.jam = r_data["Infogempa"]["gempa"].get('Jam', '')
            self.datetime = r_data["Infogempa"]["gempa"].get('DateTime', '')
            self.coordinates = r_data["Infogempa"]["gempa"].get('Coordinates', '')
            self.lintang = r_data["Infogempa"]["gempa"].get('Lintang', '')
            self.bujur = r_data["Infogempa"]["gempa"].get('Bujur', '')
            self.magnitude = r_data["Infogempa"]["gempa"].get('Magnitude', '')
            self.kedalaman = r_data["Infogempa"]["gempa"].get('Kedalaman', '')
            self.wilayah = r_data["Infogempa"]["gempa"].get('Wilayah', '')
            self.potensi = r_data["Infogempa"]["gempa"].get('Potensi', '')
            self.dirasakan = r_data["Infogempa"]["gempa"].get('Dirasakan', '')
            self.shakemap = f"https://data.bmkg.go.id/DataMKG/TEWS/{r_data['Infogempa']['gempa'].get('Shakemap', '')}"
            return self

PullData = checkGempa()

def RunGempa():
    def wrapper(func):
        @wraps(func)
        async def wrapped(*args, **kwargs):
            await PullData.GetInformation()
            await func(*args, **kwargs)
        return wrapped
    return wrapper