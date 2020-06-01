from django.db import models
from django.db.models import Sum
from django.views.generic import ListView
# Create your models here.

class CUSTOMERS(models.Model):
    ACCOUNT_BALANCE = models.FloatField(blank=True,null=True)
    ACCOUNT_ON_HOLD_FLAG = models.CharField(max_length=100,blank=True, null=True)#
    ACCOUNT_PURPOSE = models.TextField(blank=True, null=True)
    ACCOUNT_SEGMENT = models.IntegerField(blank=True, null=True)
    ACCOUNT_SOURCE_UNIQUE_ID = models.TextField(unique = True)
    ACCOUNT_STATUS_CODE = models.CharField(max_length=100, blank=True, null=True)
    ACQUISITION_DATE = models.DateField(blank=True, null=True)
    ANN_PREMIUM_AMT = models.CharField(max_length=100, blank=True, null=True)#
    BALANCE_DATE = models.DateField(blank=True, null=True)
    BENEFICIARY_FLAG = models.CharField(max_length=100, blank=True, null=True)
    BLOCKED_REASON = models.TextField(blank=True, null=True)
    BLOCKED_TYPE = models.CharField(max_length=100, blank=True, null=True)
    BRANCH_ID = models.IntegerField(blank=True, null=True)
    BUSINESS_SEGMENT_1 = models.TextField(blank=True, null=True)#
    BUSINESS_TYPE = models.TextField(blank=True, null=True)
    CANCELLED_DATE = models.DateField(null=True)
    CASH_SURR_VALUE = models.CharField(max_length=100, blank=True, null=True)#
    CHANNEL_OF_OPENING = models.CharField(max_length=100, blank=True, null=True)
    CHECK_ACCOUNT_NUMBER = models.IntegerField( blank=True, null=True)
    CITY = models.TextField( blank=True, null=True)
    COLLECTED_BALANCE = models.FloatField(null=True)
    COMMENTS = models.TextField( blank=True, null=True)
    COMPANY_FORM  = models.CharField(max_length=100,  blank=True, null=True)
    COMPANY_NAME = models.TextField( blank=True, null=True)#
    COUNTRY_OF_ORIGIN = models.CharField(max_length=100,  blank=True, null=True)
    COUNTRY_OF_RESIDENCE = models.CharField(max_length=100,  blank=True, null=True)
    CREDIT_DEBIT_CODE = models.CharField(max_length=100,  blank=True, null=True)
    CREDIT_LIMIT = models.FloatField( blank=True, null=True)
    CREDIT_TURNOVER = models.CharField(max_length=100,  blank=True, null=True)
    CURRENCY_CODE = models.CharField(max_length=100, blank=True, null=True)
    CURRENCY_CODE_BASE = models.CharField(max_length=100, blank=True, null=True)
    CURRENCY_CODE_ORIG = models.CharField(max_length=100, blank=True, null=True)
    CUSTOMER_INITIATED_CLOSURE = models.CharField(max_length=100, blank=True, null=True)#
    CUSTOMER_SEGMENT_1 = models.IntegerField(blank=True, null=True)
    CUSTOMER_SOURCE_UNIQUE_ID = models.TextField(blank=True, null=True)
    CUSTOMER_ID = models.TextField(blank=True, null=True)
    CUSTOMER_STATUS_CODE = models.IntegerField( blank=True, null=True)
    CUSTOMER_TYPE = models.CharField(max_length=100,  blank=True, null=True)
    CUSTOMER_TYPE_CODE = models.CharField(max_length=100,  blank=True, null=True)
    DATE_CLOSED = models.DateField(blank=True, null=True)
    DATE_OPENED = models.DateField(blank=True, null=True)
    DEATH_BENEFIT_AMT = models.CharField(max_length=100,  blank=True, null=True)#
    DEBIT_TRUNOVER = models.CharField(max_length=100,  blank=True, null=True)
    DELAYED_ACCOUNT_FLAG = models.CharField(max_length=100,  blank=True, null=True)#
    DELIVERY_INSTRUCTIONS = models.TextField(blank=True, null=True)#
    DEVICE_ID = models.TextField(blank=True, null=True)#
    EMPLOYEE_FLAG = models.CharField(max_length=100,  blank=True, null=True)
    EMPLOYEE_NUMBER = models.IntegerField( blank=True, null=True)
    EMPLOYMENT_STATUS = models.CharField(max_length=100,  blank=True, null=True)
    ERROR_CORRECT_FLAG = models.CharField(max_length=100,  blank=True, null=True)#
    FILTER = models.CharField(max_length=100,  blank=True, null=True)#
    FROM_DATE = models.DateField(blank=True, null=True)
    GENDER_CODE = models.CharField(max_length=100,  blank=True, null=True)
    GROSS_PREM_TTD = models.CharField(max_length=100,  blank=True, null=True)#
    HOLDING_BANK_NAME = models.TextField( blank=True, null=True)
    INCORPORATION_COUNTRY_CODE = models.CharField(max_length=100,  blank=True, null=True)
    INCORPORATION_DATE = models.DateField(blank=True, null=True)
    INST_PREMIUM_AMT = models.CharField(max_length=100,  blank=True, null=True)
    ISSUE_DATE = models.DateField(blank=True, null=True)
    LANGUAGE_PREF_CODE = models.CharField(max_length=100,  blank=True, null=True)#
    LIFE_INS_CONTRACT_DURATION = models.IntegerField( blank=True, null=True)
    MATURITY_DATE = models.DateField(blank=True, null=True)
    OCCUPATION = models.TextField( blank=True, null=True)
    ORG_UNIT_CODE = models.CharField(max_length=100,  blank=True, null=True)
    ORIGINATION_DATE = models.DateField(auto_now=False, auto_now_add =False,  blank=True, null=True)
    OTHER_HOLD_AMOUNT = models.FloatField( blank=True, null=True)
    OVERDRAFT_LIMIT = models.FloatField( blank=True, null=True)
    PAYMENT_FREQ = models.CharField(max_length=100,  blank=True, null=True)
    PAYMENT_METHOD = models.TextField( blank=True, null=True)
    PERIODIC_LOAN_AMOUNT = models.FloatField( blank=True, null=True)
    PERSON_TITLE = models.TextField( blank=True, null=True)
    POSTAL_CODE = models.IntegerField( blank=True, null=True)
    PRIMARY_CARD_ID = models.IntegerField( blank=True, null=True)
    PRIMARY_CUSTOMER_CATEGORY_CODE = models.TextField( blank=True, null=True)
    PRIME_BRANCH_ID = models.IntegerField( blank=True, null=True)
    PRODUCT_SOURCE_TYPE_CODE = models.CharField(max_length=100, blank=True, null=True)
    REGISTERED_NUMBER = models.IntegerField( blank=True, null=True)#
    RELATIONSHIP_MGR_ID = models.IntegerField( blank=True, null=True)
    REPORTING_REGION = models.TextField( blank=True, null=True)
    RISK_CATEGORY = models.CharField(max_length=100,  blank=True, null=True)
    RISK_SCORE = models.IntegerField(blank=True, null=True)
    RUN_TIMESTAMP = models.CharField(max_length=100, blank=True, null=True)#
    SALARY_LODGED_FLAG = models.CharField(max_length=100, blank=True, null=True)#
    SENT_CORRESPONDENCE_FLAG = models.CharField(max_length=100, blank=True, null=True)#
    SETTLEMENT_BANK_NAME = models.TextField(blank=True, null=True)#
    SETTLEMENT_TYPE = models.CharField(max_length=100, blank=True, null=True)#
    SINGLE_PREMIUM_TOTAL = models.CharField(max_length=100,  blank=True, null=True)#
    SOURCE_SYSTEM_CODE = models.CharField(max_length=100,  blank=True, null=True)#
    SOURCE_TXN_NUM = models.TextField( blank=True, null=True)
    SOURCE_TXN_UNIQUE_ID = models.TextField(unique = True, primary_key=True)
    SUB_DIVISION = models.IntegerField( blank=True, null=True)
    SUM_INSURED = models.CharField(max_length=100,  blank=True, null=True)#
    TO_DATE = models.DateField(blank=True, null=True)
    TOTAL_DEPOSITS_BASE = models.IntegerField( blank=True, null=True)
    TOTAL_LOANS_BASE = models.IntegerField( blank=True, null=True)
    TRANSACTION_LOCATION = models.TextField( blank=True, null=True)#
    TURNOVER_FROM_DATE = models.DateField(blank=True, null=True)
    TURNOVER_TO_DATE = models.DateField(blank=True, null=True)
    TXN_AMOUNT_ORIG = models.FloatField( blank=True, null=True)
    TXN_CHANNEL_CODE = models.IntegerField( blank=True, null=True)
    TXN_SOURCE_TYPE_CODE = models.CharField(max_length=100,  blank=True, null=True)
    TXN_STATUS_CODE = models.CharField(max_length=100,  blank=True, null=True)
    ZONE = models.TextField( blank=True, null=True)
