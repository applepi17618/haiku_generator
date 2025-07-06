import os
from dotenv import load_dotenv
import cohere

load_dotenv(dotenv_path="C:\haiku_generator_app\env")

api_key = os.getenv("COHERE_API_KEY")
if not api_key:
    raise ValueError("❌ Переменная COHERE_API_KEY не найдена или пуста.")

co = cohere.ClientV2(api_key)

def generate_haiku(theme: str) -> dict:
  '''Writes a japanese haiku based on the given topic.'''
  prompt_jp=f'''課題：
    次のテーマに沿って、日本語で俳句を作ってください：{theme}。
    俳句は古典的な形式に従いながらも、柔軟性を持たせて構いません。

    俳句の形式：
    三行構成、できれば五・七・五の音節（多少長くなっても構いません）
    長さは標準の1.5倍まで許容されます
    漢字とひらがなを使い、カタカナやアラビア数字は避けてください
    意味とイメージ：
    自然の状態（季語）を描写すること ― 単なる季節名ではなく、その季節の雰囲気を表してください
    実際の体験でも想像の世界でも構いませんが、まわりの風景や感覚を描いてください
    韻・教訓・抽象的な概念・説教的な表現は避けてください
    できる限り、比喩やたとえは避けてください（あいまいな二重の意味なら可）

    結果には、生成した俳句のみを表示してください。'''
  try:
    response = co.generate(
      model='c4ai-aya-expanse-8b',
      prompt=prompt_jp,
      max_tokens=64,
      temperature=0.8,
      k=0,
      stop_sequences=["\n\n"],
  )
    haiku = response.generations[0].text.strip()
    return {"Тема хайку" : theme, "Хайку" : haiku}
  except Exception as e:
    print(f'❌ Ошибка: {e}')
    return {'Тема хайку' : theme, 'Хайку' : '⚠️ Сбой при генерации.'}