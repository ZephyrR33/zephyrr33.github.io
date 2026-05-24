from __future__ import annotations

import csv
import json
import os
import smtplib
from datetime import datetime
from email.message import EmailMessage
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


HOST = "127.0.0.1"
PORT = int(os.getenv("PORT", "8080"))
ADMIN_LOGIN = os.getenv("ADMIN_LOGIN", "rut123")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "miit2026")
RESULT_EMAIL = os.getenv("RESULT_EMAIL", "teacher@example.com")

ROOT = Path(__file__).resolve().parent
DB_DIR = ROOT / "db"
TESTS_FILE = DB_DIR / "tests.json"
RESULTS_FILE = DB_DIR / "results.json"
RESULTS_CSV = DB_DIR / "results.csv"


def ensure_db() -> None:
    DB_DIR.mkdir(exist_ok=True)
    if not TESTS_FILE.exists():
        source = ROOT / "tests.json"
        TESTS_FILE.write_text(source.read_text(encoding="utf-8") if source.exists() else "[]", encoding="utf-8")
    if not RESULTS_FILE.exists():
        RESULTS_FILE.write_text("[]", encoding="utf-8")


def read_json(path: Path, fallback):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return fallback


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def send_email(result: dict) -> bool:
    host = os.getenv("SMTP_HOST")
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    if not host or not user or not password or RESULT_EMAIL == "teacher@example.com":
        return False

    port = int(os.getenv("SMTP_PORT", "587"))
    sender = os.getenv("SMTP_FROM", user)
    message = EmailMessage()
    message["From"] = sender
    message["To"] = RESULT_EMAIL
    message["Subject"] = f"Результат теста: {result.get('studentName', 'Студент')}"
    message.set_content(result.get("resultText", ""), subtype="plain", charset="utf-8")

    with smtplib.SMTP(host, port, timeout=20) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(message)

    return True


class Handler(BaseHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Admin-Login, X-Admin-Password")
        super().end_headers()

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.end_headers()

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/tests":
            self.send_json(read_json(TESTS_FILE, []))
            return
        if path == "/api/health":
            self.send_json({"ok": True})
            return
        self.send_error(404)

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/tests":
            self.save_tests()
            return
        if path == "/api/results":
            self.save_result()
            return
        self.send_error(404)

    def save_tests(self) -> None:
        if not self.is_admin():
            self.send_json({"error": "unauthorized"}, status=401)
            return

        data = self.read_body()
        if not isinstance(data, list):
            self.send_json({"error": "tests payload must be an array"}, status=400)
            return

        write_json(TESTS_FILE, data)
        self.send_json({"ok": True, "count": len(data)})

    def save_result(self) -> None:
        result = self.read_body()
        if not isinstance(result, dict):
            self.send_json({"error": "result payload must be an object"}, status=400)
            return

        result["createdAt"] = datetime.now().isoformat(timespec="seconds")
        results = read_json(RESULTS_FILE, [])
        results.append(result)
        write_json(RESULTS_FILE, results)
        self.append_result_csv(result)

        email_sent = False
        try:
            email_sent = send_email(result)
        except Exception as exc:
            self.send_json({"ok": True, "saved": True, "emailSent": False, "emailError": str(exc)})
            return

        self.send_json({"ok": True, "saved": True, "emailSent": email_sent})

    def append_result_csv(self, result: dict) -> None:
        is_new = not RESULTS_CSV.exists()
        with RESULTS_CSV.open("a", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            if is_new:
                writer.writerow(["Дата", "ФИО", "Тест", "Тема", "Балл", "Верно", "Всего"])
            writer.writerow([
                result.get("createdAt", ""),
                result.get("studentName", ""),
                result.get("testTitle", ""),
                result.get("topic", ""),
                result.get("percent", ""),
                result.get("correctCount", ""),
                result.get("total", ""),
            ])

    def is_admin(self) -> bool:
        return (
            self.headers.get("X-Admin-Login") == ADMIN_LOGIN
            and self.headers.get("X-Admin-Password") == ADMIN_PASSWORD
        )

    def read_body(self):
        length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(length).decode("utf-8")
        return json.loads(raw or "null")

    def send_json(self, data, status: int = 200) -> None:
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    ensure_db()
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Backend started: http://{HOST}:{PORT}")
    print("Use ngrok or Cloudflare Tunnel to expose this address for GitHub Pages.")
    server.serve_forever()
