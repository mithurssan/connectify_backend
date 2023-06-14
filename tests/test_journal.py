#GET all journal entries test
def test_get_all_entrys(client):
    res = client.get("/entries/")
    assert res.status_code == 200

#POST journal entry test
def test_create_entry(client, mock_journal_entry):
    res = client.post("/entries/add", json=mock_journal_entry)
    assert res.status_code == 200

#GET journal entry by id test
def test_get_entry_by_id(client):
    res = client.get("/entries/1")
    assert res.status_code == 200 

#PUT journal entry test
def test_update_entry(client, mock_journal_entry):
    #update content
    updated_entry = mock_journal_entry.copy()
    updated_entry["entry_content"] = "Hello me, this is my first journal entry! I will continue posting!"

    #sending update
    res = client.put("/entries/update/1", json=updated_entry)
    assert res.status_code == 200

    #making sure its updated
    res = client.get("/entries/1")
    assert res.status_code == 200
    assert res.json["entry_content"] == "Hello me, this is my first journal entry! I will continue posting!"

#DELETE journal entry test
def test_delete_entry(client, mock_journal_entry):
    #get entry
    res = client.get("/entries/1", json=mock_journal_entry)
    assert res.status_code == 200

    #delete entry
    res = client.delete("/entries/delete/1")
    assert res.status_code == 200

    #making sure its deleted
    res = client.get("/entries/1")
    assert res.status_code == 404
