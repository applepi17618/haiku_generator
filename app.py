import os
from dotenv import load_dotenv
import streamlit as st
import time
from PIL import Image

from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parent / "env")

COHERE_API_KEY = os.getenv('COHERE_API_KEY')
HF_TOKEN = os.getenv('HF_TOKEN')

from haiku_generator import generate_haiku
from russian_translation import translate
from ukiyo_e_generator import generate_ukiyo_e
from theme_validation import validate_the_theme
def run_app():
  st.set_page_config(page_title='Генератор хайку', layout='centered')
  st.title('🎐 Японский Хайку-Генератор')
  theme = st.text_input('Введите тему для хайку, пожалуйста:',
                        max_chars=50)
  if theme:
    if validate_the_theme(theme):
      with st.spinner('✨ Генерируем хайку и изображение...'):
        start_time = time.time()
        haiku = generate_haiku(theme)
        haiku_ru = translate(haiku['Хайку'])
        ukiyo_e_img = generate_ukiyo_e(theme)
      st.success('✨ Готово!')
      st.markdown('### 🖋️ Хайку:')
      st.markdown(f"<div style='font-size:22px;white-space: pre-wrap;'>{haiku['Хайку']}</div>", 
                  unsafe_allow_html=True)
      
      st.markdown("### 📜 Перевод на русский:")
      st.markdown(f"<div style='font-size:22px; white-space: pre-wrap;'>{haiku_ru}</div>", unsafe_allow_html=True)
      try:
        if ukiyo_e_img and os.path.exists(ukiyo_e_img):
          st.markdown("### 🖼️ Иллюстрация укиё-э:")
          st.image(Image.open(ukiyo_e_img), use_container_width=True)
          elapsed_time = time.time() - start_time
          st.write(f"🕓 Сгенерировано за {elapsed_time:.2f} сек.")
        else:
          st.warning("⚠️ Не удалось сгенерировать изображение.")
      except Exception as e:
        st.error(f"❌ Ошибка при отображении изображения: {e}")
        st.warning('❗ Введите более осмысленную тему (3+ символа).')

if __name__ == "__main__":
    run_app()