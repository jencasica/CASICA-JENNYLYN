import streamlit as st

# Default biography data
bio_data = {
    "Name": "Jennylyn Casica",
    "Age": 18,
    "Mother's Name": "Merly Mongado",
    "Sibling's Name": "Lesly Casica",
    "Hobby": "🎾 Playing Table Tennis",
    "Favorite Subject": "📘 Math",
    "Other Information": "Does not have a father.",
    "Achievements": ["🏆 Wtop in math competition", "🎖️ honor student"],
    "Favorite Color": "Purple",  # Default favorite color
    "Favorite Food": "Pizza"  # Default favorite food
}

# Default profile picture placeholder
DEFAULT_PROFILE_PICTURE = "https://scontent-mnl1-1.xx.fbcdn.net/v/t39.30808-6/450809836_825040332911065_2385971090331881290_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeHbmi6Qwibn_wIGuaMOjZZIheqpCfn2hvyF6qkJ-faG_FadJpoa5uyHA6cc8qdxIzFkurUGWaU46vei6uc3nB2G&_nc_ohc=1iRNBrwiWBUQ7kNvgEy3fs0&_nc_zt=23&_nc_ht=scontent-mnl1-1.xx&_nc_gid=AwXR6FKGf1zr821DU7pe5DY&oh=00_AYDq9HGrxMEdCiKXDA8MeDORbOTfMqvFE3Ir67ExooScKg&oe=674B8199"

