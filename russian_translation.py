import cohere

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

co = cohere.Client(api_key)  

def translate(haiku: str) -> str:
    '''Translates the given haiku into Russian.'''
    prompt_ru = f"""Ты - профессиональный переводчик с японского на русский. 
    Твоя задача - перевести полученное хайку на русский язык, сохранив поэтичность и дух оригинала. 
    На вывод отдай только перевод.
    Хайку: {haiku} 
    Перевод:"""
    try:
        response = co.generate(
        model='c4ai-aya-expanse-8b',
        prompt=prompt_ru,
        max_tokens=100,
        temperature=0.8,
        )
        translation = response.generations[0].text.strip()
        return translation
    except Exception as e:
        print(f"❌ Перевод не удался: {e}")
        return "⚠️ Перевод недоступен."
