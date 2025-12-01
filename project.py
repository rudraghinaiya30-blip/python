# Simple Music Recommender using CSV File
# This code reads song data from a CSV file and recommends based on genre.
# Run this in VSCode by opening the file and using the terminal to execute: python filename.py

import csv  # Built-in module for reading CSV files

# Function to load songs from CSV
def load_songs_from_csv(filename):  # Fixed: Parameter is now a valid variable name
    songs = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:  # Fixed: Uses the 'filename' variable
            reader = csv.DictReader(file)
            for row in reader:
                songs.append({
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"]
                })
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please create it with the sample data below.")  # Fixed: Uses the 'filename' variable
        return []
    return songs

# Function to recommend songs based on genre
def recommend_songs(songs, favorite_genre, num_recommendations=3):
    # Filter songs by the favorite genre
    matching_songs = [song for song in songs if song["genre"].lower() == favorite_genre.lower()]
    
    # If no matches, suggest trying another genre
    if not matching_songs:
        return f"No songs found for genre '{favorite_genre}'. Try 'Rock', 'Pop', or 'Funk'."
    
    # Recommend the first 'num_recommendations' songs
    recommendations = matching_songs[:num_recommendations]
    result = f"Recommended songs for genre '{favorite_genre}':\n"
    for song in recommendations:
        result += f"- {song['title']} by {song['artist']}\n"
    return result

# Main program
if __name__ == "__main__":
    csv_filename = "music.csv"  # Name of your CSV file
    songs = load_songs_from_csv(csv_filename)
    
    if not songs:
        print("No songs loaded. Exiting.")
    else:
        print("Welcome to the Simple Music Recommender!")
        favorite_genre = input("Enter your favorite genre (e.g., Rock, Pop, Funk): ")
        print(recommend_songs(songs, favorite_genre))
