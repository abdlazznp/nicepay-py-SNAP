from nicepay import nicepaySNAP
import datetime

nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUTklDRUVXMDUxIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJUTklDRUVXMDUxIiwiZXhwIjoiMjAyMy0wNi0wMVQwMzo1Mzo0MloifQ==.lTOx0_TT1geQi32kE4RMto3H8_i9YP0gJVAwyXU1LjI="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "1af9014925cab04606b2e77a7536cb0d5c51353924a966e503953e010234108a"
nicepaySNAP.setXPartnerID = "TNICEEW051"
nicepaySNAP.setXExternalID = "OrdNo" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setBody = {
    "partnerRefundNo": "ref202305051305841683269997",
    "merchantId": "TNICEEW051",
    "subMerchantId": "",
    "reason": "Cancel",
    "refundAmount": {
        "value": "100.00",
        "currency": "IDR"
    },
    "originalPartnerReferenceNo": "ref202305051305841683269997",
    "originalReferenceNo": "TNICEEW05105202306011010238976",
    "additionalInfo": {
        "refundType": "1"
    },
    "externaStoreId": ""
}
nicepaySNAP.refundDirectDebit()