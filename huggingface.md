# Hugging Face
- Hugging Face is the leading platform and community for ML and AI.
- Often called GitHub of AI.
- It provides the tools, models, datasets and infrastructure need to build, share and deploy state of the art models in Natural Language Processing., CV , Audio and multimodal AI.

# Hello World
- use transformers python library.
- hello world that loads pre-trained sentiment analysis model and uses it to classify text.
- Installation
```
pip install transformers torch
``` 
- python code
- 
```
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("Hugging Face makes AI incredibly easy and accessible.")

print(result)
```
- Key Components
    - The Hub
    - Transformers
    - Datasets
    - Spaces
- The Hub: huggingface.co/models, A repository hosting hundreds of thousands of open-source models like BERT, Llama, Stable Diffusion, Whisper etc.
- Transformers: A library providing APIs to easily download and train state of the ar models.
- Data sets: A library for easily accessing and sharing datasets for audio, computer vision, and NLP tasks.
- Spaces: A feature allowing you to host live ML demo apps directly in your browser using Gradio or Streamlit.

---
# Building, Training with datasets, pushing a model to the Hub, and deploying it as a web app on Hugging face Spaces involves a straight forward end to end workflow.

## Login to Hugging Face CLI
- 
```
pip install huggingface_hub
huggingface-cli login
```

## Prepare a dataset and Train a Model Using Transformers.
- use datasets library to load data and transformers Trainer API fine-tune a model.
- 
```
from datasets import load_dataset
```
-  





























