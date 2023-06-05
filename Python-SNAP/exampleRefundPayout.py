from nicepay import nicepaySNAP
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJJT05QQVlURVNUIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJCTVJJIiwiZXhwIjoiMjAyMy0wNi0wNVQwOTo0MDoxNloifQ==.3r8rIaxHVvp-VCjOk0MXEKto5DvQJNoncQy7MCXyClM="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "33F49GnCMS1mFYlGXisbUDzVf2ATWCl9k3R++d5hDd3Frmuos/XLx8XhXpe+LDYAbpGKZYSwtlyyLOtS/8aD7A=="
nicepaySNAP.setXPartnerID = "IONPAYTEST"
nicepaySNAP.setXExternalID = "OrdNo" + timestamp
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setOrigin = "www.nicepay.co.id"
nicepaySNAP.setBody = {
            "originalPartnerReferenceNo" : "OrdNo20230605162531",
            "originalReferenceNo" : "IONPAYTEST07202306051625314380",
            "merchantId" : "IONPAYTEST"
}

nicepaySNAP.refundPayout()