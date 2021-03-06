# Generated by Django 2.2.12 on 2020-05-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CUSTOMERS',
            fields=[
                ('ACCOUNT_BALANCE', models.FloatField(blank=True, null=True)),
                ('ACCOUNT_ON_HOLD_FLAG', models.CharField(blank=True, max_length=100)),
                ('ACCOUNT_PURPOSE', models.TextField(blank=True)),
                ('ACCOUNT_SEGMENT', models.IntegerField(blank=True, null=True)),
                ('ACCOUNT_SOURCE_UNIQUE_ID', models.TextField(unique=True)),
                ('ACCOUNT_STATUS_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('ACQUISITION_DATE', models.DateTimeField(blank=True, null=True)),
                ('ANN_PREMIUM_AMT', models.CharField(blank=True, max_length=100, null=True)),
                ('BALANCE_DATE', models.DateField(blank=True, null=True)),
                ('BENEFICIARY_FLAG', models.CharField(blank=True, max_length=100, null=True)),
                ('BLOCKED_REASON', models.TextField(blank=True, null=True)),
                ('BLOCKED_TYPE', models.CharField(blank=True, max_length=100, null=True)),
                ('BRANCH_ID', models.IntegerField(blank=True, null=True)),
                ('BUSINESS_SEGMENT_1', models.CharField(blank=True, max_length=100, null=True)),
                ('BUSINESS_TYPE', models.TextField(blank=True, null=True)),
                ('CANCELLED_DATE', models.DateField(blank=True, null=True)),
                ('CASH_SURR_VALUE', models.CharField(blank=True, max_length=100, null=True)),
                ('CHANNEL_OF_OPENING', models.CharField(blank=True, max_length=100, null=True)),
                ('CHECK_ACCOUNT_NUMBER', models.IntegerField(blank=True, null=True)),
                ('CITY', models.TextField(blank=True, null=True)),
                ('COLLECTED_BALANCE', models.FloatField(blank=True, null=True)),
                ('COMMENTS', models.TextField(blank=True, null=True)),
                ('COMPANY_FORM', models.CharField(blank=True, max_length=100, null=True)),
                ('COMPANY_NAME', models.TextField(blank=True, null=True)),
                ('COUNTRY_OF_ORIGIN', models.CharField(blank=True, max_length=100, null=True)),
                ('COUNTRY_OF_RESIDENCE', models.CharField(blank=True, max_length=100, null=True)),
                ('CREDIT_DEBIT_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('CREDIT_LIMIT', models.FloatField(blank=True, null=True)),
                ('CREDIT_TURNOVER', models.CharField(blank=True, max_length=100, null=True)),
                ('CURRENCY_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('CURRENCY_CODE_BASE', models.CharField(blank=True, max_length=100, null=True)),
                ('CURRENCY_CODE_ORIG', models.CharField(blank=True, max_length=100, null=True)),
                ('CUSTOMER_INITIATED_CLOSURE', models.CharField(blank=True, max_length=100, null=True)),
                ('CUSTOMER_SEGMENT_1', models.IntegerField(blank=True, null=True)),
                ('CUSTOMER_SOURCE_UNIQUE_ID', models.TextField(blank=True, null=True, unique=True)),
                ('CUSTOMER_ID', models.TextField(blank=True, null=True)),
                ('CUSTOMER_STATUS_CODE', models.IntegerField(blank=True, null=True)),
                ('CUSTOMER_TYPE', models.CharField(blank=True, max_length=100, null=True)),
                ('CUSTOMER_TYPE_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('DATE_CLOSED', models.DateField(blank=True, null=True)),
                ('DATE_OPENED', models.DateField(blank=True, null=True)),
                ('DEATH_BENEFIT_AMT', models.CharField(blank=True, max_length=100, null=True)),
                ('DEBIT_TRUNOVER', models.CharField(blank=True, max_length=100, null=True)),
                ('DELAYED_ACCOUNT_FLAG', models.CharField(blank=True, max_length=100, null=True)),
                ('DELIVERY_INSTRUCTIONS', models.CharField(blank=True, max_length=100, null=True)),
                ('DEVICE_ID', models.TextField(blank=True, null=True, unique=True)),
                ('EMPLOYEE_FLAG', models.CharField(blank=True, max_length=100, null=True)),
                ('EMPLOYEE_NUMBER', models.IntegerField(blank=True, null=True)),
                ('EMPLOYMENT_STATUS', models.CharField(blank=True, max_length=100, null=True)),
                ('ERROR_CORRECT_FLAG', models.CharField(blank=True, max_length=100, null=True)),
                ('FILTER', models.CharField(blank=True, max_length=100, null=True)),
                ('FROM_DATE', models.DateField(blank=True, null=True)),
                ('GENDER_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('GROSS_PREM_TTD', models.CharField(blank=True, max_length=100, null=True)),
                ('HOLDING_BANK_NAME', models.TextField(blank=True, null=True)),
                ('INCORPORATION_COUNTRY_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('INCORPORATION_DATE', models.DateField(blank=True, null=True)),
                ('INST_PREMIUM_AMT', models.CharField(blank=True, max_length=100, null=True)),
                ('ISSUE_DATE', models.DateField(blank=True, null=True)),
                ('LANGUAGE_PREF_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('LIFE_INS_CONTRACT_DURATION', models.IntegerField(blank=True, null=True)),
                ('MATURITY_DATE', models.DateField(blank=True, null=True)),
                ('OCCUPATION', models.TextField(blank=True, null=True)),
                ('ORG_UNIT_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('ORIGINATION_DATE', models.DateField(blank=True, null=True)),
                ('OTHER_HOLD_AMOUNT', models.FloatField(blank=True, null=True)),
                ('OVERDRAFT_LIMIT', models.FloatField(blank=True, null=True)),
                ('PAYMENT_FREQ', models.CharField(blank=True, max_length=100, null=True)),
                ('PAYMENT_METHOD', models.TextField(blank=True, null=True)),
                ('PERIODIC_LOAN_AMOUNT', models.FloatField(blank=True, null=True)),
                ('PERSON_TITLE', models.TextField(blank=True, null=True)),
                ('POSTAL_CODE', models.IntegerField(blank=True, null=True)),
                ('PRIMARY_CARD_ID', models.IntegerField(blank=True, null=True)),
                ('PRIMARY_CUSTOMER_CATEGORY_CODE', models.IntegerField(blank=True, null=True)),
                ('PRIME_BRANCH_ID', models.IntegerField(blank=True, null=True)),
                ('PRODUCT_SOURCE_TYPE_CODE', models.IntegerField(blank=True, null=True)),
                ('REGISTERED_NUMBER', models.IntegerField(blank=True, null=True)),
                ('RELATIONSHIP_MGR_ID', models.IntegerField(blank=True, null=True)),
                ('REPORTING_REGION', models.TextField(blank=True, null=True)),
                ('RISK_CATEGORY', models.CharField(blank=True, max_length=100, null=True)),
                ('RISK_SCORE', models.IntegerField(blank=True, null=True)),
                ('RUN_TIMESTAMP', models.CharField(blank=True, max_length=100, null=True)),
                ('SALARY_LODGED_FLAG', models.CharField(blank=True, max_length=100, null=True)),
                ('SENT_CORRESPONDENCE_FLAG', models.CharField(blank=True, max_length=100, null=True)),
                ('SETTLEMENT_BANK_NAME', models.CharField(blank=True, max_length=100, null=True)),
                ('SETTLEMENT_TYPE', models.CharField(blank=True, max_length=100, null=True)),
                ('SINGLE_PREMIUM_TOTAL', models.CharField(blank=True, max_length=100, null=True)),
                ('SOURCE_SYSTEM_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('SOURCE_TXN_NUM', models.IntegerField(blank=True, null=True)),
                ('SOURCE_TXN_UNIQUE_ID', models.TextField(primary_key=True, serialize=False, unique=True)),
                ('SUB_DIVISION', models.IntegerField(blank=True, null=True)),
                ('SUM_INSURED', models.CharField(blank=True, max_length=100, null=True)),
                ('TO_DATE', models.DateField(blank=True, null=True)),
                ('TOTAL_DEPOSITS_BASE', models.IntegerField(blank=True, null=True)),
                ('TOTAL_LOANS_BASE', models.IntegerField(blank=True, null=True)),
                ('TRANSACTION_LOCATION', models.TextField(blank=True, null=True)),
                ('TURNOVER_FROM_DATE', models.DateField(blank=True, null=True)),
                ('TURNOVER_TO_DATE', models.DateField(blank=True, null=True)),
                ('TXN_AMOUNT_ORIG', models.FloatField(blank=True, null=True)),
                ('TXN_CHANNEL_CODE', models.IntegerField(blank=True, null=True)),
                ('TXN_SOURCE_TYPE_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('TXN_STATUS_CODE', models.CharField(blank=True, max_length=100, null=True)),
                ('ZONE', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
