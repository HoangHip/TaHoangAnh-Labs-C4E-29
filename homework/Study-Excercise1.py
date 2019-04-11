from youtube_dl import YoutubeDL

# Sample 1 : Download a single youtube video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=gUtCfwXgDjI'])

#  Sample 2 : Download multiple youtube videos
# dl = YoutubeDL()
# Put list of song urls in download function to download them , one by one 
# dl.download(['https://www.youtube.com/watch?v=gUr4qp6YGLs', 'https://www.youtube.com/watch?v=rPU41Mw7txo'])

# Sample 3 : Download audio

# options = {
    # 'format': 'bestaudio/audio' # Tell the downloader to download only the best quality of audio
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=rPU41Mw7txo'])

# Sample 4 : Search and then download the first video

# options = {
#     'default_search' : 'ytsearch', # tell downloader to search instead of directly downloading
#     'max_downloads' : 1, # Tell downloader to download only the first entry (audio)
# }
# dl = YoutubeDL(options)
# dl.download(['Anh không thề gì đâu anh làm Phúc Du'])

# Sample 5 : Search and then download the first audio

options = {
    'default_search' : 'ytsearch',
    'max_downloads' : 1,
    'format' : 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Talk Khalid'])