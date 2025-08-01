FROM python:3.13.5-slim AS builder
COPY requirements.txt .

RUN apt-get update && \
    apt-get install --no-install-recommends -y clang libjpeg62-turbo-dev libwebp-dev python3-dev zlib1g-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -U setuptools pip && \
    pip install --no-cache-dir --user -r requirements.txt


FROM python:3.13.5-alpine
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY src/ src/

ENV PATH=/root/.local/bin:$PATH
CMD ["python", "-m", "src"]