# PhiModel.py

import json
import urllib.request

# PhiModel 클래스
class PhiModel:
    def __init__(self, endpoint, api_key):
        self.endpoint = endpoint
        self.api_key = api_key

    # 피드백 생성
    def generate_feedback_text(self, prompt):
        data = {
            "input_data": {
                "input_string": [{"role": "user", "content": prompt}],
                "parameters": {"temperature": 0.7, "top_p": 1, "max_new_tokens": 4096}
            }
        }
        body = str.encode(json.dumps(data))
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + self.api_key}
        req = urllib.request.Request(self.endpoint, body, headers)
        
        try:
            response = urllib.request.urlopen(req)
            result_json = json.loads(response.read().decode('utf-8'))
            feedback = result_json.get("output", "Failed to generate feedback.")
        except urllib.error.HTTPError as error:
            feedback = f"Failed to call the model. Error code: {error.code}"
        
        return feedback