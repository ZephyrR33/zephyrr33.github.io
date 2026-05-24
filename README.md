# Система тестирования Академии Водного транспорта

Учебный сайт для создания и прохождения тестов на любую тему.

## Вариант 1: только GitHub Pages

Студенты открывают:

```text
index.html
```

Админ-панель:

```text
admin.html
```

Временный доступ:

```text
Логин: rut123
Пароль: miit2026
```

На чистом GitHub Pages новые тесты не могут сами записываться на сайт, потому что GitHub Pages является статическим хостингом. Для этого режима после создания тестов нужно нажать `Скачать tests.json` и заменить файл `tests.json` в репозитории.

## Вариант 2: GitHub Pages + база на своем ПК

Этот режим подходит, если сайт должен отработать один день, а тесты и результаты должны храниться на вашем компьютере.

1. На своем ПК запустите backend:

```powershell
python backend_server.py
```

2. Сервер будет доступен локально:

```text
http://127.0.0.1:8080
```

3. Чтобы GitHub Pages смог обратиться к вашему ПК, сделайте временную публичную HTTPS-ссылку через ngrok, Cloudflare Tunnel или SSH-туннель.

Пример для ngrok:

```powershell
ngrok http 8080
```

Если `ngrok` не установлен, можно попробовать вариант без установки через встроенный `ssh`:

```powershell
ssh -o ServerAliveInterval=60 -R 80:localhost:8080 nokey@localhost.run
```

При первом запуске терминал может спросить подтверждение подключения. Введите:

```text
yes
```

После подключения в терминале появится публичная ссылка вида:

```text
https://something.lhr.life
```

4. Скопируйте HTTPS-ссылку, например:

```text
https://abc-123.ngrok-free.app
```

5. В файле `config.js` укажите ее:

```js
window.APP_CONFIG = {
  API_BASE_URL: 'https://abc-123.ngrok-free.app',
  RESULT_EMAIL: 'teacher@example.com',
};
```

6. Загрузите обновленный `config.js` на GitHub.

Пока ваш ПК, backend и туннель работают, все студенты будут видеть общие тесты, а результаты будут сохраняться на вашем компьютере.

## Где хранится база

После запуска backend создаст папку `db`:

```text
db/tests.json
db/results.json
db/results.csv
```

`tests.json` хранит тесты, `results.json` и `results.csv` хранят результаты студентов.

## Отправка результата на почту

Если `API_BASE_URL` пустой, сайт откроет почтовый клиент студента через `mailto`.

Если работает `backend_server.py`, результат отправляется на ваш ПК. Автоматическая отправка письма тоже возможна, но нужно указать SMTP-настройки почты перед запуском backend:

```powershell
$env:RESULT_EMAIL="your-mail@example.com"
$env:SMTP_HOST="smtp.example.com"
$env:SMTP_PORT="587"
$env:SMTP_USER="your-mail@example.com"
$env:SMTP_PASSWORD="password-or-app-password"
python backend_server.py
```

Для Gmail, Яндекс, Mail.ru обычно нужен пароль приложения, а не обычный пароль от аккаунта.

## Локальная проверка сайта

Для правильной загрузки `tests.json` лучше запускать сайт через локальный сервер:

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

После этого откройте:

```text
http://127.0.0.1:4173/index.html
http://127.0.0.1:4173/admin.html
```
