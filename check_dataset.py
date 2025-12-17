import pandas as pd

def analyze_dataset(file_path):
    """
    Analyze your dataset and show what columns are available
    """
    print("=" * 60)
    print("DATASET ANALYSIS")
    print("=" * 60)
    
    try:
        # Read the dataset
        df = pd.read_csv(file_path)
        
        print(f"\n✅ Successfully loaded: {file_path}")
        print(f"\n📊 Total rows: {len(df)}")
        print(f"📊 Total columns: {len(df.columns)}")
        
        print("\n📋 Column Names:")
        print("-" * 60)
        for i, col in enumerate(df.columns, 1):
            print(f"{i}. {col}")
        
        print("\n🔍 First 5 Rows:")
        print("-" * 60)
        print(df.head())
        
        print("\n📈 Data Types:")
        print("-" * 60)
        print(df.dtypes)
        
        print("\n❓ Missing Values:")
        print("-" * 60)
        print(df.isnull().sum())
        
        print("\n✏️ RECOMMENDED COLUMN MAPPING:")
        print("-" * 60)
        print("Based on your dataset, update main.py with these column names:")
        print()
        
        # Try to detect column names
        cols = [col.lower() for col in df.columns]
        
        suggested_mapping = {}
        
        # Detect title/song name column
        title_keywords = ['title', 'song', 'name', 'track']
        for keyword in title_keywords:
            matches = [col for col in df.columns if keyword in col.lower()]
            if matches:
                suggested_mapping['title'] = matches[0]
                break
        
        # Detect artist column
        artist_keywords = ['artist', 'singer', 'performer']
        for keyword in artist_keywords:
            matches = [col for col in df.columns if keyword in col.lower()]
            if matches:
                suggested_mapping['artist'] = matches[0]
                break
        
        # Detect genre column
        genre_keywords = ['genre', 'category', 'type']
        for keyword in genre_keywords:
            matches = [col for col in df.columns if keyword in col.lower()]
            if matches:
                suggested_mapping['genre'] = matches[0]
                break
        
        # Detect album column
        album_keywords = ['album', 'collection']
        for keyword in album_keywords:
            matches = [col for col in df.columns if keyword in col.lower()]
            if matches:
                suggested_mapping['album'] = matches[0]
                break
        
        if suggested_mapping:
            print("Suggested mapping:")
            for key, value in suggested_mapping.items():
                print(f"  {key} -> '{value}'")
        else:
            print("  Could not auto-detect columns.")
            print(f"  Available columns: {', '.join(df.columns)}")
        
        print("\n" + "=" * 60)
        print("✅ Analysis Complete!")
        print("=" * 60)
        
        return df, suggested_mapping
        
    except FileNotFoundError:
        print(f"\n❌ Error: File '{file_path}' not found!")
        print("\nMake sure your dataset file is in the same folder as this script.")
        return None, None
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return None, None

if __name__ == "__main__":
    print("\n🎵 SONG DATASET CHECKER")
    print("This script will analyze your dataset and help you configure the project.\n")
    
    # Ask for file name
    file_name = input("Enter your dataset file name (e.g., songs.csv): ").strip()
    
    if not file_name:
        file_name = "music_data.csv"  # Default
        print(f"Using default: {file_name}")
    
    df, mapping = analyze_dataset(file_name)
    
    if df is not None:
        print("\n💡 NEXT STEPS:")
        print("1. Note the column names shown above")
        print("2. Update the 'combined_features' line in main.py")
        print("3. Use the exact column names from your dataset")
        print("\nExample:")
        print("df['combined_features'] = (")
        print("    df['YourTitleColumn'].astype(str) + ' ' +")
        print("    df['YourArtistColumn'].astype(str) + ' ' +")
        print("    df['YourGenreColumn'].astype(str)")
        print(")")
