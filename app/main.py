import json
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader

from app.data import PROFILE, SKILL_CATEGORIES, PROJECT_THEMES, TIMELINE_EVENTS, CERTIFICATIONS

app = FastAPI(title="Portfolio - 박문욱")

BASE_DIR = Path(__file__).resolve().parent

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

jinja_env = Environment(
    loader=FileSystemLoader(str(BASE_DIR / "templates")),
    autoescape=True,
)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    template = jinja_env.get_template("index.html")
    html = template.render(
        profile=PROFILE,
        skills=SKILL_CATEGORIES,
        projects=PROJECT_THEMES,
        timeline=TIMELINE_EVENTS,
        certifications=CERTIFICATIONS,
        skills_json=json.dumps(SKILL_CATEGORIES, ensure_ascii=False),
        projects_json=json.dumps(PROJECT_THEMES, ensure_ascii=False),
    )
    return HTMLResponse(content=html)


@app.get("/project/{project_id}", response_class=HTMLResponse)
async def project_detail(project_id: str):
    project = next((p for p in PROJECT_THEMES if p["id"] == project_id), None)
    if not project:
        return HTMLResponse(content="Not Found", status_code=404)
    template = jinja_env.get_template("project_detail.html")
    html = template.render(
        profile=PROFILE,
        project=project,
        skills=SKILL_CATEGORIES,
        skills_json=json.dumps(SKILL_CATEGORIES, ensure_ascii=False),
        projects_json=json.dumps([project], ensure_ascii=False),
    )
    return HTMLResponse(content=html)
