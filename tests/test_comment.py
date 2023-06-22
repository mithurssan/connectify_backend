#POST comment test
def test_create_comment(client, mock_comment):
    res = client.post("/comments/add", json=mock_comment)
    assert res.status_code == 200

#GET all comments test
def test_get_all_comments(client):
    res = client.get("/comments/")
    assert res.status_code == 200

    expected_comment = [
        {
            "comment_content": "First comment!",
            "comment_id": 1,
            "comment_username": "test",
            "post_id": 1,
            "user_id": "test_user",
        }
    ]
    assert res.json == expected_comment

#GET comment by id test
def test_get_comment_by_id(client):
    res = client.get("/comments/1")
    assert res.status_code == 200 

#GET comment by post
def test_get_comment_by_post(client):
    res = client.get("/comments/post/1")
    assert res.status_code == 200

#PUT comment test
def test_update_comment(client, mock_comment):
    #update content
    updated_comment = mock_comment.copy()
    updated_comment["comment_content"] = "Hello, this is my first comment!"

    #sending update
    res = client.put("/comments/update/1", json=updated_comment)
    assert res.status_code == 200

    #making sure its updated
    res = client.get("/comments/1")
    assert res.status_code == 200
    assert res.json["comment_content"] == "Hello, this is my first comment!"

#DELETE comment test
def test_delete_comment(client, mock_comment):
    #get comment
    res = client.get("/comments/1", json=mock_comment)
    assert res.status_code == 200

    #delete comment
    res = client.delete("/comments/delete/1")
    assert res.status_code == 200

    #making sure its deleted
    res = client.get("/comments/1")
    assert res.status_code == 404
