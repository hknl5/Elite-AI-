import numpy as np
import wave
import json
from scipy.io import wavfile

# Define a dummy emotion detection function (to be replaced with an actual model)
def detect_emotion(segment):
    # Placeholder: Randomly assign one of the emotions for demonstration purposes
    emotions = ['happy', 'sad', 'excited', 'scared', 'neutral']
    return np.random.choice(emotions)

# Load the audio file
file_path = '/Users/hanouf/Downloads/sound1.wav'
rate, data = wavfile.read(file_path)

# Define the duration for each segment (1 or 2 seconds)
segment_duration = 1  # in seconds

# Calculate the number of samples per segment
samples_per_segment = segment_duration * rate

# Initialize the results list
results = []

# Process the audio file in segments
for start in range(0, len(data), samples_per_segment):
    end = start + samples_per_segment
    segment = data[start:end]
    
    # Detect emotion for the segment
    emotion = detect_emotion(segment)
    
    # Append the result to the list
    results.append({
        'start_time': start / rate,
        'end_time': end / rate,
        'emotion': emotion
    })

# Convert results to JSON format
json_results = json.dumps(results, indent=4)

# Save the JSON results to a file
json_file_path = '/Users/hanouf/Downloads/emotion_analysis.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(json_results)

json_file_path
