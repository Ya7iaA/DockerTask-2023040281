FROM alpine

WORKDIR /app

COPY app.py .

RUN apk add --no-cache python3 py3-pip

CMD ["python", "app.py"]