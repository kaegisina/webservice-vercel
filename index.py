from fastapi import FastAPI, Request
from pyproj import Transformer


app = FastAPI()
lv95 = "EPSG:2056"
wgs84 = "EPSG:4326"

@app.middleware("http")
async def addcors(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*" #Mit Stern = alle können darauf zugreifen
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World",
            "version": "1.0"}

@app.get("/api/list")
def liste():
    return {"liste": ["Apfel", "Banane", "Birne", "Ananas", "Mango", "Orange"]}


@app.get("/api/add")
def addiere(a: int, b: int):
    return {"sum": a+b}
# http://localhost:3000/api/add?a=5&b=7 Eingabe um dies auszuführen

@app.get("/api/transformiere")
async def transformiere(E: float =0, N: float =0):
    t2 = Transformer.from_crs(lv95, wgs84)
    return {"KoordinatenWGS84": t2.transform(E, N)
    }
