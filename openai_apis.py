import openai
import config
import os
import uuid

async def chat_completion(prompt: str) -> str:
    """
    Функция для выполнения завершения чата на основе подсказки
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Убедитесь, что указана правильная модель
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content']
    except Exception as e:
        print(f"Error in chat_completion: {e}")
        raise

async def text_to_speech(text: str) -> tuple:
    """
    Функция для генерации аудио ответа на основе текста
    """
    try:
        response = openai.Audio.create(
            text=text,
            voice="en_us_001",
            format=config.AUDIO_FILE_FORMAT
        )
        audio_file_path = os.path.join(config.OUTPUT_DIR, f"{uuid.uuid4()}.{config.AUDIO_FILE_FORMAT}")
        with open(audio_file_path, 'wb') as audio_file:
            audio_file.write(response['audio_content'])
        return audio_file_path, os.path.basename(audio_file_path)
    except Exception as e:
        print(f"Error in text_to_speech: {e}")
        raise

async def transcript_audio(file_path: str) -> str:
    """
    Функция для получения текста из аудиофайла
    """
    try:
        with open(file_path, 'rb') as audio_file:
            response = openai.Audio.transcribe(
                model="whisper-1",
                file=audio_file
            )
        return response['text']
    except Exception as e:
        print(f"Error at transcript_audio: {e}")
        raise
