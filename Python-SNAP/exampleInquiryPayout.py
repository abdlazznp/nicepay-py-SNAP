from nicepay import nicepaySNAP
import datetime

nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJJT05QQVlURVNUIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJCTVJJIiwiZXhwIjoiMjAyMy0wNi0wNVQwMzowODoyN1oifQ==.iulkLG2468UC-WC-4ZYGiBAkfDb2WhbbpFOx6ACSuQw="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "33F49GnCMS1mFYlGXisbUDzVf2ATWCl9k3R++d5hDd3Frmuos/XLx8XhXpe+LDYAbpGKZYSwtlyyLOtS/8aD7A=="
nicepaySNAP.setXPartnerID = "IONPAYTEST"
nicepaySNAP.setXExternalID = "OrdNo" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setOrigin = "www.nicepay.co.id"
nicepaySNAP.setBody = {
            "originalPartnerReferenceNo" : "OrdNo20230605094651",
            "originalReferenceNo" : "IONPAYTEST07202306050946523564",
            "merchantId" : "IONPAYTEST",
            "beneficiaryAccountNo" : "12355874912"
}

nicepaySNAP.inquiryPayout()