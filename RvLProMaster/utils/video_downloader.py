import yt_dlp

class videoDownloader:
    # Download Video
    @staticmethod
    def FromLinks(links):
        config_download = {
            'format': 'best',
            'outtmpl': 'video.mp4',
            'quiet': True,
            'no_warnings': True,
            'logtostderr': False,
        }
        with yt_dlp.YoutubeDL(config_download) as ydl:
            ydl.download(links)