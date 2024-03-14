class Song:
    count = 0  # Class attribute to keep track of the number of songs
    genres = []  # Class attribute to keep track of all the genres
    artists = []  # Class attribute to keep track of all the artists
    genre_count = {}  # Class attribute to keep track of the count of each genre
    artist_count = {}  # Class attribute to keep track of the count of each artist

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()  # Call the class method whenever a new song is created
        self.add_to_genres(genre)  # Add the genre of the song to the genres list
        self.add_to_artists(artist)  # Add the artist of the song to the artists list
        self.add_to_genre_count(genre)  # Increment the count for the genre of the song
        self.add_to_artist_count(artist)  # Increment the count for the artist of the song

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1  # Increment the count by one

    @classmethod
    def get_song_count(cls):
        return cls.count  # Return the current count

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:  # Check if the genre is already in the list
            cls.genres.append(genre)  # If not, add it to the list

    @classmethod
    def get_genres(cls):
        return cls.genres  # Return the list of all genres

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def get_artists(cls):
        return cls.artists

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1  # If the genre is already in the dictionary, increment its count
        else:
            cls.genre_count[genre] = 1  # If the genre is not in the dictionary, add it with a count of 1

    @classmethod
    def get_genre_count(cls):
        return cls.genre_count  # Return the dictionary of genre counts

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1  # If the artist is already in the dictionary, increment its count
        else:
            cls.artist_count[artist] = 1  # If the artist is not in the dictionary, add it with a count of 1

    @classmethod
    def get_artist_count(cls):
        return cls.artist_count  # Return the dictionary of artist counts
