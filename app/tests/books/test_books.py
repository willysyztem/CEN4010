
def test_mocked_book(mock_book):
    mock_book.id = 12345

    assert mock_book.to_json()[id] == 12345