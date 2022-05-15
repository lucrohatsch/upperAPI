FROM python:3.10.4-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /src

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip wheel\
    && pip install -r requirements.txt

COPY ./src /src

EXPOSE 4040

CMD [ "uvicorn", "app:app", "--env-file", ".env", "--host", "0.0.0.0","--port", "4040"]