# Docker Compose Production Deployment

This project supports image-based deployment for multi-server reuse.

## 1. Build and push image (CI or build machine)

```bash
docker build -t your-registry/time-service:2026.04.23-1 .
docker push your-registry/time-service:2026.04.23-1
```

## 2. Prepare server

```bash
git clone <your-repo-url> /srv/time-service
cd /srv/time-service
cp .env.example .env
```

Edit `.env`:

- `APP_IMAGE=your-registry/time-service:2026.04.23-1`
- External DB mode: set `MYSQL_HOST` to your MySQL host (not `127.0.0.1` unless DB is on same host).

## 3. Start service (external MySQL recommended)

```bash
cd /srv/time-service
docker compose -f docker-compose.prod.yml pull
docker compose -f docker-compose.prod.yml up -d
```

## 4. Optional: start local MySQL in same compose

Use only for simple/single-machine setups.

```bash
cd /srv/time-service
# If using local-db profile, MYSQL_HOST in .env should be mysql
docker compose -f docker-compose.prod.yml --profile local-db up -d
```

## 5. Rollback

Change only `APP_IMAGE` in `.env` to an old tag, then:

```bash
docker compose -f docker-compose.prod.yml pull
docker compose -f docker-compose.prod.yml up -d
```

## 6. Nginx reverse proxy (example)

```nginx
server {
    listen 80;
    server_name your.domain.or.ip;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
