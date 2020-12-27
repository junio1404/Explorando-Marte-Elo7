FROM python:3
COPY . /app
RUN pip install sys && pip install math
WORKDIR /app
CMD python Projeto_elo_7.py
