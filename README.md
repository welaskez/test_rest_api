# Тестовое задание: REST API приложение

## Описание
Этот проект реализует REST API для справочника организаций, зданий и видов деятельности

## Возможности
Приложение позволяет:

1. **Организации:**
   - Получать список всех организаций в конкретном здании.
   - Получать список всех организаций, относящихся к определенному виду деятельности.
   - Получать список организаций, расположенных в заданном радиусе или прямоугольной области относительно указанной точки на карте.
   - Получать информацию об организации по её идентификатору.
   - Искать организации по названию.

2. **Здания:**
   - Каждое здание включает адрес и географические координаты (широта и долгота).

3. **Виды деятельности:**
   - Организованы в древовидной структуре с поддержкой до 3 уровней вложенности (например, "Еда > Мясная продукция > Молочная продукция").

4. **Документация:**
   - API включает интерактивную документацию Swagger UI и Redoc.

## Технологии
- **FastAPI**
- **Pydantic**
- **SQLAlchemy**
- **Alembic**
- **Docker**
- **PostgreSQL**

## Предварительные требования
Перед запуском приложения убедитесь, что у вас установлены:

- Docker

## Инструкция по настройке
Следуйте этим шагам, чтобы настроить и запустить приложение:

### 1. Генерация пары ключей JWT
Для корректной работы JWT-токенов необходимо сгенерировать приватный и публичный ключ:

```bash
mkdir -p app/certs
openssl genrsa -out app/certs/jwt-private.pem 2048
openssl rsa -in app/certs/jwt-private.pem -outform PEM -pubout -out app/certs/jwt-public.pem
```

### 2. Настройка переменных окружения
Переименуйте файл `.env.example` в `.env`:

```bash
mv app/.env.example app/.env
```

### 3. Сборка и запуск приложения
Используйте Docker Compose для сборки и запуска приложения:

```bash
docker compose up --build -d
```

### 4. Заполнение базы данных
После запуска приложения заполните базу данных тестовыми данными:

```bash
docker exec -i postgres psql -U test_postgres -d test_postgres_db < data.sql
```

### 5. Доступ к документации API
После запуска приложения документация API доступна по следующим адресам:

- Swagger UI: [http://localhost:8080/docs](http://localhost:8080/docs)
- Redoc: [http://localhost:8080/redoc](http://localhost:8080/redoc)

### 6. Получение API ключа
Для работы с защищенными эндпоинтами:

1. Перейдите в `/api/v1/auth` в Swagger UI.
2. Введите имя пользователя и пароль для генерации API ключа.
3. Нажмите на кнопку "Authorize" в правом верхнем углу Swagger UI и введите сгенерированный API ключ.

## Дополнительные возможности
### Pre-commit хуки
Для поддержания качества кода интегрированы следующие pre-commit хуки:

- **Black**: Для форматирования кода.
- **Ruff**: В качестве линтера.
