import json
import os
import requests

import deepl
import openai

from func_package.deepl_func import translate_2en, translate_2ja
from func_package.openai_func import paraphrase_en, format_html, extract_middle, write_continue, tone_consistent, extract_former, extract_latter, paraphrase_title

### 認証まわり
# DeepLの認証とオブジェクトの生成
deepl_api_key = os.environ['DEEPL_API_KEY']
translator = deepl.Translator(deepl_api_key)

# OPEN AIオブジェクトに認証キー情報をもたせる
openai_api_key = os.environ['OPENAI_API_KEY']
openai.api_key = openai_api_key


### パラフレーズされたテキストの作成
# 日本語のオリジナル記事のIDをループで取得
post_id = 11

# DeepLで日本語から英語に翻訳
with open(f'original_ja_contents/{post_id}') as f:
    content_text = f.read()
translated_en = translate_2en(translator, content_text)

# OPEN AIで英語文章をパラフレーズ
paraphrased_text = paraphrase_en(openai, translated_en)

# OPEN AIで続きの文章を生成
extracted_text = extract_middle(paraphrased_text)
continue_text = write_continue(openai, extracted_text)

# DeepLでそれぞれを英語から日本語へ再翻訳
retranslated_ja_1 = translate_2ja(translator, paraphrased_text)
retranslated_ja_2 = translate_2ja(translator, continue_text)

# OpenAIで文末とトーンを変換: 細かく分割して実行
p_1 = tone_consistent(openai ,extract_former(retranslated_ja_1))
p_2 = tone_consistent(openai ,extract_latter(retranslated_ja_1))
p_3 = tone_consistent(openai ,extract_latter(retranslated_ja_2))
p_4 = tone_consistent(openai ,extract_latter(retranslated_ja_2))

# OpenAIでそれぞれをHTML形式のテキストへフォーマット
response_html_1 = format_html(openai, p_1)
response_html_2 = format_html(openai, p_2)
response_html_3 = format_html(openai, p_3)
response_html_4 = format_html(openai, p_4)
response_html_whole = response_html_1 + '<br>' + response_html_2 + '<br>' + response_html_3 + '<br>' + response_html_4

# OpenAIでオリジナル日本語タイトルからタイトルを生成
with open(f'./original_ja_title/{post_id}') as f:
    title_original = f.read()
title_created = paraphrase_title(openai ,title_original)

# テスト
print(title_created)
print('\n------')
print(response_html_whole)