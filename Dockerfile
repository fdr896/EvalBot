FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install pyTelegramBotAPI

COPY ./eval_bot.py /app/eval_bot.py

ENV TOKEN=$TOKEN
CMD ["python3", "/app/eval_bot.py"]