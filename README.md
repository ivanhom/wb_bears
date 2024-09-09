# Проект чат-бота "WB Bears"

## 1. Настройка
### 1.1 Настройка после клонирования репозитория

Проект имеет следующую структуру:
- `backend` - папка для кода приложения Backend (FastAPI)
- `bot` - папка для кода приложения Telegram Bot
- `infra` - папка для настроек приложений и файлов развертывания инфраструктуры
- `requirements_style.txt` - файл с зависимостями для обеспечения единой 
  стилистики кода

В каждом приложении подготовлены ряд файлов для первоначальной настройки:
- `requirements.txt` - зависимости для основного кода
- `.pre-commit-config.yaml` - настройки для проверки и исправления 
  (частично) стилистики
- `pyproject.toml` - настройки для стилизатора `black`
- `setup.cfg` - настройки для `flake8` и `isort`

После клонирования репозитория устанавливаем и настраиваем 
виртуальное окружение для приложения, над функционалом которого работаем:

<details>
<summary>
Приложение Backend (FastAPI)
</summary>

1. Переходим в папку `/backend`
2. Устанавливаем и активируем виртуальное окружение
    - Для linux/mac:
      ```shell
      python3.11 -m venv .backend_venv
      source .backend_venv/bin/activate
      ```
    - Для Windows:
      ```shell
      py -3.11 -m venv .backend_venv
      .\.backend_venv\Scripts\activate
      ```
    В начале командной строки должно появиться название виртуального окружения `(.backend_venv)`

    Папка `.backend_venv` уже прописана в настройках git и стилизатора в 
    качестве исключения
3. Обновляем менеджер пакетов `pip` (по желанию)
    ```shell
    python3 -m pip install --upgrade pip
    ```
4. Устанавливаем основные зависимости и зависимости для стилистики
    ```shell
    pip install -r requirements.txt
    pip install -r ../requirements_style.txt
    ```
</details>


<details>
<summary>
Приложение Telegram Bot
</summary>

1. Переходим в папку `/bot`
2. Устанавливаем и активируем виртуальное окружение
    - Для linux/mac:
      ```shell
      python3.11 -m venv .bot_venv
      source .bot_venv/bin/activate
      ```
    - Для Windows:
      ```shell
      py -3.11 -m venv .bot_venv
      .\.bot_venv\Scripts\activate
      ```
    В начале командной строки должно появиться название виртуального окружения `(.bot_venv)`

    Папка `.bot_venv` уже прописана в настройках git и стилизатора в 
    качестве исключения
3. Обновляем менеджер пакетов `pip` (по желанию)
    ```shell
    python3 -m pip install --upgrade pip
    ```
4. Устанавливаем основные зависимости и зависимости для стилистики
    ```shell
    pip install -r requirements.txt
    pip install -r ../requirements_style.txt
    ```
</details>


### 1.2 Проверка и фиксация стилистики

Для проверки и фиксации стилей перед итоговым коммитом:
1. Проверяем что находимся в корневой папке приложения (`backend` или `bot`)
2. Выполняем команду
    ```shell
    pre-commit run --all-files
    ```
    Возможно потребуется запуск несколько раз.
    В итоге должен получиться примерно такой вывод:
    ```
    isort.............Passed
    black.............Passed
    flake8............Passed
    ```
### 1.3 Запуск приложений

Перед запуском приложений убеждаемся, что находимся в корневой папке 
приложения (`backend` или `bot`)

При запуске отладки в IDE дополнительно проверяем, что бы корнева папка 
приложения была установлена в качестве рабочего каталога.

