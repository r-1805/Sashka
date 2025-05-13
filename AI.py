from datetime import datetime, timedelta
import sqlite3
import re
from langchain.schema import HumanMessage, SystemMessage
from langchain_community.chat_models.gigachat import GigaChat

# Авторизация в GigaChat
chat = GigaChat(
    credentials='NWMwMmQxMTQtMjM0Mi00MGQzLTk0ZWYtOTk1NDY2ODYyZmJiOjViZmQ0MGI2LTY1NTEtNDY1Mi05YTVkLWFkYTQ0MWQzYTlhMQ==',
    verify_ssl_certs=False,
    model='GigaChat-Max'
)

# Основная функция распознавания вопроса и генерации статьи
def recognize_question(raw_text, word_count, style, audience, references_format):
    # Формируем prompt для GigaChat на основе переданных параметров
    prompt = f"""
    На основе текста интервью ниже:
    {raw_text}

    Создай статью для публикации в журнале с учетом следующих настроек:

    1. Объем статьи:
       - Статья должна быть примерно {word_count} слов.

    2. Стиль написания:
       - Используй {style} стиль.

    3. Целевая аудитория:
       - Ориентируйся на аудиторию, состоящую из {audience}.

    4. Требования журнала:
       - Оформи ссылки по стандарту {references_format}.

    Подготовь текст в формате, подходящем для публикации в журнале.
    """

    messages = [
        SystemMessage(
            content="Ты бот, который создает статьи на основе интервью и заданных параметров."
        ),
        HumanMessage(content=prompt)
    ]

    # Отправляем запрос в GigaChat и получаем ответ
    res = chat.invoke(messages)
    return res.content

# Пример использования функции
# if __name__ == "__main__":
#     # Пример параметров для генерации статьи
#     raw_text = """
#     Интервьюер: Добрый день, Алексей, спасибо, что согласились на интервью. Давайте начнем с вашего взгляда на то, как искусственный интеллект может повлиять на образовательные процессы...
#     """
#     word_count = 2000
#     style = "научный"
#     audience = "экспертов в теме"
#     references_format = "ГОСТ"
#
#     # Вызов функции для генерации статьи
#     response = recognize_question(raw_text, word_count, style, audience, references_format)
#
#     # Вывод ответа
#     print(response)


# def main():
# #     # Вызов функции для генерации статьи
#     response = recognize_question()
# #
# #     # Вывод ответа
#     print(response)
 # Параметры для генерации статьи
 #    raw_text = """"""
 #    word_count_options = {"короткая": 1000, "средняя": 2000, "длинная": 3000}
 #    word_count = word_count_options["средняя"]
 #
 #    style_options = {"научный": "научный", "популярный": "популярный", "деловой": "деловой"}
 #    style = style_options["научный"]
 #
 #    audience_options = {"эксперты": "экспертов в теме", "широкая публика": "широкой публики", "студенты": "студентов"}
 #    audience = audience_options["эксперты"]
 #
 #    references_format_options = {"APA": "APA", "ГОСТ": "ГОСТ", "MLA": "MLA"}
 #    references_format = references_format_options["ГОСТ"]

# # # Запуск основной функции
# if __name__ == "__main__":
#     main()
