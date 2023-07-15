FROM python:3.9-slim-bullseye

WORKDIR /workspace

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt \
    && pip install -e .

VOLUME /workspace/outputs

CMD maccas_train