from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from toolkit import tokenize

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/tokenizer", response_class=HTMLResponse)
def read_page1(request: Request):
    return templates.TemplateResponse("tokenizer.html", {"request": request})


@app.post("/tokenize", response_class=HTMLResponse)
def tokenize_endpoint(request: Request, text: str = Form(...)):
    tokens = tokenize(text)
    return templates.TemplateResponse("tokenizer.html", {"request": request, "tokens": tokens})
