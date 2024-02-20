FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY consumer.py .
COPY init.sh .

RUN chmod +x init.sh

CMD ["./init.sh"]