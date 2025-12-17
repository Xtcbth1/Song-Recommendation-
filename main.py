from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import uvicorn
import os

app = FastAPI(title="Song Recommendation API", version="1.0.0")

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables
df = None
tfidf_matrix = None
cosine_sim = None
DATASET_FILE = 'music_data.csv'  # Change this to your dataset file name

def load_and_preprocess_data():
    """Load and preprocess the music dataset"""
    global df, tfidf_matrix, cosine_sim
    
    # Load dataset
    print(f"Loading dataset: {DATASET_FILE}")
    df = pd.read_csv(DATASET_FILE)
    
    print(f"Dataset loaded! Rows: {len(df)}, Columns: {len(df.columns)}")
    print(f"Column names: {list(df.columns)}")
    
    # Data cleaning
    df = df.dropna()
    df = df.drop_duplicates()
    
    # ⚠️ IMPORTANT: UPDATE THESE COLUMN NAMES TO MATCH YOUR DATASET
    # Run check_dataset.py first to see your column names!
    
    # Option 1: If your dataset has these exact columns
    if all(col in df.columns for col in ['title', 'artist', 'genre']):
        df['combined_features'] = (
            df['title'].astype(str) + ' ' +
            df['artist'].astype(str) + ' ' +
            df['genre'].astype(str)
        )
        if 'album' in df.columns:
            df['combined_features'] += ' ' + df['album'].astype(str)
    
    # Option 2: Auto-detect columns (tries to find similar column names)
    else:
        print("⚠️ Standard columns not found. Attempting auto-detection...")
        cols_to_use = []
        
        # Try to find title/song column
        for col in df.columns:
            if any(keyword in col.lower() for keyword in ['title', 'song', 'name', 'track']):
                cols_to_use.append(col)
                break
        
        # Try to find artist column
        for col in df.columns:
            if any(keyword in col.lower() for keyword in ['artist', 'singer', 'performer']):
                cols_to_use.append(col)
                break
        
        # Try to find genre column
        for col in df.columns:
            if any(keyword in col.lower() for keyword in ['genre', 'category', 'type', 'style']):
                cols_to_use.append(col)
                break
        
        if cols_to_use:
            print(f"✅ Using columns: {cols_to_use}")
            df['combined_features'] = df[cols_to_use[0]].astype(str)
            for col in cols_to_use[1:]:
                df['combined_features'] += ' ' + df[col].astype(str)
        else:
            # Fallback: use all text columns
            print("⚠️ Using all available text columns")
            text_cols = df.select_dtypes(include=['object']).columns.tolist()
            if text_cols:
                df['combined_features'] = df[text_cols[0]].astype(str)
                for col in text_cols[1:]:
                    df['combined_features'] += ' ' + df[col].astype(str)
            else:
                raise ValueError("No suitable columns found in dataset!")
    
    print(f"✅ Combined features created")
    print(f"Sample: {df['combined_features'].iloc[0][:100]}...")
    
    # Apply TF-IDF Vectorization
    tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
    tfidf_matrix = tfidf.fit_transform(df['combined_features'])
    
    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    print(f"✅ Data loaded and preprocessed successfully!")
    print(f"✅ TF-IDF matrix shape: {tfidf_matrix.shape}")

@app.on_event("startup")
async def startup_event():
    """Initialize data on startup"""
    load_and_preprocess_data()

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "message": "Song Recommendation API",
        "author": "DIBAKAR ROY",
        "dataset_file": DATASET_FILE,
        "total_songs": len(df) if df is not None else 0,
        "columns": list(df.columns) if df is not None else [],
        "endpoints": {
            "/songs": "Get all available songs",
            "/recommend/{song_title}": "Get recommendations for a song"
        }
    }

@app.get("/songs")
async def get_all_songs():
    """Get list of all available songs"""
    # Find the title column
    title_col = None
    for col in df.columns:
        if any(keyword in col.lower() for keyword in ['title', 'song', 'name', 'track']):
            title_col = col
            break
    
    if not title_col:
        title_col = df.columns[0]
    
    # Get columns to display
    display_cols = [title_col]
    for col in df.columns:
        if any(keyword in col.lower() for keyword in ['artist', 'singer']):
            display_cols.append(col)
            break
    for col in df.columns:
        if any(keyword in col.lower() for keyword in ['genre', 'category']):
            display_cols.append(col)
            break
    
    songs = df[display_cols].to_dict('records')
    return {
        "total_songs": len(songs), 
        "columns": display_cols,
        "songs": songs[:100]  # Limit to first 100 for performance
    }

@app.get("/recommend/{song_title}")
async def recommend_songs(song_title: str, limit: int = 10):
    """
    Get song recommendations based on similarity
    
    Args:
        song_title: Name of the song
        limit: Number of recommendations to return
    """
    try:
        # Find title column
        title_col = None
        for col in df.columns:
            if any(keyword in col.lower() for keyword in ['title', 'song', 'name', 'track']):
                title_col = col
                break
        
        if not title_col:
            title_col = df.columns[0]
        
        # Find the song in dataset
        idx = df[df[title_col].str.lower() == song_title.lower()].index
        
        if len(idx) == 0:
            raise HTTPException(
                status_code=404, 
                detail=f"Song '{song_title}' not found. Try getting the exact name from /songs endpoint"
            )
        
        idx = idx[0]
        
        # Get similarity scores
        sim_scores = list(enumerate(cosine_sim[idx]))
        
        # Sort by similarity (excluding the song itself)
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:limit+1]
        
        # Get song indices
        song_indices = [i[0] for i in sim_scores]
        
        # Get display columns
        display_cols = [title_col]
        for col in df.columns:
            if col != title_col and any(keyword in col.lower() for keyword in ['artist', 'genre', 'album']):
                display_cols.append(col)
                if len(display_cols) >= 4:
                    break
        
        # Get recommendations
        recommendations = df.iloc[song_indices][display_cols].to_dict('records')
        
        # Add similarity scores
        for i, rec in enumerate(recommendations):
            rec['similarity_score'] = round(sim_scores[i][1], 4)
        
        return {
            "query_song": song_title,
            "recommendations": recommendations
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
