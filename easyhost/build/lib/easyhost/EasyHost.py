from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
from pathlib import Path
import threading
from typing import Dict, Optional

class EasyHost:
    _servers: Dict[int, FastAPI] = {}
    _shared_dicts: Dict[int, dict] = {}

    def __init__(self, port: int):
        self.port = port
        self.app = self._get_or_create_app(port)

    def _get_or_create_app(self, port: int):
        if port not in EasyHost._servers:
            app = FastAPI()
            EasyHost._servers[port] = app
            EasyHost._shared_dicts[port] = {}

            @app.get("/get_shared_dict/{path:path}")
            async def api_get_shared_dict(path: str):
                value = self.get_shared_dict(path)
                return JSONResponse(content=value)

            @app.post("/set_shared_dict/{path:path}")
            async def api_set_shared_dict(path: str, request: Request):
                value = await request.json()
                self.set_shared_dict(path, value)
                return JSONResponse(content={"status": "success"})

            threading.Thread(target=lambda: uvicorn.run(app, host="0.0.0.0", port=port), daemon=True).start()

        return EasyHost._servers[port]

    def set(self, route: str, file: Optional[str] = None):
        if file:
            async def serve_file():
                file_path = Path(file)
                if file_path.exists():
                    return FileResponse(file_path)
                return JSONResponse(content={"error": "File not found"}, status_code=404)
            self.app.add_api_route(route, serve_file)
        else:
            # Remove route if file and html are both empty
            self.app.routes = [r for r in self.app.routes if r.path != route]

    def get_shared_dict(self, path: str):
        if self.port not in EasyHost._shared_dicts:
            EasyHost._shared_dicts[self.port] = {}

        keys = path.split('/')
        value = EasyHost._shared_dicts[self.port]
        for key in keys:
            if key in value:
                value = value[key]
            else:
                return None
        return value

    def set_shared_dict(self, dict_path: str, arg):
        if self.port not in EasyHost._shared_dicts:
            EasyHost._shared_dicts[self.port] = {}

        keys = dict_path.split('/')
        current = EasyHost._shared_dicts[self.port]
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        current[keys[-1]] = arg

