import librosa

def get_pitch(pitch):
    if pitch < 50:
        return "Low"
    elif pitch < 100:
        return "Medium"
    else:
        return "High"

audio_file =r"C:\Users\shawv\Downloads\AAAudio\harvard.wav"  #the address of the aaaudio file where the address is store.

# Load the audio file
signal,sample_rate = librosa.load(audio_file)

# Compute the pitch
pitch, _ = librosa.piptrack(y=signal, sr=sample_rate)

# Take the mean of the pitch values
mean_pitch=pitch.mean()

 # Classify the pitch
pitch_category = get_pitch(mean_pitch)

print("Pitch:", pitch_category)
