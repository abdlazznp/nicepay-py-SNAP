from nicepay import nicepaySNAP
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJJT05QQVlURVNUIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJCTVJJIiwiZXhwIjoiMjAyMy0wNi0wNVQxMDoxMjowOVoifQ==.rGPCSdVFu09RW1mdYod7m0lGgxV68Z89MPqRVjS0D7s="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "33F49GnCMS1mFYlGXisbUDzVf2ATWCl9k3R++d5hDd3Frmuos/XLx8XhXpe+LDYAbpGKZYSwtlyyLOtS/8aD7A=="
nicepaySNAP.setXPartnerID = "IONPAYTEST"
nicepaySNAP.setXExternalID = "OrdNo" + timestamp
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setOrigin = "www.nicepay.co.id"
nicepaySNAP.setBody = {
            "merchantId" : "IONPAYTEST",
            "additionalInfo" : {
                "msId": ""
            }
}

nicepaySNAP.balanceInquiryPayout()