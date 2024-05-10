# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:58:42 2024

@author: vmurc
"""

import streamlit as st
import numpy as np
from scipy.io.wavfile import write
import os

notes = {
        "C4": 261.63, "Db4": 277.18, "D4": 293.66, "Eb4": 311.13,
        "E4": 329.63, "F4": 349.23, "Gb4": 369.99, "G4": 392.00,
        "Ab4": 415.30, "A4": 440.00, "Bb4": 466.16, "B4": 493.88,
        "C5": 523.25
    }

create_audio_files(notes)  # Initialize audio files only once

note_keys = list(notes.keys())

def sanitize_filename(name):
    return name.replace("#", "Sharp").replace("b", "Flat")
        
def generate_tone(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(2 * np.pi * frequency * t)
    return (tone * 32767 / np.max(np.abs(tone))).astype(np.int16)

def create_audio_files(notes):
    sample_rate = 44100
    duration = 1  # seconds
    directory = "audio"  # Specify the directory to save audio files

    if not os.path.exists(directory):
        os.makedirs(directory)

    for note, freq in notes.items():
        filename = sanitize_filename(note)
        data = generate_tone(freq, duration, sample_rate)
        write(f"{directory}/{filename}.wav", sample_rate, data)
        
def main_menu():
    
    st.subheader("Choose your adventure:")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button('The Melodic Maze'):
            st.session_state['choice'] = 'maze'
    with col2:
        if st.button('The Quantum Quagmire'):
            st.session_state['choice'] = 'quantum'
    with col3:
        if st.button('The Harmony Heights'):
            st.session_state['choice'] = 'harmony'
    
    if 'choice' in st.session_state:
        if st.session_state['choice'] == 'maze':
            narrative_maze()
        elif st.session_state['choice'] == 'quantum':
            narrative_quantum()
        elif st.session_state['choice'] == 'harmony':
            narrative_harmony()

def narrative_maze():
    st.write("Victor and Lindsey decide to explore the Melodic Maze, a labyrinth where each turn and dead end is guided by musical cues.")
    st.image("1-1-1.webp", caption='The Melodic Maze')
    st.write("The maze is alive with the sounds of nature, and only by correctly interpreting the musical hints can they find their way to the center, where a clue to the Heart of Harmony's location awaits.")
    maze_choices()

def maze_choices():
    st.subheader("Choose your next adventure in the Melodic Maze:")
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button('The Hidden Cave'):
            st.session_state['maze_choice'] = 'hidden_cave'
    with col5:
        if st.button('The Guardian Spirit'):
            st.session_state['maze_choice'] = 'guardian_spirit'
    with col6:
        if st.button('The Echo Chamber'):
            st.session_state['maze_choice'] = 'echo_chamber'
    
    if 'maze_choice' in st.session_state:
        if st.session_state['maze_choice'] == 'hidden_cave':
            st.write("Victor and Lindsey follow the musical hints and successfully navigate through the maze to reach the center. There, they discover a hidden cave adorned with ancient symbols. Inside the cave, they find a riddle that, when solved, reveals a map leading to the Heart of Harmony's location.")
            st.image("1-2-1.webp", caption='The Hidden Cave')
            st.write("As Victor and Lindsey follow the musical hints, they notice a pattern emerging in the melodies around them, guiding them towards the center of the maze.")

            st.write("Select a note to play:")
            for note in note_keys:
                if st.button(note):
                    st.audio(f"{note}.wav")
        elif st.session_state['maze_choice'] == 'guardian_spirit':
            st.write("While navigating through the maze, Victor and Lindsey encounter a mystical guardian spirit that challenges them to a musical duel. They must perform a melody that resonates with the spirit's song to proceed further into the maze. If they succeed, the spirit reveals a secret passage that leads them closer to the Heart of Harmony.")
            st.image("1-2-2.webp", caption='The Guardian Spirit')
            st.write("With hearts pounding in rhythm, they raise their voices and instruments, blending their melodies with the spirit's song. Each note they play weaves seamlessly into the tapestry of sound, creating a harmonious symphony that reverberates through the maze.")
            
            st.write("Select a note to play:")
            for note in note_keys:
                if st.button(note):
                    st.audio(f"{note}.wav")
        elif st.session_state['maze_choice'] == 'echo_chamber':
            st.write("As Victor and Lindsey progress deeper into the maze, they become disoriented by the echoing sounds of the forest. They find themselves trapped in an echo chamber where every sound is distorted. To escape, they must rely on their intuition and teamwork to decipher the true musical hints amidst the cacophony. If they succeed, they break free from the chamber and find themselves closer to the Heart of Harmony's location.")
            st.image("1-2-3.webp", caption='The Echo Chamber')
            st.write("With renewed determination, they join hands and focus their minds, allowing their intuition to guide them towards the true source of harmony amidst the chaos. As they do, the echoes begin to fade, replaced by a serene melody that leads them towards the heart of the maze and closer to their ultimate goal: the Heart of Harmony.")
            
            st.write("Select a note to play:")
            for note in note_keys:
                if st.button(note):
                    st.audio(f"{note}.wav")
                        
def narrative_quantum():
    st.write("Choosing the path of scientific curiosity, our duo enters the Quantum Quagmire.")
    st.image("2-1-1.webp", caption='The Quantum Quagmire')
    st.write("This area of the forest is distorted by bizarre physics phenomena. To navigate through, they must solve scientific puzzles that manipulate time and space.")
    quantum_choices()

def quantum_choices():
    st.subheader("Choose your next adventure in the Quantum Quagmiree:")
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button('The Temporal Puzzle'):
            st.session_state['quantum_choice'] = 'temporal_puzzle'
    with col5:
        if st.button('The Spatial Enigma'):
            st.session_state['quantum_choice'] = 'spatial_enigma'
    with col6:
        if st.button('The Quantum Conundrum'):
            st.session_state['quantum_choice'] = 'quantum_conundrum'
    
    if 'quantum_choice' in st.session_state:
        if st.session_state['quantum_choice'] == 'temporal_puzzle':
            st.write("Victor and Lindsey encounter a series of temporal anomalies, including time loops and quantum entanglements. They must solve a series of puzzles involving causality and time manipulation to progress further.")
            st.image("2-2-1.webp", caption='The Temporal Puzzle')
            st.write("As they delve deeper into the temporal puzzle, they come across a branching pathway leading to two diverging timelines. They must choose wisely, as each path holds its own challenges and rewards.")
        elif st.session_state['quantum_choice'] == 'spatial_enigma':
            st.write("Victor and Lindsey encounter spatial distortions that defy conventional physics, including non-Euclidean geometry and multidimensional rifts. They must navigate through shifting landscapes and gravitational anomalies to reach their destination.")
            st.image("2-2-2.webp", caption='The Spatial Enigma')
            st.write("As they venture deeper into the spatial enigma, they come across a mysterious portal that offers glimpses into alternate dimensions. They must decide whether to explore further or continue on their current path.")
        elif st.session_state['quantum_choice'] == 'quantum_conundrum':
            st.write("They discover a hidden library filled with ancient texts on quantum mechanics and metaphysics. They must study the arcane knowledge within to uncover the secrets of the Quantum Quagmire and unlock its mysteries.")
            st.image("2-2-3.webp", caption='The Quantum Conundrum')
            st.write("Inside the library, Victor and Lindsey find a cryptic message written in an ancient language. They must decipher the code to reveal the next clue on their journey.")
    
def narrative_harmony():
    st.write("Opting for a test of courage and endurance, Victor and Lindsey climb the Harmony Heights.")
    st.image("3-1-1.webp", caption='The Harmony Heights')
    st.write("As they ascend, they must harmonize with the song of the winds, adjusting their actions to the melody to safely reach the summit where an ancient instrument of power is said to be hidden.")
    harmony_choices()

def harmony_choices():
    st.subheader("Choose your next adventure in the Quantum Quagmiree:")
    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button('The Harmonic Ascent'):
            st.session_state['harmony_choice'] = 'harmonic_ascent'
    with col5:
        if st.button('The Melodic Menace'):
            st.session_state['harmony_choice'] = 'melodic_menace'
    with col6:
        if st.button('The Rhythmic Resonance'):
            st.session_state['harmony_choice'] = 'quantum_conundrum'
    
    if 'harmony_choice' in st.session_state:
        if st.session_state['harmony_choice'] == 'harmonic_ascent':
            st.write("Along the journey, they encounter a group of mystical creatures known as the Wind Sirens, who test their musical prowess with a series of harmonic trials. They must impress the Sirens with their musical abilities to gain passage to the summit.")
            st.image("3-2-1.webp", caption='The Hidden Cave')
            st.write("As they delve deeper into the temporal puzzle, they come across a branching pathway leading to two diverging timelines. They must choose wisely, as each path holds its own challenges and rewards.")
            echo_chamber_puzzle()
        elif st.session_state['harmony_choice'] == 'melodic_menace':
            st.write("Victor and Lindsey encounter a malevolent entity known as the Discordant Spirit, whose dissonant melodies disrupt the harmony of the mountain. They must confront the spirit and restore balance to the natural order.")
            st.image("3-2-2.webp", caption='The Guardian Spirit')
            st.write("As they venture deeper into the spatial enigma, they come across a mysterious portal that offers glimpses into alternate dimensions. They must decide whether to explore further or continue on their current path.")
            echo_chamber_puzzle()
        elif st.session_state['harmony_choice'] == 'quantum_conundrum':
            st.write("Victor and Lindsey encounter a wise old sage known as the Melody Master, who imparts ancient wisdom about the power of harmony. They must prove their understanding of rhythm and melody to gain his guidance on their journey.")
            st.image("3-2-2.webp", caption='The Echo Chamber')
            st.write("Inside the library, Victor and Lindsey find a cryptic message written in an ancient language. They must decipher the code to reveal the next clue on their journey.")
            echo_chamber_puzzle()

def echo_chamber_puzzle():
    st.write("Arrange the symbols in the correct order to solve the puzzle:")

    # Define the symbols for the puzzle
    symbols = ["/\\_/\  ", "( o.o )", " > ^ < ", " - - -", "//    \\\\"]  # Escaped backslashes
    
    # Create columns for each symbol
    col1, col2, col3, col4, col5 = st.columns(5)

    # Create dropdowns for each symbol
    with col1:
        symbol_order_1 = st.selectbox("Symbol 1", options=symbols, index=3)

    with col2:
        symbol_order_2 = st.selectbox("Symbol 2", options=symbols, index=1)

    with col3:
        symbol_order_3 = st.selectbox("Symbol 3", options=symbols, index=4)

    with col4:
        symbol_order_4 = st.selectbox("Symbol 4", options=symbols, index=0)

    with col5:
        symbol_order_5 = st.selectbox("Symbol 5", options=symbols, index=2)
        
    # Display the selected symbols using st.text for better formatting
    drawn_picture = f"   {symbol_order_1}\n{symbol_order_2}\n{symbol_order_3}\n{symbol_order_4}\n{symbol_order_5}"
    st.code(drawn_picture, language='text')  # Using st.code to maintain formatting
   
    
    # Check if the user has arranged the symbols correctly
    if [symbol_order_1, symbol_order_2, symbol_order_3, symbol_order_4, symbol_order_5] == symbols:
        st.success("Congratulations! You've solved the puzzle and harmonized with the natural rhythms of the mountain.")
        # Create columns to display the image three times
        col1, col2, col3,col4 = st.columns(4)
        with col1:
            st.code(drawn_picture, language='text')
        with col2:
            st.code(drawn_picture, language='text')
        with col3:
            st.code(drawn_picture, language='text')
        with col4:
            st.code(drawn_picture, language='text')
        
        # Add descriptive text leading to the Heart of Harmony
        st.subheader("The Path to the Heart of Harmony")
        st.write("With the symbols aligned, a melodious hum fills the air, leading Lindsey and Victor deeper into the mountain's core. "
                 "Step by step, the path unfolds, guided by the pulse of harmony. They make their way to fabled Heart of Harmony. What secret will it reveal?")
        # Button to show a GIF
        if st.button('Discover the Heart of Harmony'):
            # Assuming you have a local path to a GIF file
            gif_path = 'prize1.gif'
            st.image(gif_path, caption='The Heart of Harmony')
            audio_file = open('bless_the_telephone.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes)
    else:
        st.info("Keep arranging the symbols to create the correct melody.")
        
if __name__ == '__main__':
    
    # Display the main image
    image_path = "1.webp"  # Replace with the path to your image
    st.image(image_path)

    # Introduction to the story
    st.title("Adventure Begins!")
    st.write("""
    Welcome to the Kingdom of Melody, a realm where every leaf and stone hums with the vibrance of music and the precision of science. Here, at the entrance of the mystical Emerald Forest, lies the beginning of an enchanting adventure.

    Deep within the verdant expanse of the Emerald Forest, an ancient treasure known as the "Heart of Harmony" is said to reside. Legend tells that this treasure was crafted from the very essence of the first song sung by the forest, harmonized with the rhythm of the natural world. The Heart of Harmony is not merely a gem; it is a powerful artifact that embodies the equilibrium and wisdom of Melody itself.

    Guarded by the enigmatic spirits of the forest, the Heart of Harmony bestows insight and tranquility upon those who are deemed worthy. However, to reach it, one must prove their worth through trials that test their musical acuity, scientific knowledge, and innate bravery. These challenges ensure that only the most balanced of hearts can claim the treasure.

    As Victor the edgy llama and Lindsey the spirited mooncake step into the forest, they are drawn by tales of the legendary treasure and the promise of an adventure that could change the very fabric of their lives. Their journey through Emerald Forest will test the strength of their friendship, challenge their minds, and encourage them to tune into the deep melodies of the forest around them.

    This is where our story begins—with Victor and Lindsey at the threshold of the forest, ready to uncover the mysteries that await in the Kingdom of Melody.
    """)
    
    if 'choice' not in st.session_state:
        st.session_state['choice'] = None
    if 'maze_choice' not in st.session_state:
        st.session_state['maze_choice'] = None
    if 'quantum_choice' not in st.session_state:
        st.session_state['quantum_choice'] = None
    if 'harmony_choice' not in st.session_state:
        st.session_state['harmony_choice'] = None
    main_menu()

