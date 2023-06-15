#POST rota test
def test_create_rota(client, mock_rota):
    res = client.post("/rotas/add", json=mock_rota)
    assert res.status_code == 200

#GET all rotas test
def test_get_all_rotas(client):
    res = client.get("/rotas/")
    assert res.status_code == 200

    expected_rota = [
        {
            "business_id":"test_business",
            "rota_content": "Assigned to user: test",
            "rota_end_date": "20-06-2023",
            "rota_id": 1,
            "rota_start_date": "15-06-2023",
        }
    ]
    assert res.json == expected_rota

#GET rota by id test
def test_get_rota_by_id(client):
    res = client.get("/rotas/1")
    assert res.status_code == 200 

#GET all rotas by business_id test
def test_get_all_rotas_by_business_id(client):
    res = client.get("/rotas/get/test_business")
    assert res.status_code == 200

#GET all rotas by WRONG business_id test
def test_get_all_rotas_by_wrong_business_id(client):
    res = client.get("/rotas/get/test_budiness")
    assert res.status_code == 404

#PUT rota test
def test_update_rota(client, mock_rota):
    #update content
    updated_rota = mock_rota.copy()
    updated_rota["rota_content"] = "Assigned to user5"

    #sending update
    res = client.put("/rotas/update/1", json=updated_rota)
    assert res.status_code == 200

    #making sure its updated
    res = client.get("/rotas/1")
    assert res.status_code == 200
    assert res.json["rota_content"] == "Assigned to user5"

#DELETE rota test
def test_delete_rota(client, mock_rota):
    #get rota
    res = client.get("/rotas/1", json=mock_rota)
    assert res.status_code == 200

    #delete rota
    res = client.delete("/rotas/delete/1")
    assert res.status_code == 200

    #making sure its deleted
    res = client.get("/rotas/1")
    assert res.status_code == 404
