
FROM python:3.10

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 80

COPY ./ /

CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]
