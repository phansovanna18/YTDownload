from pytube import YouTube


class Download:
    link = ''
    length = 0
    views = 0

    def calc_time(self):
        length = self.length
        hour = 0
        minute = 0

        while length > 59:
            minute += 1
            length -= 60

        while minute > 59:
            hour += 1
            minute -= 60

        return f"{hour}:{minute}:{length}".format(hour=hour, minute=minute, length=length)

    def download(self):
        yt = YouTube(self.link)
        self.length = yt.length
        print("Title:", yt.title)
        print("Number of views:", yt.views)
        print("Length of video:", self.calc_time())
        print("Rating of video:", yt.rating)
        ys = yt.streams.get_highest_resolution()
        print("downloading")

        # #default path
        # ys.download()

        # #custom path
        ys.download('video')

        print("completed")


if __name__ == "__main__":
    _link = input("Link:")
    d = Download()
    d.link = _link
    d.download()
