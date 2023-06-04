from nicepay import nicepaySNAP
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJJT05QQVlURVNUIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJCQkJBIiwiZXhwIjoiMjAyMy0wNi0wNFQxNzo1NTowNFoifQ==.6AOTsJMF2wfOFi0bhDuatOdq7WGrbDBqb2SnpgZ4zrQ="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "1af9014925cab04606b2e77a7536cb0d5c51353924a966e503953e010234108a"
nicepaySNAP.setXPartnerID = "IONPAYTEST"
nicepaySNAP.setXExternalID = "OrdNo" + timestamp
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setBody = {
    "originalReferenceNo":"IONPAYTEST08202306050030072253",
    "originalPartnerReferenceNo":"OrdNo20230605003007",
    "partnerRefundNo":"OrdNo" + timestamp,
    "merchantId":"IONPAYTEST",
    "externalStoreId":"NICEPAY",
    "refundAmount":{
        "value":"100.00",
        "currency":"IDR"
    },
    "reason":"This Is Cancel QRIS SNAP",
    "additionalInfo":{
        "cancelType":"1"
    }
}
nicepaySNAP.refundQRIS()