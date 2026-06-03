


# 2026-06-03 topic

## 目的
PythonでローカルログをMarkdown表に整形する

## 対象環境

- 環境：Python
- 許可根拠：自分のPC、ローカルファイル
- 範囲：`labs/sandbox/python-log-formatter/`

## 前提
Python, git がインストールされていること

## 観察
入力ログの形式、出力Markdownの形式

## 試したこと

```text
ここにコマンドや操作概要を書く。秘密情報、フラグ、パスワードは書かない。
```

## 結果

```
git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        curricula/

nothing added to commit but untracked files present (use "git add" to track)
```

Python log

```
python3 --version
Python 3.14.4
```

```
pwd
/Users/togo/Repositories/security-lab-journal
```

```
mkdir -p labs/sandbox/python-log-formatter
```

## わかったこと

- `sys.stderr` は画面に出力するエラー

- parts[開始位置:終了位置:ステップ]
- `fields = {}` は辞書で、キー指定して `fields['command']`、値を表示できる。

## まだ不明なこと

例外でログの値に空白文字の処理
Markdownファイルへの書き込み

## 次に調べること


## 参考資料

-
