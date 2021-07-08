FROM python:3.8

COPY . /bot/
WORKDIR /bot

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["bot.py"]
