"""Модуль для запуска простого HTTP-сервера."""

import http.server
import socketserver

PORT = 8000

class TestMe():
    """Класс для тестирования портов и базовой логики."""

    def take_four(self):
        """Возвращает тестовое число 4."""
        return 4
    def port(self):
        """Возвращает текущий порт сервера."""
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
