#  🎐 Japanese Haiku Generator App

This is a student project that was created for traditional Japanese haiku poems generation in response to user-defined themes — with translations and authentic Ukiyo-e style illustrations. The main aim was to wrap up some knowledge obtained during  ‘LangChain for LLM Application Development’ AI Course and practice project architecture building.

---
 
## 🎯 The Model Choice

It was decided to pick a cohere LLM model for it has an intuitively clear and coherent API. Moreover, the model demonstrates great results in creativity and handles both Russian and Japanese text generation really well.

---

## 🌸 Features

- 🖋️ **Haiku Generator** (in Japanese) using Cohere language models 
- 📜 **Automatic Russian Translation** of generated haiku 
- 🖼️ **Ukiyo-e Style Image Generation** via Stable-Diffusion 3.5 large
- 🧠 **Theme validation with simple heuristics** 
- ✨ **Minimalistic Streamlit UI** 
- 📁 **Modular, extensible project structure** 

---

## 🌸 Example Output

**Input Theme:** `Танабата` 

**Generated Haiku (日本語):**  
> 星々交わる  
> 夏の夜にたなばたの  
> 夢描く人  

**Russian Translation:** 
> Звёзды переплетаются  
> В летней ночи, Танабата  
>Люди рисуют мечты.  

**Generated Image:** 

![2c180073d892b52ff0c628c9ecef5f3fe3e3187bf8e5e8e9ba98af3a](https://github.com/user-attachments/assets/529eee4d-e608-4302-a83a-2d099b4af073)

---

## 💻 Technologies Used

| Tech | Description |
|------|-------------|
| 🐍 Python 3.10+ | Core language |
| 🌐 Streamlit | Frontend web app |
| 🧠 [Cohere](https://cohere.com/) | Haiku generation & translation |
| 🎨 [Hugging Face API](https://huggingface.co/) | stable-diffusion 3.5 large image generation |
| 📦 dotenv | Local API token management |

---

## 🛠 Installation

```bash
git clone https://github.com/yourusername/haiku-generator.git
cd haiku-generator
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create an .env file in the root directory containing the paramount API keys:

COHERE_API_KEY='your_cohere_key'  
HF_TOKEN='your_huggingface_token'  

---

## 🚀 Running the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

haiku-generator/  
├── app.py                     -> Streamlit app entry point  
├── haiku_generator.py         -> Japanese haiku generation (Cohere)    
├── russian_translation.py     -> Poetic Russian translation  
├── ukiyo_e_generator.py       -> Image generation (stable-diffusion 3.5 large)    
├── theme_validation.py        -> Theme quality checker  
├── requirements.txt  
└── .env  

---

##  ❗ Notes
A Cohere API is geo-blocked in certain regions, like Russia. So if its implementation is unavailable in your region consider using a foreign server or a VPN software. 
