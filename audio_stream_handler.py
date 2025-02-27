import sounddevice as sd
import tempfile
from scipy.io.wavfile import write


class AudioStreamHandler():
    """
    Handles operations relating to audio input such as streaming and recording.

    Attributes
    ----------
    CHANNELS : int
        Specifies whether the audio channel is mono (1) or stereo (2).
    RATE : int
        The sample rate of the audio.
    DTYPE : str
        Specifies the audio's datatype.
    input_devices : list of dicts
        A list of available audio input devices.

    Methods
    -------
    record(duration=5., in_dev_idx=0)
        Save a WAV file recording of the audio input stream.
    """
    def __init__(self):
        """The constructor for the AudioStreamHandler class."""
        self.CHANNELS = 1
        self.RATE = 44100
        self.DTYPE = "float32" # Datatype used by audio processing libraries
        self.input_devices = self._get_input_devices()

    def _get_input_devices(self):
        """Return a list of available audio input devices."""
        devices = sd.query_devices()
        input_devs = []
        for d in devices:
            if d["max_input_channels"] > 0 and d["hostapi"] == 0:
                input_devs.append(d)
        return input_devs

    def record(self, duration=5., in_dev_idx=0):
        """
        Record an audio input stream for a given duration in seconds using a
        given input device's index, saving the data to a temporary WAV file.

        Parameters
        ----------
        duration : float, default=5
            The length of time of the recording in seconds.
        input_device_idx : int, default=0
            The index of the input device.
        
        Returns
        -------
        str
            The file path to the newly-created temp file.
        
        Examples
        --------
        >>> input = AudioStreamHandler()
        >>> input.record(12.5, 1)
        C:/Users/user/AppData/Local/Temp/tmpez5ms7vo.wav # Windows
        """
        print(f"Recording {duration}s of input audio...")
        audio_data = sd.rec(
            int(duration * self.RATE),
            samplerate=self.RATE,
            device=in_dev_idx,
            channels=self.CHANNELS,
            dtype=self.DTYPE
        )
        sd.wait()

        # Save recorded audio as a temp WAV file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        write(temp_file.name, self.RATE, audio_data)
        return temp_file.name