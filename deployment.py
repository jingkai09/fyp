import streamlit as st
import openai

openai.api_key =  st.secrets["mykey"]

# Define possible options
product_features = ["Voice control", "Touch screen interface", "Smart inventory management", "Recipe suggestions"]
product_benefits = ["Convenience", "Reduced food waste", "Personalized cooking assistance", "Energy efficiency", "Longer food freshness"]
target_audience = ["Busy families", "Health-conscious individuals", "Tech enthusiasts", "Cooking aficionados", "Home chefs"]
pain_points = ["Limited kitchen space", "Difficulty meal planning", "Time constraints", "Food spoilage concerns"]
desires = ["Simplified cooking", "Healthier eating", "Optimized organization", "Culinary inspiration"]

# Streamlit UI
st.title("Smart Fridge Pro Recommendation System")

# User input for customization
selected_audience = st.selectbox("Target Audience:", target_audience)
selected_pain_points = st.multiselect("Pain Points:", pain_points)
selected_desires = st.multiselect("Desires:", desires)

# Recommendation logic based on selections
def recommend_features(selected_audience, selected_pain_points, selected_desires):
    recommended_features = []
    recommended_benefits = []

    # Sample recommendation rules based on target audience and preferences
    if selected_audience == "Busy families":
        recommended_features.extend(["Smart inventory management", "Voice control"])
        recommended_benefits.extend(["Convenience", "Reduced food waste"])

    if "Healthier eating" in selected_desires:
        recommended_features.append("Recipe suggestions")
        recommended_benefits.append("Personalized cooking assistance")

    if "Difficulty meal planning" in selected_pain_points:
        recommended_features.append("Recipe suggestions")
        recommended_benefits.append("Simplified cooking")

    if selected_audience == "Tech enthusiasts":
        recommended_features.extend(["Voice control", "Touch screen interface"])
        recommended_benefits.append("Energy efficiency")

    # Remove duplicates to clean up recommendations
    recommended_features = list(set(recommended_features))
    recommended_benefits = list(set(recommended_benefits))

    return recommended_features, recommended_benefits

# Display recommendations when user clicks the button
if st.button("Get Recommendations"):
    features, benefits = recommend_features(selected_audience, selected_pain_points, selected_desires)
    st.subheader("Recommended Features:")
    st.write(features if features else "No specific recommendations based on current selections.")
    
    st.subheader("Recommended Benefits:")
    st.write(benefits if benefits else "No specific recommendations based on current selections.")
