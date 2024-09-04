from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from pathlib import Path
import threading
import json

class EasyHost:
    def __init__(self,port=5000):
        self.app = FastAPI()
        self.routes = {}
        self.shared_dict = {}
        self.server = None
        self.port=port
        # Add API endpoints for shared_dict
        self.app.add_api_route("/get_shared_dict/{path:path}", self._api_get_shared_dict, methods=["GET"])
        self.app.add_api_route("/set_shared_dict/{path:path}", self._api_set_shared_dict, methods=["POST"])

    def set(self, route: str, html: str):
        if html:
            async def serve_html():
                content = Path(html).read_text()
                # Inject JavaScript for shared_dict operations
                script = """
                <script>
                async function getSharedDict(path) {
                    const response = await fetch(`/get_shared_dict/${path}`);
                    return await response.json();
                }
                async function setSharedDict(path, value) {
                    await fetch(`/set_shared_dict/${path}`, {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify(value)
                    });
                }
                </script>
                """
                content = content.replace('</head>', f'{script}</head>')
                return HTMLResponse(content=content, status_code=200)
            self.app.add_api_route(route, serve_html)
            self.routes[route] = html
        else:
            if route in self.routes:
                self.app.routes = [r for r in self.app.routes if r.path != route]
                del self.routes[route]

        if not self.server:
            self.server = threading.Thread(target=self._run_server)
            self.server.start()

    def _run_server(self):
        uvicorn.run(self.app, host="0.0.0.0", port=self.port)

    def get_shared_dict(self, path: str):
        keys = path.split('/')
        value = self.shared_dict
        for key in keys:
            if key in value:
                value = value[key]
            else:
                return None
        return value

    def set_shared_dict(self, dict_path: str, arg):
        keys = dict_path.split('/')
        current = self.shared_dict
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[keys[-1]] = arg

    async def _api_get_shared_dict(self, path: str):
        value = self.get_shared_dict(path)
        return JSONResponse(content=value)

    async def _api_set_shared_dict(self, path: str, request: Request):
        value = await request.json()
        self.set_shared_dict(path, value)
        return JSONResponse(content={"status": "success"})



def server():
    server1.set(route='/', file='0.png')
    while True:
        time.sleep(0.1)

def show():
    webview.create_window('My Browser with Pywebview', url)
    webview.start()

if __name__ == '__main__':
    import time
    import webview
    import threading
    port = 1234
    server1 = EasyHostV2(port=port)

    url = f'http://localhost:{port}/'
    threading.Thread(target=server).start()
    # Run the GUI-related code on the main thread
    show()
