# Hidden Service

Simple FastAPI for exposing a Tor hidden service.

```bash
git clone https://github.com/neozmmv/hidden-service
```

```bash
python -m venv env
```

```bash
./env/Scripts/activate
```

```bash
docker compose up -d
```

```bash
pip install -r requirements.txt
```

```bash
fastapi dev main.py --host 0.0.0.0
```

For mounting tor-data correctly on Linux:

```bash
sudo chown -R $(whoami):$(whoami) ./docker/tor-data
```

```bash
sudo chmod -R 700 ./docker/tor-data/hidden_service
```

To see the hostname:
```bash
sudo cat ./docker/tor-data/hidden_service/hostname
```
