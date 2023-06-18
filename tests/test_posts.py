#POST post test
def test_create_post(client, mock_post):
    res = client.post("/posts/add", json=mock_post)
    assert res.status_code == 200

#GET all posts test
def test_get_all_posts(client):
    res = client.get("/posts/")
    assert res.status_code == 200

    expected_post = [
        {
            "user_id": "test_user",
            "business_id": "business_id",
            "username": "test",
            "post_title": "first_post",
            "post_id": 1,
            "post_content":"post_content"
        }
    ]
    assert res.json == expected_post

#GET post by id test
def test_get_post_by_id(client):
    res = client.get("/posts/1")
    assert res.status_code == 200 

#PUT post test
def test_update_post(client, mock_post):
    #update content
    updated_post = mock_post.copy()
    updated_post["post_content"] = "Welcome to my first post!"

    #sending update
    res = client.put("/posts/update/1", json=updated_post)
    assert res.status_code == 200

    #making sure its updated
    res = client.get("/posts/1")
    assert res.status_code == 200
    assert res.json["post_content"] == "Welcome to my first post!"

#DELETE journal post test
def test_delete_post(client):
    #delete post
    res = client.delete("/posts/delete/1")
    assert res.status_code == 200

    #making sure its deleted
    res = client.get("/posts/1")
    assert res.status_code == 404
