from __future__ import annotations


def _create_case(client, title: str) -> dict:
    response = client.post(
        "/cases",
        json={
            "title": title,
            "description": "Password reset did not restore access to the dashboard.",
        },
    )
    assert response.status_code == 201
    return response.json()


def test_list_jobs_returns_created_jobs(client):
    first = _create_case(client, "Cannot login to portal")
    second = _create_case(client, "Cannot login to dashboard")

    response = client.get("/jobs")
    assert response.status_code == 200

    jobs = response.json()
    job_ids = {job["id"] for job in jobs}
    assert first["job"]["id"] in job_ids
    assert second["job"]["id"] in job_ids
    assert all(job["status"] == "pending" for job in jobs)


def test_list_jobs_filters_by_status(client):
    created = _create_case(client, "Cannot login to portal")

    pending = client.get("/jobs", params={"status": "pending"})
    assert pending.status_code == 200
    assert any(job["id"] == created["job"]["id"] for job in pending.json())

    completed = client.get("/jobs", params={"status": "completed"})
    assert completed.status_code == 200
    assert completed.json() == []


def test_list_jobs_rejects_unknown_status(client):
    response = client.get("/jobs", params={"status": "nope"})
    assert response.status_code == 422
