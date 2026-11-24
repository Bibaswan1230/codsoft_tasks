
movies = {
    "Action": ["John Wick", "Avengers", "The Dark Knight",
               "Mad Max: Fury Road"],
    "Comedy": ["3 Idiots", "Hera Pheri", "The Hangover",
               "Jumanji"],
    "Romance": ["The Notebook", "Titanic", "La La Land",
                "Jab We Met"],
    "Horror": ["The Conjuring", "IT", "A Quiet Place",
               "The Nun"],
    "Sci-Fi": ["Interstellar", "Inception", "The Matrix",
               "Dune"],
    "Thriller": ["Shutter Island", "Se7en", "Gone Girl",
                 "Drishyam"]
}

print("=" * 40)
print("     MOVIE RECOMMENDATION SYSTEM")
print("=" * 40)

print("\nAvailable genres:")
for genre in movies:
    print("-", genre)

while True:
    choice = input("\nEnter your favourite genre (or 'exit'): ").strip()

    if choice.lower() == "exit":
        print("Thank you for using our system!")
        break

    matched_genre = None

    for genre in movies:
        if choice.lower() == genre.lower():
            matched_genre = genre
            break

    if matched_genre:
        print("\nRecommended movies for you:")
        for movie in movies[matched_genre]:
            print("-", movie)
    else:
        print("Sorry, genre not available. Please try again.")
