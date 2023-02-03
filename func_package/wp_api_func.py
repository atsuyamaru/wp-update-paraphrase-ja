# # 独自の例外処理: API Access Failure
# class AccessError(Exception):
#     print('API Access Failure.')


def update_with_html(requests, target_url, username, password, json_html_body):
    """
    Execute WordPress PATCH API Access to update the post with HTML.
    The URL should contain the post ID.
    If success, return post JSON object.
    If failure to access API, raise AccessError.
    Pass the requests object as the 1st argument.
    JSON body needs to be contained at least post title, content, status.
    """
    response = requests.post(target_url, auth=(username, password), json=json_html_body)
    if response.status_code == 200:
        post_obj = response.json()
        return post_obj
    else:
        print (f'AccessError:{target_url}')