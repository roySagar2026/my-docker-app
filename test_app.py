from app import app


def test_home_says_i_am_here():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert b"I am here" in res.data


def test_health():
    res = app.test_client().get("/health")
    assert res.get_json() == {"status": "ok"}
