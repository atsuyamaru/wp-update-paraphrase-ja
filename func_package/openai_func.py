# OpenAIレスポンスオブジェクトをテキスト情報へ
def extract_obj_text(response_obj):
    """
    Extract the text only. From the object returned from OpenAI.
    Return the text as strings.
    """
    response_obj_text = response_obj.choices[0].text.lstrip()
    return response_obj_text


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
        prompt=f"Write the continue text following the comma(:) text, with a polite tone but lively. Exclamation marks are often used. And not needed greetings and introduction. The output word count should be at least 400 words. :\n {text}",
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
        prompt=f"Make the end of Japanese expression following after the colon(:) to be consistent, the same level of politeness. But turn the tone into more lively, use exclamation mark sometimes. And make the content length double longer. The beginning and ending may miss some phrase. In that case, create or change its part to be sound more naturally. The Output text also should be Japanese.:\n{input_paragraph}",
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
    Format the input Japanese paragraph as a HTML.
    Pass the openai object as the 1st argument, pass the input text as the 2nd argument.
    Return the string text extracted from the openai response object.
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Format the following Japanese text into HTML. You should wrap a group of Japanese sentence with <p> tag, and create original Japanese headings for each with <h2>, sometimes <h3> depending on the context, following HTML markup rule. If you find any URLs, you should format those url with <a> tag and Japanese anchor text you create.: \n{input_paragraph}",
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