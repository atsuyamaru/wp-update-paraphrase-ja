# OpenAIレスポンスオブジェクトをテキスト情報へ
def extract_obj_text(response_obj):
    """
    Extract the text only. From the object returned from OpenAI.
    Return the text as strings.
    """
    response_obj_text = response_obj.choices[0].text.lstrip()
    return response_obj_text

### 長い文章から一部分を抽出
# 前半1/2を抽出
def extract_former(paragraph):
    """
    Extract the first half part of the passed paragraph.
    Return the strings as the extracted part.
    """
    first_end_index = len(paragraph)//2
    extracted_former = paragraph[:first_end_index]
    return extracted_former


# 後半1/2を抽出
def extract_latter(paragraph):
    """
    Extract the last of a thirds part of the passed paragraph.
    Return the strings as the extracted part.
    """
    last_start_index = len(paragraph)//2
    last_end_index = len(paragraph)
    extracted_latter = paragraph[last_start_index:last_end_index]
    return extracted_latter


# 文章から中央部分1/3のみ抽出
def extract_middle(paragraph):
    """
    Extract the middle part of the passed paragraph.
    Return the strings as the extracted part.
    """

    middle_start_index = len(paragraph)//3
    middle_end_index = len(paragraph)//3*2
    extracted_middle = paragraph[middle_start_index:middle_end_index]
    return extracted_middle


### GPTへの実行指示
#  英語テキストをパラフレーズ
def paraphrase_en(openai, input_paragraph):
    """
    Paraphrase the english text randomly. And make it longer.
    Pass the openai object as the 1st argument, pass the input paragraph as the 2nd argument.
    Return the string text extracted from the openai response object.
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Paraphrase randomly the below text, and makes it longer more than 5 times of its length, keep the tone lively, exclamation marks are often used. If URL is contained, keep the url as it is.:\n{input_paragraph}",
        temperature=0.8,
        max_tokens=2000,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = extract_obj_text(response)
    return response_text


# 抽出された文章の中央部分から、続きの文章を書かせる
def write_continue(openai, text):
    """
    Write the continue contents from the passed text.
    The text is expected as the extracted middle part from the whole paragraph.
    Pass the openai object as the 1st argument, pass the input text as the 2nd argument.
    Return the string text extracted from the openai response object.
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Write the continue following comma text, with a polite tone but much more lively. Exclamation marks are often used. And not needed greetings and introduction. The word count is at least 1000 words. Be careful, usually the beginning and ending parts are missing some words. : {text}",
        temperature=0.8,
        max_tokens=2000,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = extract_obj_text(response)
    return response_text


# 日本語の文末表現を統一し、語調を明るく元気に
def tone_consistent(openai, input_paragraph):
    """
    Make the paragraph consistent and change the tone more lively.
    Passing paragraph is desirable to be short, at least not long. Consider splitting the text to pass.
    Pass the openai object as the 1st argument, pass the input text as the 2nd argument.
    Return the string text extracted from the openai response object.
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Make the end of Japanese expression following after the colon(:) to be consistent, the same level of politeness. But turn the tone into more lively, use exclamation mark sometimes. And make the content length double longer. The beginning and ending may miss some phrase. In that case, create or change its part to be sound more naturally. The Output also should be the Japanese.:\n{input_paragraph}",
        temperature=0.9,
        max_tokens=2000,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = extract_obj_text(response)
    return response_text


# HTMLで整形
def format_html(openai, input_paragraph):
    """
    Format the input paragraph as a HTML.
    Pass the openai object as the 1st argument, pass the input text as the 2nd argument.
    Return the string text extracted from the openai response object.
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Format the following Japanese text into HTML. You should wrap a group of sentence with <p> tag, and create original headings for each with <h2>.If you find any URLs, you should format those url with <a> tag and anchor text you create.: \n{input_paragraph}",
        temperature=0.9,
        max_tokens=2000,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = extract_obj_text(response)
    return response_text


# HTML形式の文章からタイトルを生成
def create_title_from_html(openai, input_paragraph):
    """
    Create the title from the contents. Creation works whichever the passed paragraph is JA or EN.
    Pass the openai object as the 1st argument, pass the input paragraph as the 2nd argument.
    Return the string text extracted from the openai response object.
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Create the title of the contents below. Make the tone lively. The output should be the text, not containing html tag, and be at least 28 words in Japanese.:\n{input_paragraph}",
        temperature=0.7,
        max_tokens=2000,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = extract_obj_text(response)
    return response_text


# 日本語タイトルをリライト, リフレーズ
def paraphrase_title(openai, input_paragraph):
    """
    Paraphrase the Japanese post title. Basically only changing the position of a each keyword the title contains.
    Pass the openai object as the 1st argument, pass the input paragraph as the 2nd argument.
    Return the string text extracted from the openai response object.
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Paraphrase the title of the Japanese title below. Especially, change the position of the word beginning and ending, and make the original part shorter. And add some your orisinal phrase in it. Turn its tone into more lively. The output also should be the Japanese.:\n{input_paragraph}",
        temperature=0.6,
        max_tokens=2000,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = extract_obj_text(response)
    return response_text


# 英文から代表キーワードを1つ抽出or生成
def extract_keyword(openai, input_title):
    """
    Extract the special one keyword from the passed text.
    If it is not found, GPT will create the keyword.
    Pass the openai object as the 1st argument, pass the input paragraph as the 2nd argument.
    Return the string text extracted from the openai response object.
    """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Extract the one special keyword from the text below. If you cannot represent in the given text, you can generate one special word on your own.:\n{input_title}",
        temperature=0.8,
        max_tokens=2000,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = extract_obj_text(response)
    return response_text