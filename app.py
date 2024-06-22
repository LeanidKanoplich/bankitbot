from fastapi import FastAPI, Request
from telegram_api import send_audio, send_message, set_webhook, get_file_path, save_file_and_get_local_path
from openai_apis import text_to_speech, transcript_audio, chat_completion
import config

{
"secret_token": "2f6OpVEPB9nnhYLvrvgEWUp6fMy_3eNqobLfoSiapSgRSR73r",
"url": "https://843a1a6f02ce.ngrok.app/telegram"
}

app = FastAPI()

# Устанавливаем webhook при старте приложения
@app.on_event("startup")
async def startup_event():
    set_webhook()

# Маршрут для домашней страницы
@app.get("/")
async def home():
    return {"message": "Hello, World!"}

# Маршрут для обработки сообщений от Telegram
@app.post("/telegram")
async def telegram_webhook(request: Request):
    try:
        message = await request.json()
        print(message)

        if 'message' in message:
            chat_id = message['message']['chat']['id']
            if 'text' in message['message']:
                text = message['message']['text']
                if text.startswith('/start'):
                    response_text = await chat_completion(text)
                    send_message(chat_id, response_text)
            elif 'voice' in message['message']:
                file_id = message['message']['voice']['file_id']
                local_file_path = save_file_and_get_local_path(file_id)
                transcript = await transcript_audio(local_file_path)
                response_text = await chat_completion(transcript)
                send_message(chat_id, response_text)

    except Exception as e:
        print(f"Error at telegram: {e}")
        send_message(chat_id, config.ERROR_MESSAGE)
