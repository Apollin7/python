class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """This method is an initializer (constructor) for the Television class.
        It is automatically invoked when a new instance of the Television class is created.
        Return:
            None: It is none because the constructor does not return a value.
            It initializes the instance variables of the object, setting the initial power
            status to 'off' (False), mute status to 'not muted', volume status to
            the minimum value, and channel status to the minimum value defined by
            the class constant MIN_CHANNEL."""
        self._status = False
        self._muted = False
        self._volume = Television.MIN_VOLUME
        self._channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Toggle the power status of the Tv"""
        self._status = not self._status

    def mute(self) -> None:
        """Toggle the muted status of the Tv only when the Tv is turned on."""
        if self._status:
            self._muted = not self._muted

    def channel_up(self) -> None:
        """Increase the channel by one step, then wrapping around to the minimum channel if the maximum is reached."""
        if self._status:
            self._channel = (self._channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the channel by one step, then wrapping around to the maximum channel if the minimum is reached."""
        if self._status:
            self._channel = (self._channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """Increase the volume by one step, but not exceeding the maximum volume."""
        if self._status:
            self._muted = False
            if self._volume < Television.MAX_VOLUME:
                self._volume += 1

    def volume_down(self) -> None:
        """Decrease the volume by one step, but not going below the minimum volume limit."""
        if self._status:
            self._muted = False
            if self._volume > Television.MIN_VOLUME:
                self._volume -= 1

    def __str__(self) -> str:
        """return a string representation of the television's current state."""
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume if not self._muted else 0}"

