'''
Основной модуль приложения.
Используется Flask для создания простого веб-приложения.
'''
from flask import Flask, render_template, jsonify, request
from llama_kb_bot import create_index, get_response

index = create_index()

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    try:
        # Отправляем запрос боту и получаем ответ
        global index
        response = get_response(str(request.json["input"]), index)
        print("Input:", request.json)
        return jsonify({
                        'query': str(request.json["input"]), 
                        'response': str(response)
                        })
    except Exception as e:
        print(f'Exception:{str(e)}')
        return jsonify({
                        'query': str(request.json["input"]), 
                        'response': str("Request error!")
                        })


if __name__ == '__main__':
    app.run('127.0.0.1', '5000', debug=True)