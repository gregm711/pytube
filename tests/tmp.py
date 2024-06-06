from pytube import Channel as PyTubeChannel, YouTube
import os

api_key = os.environ.get("SCRAPING_BEE_API_KEY")
proxies = {
    "http": f"http://{api_key}:render_js=False&premium_proxy=False@proxy.scrapingbee.com:8886",
    "https": f"https://{api_key}:render_js=False&premium_proxy=False@proxy.scrapingbee.com:8887",
}
youtube_video_url = "https://www.youtube.com/watch?v=KuKv5EMahe0"
video = YouTube(youtube_video_url, proxies=proxies)
# print(video)
# print(video.title)
# print(video.channel_url)
# print(video.streams.first)

# youtube = YouTube(url, proxies=proxies if proxies else None)
# Get the audio stream
audio_stream = video.streams.filter(only_audio=True).first()
print(audio_stream)
print(audio_stream.download(output_path=".", filename="audio"))
# audio_stream.download(output_path=".", filename="audio")
# # even with proxies this fails intermitently
# channel = PyTubeChannel(video.channel_url, proxies=proxies)
# # print(channel.channel_uri)
# print(channel.channel_id)
