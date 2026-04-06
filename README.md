# Code Docker Image

This repository contains a simple Python application containerized with Docker.

## Files

- `code.py` - The main application (prints incrementing numbers every 10 seconds)
- `Dockerfile` - Docker image configuration
- `.dockerignore` - Files to exclude from Docker build context
- `docker-compose.yml` - Docker Compose configuration for easy deployment

## Usage

### Build the Docker Image

```bash
docker build -t code-app .
```

### Run the Container

```bash
docker run -d --name code-app code-app
```

### View Container Logs

```bash
docker logs -f code-app
```

### Using Docker Compose

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop and remove
docker-compose down
```

## Application Behavior

The application prints incrementing numbers starting from 0, increasing by 10 every 10 seconds:
```
0
10
20
30
...
```