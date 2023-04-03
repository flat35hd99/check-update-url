import requests
import os

SLACK_WEBHOOK_URL = os.environ.get("SLACK_WEBHOOK_URL", "")
TARGET_URL = os.environ.get("TARGET_URL", "")

def main():
    if has_been_updated():
        notify()

# ファイルがない場合 => False
# ファイルがあって、前回の記録がある。前回の記録と同じ => False
# ファイルがあって、前回の記録がある。前回の記録と違う => True
def has_been_updated():
    filename = ".previous_data"

    present_data = requests.get(TARGET_URL).content

    # ファイルがない場合、現在のコンテンツを書き込み、
    # 更新がなかったとして返す。
    if not os.path.isfile(filename):
        with open(filename, mode="wb") as f:
            f.write(present_data)
        return False

    with open(filename, mode="rb") as f:
        previous_data = f.read()

    with open(filename, mode="wb") as f:
        f.write(present_data)

    if present_data == previous_data:
        return False

    return True

def notify():
    message = f"<{TARGET_URL}|STAR64 Model-A 8GB Single Board Computer's page> has been updated."
    requests.post(SLACK_WEBHOOK_URL, json={"text": f"{message}"})

if __name__ == "__main__":
    main()
