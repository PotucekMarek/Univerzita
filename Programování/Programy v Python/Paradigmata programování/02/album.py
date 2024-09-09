class Time:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
        self.hours = 0

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.minutes

    def get_seconds(self):
        return self.seconds

    def set_hours(self, h):
        self.hours = h
        return self

    def set_minutes(self, m):
        hours = int(m / 60)
        if hours > 0:
            self.set_hours(self.get_hours() + hours)
            self.minutes = m % 60
            return self
        self.minutes = m
        return self
    
    def set_seconds(self, s):
        minutes = int(s / 60)
        if minutes > 0:
            self.set_minutes(self.get_minutes() + minutes)
            self.seconds = s % 60
            return self
        self.seconds = s
        return self

class Track:
    def __init__(self):
        self.name = ""
        self.length = Time()
    
    def get_name(self):
        return self.name

    def set_name(self, name_track):
        self.name = name_track
        return self
    
    def get_length(self):
        return self

    def set_length(self, ho, mi, se):
        self.length.set_hours(ho)
        self.length.set_minutes(mi)
        self.length.set_seconds(se)

track = Track()
track.set_name("ahoj")
track.set_length(150,5,4)
print(track.get_length())
print(track.get_name())

class Album:
    def __init__(self):
        self.name = ""
        self.length = 0
        self.tracks = ""