Для VSCode файл запуска дебагера выглядит примерно так (при условии, что 
главный файл приложения называется `main.py`):
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Bot Debugger",
            "type": "debugpy",
            "request": "launch",
            "program": "main.py",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}/bot"
        },
        {
            "name": "Backend Debugger",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "main:app",
                "--reload"
            ],
            "jinja": true,
            "cwd": "${workspaceFolder}/backend"
        }
    ]
}
```

Для PyCharm установить параметр `Working directory`

Главное **ВСЕГДА** проверять, что активно **ПРАВИЛЬНОЕ** виртуальное окружение


## 1.4 Структура репозитория

```shell
wb_bears
│
├── backend/                            # Директория для бэкенда
│   ├── alembic/                        # Каталог для файлов Allembic
│   ├── api/                            # Каталог для API маршрутов
│   │   ├── api_v1/                     # Каталог для маршрутов API версии 1
│   │   │   ├── __init__.py             
│   │   │   └── product.py              # Эндпоинты для работы с товарами
│   │   ├── __init__.py                 
│   │   ├── utils.py                    # Вспомоготельные сервисы для работы API
│   │   └── validators.py               # Валидаторы для данных API
│   ├── core/                           # Основные настройки и конфигурации
│   │   ├── __init__.py                 
│   │   ├── base.py                     # Импорты моделей для Alembic
│   │   ├── config.py                   # Конфигурационные параметры backend
│   │   ├── constants.py                # Константы для приложения
│   │   └── db.py                       # Базовая модель для SQLAlchemy
│   ├── crud/                           # Операции CRUD
│   │   ├── __init__.py                 
│   │   ├── base.py                     # Базовые CRUD операции для СУБД
│   │   └── product.py                  # CRUD операции для модели Product
│   ├── models/                         # Модели для СУБД
│   │   ├── __init__.py                 
│   │   └── product.py                  # Модель Product для ДБ
│   ├── schemas/                        # Pydantic схемы
│   │   ├── __init__.py                 
│   │   └── product.py                  # Схемы для модели Product 
│   ├── tests/                          # Тесты бэкенд приложения
│   ├── .dockerignore                   # Файл игнорирования Docker
│   ├── .pre-commit-config.yaml         # Конфигурация для pre-commit hooks
│   ├── __init__.py                     
│   ├── alembic.ini                     # Файл конфигурации для Alembic
│   ├── docker-entrypoint.bash          # Скрипт входной точки для Docker
│   ├── Dockerfile                      # Файл описания образа Docker
│   ├── main.py                         # Главная точка входа для запуска FastAPI приложения
│   ├── pyproject.toml                  # Конфигурационный файл для black форматтера
│   ├── requirements.txt                # Зависимости для backend
│   └── setup.cfg                       # Конфигурационный файл для setuptools
│
├── bot/                                # Директория для Телеграм-бота
│   ├── tests/                          # Тесты Телеграм-бота      
│   ├── .dockerignore                   # Файл игнорирования Docker
│   ├── .pre-commit-config.yaml         # Конфигурация для pre-commit hooks
│   ├── __init__.py                     
│   ├── config.py                       # Конфигурационные параметры для Телеграм-бота
│   ├── constants.py                    # Константы для приложения
│   ├── docker-entrypoint.bash          # Скрипт входной точки для Docker
│   ├── Dockerfile                      # Файл описания образа Docker
│   ├── main.py                         # Главная точка входа для запуска Телеграм-бота
│   ├── pyproject.toml                  # Конфигурационный файл для black форматтера
│   ├── requirements.txt                # Зависимости для bot
│   ├── setup.cfg                       # Конфигурационный файл для setuptools
│   └── utils.py                        # Вспомоготельные сервисы для работы Телеграм-бота
│
├── infra/                              # Директория для инфраструктурных файлов
│   ├── env.example                     # Пример файла окружения
│   ├── docker-compose.yaml             # Файл описания сервисов Docker Compose
│   └── nginx.conf                      # Конфигурация веб-сервера Nginx
│
├── .gitignore                          # Файл, определяющий, какие файлы и директории игнорировать в Git
├── README.md                           # Файл документации проекта
└── requirements_style.txt              # Зависимости для стилей кода
```

Основные компоненты

1. *Backend (FastAPI)*
    * Предоставляет API для реализации бизнесс логики Telegram бота и доступ к БД проекта
    * Бекенд для работы с БД
2. *Bot (Telegram Specific)*
    * Содержит файлы описывающие логику работы Telegram бота, влючая handlers, кнопки, и вспомогательные функции

## 2. Запуск приложения
### 2.1 Запуск приложения локально

1. Создать `infra/.env` на основе `infra/.env.example` Указав валидные данные для подключения.

      ```ini
      # backend
      APP_TITLE=Парсер WB  # Имя бекенд приложения по-умолчанию
      APP_DESCRIPTION=Информация об остатках товаров с сайта wildberries.ru  # Описание бекенд приложения по-умолчанию

      # Postgresql database
      POSTGRES_USER=your_db_username  # Имя администратора БД
      POSTGRES_PASSWORD=your_db_password  # Пароль администратора БД
      POSTGRES_DB=wb_bears  # Имя БД 
      POSTGRES_SERVER=db  # Имя хоста подключения к БД
      POSTGRES_PORT=5432  # Номер порта подключения к БД
      # Строка подключения к БД, формируемая из переменных описанных выше
      DATABASE_URL=postgresql+asyncpg://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_SERVER}:${POSTGRES_PORT}/${POSTGRES_DB}
   
      # bot
      TELEGRAM_BOT_TOKEN='TELEGRAM_BOT_TOKEN'  # Токен Телеграм-бота
      BASE_URL=http://backend:8000  # Адрес сервера, на котором расположен бекенд
      BACKEND_API=api/v1/  # Путь к BASE_URL для доступа к API
      RATE_TIMEOUT=60  # Ограничение по времени на обработку запросов пользователя. По умолчанию 60 секунд
   
      # redis
      REDIS_HOST=redis  # Имя хоста подключения к Redis
      REDIS_PORT=6379  # Номер порта подключения к Redis
      # Строка подключения к Redis, формируемая из переменных описанных выше
      REDIS_URL=redis://${REDIS_HOST}:${REDIS_PORT}


      ```
2. Запустить `docker-compose up -d --build`.
3. Сервер будет доступен по адресу `http://localhost:8000`

### 2.2 Запуск приложения на удалённом сервере



## 3. Опробовать бот

Бот уже развёрнут и доступен в Телеграм по имени `WB Bears` или [@wb_bears_bot](https://t.me/wb_bears_bot)
Для начала работы выполните команду `/start`
При отправке боту артикула товара, в ответ будет получена собранная ботом информация об остатках товара на складах


## 4. Использованный стек технологий

	• Python 3.11
	• FastAPI 0.111
	• Pydantic 2.7
	• PostgreSQL 15
	• SQLAlchemy 2
    • Alembic 1.13
	• Aiogram 3.12
	• Docker, docker-compose
	• Celery
    • Redis 7
	• Unittest, Pytest (опционально)
