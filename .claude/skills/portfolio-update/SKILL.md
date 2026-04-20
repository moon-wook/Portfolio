---
name: portfolio-update
description: "/portfolio-update 명령어로만 실행되는 스킬. 사용자가 프로젝트 디렉토리 경로를 전달하면 해당 디렉토리를 심층 분석하고, 외부 서비스(MLflow, MinIO, Langfuse, Prefect, PostgreSQL 등)를 자동 감지·조회하여, 5단계 구조의 포트폴리오 프로젝트를 자동 생성/업데이트한다."
---

# portfolio-update: 포트폴리오 프로젝트 추가/업데이트

`/portfolio-update <디렉토리 경로>` 형태로 호출한다. 디렉토리를 분석하여 포트폴리오에 5단계 구조로 등록한다.

## 포트폴리오 환경

- **위치**: `/home/wook/Portfolio/`
- **서버**: FastAPI + Jinja2, port 8081
- **프로젝트 데이터**: `app/data/projects.py` → `PROJECT_THEMES` 리스트
- **상세 페이지 템플릿**: `app/templates/project_detail.html`
- **이미지**: `app/static/images/`

---

## 실행 흐름

### 1단계: 프로젝트 디렉토리 심층 분석

모든 파일을 탐색하여 프로젝트를 완전히 이해한다.

**분석 대상:**
- 모든 `.py` 파일 — 코드 로직, 모델 아키텍처, 파이프라인
- `pyproject.toml`, `requirements.txt`, `package.json` — 기술 스택
- `README.md`, `docs/` — 설명
- `.env`, `config.py` — **외부 서비스 연결 정보**
- `docker-compose.yml` — 배포 구성
- `git log --oneline -20` — 개발 이력

### 2단계: 외부 서비스 자동 감지 및 조회

코드·설정 파일에서 외부 서비스를 **자동 감지**하고, 감지되면 직접 접속하여 데이터를 조회한다. 사용자가 별도 지시하지 않아도 감지 시 자동 수행한다.

**감지 방법:**
1. `.env` 파일 → 환경변수 키 패턴 매칭
2. `pyproject.toml` / `requirements.txt` → 패키지 의존성
3. `*.py` import 문 스캔
4. `docker-compose.yml` → 서비스 정의

| 서비스 | 감지 신호 | 조회 |
|--------|----------|------|
| **MLflow** | `mlflow` import, `MLFLOW_TRACKING_URI` env | REST API → 실험·run·메트릭·파라미터 |
| **MinIO** | `boto3` import, `AWS_`/`MINIO_`/`S3_` env | 버킷·데이터셋 버전 |
| **Langfuse** | `langfuse` import, `LANGFUSE_` env | 트레이스·메트릭 |
| **Prefect** | `prefect` import, `@flow`/`@task` 데코레이터 | 플로우 실행 이력 |
| **PostgreSQL** | `asyncpg`/`psycopg2` import, `POSTGRES_` env | 테이블 스키마·규모 |
| **MySQL** | `pymysql`/`mysql` import, `DB_HOST` env | 테이블 구조 |

감지된 서비스의 실제 데이터(모델 메트릭, 학습 이력, 데이터셋 규모 등)를 포트폴리오에 반영한다.

### 3단계: 사용자 확인

코드에서 파악하기 어려운 항목만 질문한다 (대화에서 이미 설명한 건 생략):
- 기간, 팀 구성, 기여도, 배경/동기, 스크린샷 URL

### 4단계: 스크린샷 캡쳐 (선택)

웹 URL + 로그인 정보가 제공된 경우만 Playwright로 캡쳐. 없으면 건너뜀.
저장: `app/static/images/{project_id}_*.png`

### 5단계: projects.py 업데이트

`PROJECT_THEMES` 리스트에 새 프로젝트 추가 (id 중복 시 교체).

---

## 데이터 구조

`app/data/projects.py`의 기존 프로젝트와 **동일한 형식**을 따른다.

```python
{
    "id": "project-id",
    "title": "프로젝트 제목",
    "subtitle": "English Subtitle",
    "color": "#hex",
    "icon": "material_icon_name",
    "period": "2025.02 ~ 현재",
    "team": "BE 2 / FE 1 / AI 1",
    "contribution": "AI 기여도 100%",

    "screenshots": [{"src": "/static/images/{id}_*.png", "caption": "캡션"}],

    "summary": "한 줄 요약",
    "role": "주요 역할",
    "tech_stack": {"카테고리": ["기술1", "기술2"]},
    "metrics": [{"value": "수치", "label": "라벨"}],  # 4개

    "background": {
        "pain_points": ["문제1", "문제2", "문제3"],
        "goals": ["목표1", "목표2", "목표3"],
        "before": [{"step": "설명", "icon": "icon"}],  # 4개
        "after": [{"step": "설명", "icon": "icon"}],    # 4개
    },

    "pipeline_steps": [{"icon": "i", "label": "l", "sub": "s", "color": "#hex"}],
    "preprocess_steps": [{"label": "l", "sub": "s", "color": "#hex"}],
    "architecture_mermaid": "",
    "preprocessing_mermaid": "",
    "technical_choices": [{"choice": "기술", "reason": "이유"}],
    "cnn_architecture": [{"layer": "l", "output": "o", "detail": "d"}],
    "key_works": [{"title": "t", "icon": "i", "color": "#hex", "desc": "d", "tags": []}],

    "challenges": [{"icon": "i", "title": "t", "problem": "p", "action": "a", "result": "r", "color": "#hex"}],

    "results": [{"value": "v", "label": "l", "sub": "s"}],  # 4개
    "model_evolution": [],  # 모델 비교 있으면 채움
    "model_comparison_note": "",
    "lessons": ["교훈1", "교훈2", "교훈3"],
}
```

## 작성 원칙

**최소 텍스트, 최대 시각 요소.**
- 모든 텍스트 필드: 한 문장 이내
- key_works: 제목 + 한줄 desc + 4태그
- challenges C/A/R: 각 1줄
- 한국어 기본, 기술 용어만 영문

## 컬러: 기존과 겹치지 않게. `projects.py`에서 사용 현황 확인.

## 최종 확인

```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:8081/
curl -s -o /dev/null -w "%{http_code}" http://localhost:8081/project/{id}
curl -s http://localhost:8081/ | grep -c "자세히 보기"
```
