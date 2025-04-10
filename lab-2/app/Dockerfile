FROM python:3.13-slim

RUN apt-get update && apt-get install --no-install-recommends -y curl \
        build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Download the latest installer, install it and then remove it
ADD https://astral.sh/uv/install.sh /install.sh
RUN chmod -R 755 /install.sh && /install.sh && rm /install.sh

# Set up the UV environment path correctly
ENV PATH="/root/.local/bin:${PATH}"

COPY . .

WORKDIR /

RUN uv sync --frozen

ENV PATH="/.venv/bin:{$PATH}"

# Expose the specified port for FastAPI
EXPOSE $PORT

# Start the application with Uvicorn in production mode, using environment variable references
CMD ["uvicorn", "main:app", "--log-level", "info", "--host", "0.0.0.0" , "--port", "8081"]