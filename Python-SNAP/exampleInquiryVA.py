from nicepay import nicepaySNAP
import datetime

nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUTklDRVZBMDIyIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJUTklDRVZBMDIyIiwiZXhwIjoiMjAyMy0wNi0wMlQwMToxMzoxOVoifQ==.MZO-9NvdkPDpWqcl3zdWgImXxszUtViNeTll5LQJiy8="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "1af9014925cab04606b2e77a7536cb0d5c51353924a966e503953e010234108a"
nicepaySNAP.setXPartnerID = "TNICEVA022"
nicepaySNAP.setXExternalID = "OrdNo" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setBody = {
        "partnerServiceId": "",
        "customerNo": "",
        "virtualAccountNo": "1021492800000666",
        "inquiryRequestId": "12345",
        "totalAmount": {
            "value": "10000.00",
            "currency": "IDR"
        },
        "trxId": "MerchantReferenceNo001",
        "additionalInfo":{
            "tXidVA": "TNICEVA02202202306020758419260"
        }
}

nicepaySNAP.inquiryVA()