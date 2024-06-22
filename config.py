import os
import tempfile
from dotenv import load_dotenv, find_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
TOKEN = os.getenv('TOKEN')
CREDENTIALS_PATH = os.getenv('CREDENTIALS')  # Путь к файлу учетных данных
GCP_CLOUD_STORAGE_BUCKET_NAME = os.getenv('GCP_CLOUD_STORAGE_BUCKET_NAME')
ERROR_MESSAGE = 'We are facing an issue, please try after sometimes.'
AUDIO_FILE_FORMAT = 'mp3'

# Устанавливаем тип ответа
REPLY_TYPE = 'audio'  # или 'text'

OUTPUT_DIR = os.path.join(
    tempfile.gettempdir(),
    'telegrambot'
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Устанавливаем переменную окружения для использования учетных данных Google
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH
