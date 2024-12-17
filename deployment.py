import streamlit as st
import openai

# Set OpenAI API key
openai.api_key = st.secrets["mykey"]

# Define possible options
target_audience = ["Casual gamers", "Competitive players", "Story-driven fans", "Strategists", "Puzzle solvers"]
game_genres = ["Adventure", "Action", "RPG", "Simulation", "Strategy", "Puzzle", "Sports", "Horror"]
play_style = ["Single-player", "Multiplayer", "Co-op", "Competitive"]
pain_points = ["Limited time", "High learning curve", "Lack of guidance", "Repetitive content"]
desires = ["Engaging storyline", "Relaxing gameplay", "Challenging puzzles", "Fast-paced action", "Immersive graphics"]
platforms = ["PC", "Console", "Mobile", "VR"]
time_commitment = ["Short sessions", "Long sessions"]

# Streamlit UI
st.title("Movie Recommender System")

# User input for customization
selected_audience = st.selectbox("Target Audience:", target_audience)
selected_genres = st.multiselect("Game Genres:", game_genres)
selected_play_style = st.selectbox("Play Style:", play_style)
selected_pain_points = st.multiselect("Pain Points:", pain_points)
selected_desires = st.multiselect("Desires:", desires)
selected_platforms = st.multiselect("Preferred Platforms:", platforms)
selected_time_commitment = st.selectbox("Preferred Session Length:", time_commitment)

# Game recommendation logic
def recommend_games(selected_audience, selected_genres, selected_play_style, selected_pain_points, selected_desires, selected_platforms, selected_time_commitment):
    # Mock game recommendations
    recommended_games = [
        {"name": "Stardew Valley", "description": "A relaxing farming simulation game with RPG elements.", "prompt": "A cozy farming game with beautiful landscapes, vibrant farms, and peaceful rural life"},
        {"name": "God of War", "description": "An action-packed game with Norse mythology.", "prompt": "A fierce warrior in a Norse mythology setting, epic battles, and snowy mountains"},
        {"name": "The Witcher 3", "description": "An open-world RPG with rich storytelling and complex characters.", "prompt": "A fantasy world with a medieval setting, powerful magic, and mythical creatures"},
        {"name": "Rocket League", "description": "A fast-paced game that combines soccer with rocket-powered cars.", "prompt": "A stadium with rocket-powered cars playing soccer with giant glowing ball, action-packed scene"},
        {"name": "Tetris Effect", "description": "A visually immersive and rhythmic twist on the classic Tetris game.", "prompt": "A vibrant, visually stunning Tetris game with glowing blocks and rhythmic lights"}
    ]
    return recommended_games

# Function to generate an image using OpenAI's DALL-E API
def generate_game_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

# Display recommendations when user clicks the button
if st.button("Get Recommendations"):
    # Get the list of recommended games
    games = recommend_games(
        selected_audience,
        selected_genres,
        selected_play_style,
        selected_pain_points,
        selected_desires,
        selected_platforms,
        selected_time_commitment
    )
    
    # Display each recommended game with generated image and description
    for game in games:
        st.subheader(game['name'])
        st.write(game['description'])
        
        # Generate an image for each game
        image_url = generate_game_image(game['prompt'])
        st.image(image_url, caption=game['name'])
