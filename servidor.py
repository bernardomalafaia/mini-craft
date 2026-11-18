import http.server
import socketserver
import webbrowser
import os


PORT = 8000


# Garante que o servidor vai servir a pasta atual
os.chdir(os.path.dirname(os.path.abspath(__file__)))


Handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor rodando em http://localhost:{PORT}")
    # Abre direto o index.html
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    httpd.serve_forever()




