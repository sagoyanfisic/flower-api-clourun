FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8080

COPY . /app
RUN pip3 install -r requirements/local.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
