import yt_dlp
import sys

def download_video(url, output_path='.'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'verbose': True,
    }
    print(f"Starting download for {url}...")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        download_video(url)
    else:
        print("Usage: python download.py <youtube_url>")
