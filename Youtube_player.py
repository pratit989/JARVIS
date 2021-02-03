from urllib.parse import quote as encode
from urllib.request import urlopen
from re import findall
from pafy import new
from vlc import Instance


class YoutubePlayer:
    def __init__(self, term: str):
        self.i = 1
        self.search_term = encode(term)
        self.result = self.search()
        self.link = self.choice()
        self.play()

    def search(self):
        html = urlopen("https://www.youtube.com/results?search_query=" + self.search_term)
        video_ids = findall(r"watch\?v=(\S{11})", html.read().decode())[:5]
        results = {}
        for video_id in video_ids:
            link = "https://youtube.com/watch?v=" + video_id
            try:
                name = new(link).title
                results[name] = link
            except OSError:
                pass
        return results

    def choice(self):
        from TTS import print_and_speak
        print_and_speak("Here are the top " + str(len(self.result)) + " results for your search")
        titles = list(self.result.keys())
        for title in titles:
            print(str(self.i) + '. ' + title)
            self.i += 1
        selector = int(input('\nEnter your choice:')) - 1
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
            return self.player
        except OSError:
            self.play()

    def stop(self):
        self.player.stop()

    def pause_or_resume(self):
        self.player.pause()
