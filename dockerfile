# Use small official Python image
FROM python:3.11-slim

WORKDIR /app
ENV PYTHONUNBUFFERED=1

# Install build deps needed by some DB adapters
RUN apt-get update \
  && apt-get install -y --no-install-recommends gcc libmysqlclient-dev \
  && rm -rf /var/lib/apt/lists/*

# copy requirements first (leverage caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . /app

# expose Uvicorn port
EXPOSE 8000

# Wait-for-db script will run before starting the app
CMD ["sh", "-c", "python wait_for_db.py && uvicorn main:app --host 0.0.0.0 --port 8000"]
