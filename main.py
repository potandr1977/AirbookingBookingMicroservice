import uvicorn
from fastapi import FastAPI

from di import engine
from routing.aircrafts import router as aircraft_routing
import webbrowser

app = FastAPI()

app.include_router(aircraft_routing)

if __name__ == "__main__":
    _port = 3001
    webbrowser.open(f'http://localhost:{_port}/docs', new = 2)
    uvicorn.run(app, port = _port)


