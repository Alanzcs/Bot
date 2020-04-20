# This program will allow your bot to join / leave the voice channel and play the sound from a YouTube video in the voice channel


# Commands: .join -> bot joins the Voice Channel that you are in;
#           .leave -> bot leaves the Voice Channel
#           .play (the link of the YouTube video) -> plays the sound from the YouTube link

# join vc
if message.content.startswith('.join'):
    channel = message.author.voice.channel
    await channel.connect()
# leave vc
if message.content.startswith('.leave'):
    if message.author.guild.voice_client == None:
        await message.channel.send('I am not in the voice channel!')
    else:
        await message.author.guild.voice_client.disconnect()

# play a song
if message.content.startswith('.play ') and message.author.guild.voice_client != None:
    song = message.content[6:]
    if os.path.exists("song.mp3"):
        os.remove('song.mp3')
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'song.mp3',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song])
    audio = discord.FFmpegPCMAudio('song.mp3')
    message.author.guild.voice_client.play(audio)
    await message.channel.send('Playing ' + song)