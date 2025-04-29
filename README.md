```markdown
# Hacker-News Crawler 

Small weekend project built as part of a coding exercise for Stack Builders.  
It scrapes the first 30 posts on [news.ycombinator.com](https://news.ycombinator.com) and lets you explore them through a tiny FastAPI web app.

<p align="center">
  <img src="docs/screenshot.png" width="720" alt="UI screenshot"/>
</p>

---

## Table of contents
1. [Why & what](#why--what)
2. [Quick start](#quick-start)
3. [Features](#features)
4. [Project layout](#project-layout)
5. [Architecture notes](#architecture-notes)
6. [Running tests](#running-tests)
7. [Docker](#docker)
8. [Performance](#performance)
9. [Future work](#future-work)
10. [Author](#author)
11. [License](#license)

---

## Why & what

* **Goal.** Demonstrate the ability to write a clean, test-driven web crawler and expose its results through a browser-friendly UI.  
* **Stack.**  
  - Python 3.12  
  - FastAPI + Jinja2 (UI)  
  - httpx + BeautifulSoup 4 (scraping)  
  - pytest / requests-mock (tests)  
  - Poetry (dependency management)  

The app performs two custom filters required by the exercise:

| Filter | Rule | Sort order |
|--------|------|------------|
| **Long titles** | title has **more than 5** words | descending by **comments** |
| **Short titles** | title has **≤ 5** words | descending by **points** |

“Words” are tokens separated by spaces; punctuation such as dashes is ignored  
→ `This is – a self-explained example` counts as **5 words**.

---

## Quick start

### Local (Poetry)

```bash
git clone https://github.com/your-handle/hn-crawler.git
cd hn-crawler
poetry install -n                # creates venv + installs deps
poetry run uvicorn src.main:app --reload
# → http://localhost:8000
```

### Makefile shortcuts

```bash
make run        # same as the uvicorn command above
make lint       # Ruff static checks
make test       # run all tests
```

### Docker

```bash
docker compose up --build        # http://localhost:8000
```

---

## Features

* **Scrapes once, caches in-memory** – no hammering Hacker News on every refresh.
* **Fast filter switching** via query-string (`?filter=long|short`).
* Clean responsive table, zero JS apart from the native `<select>` reload.
* **100 % test coverage** for business rules (word count + filters).
* Fully typed code (PEP 695), docstrings, and a strict Ruff config keep the codebase tidy.

---

## Project layout

```
src/
└── hn_crawler/
    ├── domain/         # entities (Entry)
    ├── infra/          # HackerNewsScraper → external world
    ├── application/    # use-cases, filters, caching
    ├── interfaces/     # FastAPI routes + HTML template
    └── main.py         # uvicorn entry-point
templates/
tests/
docs/                   # screenshots, diagrams (not tracked by tests)
```

---

## Architecture notes

* **Hexagonal / Clean-ish**: core rules live in `domain` + `application`; everything else is a plug-in.  
* `infra.scraper` is the only module that knows HN’s HTML structure.  
* Simple in-process cache (`functools.lru_cache`) ⇒ constant-time response after first hit.  
* All I/O with timeouts; the app won’t hang if HN is slow.

```text
┌──────────────┐
│   FastAPI    │  UI / REST
└──────┬───────┘
       │
       ▼
┌──────────────────────────┐
│  application.service     │  decides filter, memoises scrape
└──────┬─────────┬─────────┘
       │filters  │cache
       ▼         │
   domain.Entry  │
                 ▼
          infra.HackerNewsScraper
```

---

## Running tests

```bash
poetry run pytest -q
```

`tests/conftest.py` injects a static copy of HN’s front page so the suite doesn’t depend on the network.

---

## Docker

```bash
docker compose up --build
# hot-reload is enabled for local hacking
```

Multi-stage build, final image ~70 MB.

---

## Performance

* First request = ~120 ms on my laptop (HTML download + parse).  
* Subsequent requests = <3 ms thanks to L1 cache.  
* CPU / memory footprint negligible (<40 MB RSS).

---

## Future work

* Redis cache (TTL-backed) for multi-process deployments.  
* Switch scraper to `httpx.AsyncClient` + asyncio gather for multiple pages.  
* Add pagination & search.  
* Replace Jinja2 page reloads with HTMX for snappier UX.  
* Emit structured logs (`structlog`) to observe latency histograms.

---

## Author

**Andrés Núñez** — Full-stack Developer  
andres.nunez@example.com · Quito, EC