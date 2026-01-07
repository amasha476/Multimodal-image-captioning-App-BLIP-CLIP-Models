import streamlit as st
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Page config
st.set_page_config(page_title="Image Caption Generator", layout="centered")

st.title(" Image Caption Generator")
st.write("Upload an image and generate a caption using a multimodal AI model.")

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"

@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    ).to(device)
    return processor, model

processor, model = load_model()

# Image upload
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        with st.spinner("Generating caption..."):
            inputs = processor(images=image, return_tensors="pt").to(device)

            with torch.no_grad():
                output_ids = model.generate(
                    **inputs,
                    max_length=30,
                    num_beams=5
                )

            caption = processor.decode(
                output_ids[0],
                skip_special_tokens=True
            )

        st.success("Caption Generated!")
        st.markdown(f"###  Caption:\n**{caption}**")