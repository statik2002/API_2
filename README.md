# API_2
Второй урок по API на Devman

# Установка
- Скачать
- Создать виртуальное окружение
- Установить зависимости командой `install -r requirements.txt`
- Пропишите в переменной окружения ваш токен на Bit.ly (Для этого создайте файл `.env` в папке со скриптом)
  - BITLY_TOKEN={token}

# Использование
- запустите скрипт командой `python main.py`
- введите либо битлинк, либо длинную ссылку
  - Битлинк. Например: `https://bit.ly/3POye6z`
  - Длинную ссылку. Например: `https://google.com`
- При вводе существующего битлинка, будет выведено общее количество кликов по нему
- При вводе длинной ссылки у которой уже есть битлинк, будет выведен битлинк для длинной ссылки. Если нет битлинка для длинной ссылки, то будет создан новый битлинк и выведен на экран.
