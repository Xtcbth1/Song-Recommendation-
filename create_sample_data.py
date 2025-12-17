import pandas as pd
import random

# Sample data for music recommendation
songs_data = {
    'title': [
        'Shape of You', 'Blinding Lights', 'Bohemian Rhapsody', 'Stairway to Heaven',
        'Hotel California', 'Smells Like Teen Spirit', 'Billie Jean', 'Hey Jude',
        'Imagine', 'Sweet Child O Mine', 'Wonderwall', 'Lose Yourself',
        'Thinking Out Loud', 'Someone Like You', 'Rolling in the Deep',
        'Uptown Funk', 'Despacito', 'Old Town Road', 'Bad Guy', 'Circles',
        'Dance Monkey', 'Senorita', 'Sunflower', 'Memories', 'Beautiful',
        'Perfect', 'Photograph', 'All of Me', 'Let Her Go', 'Counting Stars',
        'Radioactive', 'Demons', 'Thunder', 'Believer', 'Whatever It Takes',
        'Natural', 'Bad Liar', 'Zero', 'Born to Be Yours', 'Machine',
        'Rockabye', 'Closer', 'Something Just Like This', 'Paris', 'Roses',
        'Don't Let Me Down', 'Cold Water', 'Hymn for the Weekend', 'Adventure of a Lifetime',
        'Fix You', 'The Scientist', 'Yellow', 'Clocks', 'Paradise', 'Viva La Vida'
    ],
    'artist': [
        'Ed Sheeran', 'The Weeknd', 'Queen', 'Led Zeppelin',
        'Eagles', 'Nirvana', 'Michael Jackson', 'The Beatles',
        'John Lennon', 'Guns N Roses', 'Oasis', 'Eminem',
        'Ed Sheeran', 'Adele', 'Adele',
        'Mark Ronson', 'Luis Fonsi', 'Lil Nas X', 'Billie Eilish', 'Post Malone',
        'Tones and I', 'Shawn Mendes', 'Post Malone', 'Maroon 5', 'Christina Aguilera',
        'Ed Sheeran', 'Ed Sheeran', 'John Legend', 'Passenger', 'OneRepublic',
        'Imagine Dragons', 'Imagine Dragons', 'Imagine Dragons', 'Imagine Dragons', 'Imagine Dragons',
        'Imagine Dragons', 'Imagine Dragons', 'Imagine Dragons', 'Imagine Dragons', 'Imagine Dragons',
        'Clean Bandit', 'The Chainsmokers', 'The Chainsmokers', 'The Chainsmokers', 'The Chainsmokers',
        'The Chainsmokers', 'Major Lazer', 'Coldplay', 'Coldplay',
        'Coldplay', 'Coldplay', 'Coldplay', 'Coldplay', 'Coldplay', 'Coldplay'
    ],
    'genre': [
        'Pop', 'Pop', 'Rock', 'Rock',
        'Rock', 'Rock', 'Pop', 'Rock',
        'Rock', 'Rock', 'Rock', 'Hip Hop',
        'Pop', 'Pop', 'Pop',
        'Pop', 'Latin Pop', 'Country Rap', 'Pop', 'Hip Hop',
        'Pop', 'Pop', 'Hip Hop', 'Pop', 'Pop',
        'Pop', 'Pop', 'Pop', 'Pop', 'Pop',
        'Alternative Rock', 'Alternative Rock', 'Alternative Rock', 'Alternative Rock', 'Alternative Rock',
        'Alternative Rock', 'Alternative Rock', 'Alternative Rock', 'Alternative Rock', 'Alternative Rock',
        'Pop', 'EDM', 'EDM', 'EDM', 'EDM',
        'EDM', 'EDM', 'Alternative Rock', 'Alternative Rock',
        'Alternative Rock', 'Alternative Rock', 'Alternative Rock', 'Alternative Rock', 'Alternative Rock', 'Alternative Rock'
    ],
    'album': [
        'Divide', 'After Hours', 'A Night at the Opera', 'Led Zeppelin IV',
        'Hotel California', 'Nevermind', 'Thriller', 'Hey Jude',
        'Imagine', 'Appetite for Destruction', 'Morning Glory', 'The Eminem Show',
        'X', '21', '21',
        'Uptown Special', 'Vida', '7 EP', 'When We All Fall Asleep', 'Hollywood's Bleeding',
        'The Kids Are Coming', 'Shawn Mendes', 'Hollywood's Bleeding', 'Memories', 'Stripped',
        'Divide', 'X', 'Love in the Future', 'All the Little Lights', 'Native',
        'Night Visions', 'Night Visions', 'Evolve', 'Evolve', 'Origins',
        'Origins', 'Origins', 'Origins', 'Origins', 'Origins',
        'Glory Days', 'Collage', 'Memories', 'Memories', 'Collage',
        'Collage', 'Major Lazer', 'A Head Full of Dreams', 'A Head Full of Dreams',
        'X&Y', 'A Rush of Blood to the Head', 'Parachutes', 'A Rush of Blood to the Head', 'Mylo Xyloto', 'Viva la Vida'
    ]
}

# Create DataFrame
df = pd.DataFrame(songs_data)

# Add year and duration
df['year'] = [random.randint(1970, 2023) for _ in range(len(df))]
df['duration_ms'] = [random.randint(180000, 360000) for _ in range(len(df))]

# Save to CSV
df.to_csv('music_data.csv', index=False)
print("Sample music dataset created successfully!")
print(f"Total songs: {len(df)}")
