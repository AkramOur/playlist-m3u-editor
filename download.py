import os
import yt_dlp

# Replace with the URL of the YouTube playlist you want to download
playlist_url = "https://www.youtube.com/watch?v=pRpeEdMmmQ0&list=PLo1H4Rahb4WaF3bWJPTeujaeOeilzAHpL"

# Create a `yt-dlp` instance
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'outtmpl': 'downloaded_mp3s/%(title)s.%(ext)s',
    'ffmpeg_location': 'C:/ffmpeg-master-latest-win64-gpl/bin',  # Replace with the actual path to the directory containing ffmpeg.exe and ffprobe.exe
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(playlist_url, download=True)
    if 'entries' in info_dict:
        for entry in info_dict['entries']:
            print(f"Downloaded: {entry['title']}")

print("Playlist download complete.")
