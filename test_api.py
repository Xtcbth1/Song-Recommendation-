import requests
import json

BASE_URL = "http://localhost:8000"

def test_root():
    """Test root endpoint"""
    print("\n=== Testing Root Endpoint ===")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")

def test_get_songs():
    """Test get all songs endpoint"""
    print("\n=== Testing Get All Songs ===")
    response = requests.get(f"{BASE_URL}/songs")
    print(f"Status Code: {response.status_code}")
    data = response.json()
    print(f"Total Songs: {data['total_songs']}")
    print(f"First 3 Songs: {json.dumps(data['songs'][:3], indent=2)}")

def test_recommendations(song_title, limit=5):
    """Test recommendation endpoint"""
    print(f"\n=== Testing Recommendations for '{song_title}' ===")
    response = requests.get(f"{BASE_URL}/recommend/{song_title}?limit={limit}")
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print(f"Query Song: {data['query_song']}")
        print(f"\nTop {limit} Recommendations:")
        for i, rec in enumerate(data['recommendations'], 1):
            print(f"{i}. {rec['title']} by {rec['artist']} - {rec['genre']}")
            print(f"   Similarity Score: {rec['similarity_score']}")
    else:
        print(f"Error: {response.json()}")

if __name__ == "__main__":
    print("Starting API Tests...")
    print("=" * 50)
    
    # Test all endpoints
    test_root()
    test_get_songs()
    test_recommendations("Shape of You", 5)
    test_recommendations("Blinding Lights", 5)
    test_recommendations("Bohemian Rhapsody", 5)
    
    print("\n" + "=" * 50)
    print("All tests completed!")
