import os
from huggingface_hub import InferenceClient
hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise ValueError("❌ Переменная HF_TOKEN не найдена или пуста.")
def generate_ukiyo_e(theme: str, output_path: str = "ukiyo_e.png") -> str:
  '''Generates an ukiyo-e image based on the given haiku topic.'''
  ukiyo_e_prompt = f'ukiyo-e, japanese painting, traditional art, Utagawa Hiroshige, soft pastel colours, detailed, {theme}'
  client = InferenceClient(
      provider='hf-inference',
      api_key=hf_token,
      )
  try:
    image = client.text_to_image(
    ukiyo_e_prompt,
    model="stabilityai/stable-diffusion-3.5-large",
    )
    image.save(output_path)
    return output_path
  except Exception as e:
    print(f'❌ Ошибка генерации изображения: {e}')
    return None
