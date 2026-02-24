from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import requests
import html

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    # utf-8-sig handles Japanese characters and removes "Ã" issues
    df = pd.read_csv("anime_updated.csv", encoding='utf-8-sig')
    df['name'] = df['name'].apply(lambda x: html.unescape(str(x)).strip())
    if 'english_name' not in df.columns:
        df['english_name'] = df['name']
    df['english_name'] = df['english_name'].fillna(df['name']).apply(lambda x: html.unescape(str(x)).strip())
    df['genre'] = df['genre'].fillna('Unknown')
    df = df[~df['genre'].str.contains('Hentai', case=False, na=False)]
    print("✓ Backend Master: Levels 1-3 Stable")
except Exception as e:
    print(f"Error: {e}")

@app.get("/search")
def search(genres: str = "", min_rating: float = 0.0, page: int = 1):
    results = df[df['rating'] >= min_rating]
    if genres:
        selected_tags = [g.strip() for g in genres.split(",") if g.strip()]
        for tag in selected_tags:
            results = results[results['genre'].str.contains(tag, case=False, na=False)]
    
    # Existing pagination feature preserved [cite: 4, 58-59]
    limit = 50
    start = (page - 1) * limit
    return results.sort_values(by='rating', ascending=False).iloc[start:start+limit].to_dict(orient="records")

@app.get("/live-details/{anime_id}")
def get_live_details(anime_id: int):
    try:
        # Jikan v4 live fetch preserved [cite: 5-6]
        response = requests.get(f"https://api.jikan.moe/v4/anime/{anime_id}", timeout=5)
        if response.status_code == 200:
            data = response.json()['data']
            return {
                "real_image": data['images']['jpg']['large_image_url'],
                "real_about": data.get('synopsis', "No official synopsis found.")
            }
        return {"error": "API Error"}
    except:
        return {"error": "Timeout"}