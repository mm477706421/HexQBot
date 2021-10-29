import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models

def trans_to_zh(msg):
    try:
        cred = credential.Credential("AKIDobw3IIqxJpBejip8Vp05yKfu8LPKdfCU", "B6C6mNEwlWHo55pIUQ6Ylgz5vUt6B6rS")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)

        req = models.TextTranslateRequest()
        params = {
            "SourceText": msg,
            "Source": "auto",
            "Target": "zh",
            "ProjectId": 0
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextTranslate(req)
        return [True,str(json.loads(resp.to_json_string())['TargetText'])]

    except TencentCloudSDKException as err:
        print(err)

def trans_to_en(msg):
    try:
        cred = credential.Credential("AKIDobw3IIqxJpBejip8Vp05yKfu8LPKdfCU", "B6C6mNEwlWHo55pIUQ6Ylgz5vUt6B6rS")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)

        req = models.TextTranslateRequest()
        params = {
            "SourceText": msg,
            "Source": "auto",
            "Target": "en",
            "ProjectId": 0
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextTranslate(req)
        return [True,str(json.loads(resp.to_json_string())['TargetText'])]

    except TencentCloudSDKException as err:
        print(err)

def trans_to_ja(msg):
    try:
        cred = credential.Credential("AKIDobw3IIqxJpBejip8Vp05yKfu8LPKdfCU", "B6C6mNEwlWHo55pIUQ6Ylgz5vUt6B6rS")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)

        req = models.TextTranslateRequest()
        params = {
            "SourceText": msg,
            "Source": "auto",
            "Target": "ja",
            "ProjectId": 0
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextTranslate(req)
        return [True,str(json.loads(resp.to_json_string())['TargetText'])]

    except TencentCloudSDKException as err:
        print(err)

def trans_to_ko(msg):
    try:
        cred = credential.Credential("AKIDobw3IIqxJpBejip8Vp05yKfu8LPKdfCU", "B6C6mNEwlWHo55pIUQ6Ylgz5vUt6B6rS")
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tmt.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)

        req = models.TextTranslateRequest()
        params = {
            "SourceText": msg,
            "Source": "auto",
            "Target": "ko",
            "ProjectId": 0
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextTranslate(req)
        return [True,str(json.loads(resp.to_json_string())['TargetText'])]

    except TencentCloudSDKException as err:
        print(err)
