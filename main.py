from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from toolkit import tokenize_text, pos_tag_text, chunk_text

templates = Jinja2Templates(directory="templates")
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/tokenizer", response_class=HTMLResponse)
def read_tokenizer(request: Request):
    return templates.TemplateResponse("tokenizer.html", {"request": request})


@app.get("/pos_tagger", response_class=HTMLResponse)
def read_pos_tag(request: Request):
    return templates.TemplateResponse("pos_tagger.html", {"request": request})


@app.get("/chunker", response_class=HTMLResponse)
def read_chunker(request: Request):
    return templates.TemplateResponse("chunker.html", {"request": request})


@app.post("/chunk", response_class=HTMLResponse)
def chunk_endpoint(request: Request, text: str = Form(...)):
    entities = chunk_text(text)
    return templates.TemplateResponse("chunker.html", {"request": request, "entities": entities})


@app.post("/pos_tag", response_class=HTMLResponse)
def pos_tag_endpoint(request: Request, text: str = Form(...)):
    pos_tags = pos_tag_text(text)
    return templates.TemplateResponse("pos_tagger.html", {"request": request, 'pos_tags': pos_tags})


@app.post("/tokenize", response_class=HTMLResponse)
def tokenize_endpoint(request: Request, text: str = Form(...)):
    tokens = tokenize_text(text)
    return templates.TemplateResponse("tokenizer.html", {"request": request, "tokens": tokens})
