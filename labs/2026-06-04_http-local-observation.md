# 2026-06-04 topic

## 目的

ローカルHTTP通信のrequest/responseを読む。

## 対象環境

- 対象環境：自分のPC、127.0.0.1、Python標準HTTPサーバ。
- 許可根拠：自分のローカル環境。

## 前提

Git、Python、Curlコマンドが使用できること

## 観察

リクエストの結果：`200 OK` と `404` の差。

## 試したこと

指定フォルダ内でHTMLファイルを作成し、Pythonで該当フォルダを実行先に指定して、HTTPサーバーを起動した

```bash
mkdir -p labs/sandbox/http-demo
printf '<!doctype html><title>Phase0 HTTP</title><h1>Hello HTTP</h1>\n' > labs/sandbox/http-demo/index.html
python3 -m http.server 8000 --bind 127.0.0.1 --directory labs/sandbox/http-demo
```

対象のローカルポートに `curl` コマンドを実行

```bash
curl -v http://127.0.0.1:8000/
curl -v http://127.0.0.1:8000/hello
```

## 結果

実行結果

200

```text
*   Trying 127.0.0.1:8000...
* Connected to 127.0.0.1 (127.0.0.1) port 8000
> GET / HTTP/1.1
> Host: 127.0.0.1:8000
> User-Agent: curl/8.7.1
> Accept: */*
>
* Request completely sent off
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: SimpleHTTP/0.6 Python/3.14.4
< Date: Thu, 04 Jun 2026 06:57:28 GMT
< Content-type: text/html
< Content-Length: 61
< Last-Modified: Thu, 04 Jun 2026 06:57:15 GMT
<
<!doctype html><title>Phase0 HTTP</title><h1>Hello HTTP</h1>
* Closing connection
```

404
```
*   Trying 127.0.0.1:8000...
* Connected to 127.0.0.1 (127.0.0.1) port 8000
> GET /hello HTTP/1.1
> Host: 127.0.0.1:8000
> User-Agent: curl/8.7.1
> Accept: */*
>
* Request completely sent off
* HTTP 1.0, assume close after body
< HTTP/1.0 404 File not found
< Server: SimpleHTTP/0.6 Python/3.14.4
< Date: Thu, 04 Jun 2026 07:20:51 GMT
< Connection: close
< Content-Type: text/html;charset=utf-8
< Content-Length: 460
<
<!DOCTYPE HTML>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <style type="text/css">
            :root {
                color-scheme: light dark;
            }
        </style>
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: 404</p>
        <p>Message: File not found.</p>
        <p>Error code explanation: 404 - Nothing matches the given URI.</p>
    </body>
</html>
* Closing connection
```

## わかったこと

- これは何か：HTTPのリクエストとレスポンス
- なぜ必要か：実行側と受け取り側の双方の詳細情報が出力できることで問題発生時に調査できる
- 手元でどう確認したか：ログを一行ずつ読み、理解した。
- 200は正常、404はページ無しは前から知っている

## まだ不明なこと

JavaScriptが絡むとどれくらい複雑になるのか、どこまで改竄できるのか？

## 次に調べること

もっと、実装したり、キャプチャーしたり分析してみたい。

## 参考資料

カリキュラム
