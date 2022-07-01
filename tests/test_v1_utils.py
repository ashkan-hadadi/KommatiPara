from urllib.parse import unquote
from app.core.utils.secure_link import generate_secure_hash


def test_generate_secure_hash_valid_s():
    url = "https%3A%2F%2Fwww.aparat.com%2Fv%2F8u9DN"
    url = unquote(url)
    s = "W1gzvW3FQqrZtaaqhQStJA"
    assert generate_secure_hash(url, expire=4764998504, secret='Zarebin') == s


def test_generate_secure_hash_empty_url_and_s():
    url = ""
    url = unquote(url)
    s = ""
    assert generate_secure_hash(url, expire=4764998504, secret='Zarebin') != s


def test_generate_secure_hash_with_invalid_secret():
    url = "https%3A%2F%2Fwww.aparat.com%2Fv%2F8u9DN"
    url = unquote(url)
    s = "W1gzvW3FQqrZtaaqhQStJA"
    assert generate_secure_hash(url, expire=4764998504, secret='INVALID') != s


def test_generate_secure_hash_with_invalid_expire():
    url = "https%3A%2F%2Fwww.aparat.com%2Fv%2F8u9DN"
    url = unquote(url)
    s = "W1gzvW3FQqrZtaaqhQStJA"
    assert generate_secure_hash(url, expire=100, secret='INVALID') != s
