from django import forms 
from AppVS_PoCFinCrime.models import CUSTOMER 
  
  
# creating a form 
class ClientesForm(forms.ModelForm): 
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = CUSTOMERS 
  
        # specify fields to be used 
        fields = [
            "ACCOUNT_BALANCE",
            "ACCOUNT_ON_HOLD_FLAG",
            "ACCOUNT_PURPOSE",
            "ACCOUNT_SEGMENT",
            "ACCOUNT_SOURCE_UNIQUE_ID",
            "ACCOUNT_STATUS_CODE",
            "ACQUISITION_DATE",
            "ANN_PREMIUM_AMT",
            "BALANCE_DATE",
            "BENEFICIARY_FLAG",
            "BLOCKED_REASON",
            "BLOCKED_TYPE",
            "BRANCH_ID",
            "BUSINESS_SEGMENT_1",
            "BUSINESS_TYPE",
            "CANCELLED_DATE",
            "CASH_SURR_VALUE",
            "CHANNEL_OF_OPENING",
            "CHECK_ACCOUNT_NUMBER",
            "CITY",
            "COLLECTED_BALANCE",
            "COMMENTS",
            "COMPANY_FORM",
            "COMPANY_NAME",
            "COUNTRY_OF_ORIGIN",
            "COUNTRY_OF_RESIDENCE ",
            "CREDIT_DEBIT_CODE ",
            "CREDIT_LIMIT",
            "CREDIT_TURNOVER",
            "CURRENCY_CODE ",
            "CURRENCY_CODE_BASE ",
            "CURRENCY_CODE_ORIG ",
            "CUSTOMER_INITIATED_CLOSURE ",
            "CUSTOMER_SEGMENT_1",
            "CUSTOMER_SOURCE_UNIQUE_ID ",
            "CUSTOMER_ID",
            "CUSTOMER_STATUS_CODE ",
            "CUSTOMER_TYPE ",
            "CUSTOMER_TYPE_CODE",
            "DATE_CLOSED ",
            "DATE_OPENED ",
            "DEATH_BENEFIT_AMT",
            "DEBIT_TRUNOVER ",
            "DELAYED_ACCOUNT_FLAG ",
            "DELIVERY_INSTRUCTIONS ",
            "DEVICE_ID ",
            "EMPLOYEE_FLAG ",
            "EMPLOYEE_NUMBER ",
            "EMPLOYMENT_STATUS ",
            "ERROR_CORRECT_FLAG ",
            "FILTER ",
            "FROM_DATE",
            "GENDER_CODE ",
            "GROSS_PREM_TTD ",
            "HOLDING_BANK_NAME ",
            "INCORPORATION_COUNTRY_CODE ",
            "INCORPORATION_DATE ",
            "INST_PREMIUM_AMT ",
            "ISSUE_DATE ",
            "LANGUAGE_PREF_CODE ",
            "LIFE_INS_CONTRACT_DURATION ",
            "MATURITY_DATE ",
            "OCCUPATION ",
            "ORG_UNIT_CODE ",
            "ORIGINATION_DATE ",
            "OTHER_HOLD_AMOUNT ",
            "OVERDRAFT_LIMIT ",
            "PAYMENT_FREQ ",
            "PAYMENT_METHOD ",
            "PERIODIC_LOAN_AMOUNT ",
            "PERSON_TITLE ",
            "POSTAL_CODE ",
            "PRIMARY_CARD_ID ",
            "PRIMARY_CUSTOMER_CATEGORY_CODE ",
            "PRIME_BRANCH_ID ",
            "PRODUCT_SOURCE_TYPE_CODE ",
            "REGISTERED_NUMBER ",
            "RELATIONSHIP_MGR_ID ",
            "REPORTING_REGION ",
            "RISK_CATEGORY ",
            "RISK_SCORE ",
            "RUN_TIMESTAMP ",
            "SALARY_LODGED_FLAG ",
            "SENT_CORRESPONDENCE_FLAG ",
            "SETTLEMENT_BANK_NAME ",
            "SETTLEMENT_TYPE ",
            "SINGLE_PREMIUM_TOTAL ",
            "SOURCE_SYSTEM_CODE ",
            "SOURCE_TXN_NUM",
            "SOURCE_TXN_UNIQUE_ID ",
            "SUB_DIVISION ",
            "SUM_INSURED  ",
            "TO_DATE ",
            "TOTAL_DEPOSITS_BASE ",
            "TOTAL_LOANS_BASE ",
            "TRANSACTION_LOCATION ",
            "TURNOVER_FROM_DATE ",
            "TURNOVER_TO_DATE ",
            "TXN_AMOUNT_ORIG  ",
            "TXN_CHANNEL_CODE ",
            "TXN_SOURCE_TYPE_CODE ",
            "TXN_STATUS_CODE "
            "ZONE "    
      ] 