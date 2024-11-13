import streamlit as st
import openai

openai.api_key = st.secrets["mykey"]

# Define possible options
game_features = ["Multiplayer mode", "Open world", "Story-driven gameplay", "Realistic graphics", "Customizable characters", "Frequent updates"]
game_benefits = ["Social interaction", "Immersive experience", "Engaging storyline", "Skill-building", "Freedom of choice", "Consistent fresh content"]
target_audience = ["Casual gamers", "Competitive players", "Adventure seekers", "Fantasy lovers", "Story-driven gamers", "Realism enthusiasts"]
pain_points = ["Limited time to play", "High difficulty levels", "Repetitive gameplay", "Low-quality graphics", "Lack of updates"]
desires = ["Fun in short sessions", "Challenging gameplay", "Engrossing story", "High replay value", "Community engagement"]

# Streamlit UI
st.title("Game Recommendation System")

# User input for customization
selected_audience = st.selectbox("Target Audience:", target_audience)
selected_pain_points = st.multiselect("Pain Points:", pain_points)
selected_desires = st.multiselect("Desires:", desires)

# Recommendation logic based on selections
def recommend_features(selected_audience, selected_pain_points, selected_desires):
    recommended_features = []
    recommended_benefits = []

    # Sample recommendation rules based on target audience and preferences
    if selected_audience == "Casual gamers":
        recommended_features.extend(["Multiplayer mode", "Fun in short sessions"])
        recommended_benefits.extend(["Social interaction", "Quick enjoyment"])

    if "Engrossing story" in selected_desires:
        recommended_features.append("Story-driven gameplay")
        recommended_benefits.append("Engaging storyline")

    if "Challenging gameplay" in selected_desires:
        recommended_features.append("High difficulty levels")
        recommended_benefits.append("Skill-building")

    if selected_audience == "Fantasy lovers":
        recommended_features.extend(["Open world", "Story-driven gameplay"])
        recommended_benefits.append("Immersive experience")

    if "Lack of updates" in selected_pain_points:
        recommended_features.append("Frequent updates")
        recommended_benefits.append("Consistent fresh content")

    # Remove duplicates to clean up recommendations
    recommended_features = list(set(recommended_features))
    recommended_benefits = list(set(recommended_benefits))

    return recommended_features, recommended_benefits

# Display recommendations when user clicks the button
if st.button("Get Recommendations"):
    features, benefits = recommend_features(selected_audience, selected_pain_points, selected_desires)
    st.subheader("Recommended Game Features:")
    st.write(features if features else "No specific recommendations based on current selections.")
    
    st.subheader("Recommended Game Benefits:")
    st.write(benefits if benefits else "No specific recommendations based on current selections.")
