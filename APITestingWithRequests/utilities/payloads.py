def get_add_json_payload(isbn='bc424d', aisle='211'):
    payload = {
        "name": "book with nice long name",
        "isbn": isbn,
        "aisle": aisle,
        "author": "John foe"
    }
    return payload
