from pytube import Channel as PyTubeChannel, YouTube

youtube_video_url = "https://www.youtube.com/watch?v=BQz5vazLkFY"
video = YouTube(youtube_video_url)
print(video)
channel = PyTubeChannel(video.channel_url)
print(channel.channel_id)
