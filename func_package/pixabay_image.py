# 検索結果が0でないことのチェック
def check_result_is_0(response):
    """
    Check the Search Result is 0 or not.
    If the result is 0, Return True. If not, return False.
    If status code is not 200, raise Exception error.
    Pass Response Object as the argument.
    """
    if response.status_code == 200:
        response_dict = response.json()

        if response_dict['totalHits'] == 0:
            return True
        else:
            return False
    else:
        raise Exception


# Responseオブジェクトから画像URLを抽出
def extract_image_url(response):
    """
    Extract Image URL from Response Object.
    Return image URL as a string.
    Arg: response object.
    """
    response_dict = response.json()
    image_url = response_dict['hits'][0]['webformatURL']
    return image_url


# Pixabay検索
def search_pixabay(requests, pixabay_api_key, keyword):
    """
    Search in Pixabay with given keyword.
    1st arg: request object.
    2nd arg: pixabay_api_key.
    3rd arg: Search Keyword.
    """
    
    params = {
        "key": pixabay_api_key,
        "q": keyword
    }
    response = requests.get("https://pixabay.com/api/", params=params)
    return response