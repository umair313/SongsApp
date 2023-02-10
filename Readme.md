# runing the app without docker compose

## Create volumes

### static files Volume
```bash
docker volume create spotify_static
```

### database volume
```bash
docker volume create spotify_postgres
```

## Build image
create the image with tag name `spotify`, using the Dockerfile in current context
```bash
docker build -t spotify .
```

## Running Containers

### Run Databse Container

```bash
docker run --name spotify_postgres \
              --network=spotify_network \
              -p 5432:5432 \
              -v spotify_postgres:/var/lib/postgresql/data \
              --env-file ./.postgres \
              postgres:latest
```

### run Django server
```bash
docker run -it --name spotify_django \
--network=spotify_network \
-p 8000:8000 \
-v $(pwd):/app \
-v spotify_static:/app/static \
--restart unless-stopped \
--env-file ./.env spotify \
bash -c "python manage.py runserver 0.0.0.0:8000"

```