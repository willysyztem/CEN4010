
def test_mocked_author(mock_author):
    mock_author.id = 12345

    assert mock_author.to_json()[id] == 12345