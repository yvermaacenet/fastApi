from ctypes.wintypes import INT
from datetime import date, datetime
from pydantic import BaseModel
from zoneinfo import ZoneInfo
from dateutil.tz import gettz
from pytz import timezone


class Globalnetwork_Candidate_Schemas(BaseModel):
     email:str
     phone:str
     role:str
     experience_years:int
     experience_months:int
     industry_id:int
     cv:str
     cover_letter:str
     job_id:int
     remarks:str
     status:int
     current_ctc:int
     expected_ctc:int
     notice_period:int
     open_to_relocate:int
     city_id :int
     country_id :int
     country_calling_code_id :int
     current_ctc_currency_id :int
     expected_ctc_currency_id :int
     first_name:str
     last_name:str
     other_industry:str
     salutation:int
     state_id:int
     submitted_datetime:datetime
     job_change_reason_id:int
     cv_displayname:str
     exported:int
     mail_response:int
     mail_send:int
     transaction_error:str
     middle_name:str
     father_name :str
     gender :str
     permanent_address:str
     communication :str
     emergency_contact:int
     emergency_contact_name :str
     emergency_contact_relationship:str
     blood_group :str
     uan_number :str
     passport :str
     passport_validity:str
     adhaar_number :int
     pan_number:str
     Education:str
     bank_name :str
     branch :str
     account_name :str
     account_number :int
     ifsc_code:int
     old_bank_name :str
     old_bank_branch :str
     old_account_name :str
     old_account_number :int
     old_ifsc_code:int
     prf_department :str
     prf_joining_date : datetime
     prf_group_health_insurance : bool
     prf_acenet_asset : bool
     prf_client_asset : bool
     prf_form_16 : bool
     prf_covid_certificate : bool
     prf_bgv_certificate : bool
     prf_inititation_date :datetime
     prf_report_date : datetime
     prf_client_name : str
     prf_agency : str
     prf_submission_date : datetime


