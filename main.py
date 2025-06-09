import streamlit as st
from few_shots import FewshotPosts
from post_generator import generate_posts

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="📝", layout="wide")
# st.set_page_config(layout="wide")
def main():
    st.title("LinkedIn Posts Generator")
    col1,col2,col3,col4 = st.columns(4)
    
    fs = FewshotPosts()
    tags = fs.get_tags()
    creator = fs.get_creator()
    print(tags)
    default_index = tags.index("Job Search") if "Job Search" in tags else 0
    print(default_index)
    
    with col1:
        selected_title = st.selectbox("Title",options= tags,index=default_index)
    with col2:
        selected_length = st.selectbox("Length",options= length_options)
    with col3:
        selected_language =st.selectbox("Language",options= language_options)
    with col4:
        selected_creator =st.selectbox("Creator",options= creator)
    if st.button("🚀 Generate Post"):
        with st.spinner("Creating magic..."):
            # post = f"Generating posts... for {selected_title}, {selected_length}, {selected_language}, {selected_creator}"
            post = generate_posts(selected_title, selected_length, selected_language, selected_creator)
        st.success("Here's your post:")
        st.markdown(f"#### ✨ Output by {selected_creator}")
        st.markdown(f"```text\n{post.strip()}\n```")    
if __name__ == "__main__":
    main()