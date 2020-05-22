from django.db import models
from django.db.models import Sum
from django.views.generic import ListView
# Create your models here.

class CUSTOMERS(models.Model):
    CUSTOMER_SOURCE_UNIQUE_ID = models.CharField(max_length=100,primary_key=True,)
    ACCOUNT_BALANCE = models.FloatField(blank=True, null=True)
    ACCOUNT_ON_HOLD_FLAG = models.CharField(max_length=100)#
    ACCOUNT_PURPOSE = models.TextField()
    ACCOUNT_SEGMENT = models.IntegerField()
    ACCOUNT_SOURCE_UNIQUE_ID = models.TextField(unique = True)
    ACCOUNT_STATUS_CODE = models.CharField(max_length=100)
    ACQUISITION_DATE = models.DateField()
    ANN_PREMIUM_AMT = models.CharField(max_length=100)#
    BALANCE_DATE = models.DateField(auto_now=False, auto_now_add =False)
    BENEFICIARY_FLAG = models.CharField(max_length=100)
    BLOCKED_REASON = models.TextField()
    BLOCKED_TYPE = models.CharField(max_length=100)
    BRANCH_ID = models.IntegerField()
    BUSINESS_SEGMENT_1 = models.CharField(max_length=100)#
    BUSINESS_TYPE = models.TextField()
    CANCELLED_DATE = models.DateField(auto_now=False, auto_now_add =False)
    CASH_SURR_VALUE = models.CharField(max_length=100)#
    CHANNEL_OF_OPENING = models.CharField(max_length=100)
    CHECK_ACCOUNT_NUMBER = models.IntegerField()
    CITY = models.TextField()
    COLLECTED_BALANCE = models.FloatField()
    COMMENTS = models.TextField()
    COMPANY_FORM  = models.CharField(max_length=100)
    COMPANY_NAME = models.TextField()#
    COUNTRY_OF_ORIGIN = models.CharField(max_length=100)
    COUNTRY_OF_RESIDENCE = models.CharField(max_length=100)
    CREDIT_DEBIT_CODE = models.CharField(max_length=100)
    CREDIT_LIMIT = models.FloatField()
    CREDIT_TURNOVER = models.CharField(max_length=100)
    CURRENCY_CODE = models.CharField(max_length=100)
    CURRENCY_CODE_BASE = models.CharField(max_length=100)
    CURRENCY_CODE_BASE = models.CharField(max_length=100)
    CURRENCY_CODE_ORIG = models.CharField(max_length=100)
    CUSTOMER_INITIATED_CLOSURE = models.CharField(max_length=100)#
    CUSTOMER_SEGMENT_1 = models.IntegerField()
    CUSTOMER_SOURCE_UNIQUE_ID = models.TextField(unique = True)
    CUSTOMER_SOURCE_UNIQUE_ID = models.TextField(unique = True)
    CUSTOMER_STATUS_CODE = models.IntegerField()
    CUSTOMER_TYPE = models.CharField(max_length=100)
    CUSTOMER_TYPE_CODE = models.CharField(max_length=100)
    DATE_CLOSED = models.DateField(auto_now=False, auto_now_add =False)
    DATE_OPENED = models.DateField(auto_now=False, auto_now_add =False)
    DEATH_BENEFIT_AMT = models.CharField(max_length=100)#
    DEBIT_TRUNOVER = models.CharField(max_length=100)
    DELAYED_ACCOUNT_FLAG = models.CharField(max_length=100)#
    DELIVERY_INSTRUCTIONS = models.CharField(max_length=100)#
    DEVICE_ID = models.TextField(unique = True)#
    EMPLOYEE_FLAG = models.CharField(max_length=100)
    EMPLOYEE_NUMBER = models.IntegerField()
    EMPLOYMENT_STATUS = models.CharField(max_length=100)
    ERROR_CORRECT_FLAG = models.CharField(max_length=100)#
    FILTER = models.CharField(max_length=100)#
    FROM_DATE = models.DateField(auto_now=False, auto_now_add =False)
    GENDER_CODE = models.CharField(max_length=100)
    GROSS_PREM_TTD = models.CharField(max_length=100)#
    HOLDING_BANK_NAME = models.TextField()
    INCORPORATION_COUNTRY_CODE = models.CharField(max_length=100)
    INCORPORATION_DATE = models.DateField(auto_now=False, auto_now_add =False)
    INST_PREMIUM_AMT = models.CharField(max_length=100)
    ISSUE_DATE = models.DateField(auto_now=False, auto_now_add =False)
    LANGUAGE_PREF_CODE = models.CharField(max_length=100)#
    LIFE_INS_CONTRACT_DURATION = models.IntegerField()
    MATURITY_DATE = models.DateField(auto_now=False, auto_now_add =False)
    OCCUPATION = models.TextField()
    ORG_UNIT_CODE = models.CharField(max_length=100)
    ORG_UNIT_CODE = models.CharField(max_length=100)
    ORIGINATION_DATE = models.DateField(auto_now=False, auto_now_add =False)
    OTHER_HOLD_AMOUNT = models.FloatField()
    OVERDRAFT_LIMIT = models.FloatField()
    PAYMENT_FREQ = models.CharField(max_length=100)
    PAYMENT_METHOD = models.TextField()
    PERIODIC_LOAN_AMOUNT = models.FloatField()
    PERSON_TITLE = models.TextField()
    POSTAL_CODE = models.IntegerField()
    PRIMARY_CARD_ID = models.IntegerField()
    PRIMARY_CUSTOMER_CATEGORY_CODE = models.IntegerField()
    PRIME_BRANCH_ID = models.IntegerField()
    PRODUCT_SOURCE_TYPE_CODE = models.IntegerField()
    PRODUCT_SOURCE_TYPE_CODE = models.IntegerField()
    REGISTERED_NUMBER = models.IntegerField()#
    RELATIONSHIP_MGR_ID = models.IntegerField()
    REPORTING_REGION = models.TextField()
    RISK_CATEGORY = models.CharField(max_length=100)
    RISK_SCORE = models.IntegerField()
    RUN_TIMESTAMP = models.CharField(max_length=100)#
    SALARY_LODGED_FLAG = models.CharField(max_length=100)#
    SENT_CORRESPONDENCE_FLAG = models.CharField(max_length=100)#
    SETTLEMENT_BANK_NAME = models.CharField(max_length=100)#
    SETTLEMENT_TYPE = models.CharField(max_length=100)#
    SINGLE_PREMIUM_TOTAL = models.CharField(max_length=100)#
    SOURCE_SYSTEM_CODE = models.CharField(max_length=100)#
    SOURCE_TXN_NUM = models.IntegerField()
    SOURCE_TXN_UNIQUE_ID = models.TextField(unique = True)
    SUB_DIVISION = models.IntegerField()
    SUM_INSURED = models.CharField(max_length=100)#
    TO_DATE = models.DateField(auto_now=False, auto_now_add =False)
    TOTAL_DEPOSITS_BASE = models.IntegerField()
    TOTAL_LOANS_BASE = models.IntegerField()
    TRANSACTION_LOCATION = models.TextField()#
    TURNOVER_FROM_DATE = models.DateField(auto_now=False, auto_now_add =False)
    TURNOVER_TO_DATE = models.DateField(auto_now=False, auto_now_add =False)
    TXN_AMOUNT_ORIG = models.FloatField()
    TXN_CHANNEL_CODE = models.IntegerField()
    TXN_SOURCE_TYPE_CODE = models.CharField(max_length=100)
    TXN_STATUS_CODE = models.CharField(max_length=100)
    ZONE = models.TextField()
