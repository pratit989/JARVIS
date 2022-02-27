# importing the module

from re import findall
from urllib.parse import quote as encode
from urllib.request import urlopen

from pafy import new
from pytube import YouTube
from vlc import Instance
from TTS import print_and_speak
import Settings


class YoutubePlayer:
    def __init__(self, term: str, download=False):
        self.title: str
        self.i = 1
        self.search_term = encode(term)
        print_and_speak("Searching")
        self.result = self.search()
        self.link = self.choice()
        if not download:
            self.play()
        elif download:
            self.download()

    def search(self):
        html = urlopen(f"https://www.youtube.com/results?search_query={self.search_term}")
        video_ids = findall(r"watch\?v=(\S{11})", html.read().decode())[:5]
        results = {}
        for video_id in video_ids:
            link = f"https://youtube.com/watch?v={video_id}"
            try:
                name = new(link)
                results[name.title] = link
            except OSError as osError:
                print(osError)
                pass
            except KeyError as keyError:
                print(keyError)
                pass
            except Exception as e:
                print(e)
        return results

    def choice(self):
        from TTS import print_and_speak
        print_and_speak(f"Here are the top {len(self.result)} results for your search")
        titles = list(self.result.keys())
        for title in titles:
            print(str(self.i) + '. ' + title)
            self.i += 1
        selector = int(input('\nEnter your choice:')) - 1
        self.title = titles[selector]
        return self.result[titles[selector]]

    def play(self):
        try:
            video = new(self.link).getbest()
            vlc = Instance()
            self.player = vlc.media_player_new()
            media = vlc.media_new(video.url)
            media.get_mrl()
            self.player.set_media(media)
            self.player.play()
            Settings.program_sound = False
            return self.player
        except OSError:
            self.play()

    def stop(self):
        self.player.stop()

    def pause_or_resume(self):
        self.player.pause()

    def download(self):
        # where to save
        try:
            print_and_speak(f'Downloading {self.title}')
            YouTube(self.link).streams.first().download(output_path='Downloads')
            open('Downloads')
        except PermissionError:
            pass
        except Exception as e:
            print_and_speak(f"The following error occurred while Downloading Error downloading {self.title}")
