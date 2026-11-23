from app import app

def test_saude_responde_200_e_json():
    resp = app.test_client().get("/saude")
    assert resp.status_code == 200
    assert resp.is_json