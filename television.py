class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self):
        self._status = not self._status

    def mute(self):
        if self._status:
            self._muted = not self._muted

    def channel_up(self):
        if self._status:
            self._channel = (self._channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self):
        if self._status:
            self._channel = (self._channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self):
        if self._status:
            self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self):
        if self._status:
            self._muted = False
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume if not self._muted else 0}"

