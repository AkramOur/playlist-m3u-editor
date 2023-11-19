import os
import yt_dlp




def download_playlist_youtube(url, output_folder):
    # Create a `yt-dlp` instance
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_folder+'/%(title)s.%(ext)s',
        'ffmpeg_location': 'C:/ffmpeg-master-latest-win64-gpl/bin',  # Replace with the actual path to the directory containing ffmpeg.exe and ffprobe.exe
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        if 'entries' in info_dict:
            for entry in info_dict['entries']:
                print(f"Downloaded: {entry['title']}")

    print("Playlist download complete.")
