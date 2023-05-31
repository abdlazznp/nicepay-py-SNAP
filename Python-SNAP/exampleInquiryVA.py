from nicepay import nicepaySNAP
import datetime

nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessTokenInquiryVA = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUTklDRVZBMDIyIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJUTklDRVZBMDIyIiwiZXhwIjoiMjAyMy0wNS0zMVQwODozNzo1MFoifQ==.hz1wrt1e9_9AcdHJvZl87KvnzhkPk_FxeHmzruVTYxY="
nicepaySNAP.setXTimestampInquiryVA = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecretInquiryVA = "1af9014925cab04606b2e77a7536cb0d5c51353924a966e503953e010234108a"
nicepaySNAP.setXClientIDInquiryVA = "TNICEVA022"
nicepaySNAP.setXExternalIDInquiryVA = "OrdNo" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setChannelIDInquiryVA = "NICE"
nicepaySNAP.setBodyInquiryVA = {
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
            "tXidVA": "TNICEVA02202202305311534587360"
        }
}

nicepaySNAP.inquiryVA()