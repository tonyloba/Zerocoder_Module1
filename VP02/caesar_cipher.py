def caesar_cipher(text, shift, mode='encrypt'):
  """
  Реализация шифра Цезаря для шифрования и дешифрования текста.
  :param text: Входной текст
  :param shift: Сдвиг (целое число)
  :param mode: Режим: 'encrypt' для шифрования, 'decrypt' для дешифрования
  :return: Преобразованный текст
  """
  result = []
  if mode == 'decrypt':
      shift = -shift  # Для дешифрования сдвиг в противоположную сторону
  for char in text:
      if char.isalpha():  # Только буквы будут шифроваться
          ascii_offset = ord('A') if char.isupper() else ord('a')
          new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
          result.append(new_char)
      else:
          result.append(char)  # Символы, не являющиеся буквами, остаются без изменений
  return ''.join(result)

# Пример использования
text_to_encrypt = "Hello, World!"
shift_value = 3

# Шифрование
encrypted_text = caesar_cipher(text_to_encrypt, shift_value, mode='encrypt')
print("Зашифрованный текст:", encrypted_text)

# Дешифрование
decrypted_text = caesar_cipher(encrypted_text, shift_value, mode='decrypt')
print("Расшифрованный текст:", decrypted_text)

