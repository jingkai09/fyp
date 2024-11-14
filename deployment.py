import streamlit as st
import openai

openai.api_key = st.secrets["mykey"]

# Define possible options
game_features = [
    "Multiplayer mode", "Open world", "Story-driven gameplay", "Realistic graphics",
    "Customizable characters", "Frequent updates", "In-depth lore", "Character progression",
    "VR support", "Cross-platform compatibility", "Puzzle-solving mechanics", 
    "Skill-based combat", "Procedural generation", "Real-time strategy elements",
    "Exploration-based rewards"
]
game_benefits = [
    "Social interaction", "Immersive experience", "Engaging storyline", "Skill-building",
    "Freedom of choice", "Consistent fresh content", "Sense of accomplishment", 
    "Educational value", "Relaxing gameplay", "High replay value", "Competitive satisfaction",
    "Problem-solving skills", "Community connection", "Escapism"
]
target_audience = [
    "Casual gamers", "Competitive players", "Adventure seekers", "Fantasy lovers", 
    "Story-driven gamers", "Realism enthusiasts", "Puzzle solvers", "Explorers", 
    "Survival enthusiasts", "Sci-fi fans", "History buffs", "Young kids", "Teenagers", 
    "Adults", "Seniors"
]
pain_points = [
    "Limited time to play", "High difficulty levels", "Repetitive gameplay", 
    "Low-quality graphics", "Lack of updates", "Poor matchmaking", "Complicated controls", 
    "No solo mode", "Pay-to-win mechanics", "Inadequate tutorials", "Too much screen time",
    "Inaccessible gameplay", "Confusing interfaces"
]
desires = [
    "Fun in short sessions", "Challenging gameplay", "Engrossing story", "High replay value", 
    "Community engagement", "Creative freedom", "Realistic simulations", "Strategic depth",
    "Character customization", "Educational content", "Stress relief", "Relaxing vibe", 
    "Rich lore and history", "Unpredictable challenges", "Fast-paced action"
]
game_genres = [
    "Action", "Adventure", "Role-playing", "Simulation", "Strategy", "Sports", 
    "Puzzle", "Survival horror", "Shooter", "Platformer", "Racing"
]
platforms = [
    "PC", "Console", "Mobile", "VR", "Cross-platform"
]
play_style = [
    "Solo", "Cooperative", "Competitive", "Casual", "Intense"
]
time_commitment = [
    "Short sessions (<30 minutes)", "Moderate (1-2 hours)", "Extended (3+ hours)", 
    "Varies based on mood"
]

# Streamlit UI
st.title("Game Recommendation System")

# User input for customization
selected_audience = st.selectbox("Target Audience:", target_audience)
selected_pain_points = st.multiselect("Pain Points:", pain_points)
selected_desires = st.multiselect("Desires:", desires)
selected_genres = st.multiselect("Preferred Game Genres:", game_genres)
selected_platforms = st.selectbox("Preferred Platform:", platforms)
selected_play_style = st.selectbox("Preferred Play Style:", play_style)
selected_time_commitment = st.selectbox("Preferred Time Commitment:", time_commitment)

# Recommendation logic based on selections
def recommend_features(selected_audience, selected_pain_points, selected_desires, selected_genres, selected_platforms, selected_play_style, selected_time_commitment):
    recommended_features = []
    recommended_benefits = []

    # Sample recommendation rules based on target audience and preferences
    if selected_audience == "Casual gamers":
        recommended_features.extend(["Multiplayer mode", "Fun in short sessions", "Relaxing gameplay"])
        recommended_benefits.extend(["Quick enjoyment", "Stress relief"])

    if "Engrossing story" in selected_desires or "Role-playing" in selected_genres:
        recommended_features.append("Story-driven gameplay")
        recommended_benefits.append("Engaging storyline")

    if "Challenging gameplay" in selected_desires or selected_play_style == "Competitive":
        recommended_features.append("Skill-based combat")
        recommended_benefits.append("Skill-building")

    if selected_audience == "Fantasy lovers" or "Adventure" in selected_genres:
        recommended_features.extend(["Open world", "In-depth lore", "Character progression"])
        recommended_benefits.append("Immersive experience")

    if "Lack of updates" in selected_pain_points:
        recommended_features.append("Frequent updates")
        recommended_benefits.append("Consistent fresh content")

    if selected_play_style == "Cooperative" or selected_platforms == "Cross-platform":
        recommended_features.append("Multiplayer mode")
        recommended_benefits.append("Social interaction")

    if selected_time_commitment == "Short sessions (<30 minutes)":
        recommended_features.append("Casual gameplay")
        recommended_benefits.append("Quick enjoyment")

    # Remove duplicates to clean up recommendations
    recommended_features = list(set(recommended_features))
    recommended_benefits = list(set(recommended_benefits))

    return recommended_features, recommended_benefits

# Display recommendations when user clicks the button
if st.button("Get Recommendations"):
    features, benefits = recommend_features(
        selected_audience, selected_pain_points, selected_desires, 
        selected_genres, selected_platforms, selected_play_style, selected_time_commitment
    )
    st.subheader("Recommended Game Features:")
    st.write(features if features else "No specific recommendations based on current selections.")
    
    st.subheader("Recommended Game Benefits:")
    st.write(benefits if benefits else "No specific recommendations based on current selections.")
