from app import db, APIKey

def test_api_key():
    key = APIKey.query.filter_by(key='22b0296cac97ed3c9913290cfa5a4d37').first()
    if key:
        print(f"Key: {key.key}")
        print(f"Description: {key.description}")
        print(f"Active: {key.active}")
    else:
        print("API key not found")

if __name__ == "__main__":
    test_api_key()
