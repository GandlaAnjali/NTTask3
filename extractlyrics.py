import tkinter as tk
from tkinter import messagebox
import lyricsgenius

# Replace 'your_access_token' with your actual Genius API access token
genius = lyricsgenius.Genius("your_access_token")

def fetch_lyrics():
    artist_name = artist_entry.get()
    song_title = song_entry.get()
    if not artist_name or not song_title:
        messagebox.showwarning("Input Error", "Please enter both artist name and song title.")
        return
    
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, song.lyrics)
        else:
            messagebox.showwarning("Not Found", "Lyrics not found for the given song.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Set up the main application window
root = tk.Tk()
root.title("Lyrics Extractor")

# Artist input
tk.Label(root, text="Artist Name").grid(row=0, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root, width=50)
artist_entry.grid(row=0, column=1, padx=10, pady=10)

# Song input
tk.Label(root, text="Song Title").grid(row=1, column=0, padx=10, pady=10)
song_entry = tk.Entry(root, width=50)
song_entry.grid(row=1, column=1, padx=10, pady=10)

# Fetch lyrics button
fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, column=0, columnspan=2, pady=20)

# Text box to display lyrics
lyrics_text = tk.Text(root, wrap='word', width=60, height=20)
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
