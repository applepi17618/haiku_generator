def validate_the_theme(theme: str, max_length=50) -> bool:
  """Theme validation process based on the topic length."""
  if not theme.strip():
    print("Пожалуйста, введите тему.")
    return False
  if len(theme) > max_length:
    print("Извините, но ваша тема слишком длинная.")
    return False
  return True
