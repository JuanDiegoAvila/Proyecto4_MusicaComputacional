from music import *
import random

# Set up the tempo
tempo = 120

# Define the transition matrix (probability matrix)
transition_matrix = [
    [0.2, 0.4, 0.2, 0.1, 0.1],
    [0.3, 0.1, 0.2, 0.2, 0.2],
    [0.2, 0.3, 0.1, 0.2, 0.2],
    [0.1, 0.2, 0.3, 0.1, 0.3],
    [0.2, 0.2, 0.2, 0.3, 0.1]
]


# Generate a melody using the Markov chain
def generate_melody(transition_matrix, num_notes):
    melody = []
    current_state = random.randint(0, len(transition_matrix) - 1)
    
    for _ in range(num_notes):
        melody.append(current_state)
        next_state = random.choice(range(len(transition_matrix[current_state])))
        current_state = next_state
        
    return melody

# Convert state to MIDI pitch
def state_to_pitch(state):
    return 60 + state  # Map state to MIDI note values

# Generate the melody
num_notes = 16
melody_states = generate_melody(transition_matrix, num_notes)
melody_pitches = [state_to_pitch(state) for state in melody_states]

# Create a Phrase to play the melody
phrase = Phrase()
for pitch in melody_pitches:
    note = Note(pitch, 0.5)
    phrase.addNote(note)

# Create a Part to play the Phrase
part = Part()
part.addPhrase(phrase)

# Play the composition
Play.midi(part)
 