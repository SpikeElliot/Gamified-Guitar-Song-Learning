import os
import sys
# Allow importing modules from parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from audio_load_handler import AudioLoadHandler
from pitch_detection import save_pitches


test_audio = AudioLoadHandler(path="./separated_tracks/htdemucs_6s/nerv/guitar.wav")
save_pitches(test_audio)