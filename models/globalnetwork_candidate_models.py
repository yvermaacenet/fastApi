
from sqlalchemy import Boolean, Column,String ,INT, TEXT, DATETIME, SMALLINT, DateTime
from database import Base
import datetime
from sqlalchemy.sql import func
class Globalnetwork_Candidate_Models(Base):
    # __tablename__ = "globalnetwork_candidate"
    __tablename__ = 'globalnetwork_candidate'
    __table_args__ = {'extend_existing': True}
    # __abstract__ = False
    id = Column(INT,primary_key=True )
    email = Column(String(100), unique=True, index=True)
    phone=Column(String(100))
    role=Column(String(100))
    experience_years= Column(INT )
    experience_months= Column(INT )
    industry_id= Column(INT )
    cv=Column(String(100))
    cover_letter=Column(TEXT(100))
    job_id= Column(INT )
    remarks=Column(TEXT(100))
    status=Column(SMALLINT)
    current_ctc= Column(INT )
    expected_ctc= Column(INT )
    notice_period=Column(SMALLINT)
    open_to_relocate=Column(SMALLINT)
    city_id= Column(INT )
    country_id= Column(INT )
    country_calling_code_id= Column(INT )
    current_ctc_currency_id= Column(INT )
    expected_ctc_currency_id= Column(INT )
    first_name=Column(String(100))
    last_name=Column(String(100))
    other_industry=Column(String(200))
    salutation=Column(SMALLINT)
    state_id= Column(INT )
    submitted_datetime=Column(DATETIME)
    job_change_reason_id= Column(INT )
    cv_displayname=Column(String(150))
    exported=Column(SMALLINT)
    mail_response=Column(SMALLINT)
    mail_send=Column(SMALLINT)
    transaction_error=Column(TEXT(100))
    middle_name=Column(String(100))
    father_name =Column(String(100))
    gender =Column(String(100))
    permanent_address=Column(String(100))
    communication =Column(String(100))
    emergency_contact=Column(INT )
    emergency_contact_name =Column(String(100))
    emergency_contact_relationship=Column(String(100))
    blood_group =Column(String(100))
    uan_number =Column(String(100))
    passport =Column(String(100))
    passport_validity=Column(String(100))
    adhaar_number =Column(INT )
    pan_number=Column(String(100))
    Education=Column(String(100))
    bank_name =Column(String(100))
    branch =Column(String(100))
    account_name =Column(String(100))
    account_number =Column(INT )
    ifsc_code=Column(INT )
    old_bank_name =Column(String(100))
    old_bank_branch =Column(String(100))
    old_account_name =Column(String(100))
    old_account_number =Column(INT )
    old_ifsc_code=Column(INT )
    prf_department =Column(String(100))
    prf_joining_date =Column(DATETIME)
    prf_group_health_insurance =Column(Boolean )
    prf_acenet_asset =Column(Boolean )
    prf_client_asset =Column(Boolean )
    prf_form_16 =Column(Boolean )
    prf_covid_certificate =Column(Boolean )
    prf_bgv_certificate =Column(Boolean )
    prf_inititation_date =Column(DATETIME )
    prf_report_date =Column(DATETIME)
    prf_client_name = Column(String(100))
    prf_agency = Column(String(100))
    prf_submission_date = Column(DATETIME)
     