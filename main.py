import streamlit as st
from few_shots import FewshotPosts
from post_generator import generate_posts

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    st.title("LinkedIn Posts Generator")
    col1,col2,col3 = st.columns(3)
    
    fs = FewshotPosts()
    tags = fs.get_tags()
    with col1:
        selected_title = st.selectbox("Title",options= tags)
    with col2:
        selected_length = st.selectbox("Length",options= length_options)
    with col3:
        selected_language =st.selectbox("Language",options= language_options)

    if st.button("Generate Posts"):
        # st.write(f"Generating posts... for {selected_title} , {selected_length} , {selected_language}")
        post = generate_posts(selected_title, selected_length, selected_language)
        st.write("Generated Post:")
        st.write(post)
        
if __name__ == "__main__":
    main()