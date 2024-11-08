# encoding: utf-8

from music import *
import random

# Configurar el tempo (igual que el piano)
tempo = 120

# Definir la matriz de transición para las cuerdas (más lentos y sostenidos)
transition_matrix_strings = [
    [0.5, 0.3, 0.1, 0.1, 0.0],  # Prefiere moverse poco
    [0.2, 0.5, 0.2, 0.1, 0.0],
    [0.1, 0.2, 0.5, 0.2, 0.0],
    [0.0, 0.1, 0.3, 0.5, 0.1],
    [0.0, 0.0, 0.1, 0.3, 0.6]
]

# Reutilizamos la misma escala mayor
major_scale = [0, 2, 4, 5, 7, 9, 11]  # Intervalos en semitonos

# Convertir el estado a tono MIDI usando la escala mayor, ajustado para cuerdas
def state_to_pitch_strings(state, base_pitch=55):  # Base en una octava más baja
    scale_degree = state % len(major_scale)
    octave = state // len(major_scale)
    return base_pitch + major_scale[scale_degree] + 12 * octave

# Seleccionar el siguiente estado para cuerdas basado en la matriz de transición
def next_state_strings(current_state):
    probabilities = transition_matrix_strings[current_state]
    cumulative_prob = 0.0
    r = random.uniform(0, 1)

    for i, prob in enumerate(probabilities):
        cumulative_prob += prob
        if r <= cumulative_prob:
            return i

# Generar una melodía para las cuerdas
def generate_string_melody(transition_matrix, num_notes, base_pitch=55):
    melody = []
    current_state = random.randint(0, len(transition_matrix) - 1)

    for _ in range(num_notes):
        pitch = state_to_pitch_strings(current_state, base_pitch)
        dynamic = random.randint(50, 80)  # Volumen más suave

        # Crear la nota con una duración más larga (blanca o mínima)
        note = Note(pitch, HN, dynamic)
        melody.append(note)

        current_state = next_state_strings(current_state)

    return melody

# Crear una frase con la melodía de cuerdas
def create_string_phrase(melody):
    phrase = Phrase()
    phrase.setTempo(tempo)
    for note in melody:
        phrase.addNote(note)
    return phrase

# Generar y reproducir la melodía de cuerdas
num_notes = 360
string_melody = generate_string_melody(transition_matrix_strings, num_notes)

string_phrase = create_string_phrase(string_melody)
string_part = Part(STRINGS, 1)  # Usamos instrumento de cuerdas

string_part.addPhrase(string_phrase)

# Reproducir la composición
Play.midi(string_part)

# Guardar la composición en un archivo MIDI
Write.midi(string_part, "strings.mid")
