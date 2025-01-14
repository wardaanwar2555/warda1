import pyttsx3
import os
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage, filedialog

# Function to play the audio
def play_audio(voice, text, rate, volume):
    # Initialize pyttsx3 engine
    engine = pyttsx3.init()

    # Set speech rate and volume
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)

    # Get available voices
    voices = engine.getProperty('voices')

    # Set voice based on gender choice
    if voice == "B" and len(voices) > 1:
        engine.setProperty('voice', voices[1].id)  # Female voice
    else:
        engine.setProperty('voice', voices[0].id)  # Male voice

    # Speak the provided text
    engine.say(text)
    engine.runAndWait()

# Function to save the audio as a file
def save_audio(voice, text, rate, volume):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    
    voices = engine.getProperty('voices')
    if voice == "B" and len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)

    # Ask user where to save the audio file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".mp3",
        filetypes=[("MP3 Files", "*.mp3"), ("WAV Files", "*.wav")]
    )
    if file_path:
        engine.save_to_file(text, file_path)
        engine.runAndWait()
        messagebox.showinfo("Success", f"Audio saved successfully at {file_path}!")

# GUI for the TTS application
def create_tts_app():
    window = tk.Tk()
    window.title("Text-to-Speech")
    window.geometry("800x600")
    window.configure(bg="navy")

    # Frame for the content
    frame = tk.Frame(window, bg="lightblue", padx=30, pady=30, relief="groove", borderwidth=5)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    # Placeholder graphic
    try:
        image = PhotoImage(file="a.jpeg")  # Replace with your image file
        graphic = tk.Label(frame, image=image, bg="lightblue")
        graphic.image = image
        graphic.pack(pady=10)
    except:
        graphic = tk.Label(frame, text="[Graphic Here]", font=("Arial", 16), bg="lightblue")
        graphic.pack(pady=10)

    # Text input
    tk.Label(frame, text="Enter text:", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)
    text_input = tk.Text(frame, font=("Arial", 14), height=5, width=40)
    text_input.pack(pady=10)

    # Voice selection
    tk.Label(frame, text="Choose voice:", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)
    voice_choice = ttk.Combobox(frame, values=["A ", "B "], font=("Arial", 14))
    voice_choice.set("A")
    voice_choice.pack(pady=10)

    # Speech rate control
    tk.Label(frame, text="Speech Speed:", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)
    rate_slider = ttk.Scale(frame, from_=50, to=300, value=150, orient="horizontal", length=300)
    rate_slider.pack(pady=10)

    # Volume control
    tk.Label(frame, text="Volume:", font=("Arial", 18, "bold"), bg="lightblue").pack(pady=10)
    volume_slider = ttk.Scale(frame, from_=0.0, to=1.0, value=1.0, orient="horizontal", length=300)
    volume_slider.pack(pady=10)

    # Playback functionality
    def play():
        text = text_input.get("1.0", tk.END).strip()
        voice = "B" if "B" in voice_choice.get() else "A"
        rate = int(rate_slider.get())
        volume = float(volume_slider.get())
        if text:
            play_audio(voice, text, rate, volume)
        else:
            messagebox.showwarning("Input Required", "Please enter text to convert to speech.")

    def save():
        text = text_input.get("1.0", tk.END).strip()
        voice = "B" if "B" in voice_choice.get() else "A"
        rate = int(rate_slider.get())
        volume = float(volume_slider.get())
        if text:
            save_audio(voice, text, rate, volume)
        else:
            messagebox.showwarning("Input Required", "Please enter text to convert to speech.")

    # Buttons for play and save
    tk.Button(frame, text="Play Audio", command=play, font=("Arial", 16, "bold"), bg="darkblue", fg="white", width=15, height=2).pack(pady=10)
    tk.Button(frame, text="Save Audio", command=save, font=("Arial", 16, "bold"), bg="green", fg="white", width=15, height=2).pack(pady=10)

    window.mainloop()

# Run the application
create_tts_app()
