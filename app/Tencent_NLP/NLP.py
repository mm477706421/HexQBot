import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models

def charNLP(msg):
    try:
        cred = credential.Credential("", "")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        req = models.ChatBotRequest()
        params = {
            "Query": msg
        }
        req.from_json_string(json.dumps(params))

        resp = client.ChatBot(req)
        print(str(json.loads(resp.to_json_string())['Reply']))
        return [True,str(json.loads(resp.to_json_string())['Reply'])]

    except TencentCloudSDKException as err:
        print(err)
