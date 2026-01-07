#  Image Caption Generator using Multimodal AI

This project demonstrates **image caption generation using multimodal AI models**, covering both **research-oriented sample scripts** and a **user-friendly web application** built with **Streamlit**.

The repository is designed for:
- Beginners who want to understand **image captioning**
- Learners exploring **CLIP vs BLIP**
- Developers looking to build **real-world multimodal AI applications**

---

##  Sample Scripts 

Before using the web app, users are encouraged to explore the **sample Jupyter notebooks** to understand how image captioning works at a model level.

### 1️ CLIP-based Caption Generation (CIFAR-10)

**File:**  
`Sample_scripts/MutiModal_Experiment_with_CLIP_models_and_CIFAR10_data.ipynb`

**What this script does:**
- Uses the **CLIP model**
- Loads images from the **CIFAR-10 dataset**
- Matches images with **predefined textual prompts**
- Selects the most relevant caption based on similarity scores

**Key learning:**
- CLIP does **not generate new text**
- It performs **image–text matching**, not true caption generation

---

### 2️ BLIP-based Caption Generation (STL-10)

**File:**  
`Sample_scripts/Multimodal_experiment_with_BLIP_model_and_STL10.ipynb`

**What this script does:**
- Uses **BLIP (Bootstrapped Language-Image Pretraining)**
- Processes images from the **STL-10 dataset**
- Generates **natural language captions**
- Produces more descriptive and human-like outputs

**Key learning:**
- BLIP is a **generative multimodal model**
- Captions are created dynamically, not selected from a list

---

##  Understanding the Models

###  CLIP (Contrastive Language–Image Pretraining)

**How CLIP works:**
- Trains on image–text pairs
- Converts images and text into a shared embedding space
- Measures similarity between image and text embeddings

**Strengths:**
- Excellent for:
  - Image classification
  - Image–text retrieval
  - Zero-shot learning

**Limitations:**
-  Cannot generate novel captions
-  Limited creativity
-  Depends on predefined text prompts

---

###  BLIP (Bootstrapped Language-Image Pretraining)

**How BLIP works:**
- Combines:
  - Vision encoder
  - Language model
  - Cross-modal attention
- Learns to **generate text conditioned on images**

**Strengths:**
-  True image caption generation
-  Rich, descriptive language
-  Handles complex scenes better

---

###  CLIP vs BLIP – Key Differences

| Feature | CLIP | BLIP |
|------|------|------|
| Caption generation |  No |  Yes |
| Text output | Matching-based | Generative |
| Creativity | Low | High |
| Image storytelling |  Limited |  Strong |
| Best use cases | Retrieval, classification | Captioning, VQA, storytelling |


###  Why BLIP is Ideal for Image Storytelling

BLIP is particularly suited for **image storytelling** because:
- It understands **context**, not just objects
- It generates **fluent, natural sentences**
- It can describe **relationships and scenes**
- It does not rely on fixed caption templates

This makes BLIP a better choice for:
- Image captioning apps
- Assistive technologies
- Content generation
- Accessibility tools

---

##  Streamlit Web Application

###  Application Overview

The Streamlit app allows users to:
- Upload an image
- Generate a caption using **BLIP**
- Instantly view the AI-generated description

**Model used:**  
`Salesforce/blip-image-captioning-base`

---

###  How the App Works

1. User uploads an image via the Streamlit interface
2. Image is preprocessed using BLIP’s processor
3. The BLIP model generates a caption
4. Caption is displayed on the UI

---

###  Running the Application

#### 1️ Install Dependencies
```bash
pip install -r requirements.txt
```


#### 2 Run App
```bash
streamlit run app.py

```


##  Testing & Observations

The application was tested with a wide range of real-world images to evaluate the robustness and practical usefulness of the BLIP-based image captioning model.

###  Successful Examples

The model performed particularly well in the following scenarios:

- **Occluded objects:**  
  An image of a **dog partially hidden under a sofa** was correctly identified, with the model generating a meaningful and context-aware caption.

- **Reflections and visual ambiguity:**  
  An image showing a **man visible only through a water reflection** was also described accurately, demonstrating the model’s ability to reason beyond direct object visibility.

These examples indicate that the model can handle:
- Partial visibility
- Complex lighting
- Indirect visual cues

---

###  Chart Understanding Example

A **bar chart image** was also tested using the application.

- The model correctly **identified the image as a bar chart**
- However, the **explanation of the chart was not fully accurate or detailed**

This highlights that while the model has some level of visual structure understanding, it is **not specialized for data visualization interpretation**.

---

##  Strengths of the Application

- Uses a **state-of-the-art multimodal generative model (BLIP)**
- Generates **natural and human-like captions**
- Handles **complex scenes and occlusions**
- Simple and intuitive **Streamlit-based UI**
- Useful for:
  - Image understanding demos
  - Educational purposes
  - Accessibility-related applications
  - Multimodal AI learning

---

##  Limitations

- Not optimized for **detailed chart or data explanation**
- Does not extract numerical values from graphs
- Performance depends on:
  - Image quality
  - Lighting conditions
  - Visual complexity
- The base BLIP model may miss **fine-grained semantic details**
- Not designed for domain-specific imagery (e.g., medical or satellite images)

---



Overview of the app is shown via following screenshots.

<img width="843" height="801" alt="image" src="https://github.com/user-attachments/assets/ebea4384-be49-4c84-b0fa-2c3e18cf4ba8" />

<img width="737" height="233" alt="image" src="https://github.com/user-attachments/assets/22eadf30-0c94-439d-920c-6a678b3c11fc" />

Following are some further examples.

<img width="655" height="795" alt="image" src="https://github.com/user-attachments/assets/84df55f5-2136-48b6-9796-7a5c36086976" />

<img width="662" height="733" alt="image" src="https://github.com/user-attachments/assets/57436e36-7489-453b-af9d-3e292206cfce" />

<img width="662" height="785" alt="image" src="https://github.com/user-attachments/assets/c892a964-990e-4bc5-9354-1999602b1246" />

<img width="618" height="755" alt="image" src="https://github.com/user-attachments/assets/0bc85902-10cf-4aaa-98a9-9f622e72ff42" />







