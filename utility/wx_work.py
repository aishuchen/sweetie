import const
import requests

class Messenger:

    work_url = const.work_url

    def send(self, msg):
        self.request_work_url(msg)


    def request_work_url(self, msg):
        body = {
            "msgtype": "markdown",
            "markdown": {
                "content": msg,
                "mentioned_list": ["@all"]
            }
        }
        print(body)
        resp = requests.post(self.work_url, json=body)
        print(resp.status_code)
        print(resp.content)


messenger = Messenger()