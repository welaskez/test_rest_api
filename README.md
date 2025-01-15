# Тестовое задание

### Помимо основных требований тестового были интегрированы pre-commit хуки

### Перед запуском необходимо выполнить несколько шагов

1. Нужно создать папку с приватным и публичном ключом для корректной работы JWT-токенов
```shell
mkdir app/certs
openssl genrsa -out app/certs/jwt-private.pem 2048
openssl rsa -in app/certs/jwt-private.pem -outform PEM -pubout -out app/certs/jwt-public.pem
```

2. Затем нужно переименовать .env.example в .env
```shell
mv .env.example .env
```

4. После можно запускать приложение
```shell
docker compose up --build
```













