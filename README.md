- `SLACK_WEBHOOK_URL`と`TARGET_URL`を指定する。
- 内部で`.previous_data`ファイルを作成して、前回の実行と比較している。
- cronを使うときは下記のようにする。(5分おき)

```
*/5 * * * * username /path/to/entrypoint.sh
```