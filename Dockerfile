FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

WORKDIR /app

RUN git clone https://github.com/pytorch/fairseq

WORKDIR /app/fairseq

RUN pip install --editable .

WORKDIR /app

RUN pip install --no-cache-dir fastapi sentencepiece mosestokenizer
