FROM gorialis/discord.py:master

WORKDIR /app
ADD . /app

EXPOSE 8881

RUN pip install -r requirements.txt

CMD ["python", "app.py"]