# PostCraft - LinkedIn Post Generator
Generate engaging LinkedIn posts based on user inputs like topic, length, language, and writing style of popular content creators. This tool leverages few-shot examples and an LLM (Language Model) to create authentic, styled LinkedIn posts.

---
### Outputs
<img src="./img/output 1_hinglish.png" alt="Preview" width="600" height="400">
<img src="./img/output 2_english.png" alt="Preview" width="600" height="400">

## Features

- Generate posts with customizable:
  - **Topic/Title**
  - **Length** (Short, Medium, Long)
  - **Language** (English, Hinglish)
  - **Creator Tone** (Choose from multiple content creators to match their style)
- Uses few-shot learning examples filtered by parameters to guide generation
- Supports Hinglish — a blend of Hindi and English with script always in English
- Streamlit UI for easy interaction and post generation
- Output formatting and styled examples for better prompt crafting

---

## Getting Started

### Prerequisites

- Python 3.8+
- Access to an LLM backend (e.g., Llama) — ensure API keys/config are set
- MongoDB
- Recommended to create a virtual environment

### Installation

1. Clone the repository:
```bash
   git clone https://github.com/yourusername/linkedin-post-generator.git
   cd linkedin-post-generator
   ```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Preprocess your data:
```bash

python preprocess.py
```
4. Prepare your data:

Ensure you have data/processed_posts.json with your post dataset

This file should contain posts with keys: text, engagement, creator, tags, line_count, language

```bash

streamlit run app.py
```
This launches the web app on your local machine where you can select parameters and generate posts interactively.

### Usage
- Select a Title/Topic from the dropdown
- Select Length (Short, Medium, Long)
- Choose Language (English or Hinglish)
- Choose a Creator whose style you want to emulate
- Click Generate Post

The generated post will appear below, styled according to the chosen creator

### Extending the Project
- Add more content creators and curated posts to dataset
- Integrate more advanced LLMs or tune prompt templates
- Improve UI with more options and formatting
- Add post scheduling or export features

### License
This project is licensed under the MIT License.

### Acknowledgments
- This project was primarily inspired and guided by the work of **Dhaval Patel**.
- The writing styles used in this project were influenced by posts from:
  - **Muskan**
  - **Sahil Bloom**
  - **Justin Welsh**
  - **Shraddha Sharma**
  - **Vaibhav Sisinty**
- Built using LLama and Streamlit for rapid prototyping
