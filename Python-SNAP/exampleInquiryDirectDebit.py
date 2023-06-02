from nicepay import nicepaySNAP
import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUTklDRUVXMDUxIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJUTklDRUVXMDUxIiwiZXhwIjoiMjAyMy0wNi0wMVQwMzozMTowNFoifQ==.mKc44dpf2NkQhlwqdu2_SwWspZ4ijMEXRBiUz2csB74="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "1af9014925cab04606b2e77a7536cb0d5c51353924a966e503953e010234108a"
nicepaySNAP.setXPartnerID = "TNICEEW051"
nicepaySNAP.setXExternalID = "OrdNo" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setBody = {
    "merchantId": "TNICEEW051",
    "subMerchantId": "",
    "originalPartnerReferenceNo": "ref202305081205331683522921",
    "originalReferenceNo": "TNICEEW05105202306011010238976",
    "serviceCode": "54",
    "transactionDate": timestamp,
    "externalStoreId": "",
    "amount": {
        "value": "100.00",
        "currency": "IDR"
    },
    "additionalInfo": {

    }
}
nicepaySNAP.inquiryDirectDebit()