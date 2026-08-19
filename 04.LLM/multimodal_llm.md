# Multimodal LLM
- Traditional text only LLM cannot handle images or videos natively.
- Modern multimodal LLM (MLLMs) often still broadly referred to as LLMs (such as Google Gemini)
- Can directly process, understand, and reason about image and video data.

---
# How do LLMs handle visual data?
- visual data cannot be read directly as raw pixels by a standard language network. Instead MLLMs use specialized architectures.
    - Visual Encoders
        - Images (or video frames sampled over time) are passed through a vision encoder (e.g., vision transformer or CNN) that converts pixels into mathematical embedding or tokens.
    - Modality Alignment
        - Projection layers or specialized modules bridge the gap between visual tokens and the LLMs text based semantic space.
    - Joint Reasoning
        - The LLM processes the visual tokens alongside text tokens, allowing it to see and reason about the content simultaneously.

---
# What can they do directly?
- Image Understanding Analysis
    - captioning
    - visual QA
    - object detection and Localization
    - Document parsing 
- Video Understanding Analysis
    - Temporal Reasoning
    - Event Localization
    - Video Summarization
---
# Direct processing vs. Assistance.
- While MLLMs can work directly on perception tasks, they usually rely on external tools or code execution for heavy image/video manipulation.
- 

---
# Use Cases
- Image / Video Captioning and QA
- Object / Text Extraction OCR
- video event search
- Image/ Video Editing and Rendering

---





























