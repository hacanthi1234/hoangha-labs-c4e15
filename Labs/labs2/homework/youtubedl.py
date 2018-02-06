from youtube_dl import YoutubeDL

# options = {
#     'format': 'bestaudio/audio'
# }
#
# dl = YoutubeDL (options)
# dl.download(['https://www.youtube.com/watch?v=ZHoLaLlL5lA','https://www.youtube.com/watch?v=qAQHz2zPFFQ'])


# options = {
#     'default_search': 'ytsearch',
#     'max_downloads': 1
# }
# dl = YoutubeDL(options)
# dl.download(['con điên TAMKA PKL'])

options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    # 'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Em dạo này có'])
