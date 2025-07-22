# TGBotGoroskop

📆 Telegram-бот, предоставляющий актуальные гороскопы по знакам зодиака.  
Простой в использовании, легко разворачивается и адаптируется под любые нужды.

## Возможности

- Получение гороскопов по 12 знакам зодиака
- Поддержка команд Telegram бота
- Асинхронная работа (на базе `aiogram`)
- Удобный шаблон для добавления новых источников
- Минималистичный, быстрый и расширяемый

## Использование

1. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

2. Создайте файл `.env` со своим токеном:
    ```
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    ```

3. Запустите бота:
    ```bash
    python bot.py
    ```
## Скрипт для быстрой развертки в Docker
```
#!/bin/bash

set -euo pipefail

# === Цвета ===
YELLOW='\033[1;33m'
GREEN='\033[1;32m'
BLUE='\033[1;34m'
RED='\033[1;31m'
RESET='\033[0m'

# === Очистка окружения от ошибочных bash-функций ===
if env | grep -q 'BASH_FUNC_'; then
    echo -e "${YELLOW}[WARN]${RESET} Обнаружены остаточные bash-функции в окружении."
    echo -e "${BLUE}[INFO]${RESET} Это не связано с ошибкой скрипта, а вызвано конфликтом импортируемой функции ${YELLOW}_file${RESET}."
    echo -e "${BLUE}[FIX]${RESET} Выполняется попытка автоматической очистки переменных окружения..."

    env | grep BASH_FUNC_ | cut -d= -f1 | while read -r fn; do
        unset "$fn" 2>/dev/null || true
    done

    echo -e "${GREEN}[OK]${RESET} Переменные ${YELLOW}BASH_FUNC_*${RESET} очищены. Продолжаем выполнение."
    echo
fi

# === Загрузка .env файла, если он есть ===
if [[ -f .env ]]; then
    set -a
    source .env
    set +a
    echo -e "${GREEN}[OK]${RESET} Файл ${BLUE}.env${RESET} загружен."
else
    echo -e "${YELLOW}[WARN]${RESET} Файл .env не найден. Используются только переменные окружения."
fi

# === Конфигурация ===
TAG="tg_goroskop"
TOKEN_ENV_VAR="TELEGRAM_BOT_TOKEN"

# === Проверка переменной ===
if [[ -z "${!TOKEN_ENV_VAR:-}" ]]; then
  echo -e "${RED}[ERROR]${RESET} Переменная окружения ${YELLOW}$TOKEN_ENV_VAR${RESET} не установлена."
  echo "Установите её в .env или передайте вручную:"
  echo -e "  ${BLUE}$TOKEN_ENV_VAR=your_token ./test.sh${RESET}"
  exit 1
fi

# === Проверка и сборка образа ===
if ! docker image inspect "$TAG" > /dev/null 2>&1; then
  echo -e "${BLUE}[INFO]${RESET} Образ ${YELLOW}$TAG${RESET} не найден. Выполняется сборка..."
  docker build -t "$TAG" .
  echo -e "${GREEN}[OK]${RESET} Образ ${YELLOW}$TAG${RESET} собран."
fi

# === Удаление старых контейнеров ===
containers=$(docker ps -a --filter "ancestor=$TAG" --format "{{.ID}}")

if [[ -n "$containers" ]]; then
  echo -e "${BLUE}[INFO]${RESET} Удаление старых контейнеров..."
  for container in $containers; do
    docker rm -f "$container" && echo -e "${GREEN}Удалён:${RESET} $container"
  done
else
  echo -e "${BLUE}[INFO]${RESET} Старые контейнеры не найдены."
fi

# === Запуск нового контейнера ===
echo -e "${BLUE}[INFO]${RESET} Запуск нового контейнера..."
docker run -d \
  --name "${TAG}_bot" \
  --network=host \
  -e "$TOKEN_ENV_VAR=${!TOKEN_ENV_VAR}" \
  "$TAG"

echo -e "${GREEN}[OK]${RESET} Бот запущен. Активные контейнеры:"
docker ps --filter "ancestor=$TAG"
```
# Dockerfile

```
# Используем минимальный образ Python
FROM python:3.12-slim

# Создаем рабочую директорию
WORKDIR /app

# Обновляем систему и устанавливаем инструменты
RUN apt-get update && \
    apt-get install -y --no-install-recommends git sed && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*

# Создаем виртуальное окружение и обновляем pip
RUN python3 -m venv /app/venv && \
    /app/venv/bin/pip install --upgrade pip

# Устанавливаем зависимости из requirements.txt
COPY requirements.txt /app/requirements.txt
RUN /app/venv/bin/pip install --no-cache-dir -r /app/requirements.txt

# Клонируем репозиторий с GitHub
RUN git clone --depth 1 https://github.com/tiko34/TGBotGoroskop.git /app/TGBotGoroskop

# Указываем Python из виртуального окружения для запуска основного скрипта
ENTRYPOINT ["/app/venv/bin/python"]
CMD ["/app/TGBotGoroskop/main.py"]
```

