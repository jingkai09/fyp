import streamlit as st
import openai

openai.api_key = st.secrets["mykey"]

# Define possible options for each input category
target_audience = ["Casual gamers", "Hardcore gamers", "Families", "Esports enthusiasts", "Retro gaming fans"]
game_genres = ["Action", "Adventure", "Role-playing", "Simulation", "Strategy", "Sports", "Puzzle", "Horror", "MMO"]
platforms = ["PC", "Console", "Mobile", "VR", "Cloud gaming"]
play_style = ["Single-player", "Multiplayer", "Cooperative", "Competitive"]
time_commitment = ["Less than 1 hour", "1-3 hours", "3-5 hours", "5+ hours"]
pain_points = ["Limited playtime", "High hardware requirements", "In-game purchases", "Repetitive gameplay", "Long updates"]
desires = ["Immersive story", "High-quality graphics", "Challenging gameplay", "Relaxing experience", "Social interaction"]

# Streamlit UI
st.title("Game Recommendation System")

# User input for customization
col1, col2 = st.columns(2)  # Arrange inputs in two columns for better layout

with col1:
    selected_audience = st.selectbox("Target Audience:", target_audience)
    selected_genres = st.multiselect("Preferred Game Genres:", game_genres)
    selected_play_style = st.selectbox("Preferred Play Style:", play_style)

with col2:
    selected_pain_points = st.multiselect("Pain Points:", pain_points)
    selected_desires = st.multiselect("Desires:", desires)
    selected_platforms = st.selectbox("Preferred Platform:", platforms)
    selected_time_commitment = st.selectbox("Preferred Time Commitment:", time_commitment)

# Recommendation logic based on selections
def recommend_games(selected_audience, selected_genres, selected_play_style, selected_pain_points, selected_desires, selected_platforms, selected_time_commitment):
    recommended_games = []
    recommended_features = []

    # Sample recommendation rules based on preferences
    if selected_audience == "Casual gamers":
        recommended_games.extend(["Stardew Valley", "Animal Crossing"])
        recommended_features.extend(["Relaxing gameplay", "Easy to pick up and play"])

    if "Action" in selected_genres:
        recommended_games.append("God of War")
        recommended_features.append("Intense action and combat")

    if selected_play_style == "Multiplayer":
        recommended_games.append("Fortnite")
        recommended_features.append("Engaging multiplayer experience")

    if "High-quality graphics" in selected_desires:
        recommended_games.append("Cyberpunk 2077")
        recommended_features.append("Cutting-edge graphics")

    if selected_platforms == "Mobile":
        recommended_games.extend(["Clash of Clans", "Candy Crush"])
        recommended_features.append("Optimized for mobile devices")

    if selected_time_commitment == "Less than 1 hour":
        recommended_games.append("Among Us")
        recommended_features.append("Quick gameplay sessions")

    # Remove duplicates to clean up recommendations
    recommended_games = list(set(recommended_games))
    recommended_features = list(set(recommended_features))

    return recommended_games, recommended_features

# Display recommendations when user clicks the button
if st.button("Get Recommendations"):
    games, features = recommend_games(
        selected_audience,
        selected_genres,
        selected_play_style,
        selected_pain_points,
        selected_desires,
        selected_platforms,
        selected_time_commitment
    )
    st.subheader("Recommended Games:")
    st.write(games if games else "No specific recommendations based on current selections.")
    
    st.subheader("Recommended Features:")
    st.write(features if features else "No specific recommendations based on current selections.")
