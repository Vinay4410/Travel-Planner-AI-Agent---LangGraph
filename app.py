# app.py

import streamlit as st
from datetime import datetime
from src.agent_setup import AgentSetup
from src.travel_agent import TravelAgent
from src.utils import MarkdownExporter

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- Custom CSS for Better Look --------------------
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Main styling */
    .main {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        font-weight: 300;
    }
    
    /* Cards styling */
    .feature-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        border: 1px solid #f0f2f6;
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    
    /* Success message styling */
    .success-box {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        border: 2px solid #28a745;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        text-align: center;
    }
    
    /* Info box styling */
    .info-box {
        background: linear-gradient(135deg, #e7f3ff 0%, #cce7ff 100%);
        border-left: 5px solid #007bff;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* Stats cards */
    .stat-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem 0;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    
    /* Text area styling */
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e9ecef;
        padding: 1rem;
        font-family: 'Poppins', sans-serif;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div > div {
        border-radius: 10px;
        border: 2px solid #e9ecef;
    }
    
    /* Spinner styling */
    .stSpinner > div {
        border-top-color: #667eea !important;
    }
    
    /* Download button */
    .download-btn {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 500;
        display: inline-block;
        margin: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .download-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(40, 167, 69, 0.4);
    }
    
    /* Hide streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -------------------- Initialize Components --------------------
@st.cache_resource
def load_components():
    """Load and cache the AI components"""
    agent = AgentSetup()
    planner = TravelAgent(agent)
    exporter = MarkdownExporter()
    return agent, planner, exporter

# -------------------- Main App --------------------
def main():
    # Beautiful Header
    st.markdown("""
    <div class="main-header">
        <h1>✈️ AI Travel Planner</h1>
        <p>Create amazing travel experiences with the power of AI</p>
    </div>
    """, unsafe_allow_html=True)

    # Load components
    try:
        agent, planner, exporter = load_components()
    except Exception as e:
        st.error(f"❌ Failed to initialize AI components: {e}")
        return

    # Create two main columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Main planning section
        st.markdown("""
        <div class="feature-card">
            <h2>🎯 Plan Your Dream Trip</h2>
            <p>Tell us about your perfect vacation and let AI create a detailed itinerary for you!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick templates
        st.subheader("🚀 Quick Start Templates")
        template_options = {
            "🏖️ Beach Paradise": "Plan a 7-day relaxing beach vacation with luxury resorts, water sports, and beachside dining. Budget around ₹1.5 lakh.",
            "🏛️ European Cultural Tour": "Create a 10-day cultural journey through Paris, Rome, and Barcelona with museums, historic sites, and local cuisine. Budget ₹2 lakh.",
            "🍜 Asian Food Adventure": "Design a 8-day culinary trip through Thailand and Vietnam focusing on street food, cooking classes, and local markets. Budget ₹80,000.",
            "🏔️ Mountain Adventure": "Plan a 6-day mountain adventure in Nepal with trekking, scenic views, and cultural experiences. Budget ₹1.2 lakh.",
            "✨ Custom Trip": "Create your own unique travel plan"
        }
        
        selected_template = st.selectbox(
            "Choose a template or create custom:",
            list(template_options.keys()),
            index=4
        )
        
        # Text input based on template
        if selected_template == "✨ Custom Trip":
            default_query = (
                "Plan a 6-day trip to London with hotel views, return flights, top food & historic places. "
                "Keep it within ₹1 lakh and convert everything to INR."
            )
        else:
            default_query = template_options[selected_template]
        
        # Main input area
        user_query = st.text_area(
            "✏️ Describe your perfect trip:",
            value=default_query,
            height=150,
            placeholder="E.g., Plan a romantic 5-day trip to Paris with wine tasting, museums, and cozy restaurants..."
        )
        
        # Travel preferences in expandable section
        with st.expander("🎨 Advanced Trip Preferences", expanded=False):
            col_a, col_b = st.columns(2)
            
            with col_a:
                budget_mode = st.selectbox(
                    "💰 Budget Style",
                    ["💸 Budget-Friendly", "🎯 Standard", "💎 Luxury"],
                    index=1
                )
                
                trip_type = st.multiselect(
                    "🎭 Trip Interests",
                    ["🏛️ Culture", "🍽️ Food", "🏞️ Nature", "🎪 Adventure", "🛍️ Shopping", "🌙 Nightlife", "📸 Photography"],
                    default=["🏛️ Culture", "🍽️ Food"]
                )
            
            with col_b:
                group_size = st.selectbox(
                    "👥 Group Size",
                    ["🚶 Solo", "💑 Couple", "👨‍👩‍👧 Family", "👫 Friends Group"],
                    index=1
                )
                
                special_needs = st.text_input(
                    "♿ Special Requirements",
                    placeholder="Dietary restrictions, accessibility needs, etc."
                )

    with col2:
        # Side panel with stats and info
        st.markdown("""
        <div class="feature-card">
            <h3>📊 AI Travel Assistant</h3>
            <p>Our AI analyzes thousands of travel options to create your perfect itinerary!</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Features showcase
        features = [
            ("🎯", "Smart Planning", "AI-powered recommendations"),
            ("✈️", "Flight Booking", "Best flight options"),
            ("🏨", "Hotel Selection", "Perfect accommodations"),
            ("🗺️", "Daily Itineraries", "Hour-by-hour plans"),
            ("💰", "Budget Tracking", "Cost breakdowns"),
            ("🍽️", "Food Recommendations", "Local cuisine spots")
        ]
        
        for icon, title, desc in features:
            st.markdown(f"""
            <div style="background: #f8f9fa; padding: 1rem; border-radius: 10px; margin: 0.5rem 0; border-left: 4px solid #667eea;">
                <strong>{icon} {title}</strong><br>
                <small style="color: #6c757d;">{desc}</small>
            </div>
            """, unsafe_allow_html=True)

    # Generate button (full width)
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("🚀 Generate My Perfect Itinerary", use_container_width=True):
        if not user_query.strip():
            st.warning("⚠️ Please describe your trip or select a template!")
        else:
            generate_itinerary(user_query, planner, exporter, {
                'budget_mode': budget_mode,
                'trip_type': trip_type,
                'group_size': group_size,
                'special_needs': special_needs
            })

def generate_itinerary(query, planner, exporter, preferences):
    """Generate the travel itinerary with beautiful UI"""
    
    # Create enhanced query
    enhanced_query = enhance_query_with_preferences(query, preferences)
    
    # Beautiful progress indicator
    st.markdown("""
    <div class="info-box">
        <h4>🤖 AI is working on your travel plan...</h4>
        <p>This may take a few moments while we analyze the best options for you!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress steps
    progress_container = st.container()
    with progress_container:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        steps = [
            (20, "🎯 Analyzing your preferences..."),
            (40, "🌍 Finding perfect destinations..."),
            (60, "✈️ Searching for best flights..."),
            (80, "🏨 Selecting ideal accommodations..."),
            (100, "📝 Creating your detailed itinerary...")
        ]
        
        for progress, message in steps:
            status_text.info(message)
            progress_bar.progress(progress)
            # Small delay for better UX (remove if too slow)
            import time
            time.sleep(0.5)
    
    try:
        # Generate the itinerary
        response = planner.plan_trip(enhanced_query)
        
        # Clear progress indicators
        progress_container.empty()
        
        # Success message
        st.markdown("""
        <div class="success-box">
            <h2>🎉 Your Travel Plan is Ready!</h2>
            <p>Here's your personalized itinerary created by AI</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Display the itinerary
        st.markdown("---")
        st.markdown(response)
        st.markdown("---")
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Download Markdown
            filename = f"travel_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
            saved_path = exporter.export(response, filename)
            
            with open(saved_path, "r", encoding="utf-8") as f:
                st.download_button(
                    "📥 Download Plan",
                    f,
                    file_name=filename,
                    mime="text/markdown",
                    use_container_width=True
                )
        
        with col2:
            if st.button("🔄 Generate New Plan", use_container_width=True):
                st.rerun()
        
        with col3:
            if st.button("📧 Share Plan", use_container_width=True):
                st.info("💡 Use the download button to save and share your plan!")
        
        # Feedback section
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="feature-card">
            <h3>💭 How was your experience?</h3>
        </div>
        """, unsafe_allow_html=True)
        
        feedback_col1, feedback_col2 = st.columns(2)
        with feedback_col1:
            if st.button("👍 Love it!", use_container_width=True):
                st.success("🎉 Thank you! We're glad you loved your travel plan!")
        
        with feedback_col2:
            if st.button("💡 Suggest improvements", use_container_width=True):
                st.info("💬 Try adjusting your preferences and generating a new plan!")

    except Exception as e:
        progress_container.empty()
        
        st.markdown("""
        <div style="background: #f8d7da; border: 2px solid #dc3545; border-radius: 15px; padding: 1.5rem; text-align: center;">
            <h3>😅 Oops! Something went wrong</h3>
            <p>Don't worry, let's try again!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.error(f"Error details: {e}")
        
        if st.button("🔄 Try Again", use_container_width=True):
            st.rerun()

def enhance_query_with_preferences(query, preferences):
    """Add user preferences to the query"""
    enhancements = []
    
    if preferences.get('budget_mode'):
        mode = preferences['budget_mode'].split(' ')[-1].lower()  # Extract actual mode
        enhancements.append(f"Travel style: {mode}")
    
    if preferences.get('trip_type'):
        interests = [t.split(' ', 1)[1] for t in preferences['trip_type']]  # Remove emojis
        enhancements.append(f"Interests: {', '.join(interests)}")
    
    if preferences.get('group_size'):
        group = preferences['group_size'].split(' ', 1)[1].lower()  # Remove emoji
        enhancements.append(f"Group type: {group}")
    
    if preferences.get('special_needs'):
        enhancements.append(f"Special requirements: {preferences['special_needs']}")
    
    if enhancements:
        return f"{query}\n\nAdditional preferences: {'. '.join(enhancements)}"
    
    return query

if __name__ == "__main__":
    main()