def main():
    # Page configuration
    st.set_page_config(
        page_title="🎨 My Biography",
        page_icon="📖",
        layout="centered"
    )

    # Apply custom styles
    st.markdown(
        """
        <style>
            .big-font {
                font-size:40px !important;
                color: #4C9BFD;
            }
            .section-title {
                font-size: 28px !important;
                color: #4C9BFD;
                font-weight: bold;
                margin-top: 30px;
            }
            .bio-text {
                font-size: 18px;
                line-height: 1.8;
                margin-bottom: 20px;
            }
            .bio-text-strong {
                font-weight: bold;
            }
            .bio-container {
                margin-bottom: 40px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main menu
    menu = ["🏠 Home", "✏️ Edit Biography", "👀 View Biography"]
    choice = st.sidebar.selectbox("Main Menu", menu)

    if choice == "🏠 Home":
        # Home page
        st.title("🎉 Welcome to Your Personalized Biography!")
        st.write(
            """
            This app helps you create and organize your biography beautifully.  
            Use the menu on the left to edit or view your biography details.  
            """
        )
        st.image(DEFAULT_PROFILE_PICTURE, caption="Welcome!", width=200)  # Adjusted width for normal size

    elif choice == "✏️ Edit Biography":
        # Edit biography page
        st.title("✏️ Edit Your Biography")
        st.write("Fill out the form below to update your details.")
        
        # Profile picture upload
        st.subheader("🖼️ Upload Profile Picture")
        uploaded_file = st.file_uploader("Upload your profile picture (JPG/PNG):", type=["jpg", "png"])
        if uploaded_file:
            st.image(uploaded_file, caption="Your Profile Picture", width=200)  # Adjusted width for normal size
        
        # Edit form
        with st.form("edit_bio_form"):
            name = st.text_input("👤 Name", value=bio_data["Name"])
            age = st.number_input("🎂 Age", value=bio_data["Age"], step=1)
            mothers_name = st.text_input("👩‍👧 Mother's Name", value=bio_data["Mother's Name"])
            siblings_name = st.text_input("👨‍👩‍👧‍👦 Sibling's Name", value=bio_data["Sibling's Name"])
            hobby = st.text_input("🎨 Hobby", value=bio_data["Hobby"])
            favorite_subject = st.text_input("📚 Favorite Subject", value=bio_data["Favorite Subject"])
            other_info = st.text_area("📝 Other Information", value=bio_data["Other Information"])
            
            # Selectable fields for favorite color and food
            favorite_color = st.selectbox(
                "💜 Favorite Color",
                options=["Purple", "Blue", "Red", "Green", "Yellow", "Orange", "Black", "Pink", "White"],
                index=["Purple", "Blue", "Red", "Green", "Yellow", "Orange", "Black", "Pink", "White"].index(bio_data["Favorite Color"])
            )
            favorite_food = st.selectbox(
                "🍕 Favorite Food",
                options=["Pizza", "Sushi", "Burger", "Pasta", "Salad", "Ice Cream", "Tacos", "Rice", "Steak"],
                index=["Pizza", "Sushi", "Burger", "Pasta", "Salad", "Ice Cream", "Tacos", "Rice", "Steak"].index(bio_data["Favorite Food"])
            )
            
            # Achievements input
            st.subheader("🏅 Achievements")
            achievements = st.text_area(
                "List your achievements (one per line):",
                value="\n".join(bio_data["Achievements"])
            )
            
            submitted = st.form_submit_button("💾 Save Changes")
            if submitted:
                bio_data["Name"] = name
                bio_data["Age"] = age
                bio_data["Mother's Name"] = mothers_name
                bio_data["Sibling's Name"] = siblings_name
                bio_data["Hobby"] = hobby
                bio_data["Favorite Subject"] = favorite_subject
                bio_data["Other Information"] = other_info
                bio_data["Favorite Color"] = favorite_color
                bio_data["Favorite Food"] = favorite_food
                bio_data["Achievements"] = [ach.strip() for ach in achievements.split("\n") if ach.strip()]
                st.success("🎉 Biography updated successfully!")

    elif choice == "👀 View Biography":
        # View biography page
        st.title("👀 Your Organized Biography")
        
        # Profile picture
        if "uploaded_file" in locals() and uploaded_file:
            st.image(uploaded_file, caption="Your Profile Picture", width=200)  # Adjusted width for normal size
        else:
            st.image(DEFAULT_PROFILE_PICTURE, caption="Default Profile Picture", width=200)  # Adjusted width for normal size
        
        # Biography details grouped
        st.markdown('<p class="big-font">Personal Information</p>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <p class="bio-text"><span class="bio-text-strong">Name</span>: {bio_data["Name"]}</p>
            <p class="bio-text"><span class="bio-text-strong">Age</span>: {bio_data["Age"]}</p>
            """, unsafe_allow_html=True
        )
        
        st.markdown('<p class="section-title">Family Information</p>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <p class="bio-text"><span class="bio-text-strong">Mother's Name</span>: {bio_data["Mother's Name"]}</p>
            <p class="bio-text"><span class="bio-text-strong">Sibling's Name</span>: {bio_data["Sibling's Name"]}</p>
            """, unsafe_allow_html=True
        )
        
        st.markdown('<p class="section-title">Hobbies and Interests</p>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <p class="bio-text"><span class="bio-text-strong">Hobby</span>: {bio_data["Hobby"]}</p>
            <p class="bio-text"><span class="bio-text-strong">Favorite Subject</span>: {bio_data["Favorite Subject"]}</p>
            """, unsafe_allow_html=True
        )
        
        st.markdown('<p class="section-title">Other Information</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bio-text">{bio_data["Other Information"]}</p>', unsafe_allow_html=True)
        
        st.markdown('<p class="section-title">Favorite Color & Food</p>', unsafe_allow_html=True)
        st.markdown(
            f"""
            <p class="bio-text"><span class="bio-text-strong">Favorite Color</span>: {bio_data["Favorite Color"]}</p>
            <p class="bio-text"><span class="bio-text-strong">Favorite Food</span>: {bio_data["Favorite Food"]}</p>
            """, unsafe_allow_html=True
        )
        
        st.markdown('<p class="section-title">Achievements</p>', unsafe_allow_html=True)
        if bio_data["Achievements"]:
            for achievement in bio_data["Achievements"]:
                st.markdown(f'<p class="bio-text">- {achievement}</p>', unsafe_allow_html=True)
        else:
            st.write("No achievements listed yet.")
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.info("🌟 Thank you! We hope you love your organized biography.")

if __name__ == "__main__":
    main()
