# wp-update-paraphrase-ja

Create a Japanese paraphrased text from WordPress posts and Update (Replace).

## 下記サービスを利用します

- OpenAI (GPT3)
- DeepL

## 各ファイルの動作説明

### post_wp_paraphrased_ja2ja.py

テキストファイルに記載された WordPress 投稿の日本語本文を一旦英語に変換し、その英語をパラフレーズ（同一の意味内容を保ったまま言い回しや構成を変更）し、一部テキストを追加したうえで、再度日本語に再翻訳します。  
再翻訳した日本語テキストを見出し付きの HTML 形式で出力。  
別途、投稿タイトルを格納したテキストファイルから元のタイトルを読み取り、GPT によってパラフレーズしたタイトルを出力します。

出力した HTML とタイトルを、WordPress の REST API 経由で WordPress の投稿に上書き保存し、公開状態にします。

### post_wp_thumbnail_ja_pixabay.py

## 使用のための準備

### 必要な外部ライブラリのインストール

下記の外部ライブラリを利用します。

#### post_wp_paraphrased_ja2ja.py

- BeautifulSoup
- requests
- deepl
- openai

#### post_wp_thumbnail_ja_pixabay.py

- requests
- PIL
- deepl
- openai

### 必要な API キー、ログイン情報

You need 3 Info as below:

- OpenAI (GPT3): API key
- DeepL : API key
- WordPress: admin user's username and password

### 環境変数およびログイン情報の設定

OpenAI の API キーは環境変数"OPENAI_API_KEY"に設定してください。  
Deep の API キーは環境変数"DEEPL_API_KEY"に設定してください。  
WordPress のログイン情報は wp_login_info.json に下記のように設定してください。

```
{
"username": "your_username",
"password": "your_password",
"wp_root_url": "https://your_wordpress_site_url.com"
}
```
