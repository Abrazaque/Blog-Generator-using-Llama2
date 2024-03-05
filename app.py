import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getLLamaresponse(input_text, no_words, blog_style):
    llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin',  
                        model_type='llama',
                        config={'max_new_tokens': 256, 'temperature': 0.01})
    
    template = """
    Write a blog for {blog_style} job profile on the topic: {input_text}
    within {no_words} words.
    """
    
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)
    
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    return response

st.set_page_config(page_title="Generate Blogs", page_icon='🤖', layout='centered', initial_sidebar_state='collapsed')
st.header("Generate Blogs")

input_text = st.text_area("Enter the Blog Topic", height=150)
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.slider('Number of Words', min_value=100, max_value=1000, value=500, step=50)
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

if submit and input_text:
    with st.spinner('Generating your blog...'):
        blog_content = getLLamaresponse(input_text, no_words, blog_style)
        
        st.subheader("Generated Blog")
        with st.expander("See generated blog"):
            st.write(blog_content)
        
        st.download_button(label="Download Blog", data=blog_content, file_name="generated_blog.txt", mime='text/plain')
else:
    st.error("Please enter a blog topic.")
    
