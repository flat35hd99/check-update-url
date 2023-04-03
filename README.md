- `SLACK_WEBHOOK_URL`と`TARGET_URL`を`.env`ファイルで指定する。
- 内部で`.previous_data`ファイルを作成して、前回の実行と比較している。
- minicondaのbase環境にrequestsが入っていると想定されている。
- cronを使うときは`crontab -e`して、開いたエディタで下記のようにする。(5分おき)

```
*/5 * * * * /path/to/entrypoint.sh > /path/to/job.log 2>&1
```
