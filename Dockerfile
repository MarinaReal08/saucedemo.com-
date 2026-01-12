FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Установка браузеров и зависимостей Playwright
RUN playwright install --with-deps

COPY . .

CMD ["pytest", "-v", "--alluredir=allure-results"]
