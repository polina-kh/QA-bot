'''
Модуль для формирования QA-bot, "обученного" на нашей базе знаний
'''
from llama_index.core import GPTVectorStoreIndex, Document
import os
import json
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")
OPENAI_API_BASE=os.environ.get("OPENAI_API_BASE")
OPENAI_MODEL=os.environ.get("OPENAI_MODEL")

# Чтение базы знаний из файла, загрузка информации в индекс
def create_index():
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        documents = [Document(text=item['content'], title=item['title']) for item in data]
        index = GPTVectorStoreIndex(documents)
        return index
    
    except FileNotFoundError:
        print('Json-file not found')
    except Exception as e:
        print(f'Exception:{str(e)}')

# Возврат ответа на вопрос от нашего бота
def get_response(question, index):
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    return response