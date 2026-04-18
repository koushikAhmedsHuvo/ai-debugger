import streamlit as st
from PIL import Image
from api_calling import note_generator


st.title("AI Code Debugger")
st.markdown("Upload at max 3 images to debug your code")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader("Upload your image", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    
    pil_images=[]
    for img in images:
        pil_img=Image.open(img)
        pil_images.append(pil_img)
        
    if images:
        if len(images)>3:
            st.error("Please upload at max 3 images")
        else:
            st.subheader("Uploaded Images")
            col=st.columns(len(images))
            
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    selected_options=st.selectbox("Enter the debugeer mode",("Hints","Solution with code"),index=None)
    
    pressed=st.button("Debug Code",type="primary")
    
    if pressed:
        if not images:
            st.error("Please upload at least one image")
        if not selected_options:
            st.error("Please select a debug mode")

if pressed and images and selected_options:
    with st.container(border=True):
        st.subheader("Problems")
        
        with st.spinner("AI is Thinking..."):
            generated_notes=note_generator(pil_images, selected_options)
            st.markdown(generated_notes)
                    
                    
                
                
            
    
                    
            
    