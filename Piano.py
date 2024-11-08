# encoding: utf-8

from music import *
import random

# Configurar el tempo
tempo = 120
# Play.setTempo(tempo)

# Definir la matriz de transición (probabilidades entre notas)
transition_matrix = [
    [0.4, 0.3, 0.2, 0.1, 0.0], 
    [0.3, 0.4, 0.2, 0.1, 0.0],
    [0.2, 0.3, 0.4, 0.1, 0.0],
    [0.1, 0.2, 0.4, 0.3, 0.0],
    [0.0, 0.1, 0.2, 0.3, 0.4]
]

major_scale = [0, 2, 4, 5, 7, 9, 11]

# Convertir el estado a tono MIDI
def state_to_pitch(state, base_pitch=60):
    scale_degree = state % len(major_scale)
    octave = state // len(major_scale)
    return base_pitch + major_scale[scale_degree] + 12 * octave

# Seleccionar la siguiente nota basada en probabilidades de la matriz
def next_state(current_state):
    probabilities = transition_matrix[current_state]
    # return random.choices(range(len(probabilities)), probabilities)[0]

    cumulative_prob = 0.0
    r = random.uniform(0, 1)  # Genera un número aleatorio entre 0 y 1

    # Itera sobre las probabilidades acumulándolas
    for i, prob in enumerate(probabilities):
        cumulative_prob += prob
        if r <= cumulative_prob:
            return i  # Retorna el estado correspondiente

# Generar una melodía utilizando la cadena de Markov
def generate_melody(transition_matrix, num_notes, base_pitch=60):
    melody = []
    current_state = random.randint(0, len(transition_matrix) - 1)

    for _ in range(num_notes):
        pitch = state_to_pitch(current_state, base_pitch)
        #duration = random.choice(durations)  # Elegir duración aleatoria
        dynamic = random.randint(60, 100)  # Elegir volumen dinámico

        note = Note(pitch, QN, dynamic)  # Crear la nota con expresión
        melody.append(note)

        current_state = next_state(current_state)  # Transición al siguiente estado

    return melody

# Crear una frase con la melodía generada
def create_phrase(melody):
    phrase = Phrase()
    phrase.setTempo(tempo)
    for note in melody:
        phrase.addNote(note)
    return phrase

# Generar y reproducir la melodía
num_notes = 360
melody = generate_melody(transition_matrix, num_notes)

phrase = create_phrase(melody)
part = Part()
part.addPhrase(phrase)

# Reproducir la composición
Play.midi(part)

# Guardar la composición en un archivo MIDI
Write.midi(part, "piano.mid")
