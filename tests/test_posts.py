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
            "business_id": "business_id",
            "post_content":"post_content",
            "post_downvotes": 0,
            "post_id": 1,
            "post_title": "first_post",
            "post_upvotes": 0,
            "user_id": "test_user",
            "username": "test",
        }
    ]
    assert res.json == expected_post

#GET post by id test
def test_get_post_by_id(client):
    res = client.get("/posts/1")
    assert res.status_code == 200 

#GET post by business id test
def test_get_post_by_business_id(client):
    res = client.get("/posts/get/business_id")
    assert res.status_code == 200

    expected_post = [
        {
            "business_id": "business_id",
            "post_content":"post_content",
            "post_downvotes": 0,
            "post_id": 1,
            "post_title": "first_post",
            "post_upvotes": 0,
            "user_id": "test_user",
            "username": "test",
        }
    ]
    assert res.json == expected_post

#PUT post test
def test_update_post(client, mock_post):
    #update content
    updated_post = mock_post.copy()
    updated_post["post_content"] = "Welcome to my first post!"

    #sending update
    res = client.patch("/posts/update/1", json=updated_post)
    assert res.status_code == 200

    #making sure its updated
    res = client.get("/posts/1")
    assert res.status_code == 200
    assert res.json["post_content"] == "Welcome to my first post!"

#PUT upvote post test
def test_upvote_post(client):
    res = client.patch("/posts/update/1/upvote")
    assert res.status_code == 200

#PUT cancel upvote post test
def test_cancel_upvote_post(client):
    res = client.patch("/posts/update/1/cancel_upvote")
    assert res.status_code == 200

#PUT downvote post test
def test_downvote_post(client):
    res = client.patch("/posts/update/1/downvote")
    assert res.status_code == 200

#DELETE journal post test
def test_delete_post(client):
    #delete post
    res = client.delete("/posts/delete/1")
    assert res.status_code == 200

    #making sure its deleted
    res = client.get("/posts/1")
    assert res.status_code == 404
