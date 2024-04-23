from youtubesearchpython import VideosSearch
from youtubesearchpython import PlaylistsSearch
import subprocess
import torch

def main ():
    print(torch.cuda.is_available())


    # channelsSearch = VideosSearch('Lex Fridman Podcast')

    # results = channelsSearch.result()['result']
    # ids = [id['title'] for id in results]
    # print(ids)


    video_ids = [
        
    ]


    for id in video_ids:
        result = subprocess.run("yt-dlp -x --audio-format mp3 -o vids/" + id + " -- https://www.youtube.com/watch?v=" + id, shell=True)
        result = subprocess.run("whisper --language en --device cuda --model medium -o vids -- vids/" + id + ".mp3", shell=True)
        result = subprocess.run("rm vids/" + id + ".mp3", shell=True)
        print(id + " done")

if __name__ == "__main__":
    main()