from pytubefix import Stream, YouTube


def on_progress(stream, chunk, bytes_remaining):
    """Callback function"""
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100
    print(f"Download: {round(pct_completed, 2)}% complete")


vid = YouTube(input("URL: ").strip(), on_progress_callback=on_progress)
taitoru = vid.title
print(f"Title: {taitoru}")
audio_track: Stream = vid.streams.filter(only_audio=True).last()
print(f"Audio track found!\nBitrate: {audio_track.abr}\nCodec: {audio_track.audio_codec}")
audio_track.download(output_path="./audio")
# TODO: convert to mp3; delete the m4a?
