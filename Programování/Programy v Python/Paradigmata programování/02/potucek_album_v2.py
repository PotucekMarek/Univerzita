class Time:
    def __init__(self):
        self._seconds = 0
        self._minutes = 0
        self._hours = 0

    def get_hours(self):
        return self._hours

    def get_minutes(self):
        return self._minutes

    def get_seconds(self):
        return self._seconds

    def set_hours(self, h):
        self._hours = h
        return self

    def set_minutes(self, m):
        if m > 59:
            raise ValueError("Minutes can't be higher than 59.")
        self._minutes = m
        return self

    def set_seconds(self, s):
        if s > 59:
            raise ValueError("Seconds can't be higher than 59.")
        self._seconds = s
        return self


def _check_track_list(track_list):
    for element in track_list:
        if not (isinstance(element, Track)):
            return False
    return True


class Track:
    def __init__(self):
        self._name = ""
        self._length = Time()

    def get_name(self):
        return self._name

    def set_name(self, track_name):
        self._name = track_name
        return self

    def get_length(self):
        return self._length


class Album:
    def __init__(self):
        self._name = ""
        self._tracks = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name
        return self

    def get_length(self):
        s = 0
        m = 0
        h = 0
        for track in self.get_tracks():
            s += track.get_length().get_seconds()
            m += track.get_length().get_minutes()
            h += track.get_length().get_hours()
        if s > 59:
            m += int(s / 60)
            s %= 60
        if m > 59:
            h += int(m / 60)
            m %= 60
        ret = Time()
        ret.set_hours(h)
        ret.set_minutes(m)
        ret.set_seconds(s)
        return ret

    def get_tracks(self):
        return self._tracks.copy()

    def set_tracks(self, track_list):
        if not isinstance(track_list, list) or not _check_track_list(track_list):
            raise ValueError("All elements must be tracks.")
        self._tracks = track_list.copy()
        return self


def make_track(name, m, s):
    track = Track()
    track.set_name(name)
    track.get_length().set_minutes(m)
    track.get_length().set_seconds(s)
    return track


def make_album(name, tracks):
    album = Album()
    album.set_name(name)
    album.set_tracks(tracks)
    return album


if __name__ == '__main__':
    song_1 = make_track("ahoj", 5, 40)
    song_2 = make_track("jak", 1, 44)
    song_3 = make_track("se", 2, 30)
    song_4 = make_track("mas", 7, 11)
    song_5 = make_track("smog", 5, 48)
    song_6 = make_track("ostrava", 3, 7)
    song_7 = make_track("cigan", 6, 5)

    lst = [song_1, song_2, song_3, song_4, song_5, song_6, song_7]
    lst_2 = [song_1, song_2]

    album = make_album("republika", lst)
    album_2 = make_album("haf", lst_2)

    haf = album.get_tracks()
    print(album.get_name())
    print(haf[1].get_name())

    print(album.get_length().get_hours(), album.get_length().get_minutes(), album.get_length().get_seconds())
    print(album_2.get_length().get_hours(), album_2.get_length().get_minutes(), album_2.get_length().get_seconds())
