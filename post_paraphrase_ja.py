import json
import os
import re
import requests
import time

from bs4 import BeautifulSoup
import deepl
import openai

from func_package.deepl_func import translate_2en, translate_2ja
from func_package.extract_text import extract_former_half, extract_latter_half, extract_first_thirds, extract_middle_thirds, extract_last_thirds
from func_package.openai_func import paraphrase_en, format_html, write_continue, paraphrase_title
from func_package.wp_api_func import update_with_html

### 認証まわり
# DeepLの認証とtranslatorオブジェクトの生成
deepl_api_key = os.environ['DEEPL_API_KEY']
translator = deepl.Translator(deepl_api_key)

# OPEN AIオブジェクトに認証キー情報をもたせる
openai.api_key = os.environ['OPENAI_API_KEY']

# WordPressのログイン情報を読み込み
with open('wp_login_info.json', 'r') as f:
    wp_login_info = json.load(f)
username = wp_login_info['username']
password = wp_login_info['password']


### パラフレーズされたテキストの作成
# 投稿IDをループで取得
with open('./wp-post-ids.txt') as f:
    post_ids = f.read()
post_ids_list = post_ids.split(' ')

for post_id in post_ids_list:
    # DeepLで日本語から英語に翻訳
    with open(f'original_ja_contents/{post_id}') as f:
        content_text = f.read()
    translated_en = translate_2en(translator, content_text)

    # 3分割して、OPEN AIで英語文章をパラフレーズ
    translated_en_1 = extract_first_thirds(translated_en)
    translated_en_2 = extract_middle_thirds(translated_en)
    translated_en_3 = extract_last_thirds(translated_en)

    paraphrased_text_1 = paraphrase_en(openai, translated_en_1)
    time.sleep(5)
    paraphrased_text_2 = paraphrase_en(openai, translated_en_2)
    time.sleep(5)
    paraphrased_text_3 = paraphrase_en(openai, translated_en_3)
    time.sleep(4)

    # OPEN AIで続きの文章を生成
    last_part = extract_latter_half(paraphrased_text_3)
    continue_text = write_continue(openai, last_part)

    # DeepLでそれぞれを英語から日本語へ再翻訳
    retranslated_ja_1 = translate_2ja(translator, paraphrased_text_1)
    time.sleep(3)
    retranslated_ja_2 = translate_2ja(translator, paraphrased_text_2)
    time.sleep(3)
    retranslated_ja_3 = translate_2ja(translator, paraphrased_text_3)
    time.sleep(3)
    retranslated_ja_4 = translate_2ja(translator, continue_text)

    # それぞれを2分割し、OpenAIでHTML形式のテキストへフォーマット
    response_html_1 = format_html(openai, extract_former_half(retranslated_ja_1))
    time.sleep(4)
    response_html_2 = format_html(openai, extract_latter_half(retranslated_ja_1))
    time.sleep(4)

    response_html_3 = format_html(openai, extract_former_half(retranslated_ja_2))
    time.sleep(4)
    response_html_4 = format_html(openai, extract_latter_half(retranslated_ja_2))
    time.sleep(4)

    response_html_5 = format_html(openai, extract_former_half(retranslated_ja_3))
    time.sleep(4)
    response_html_6 = format_html(openai, extract_latter_half(retranslated_ja_3))
    time.sleep(4)

    response_html_7 = format_html(openai, extract_former_half(retranslated_ja_4))
    time.sleep(4)
    response_html_8 = format_html(openai, extract_latter_half(retranslated_ja_4))
    time.sleep(4)

    response_html_whole = response_html_1 + '<br>' + response_html_2 + '<br>' + \
        response_html_3 + '<br>' + response_html_4 + '<br>' + \
        response_html_5 + '<br>' + response_html_6 + '<br>' + \
        response_html_7 + '<br>' + response_html_8 + '<br>'

    # OpenAIでオリジナル日本語タイトルからタイトルを生成
    with open(f'./original_ja_title/{post_id}') as f:
        title_original = f.read()
    title_created = paraphrase_title(openai ,title_original)


    ### WordPressへのUpdateを実行
    # エンドポイントを定義
    base_url = "https://livernet.jp/wp-json/wp/v2/posts"
    update_url = f"{base_url}/{post_id}"

    ## Updateの実行
    json_html_body = {
        "title": title_created,
        "content": response_html_whole,
        "status": "publish"
    }

    # 実行結果を出力
    returned_post_obj = update_with_html(requests, update_url, username, password, json_html_body)
    print(f"Success! Post ID: {returned_post_obj['id']}; URL:{returned_post_obj['link']}\nTitle: {returned_post_obj['title']['rendered']}\n------")