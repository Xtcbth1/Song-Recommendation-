# Song Recommendation System
**Author:** DIBAKAR ROY

## Project Overview
A content-based music recommendation system using TF-IDF and cosine similarity to suggest similar songs based on song metadata.

## Features
- Content-based filtering using TF-IDF vectorization
- Cosine similarity for finding similar songs
- RESTful API built with FastAPI
- Easy to deploy and test

## Installation

### Step 1: Clone the repository
```bash
git clone <your-repo-url>
cd song-recommendation-system
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Create sample dataset
```bash
python create_sample_data.py
```

### Step 4: Run the API
```bash
python main.py
```

The API will be available at: http://localhost:8000

## API Endpoints

### 1. Root Endpoint
```
GET /
```
Returns API information and available endpoints.

### 2. Get All Songs
```
GET /songs
```
Returns list of all available songs in the database.

### 3. Get Recommendations
```
GET /recommend/{song_title}?limit=10
```
Returns song recommendations based on similarity.

**Parameters:**
- `song_title`: Name of the song (case-insensitive)
- `limit`: Number of recommendations (default: 10)

## Example Usage

### Using cURL
```bash
# Get all songs
curl http://localhost:8000/songs

# Get recommendations for "Shape of You"
curl http://localhost:8000/recommend/Shape%20of%20You?limit=5
```

### Using Python
```python
import requests

# Get recommendations
response = requests.get("http://localhost:8000/recommend/Shape of You?limit=5")
print(response.json())
```

## How It Works

1. **Data Preprocessing**: Song features (title, artist, genre, album) are combined into a single text field
2. **TF-IDF Vectorization**: Text data is converted into numerical feature vectors
3. **Cosine Similarity**: Similarity scores are calculated between all songs
4. **Recommendation**: Most similar songs are returned based on cosine similarity scores

## Project Structure
```
song-recommendation-system/
│
├── main.py                  # FastAPI application
├── create_sample_data.py    # Script to generate sample dataset
├── music_data.csv           # Music dataset
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## Deployment Options

### Option 1: Render
1. Create a Render account
2. Connect your GitHub repository
3. Deploy as a Web Service

### Option 2: Railway
1. Create a Railway account
2. Connect your GitHub repository
3. Deploy with one click

### Option 3: Heroku
1. Create a Heroku account
2. Install Heroku CLI
3. Deploy using:
```bash
heroku create
git push heroku main
```

## Technologies Used
- **FastAPI**: Modern web framework for building APIs
- **scikit-learn**: TF-IDF vectorization and cosine similarity
- **pandas**: Data manipulation and analysis
- **uvicorn**: ASGI server

## Author
**DIBAKAR ROY**

## License
MIT License
