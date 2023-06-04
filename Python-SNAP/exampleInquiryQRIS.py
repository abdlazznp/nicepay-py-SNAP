from nicepay import nicepaySNAP
import datetime

nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJJT05QQVlURVNUIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJCQkJBIiwiZXhwIjoiMjAyMy0wNi0wNFQxNzozNzozNFoifQ==.TPNwCBxWd7VhYm7duINyRvAO8X68D153Fbbj3BqVwPE="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "1af9014925cab04606b2e77a7536cb0d5c51353924a966e503953e010234108a"
nicepaySNAP.setXPartnerID = "IONPAYTEST"
nicepaySNAP.setXExternalID = "OrdNo" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setBody = {
    "originalReferenceNo":"IONPAYTEST08202306050030072253",
    "originalPartnerReferenceNo":"OrdNo20230605003007",
    "merchantId": "IONPAYTEST",
    "externalStoreId" : "NICEPAY",
    "serviceCode":"51",
    "additionalInfo":{}
}
nicepaySNAP.inquiryQRIS()