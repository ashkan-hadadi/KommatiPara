from fastapi.testclient import TestClient

import backend

client = TestClient(backend)


def test_redirect_with_valid_url_with_optional_params():
    url = "https%3A%2F%2Fwww.aparat.com%2Fv%2F8u9DN"
    s = "W1gzvW3FQqrZtaaqhQStJA"
    page_url = f"http://0.0.0.0:8000/api/v1/redirect/?url={url}" \
               f"&result_index_in_page=4%20%20%20%20%20%20&page=1&tab" \
               f"=MEDIA&component=VideoCard&q=behnam%20%20%20%20%20%20" \
               f"&src=https://www.aparat.com/v/8u9DN&qsrc=null&s" \
               f"={s}"
    response = client.get(page_url, allow_redirects=False)
    assert response.status_code == 307


def test_redirect_with_valid_url_without_optional_params():
    url = "https%3A%2F%2Fwww.aparat.com%2Fv%2F8u9DN"
    s = "W1gzvW3FQqrZtaaqhQStJA"
    page_url = f"http://0.0.0.0:8000/api/v1/redirect/?url={url}&s={s}"
    response = client.get(page_url, allow_redirects=False)
    assert response.status_code == 307


def test_redirect_with_invalid_s():
    url = "https%3A%2F%2Fwww.aparat.com%2Fv%2F8u9DN"
    s = "INVALID_S"
    page_url = f"http://0.0.0.0:8000/api/v1/redirect/?url={url}" \
               f"&result_index_in_page=4%20%20%20%20%20%20&page=1&tab" \
               f"=MEDIA&component=VideoCard&q=behnam%20%20%20%20%20%20" \
               f"&src=https://www.aparat.com/v/8u9DN&qsrc=null&s" \
               f"={s} "
    response = client.get(page_url, allow_redirects=False)
    assert response.status_code == 403


def test_redirect_with_invalid_url():
    url = ""
    s = "INVALID_S"
    page_url = f"http://0.0.0.0:8000/api/v1/redirect/?url={url}" \
               f"&result_index_in_page=4%20%20%20%20%20%20&page=1&tab" \
               f"=MEDIA&component=VideoCard&q=behnam%20%20%20%20%20%20&" \
               f"src=https://www.aparat.com/v/8u9DN&qsrc=null&s" \
               f"={s} "
    response = client.get(page_url, allow_redirects=False)
    assert response.status_code == 400


def test_redirect_with_empty_s():
    url = "https%3A%2F%2Fwww.aparat.com%2Fv%2F8u9DN"
    page_url = f"http://0.0.0.0:8000/api/v1/redirect/?url={url}" \
               f"&result_index_in_page=4%20%20%20%20%20%20&page=1&tab" \
               f"=MEDIA&component=VideoCard&q=behnam%20%20%20%20%20%20" \
               f"&src=https://www.aparat.com/v/8u9DN&qsrc=null"
    response = client.get(page_url, allow_redirects=False)
    assert response.status_code == 422
