from pytube import Channel as PyTubeChannel, YouTube
import os

api_key = os.environ.get("SCRAPINGBEE_API_KEY")
proxies = {
    "http": f"http://{api_key}:render_js=False&premium_proxy=False@proxy.scrapingbee.com:8886",
    "https": f"https://{api_key}:render_js=False&premium_proxy=False@proxy.scrapingbee.com:8887",
}
youtube_video_url = "https://www.youtube.com/watch?v=KuKv5EMahe0"
video = YouTube(youtube_video_url, proxies=proxies)
print(video)
print(video.title)
print(video.channel_url)
# # print(video.streams.first)
channel = PyTubeChannel(video.channel_url)
print(channel.channel_uri)
print(channel.channel_id)
