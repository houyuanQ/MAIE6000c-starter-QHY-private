# Week 3 Submission — Individual Readiness Lab

## Student information

- Name:
- Student ID:
- Repository: https://github.com/houyuanQ/MAIE6000c-starter-QHY-private
- Checkpoint tag: `w03-readiness`
- Commit SHA:

## 1. What I changed

Added `GET /jobs` so jobs can be listed, with an optional `status` filter.

Before this change the API could create a job and read one job by id, but it could not list jobs. After this change:

- `GET /jobs` returns jobs newest first, default limit 20, maximum 100.
- `GET /jobs?status=pending` returns only jobs in that status. Allowed values are `pending`, `claimed`, `completed`, and `failed`.
- `GET /jobs?status=nope` returns 422.
- `GET /jobs/{job_id}` is unchanged.

## 2. Files touched

- `services/api/app/main.py`
- `tests/integration/test_jobs_list.py`
- `submissions/week03/README.md`

## 3. How I verified it

- `pytest -q tests/unit tests/integration` — 7 passed (4 existing tests plus 3 new job-list tests).
- New tests cover listing created jobs, filtering by `pending` and `completed`, and rejecting an unknown status with 422.

## 4. Known limitations or notes

- The list is read-only. It does not claim, retry, or reprioritize jobs.
- `limit` below 1 or above 100 returns 422, matching `GET /cases`.
- Failed jobs are still not retried when the AI service comes back. That existing worker limitation is unchanged.

## 5. AI Use Statement

- Tool: Cursor, using Grok 4.7.
- Used to read the Week 3 lab brief, inspect the starter API, and implement `GET /jobs` plus its integration tests and this note.
- I checked the diff against the starter and re-ran the unit and integration tests. The 7 passing tests match the behaviour described above. The tag `w03-readiness` has not been created yet.
