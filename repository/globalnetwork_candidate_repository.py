from sqlalchemy.orm import Session
import models.globalnetwork_candidate_models as globalnetwork_candidate_models
from schemas import globalnetwork_candidate_schemas
 
def Get_Globalnetwork_Candidate_Data(db: Session):
    get_Candidate = db.query(globalnetwork_candidate_models.Globalnetwork_Candidate_Models).all()
    return get_Candidate

def Post_Globalnetwork_Candidate_Data(request: globalnetwork_candidate_schemas.Globalnetwork_Candidate_Schemas , db:Session):
    Post_Candidate = globalnetwork_candidate_models.Globalnetwork_Candidate_Models( 
    email=request.email,
    phone=request.phone,
    role=request.role,
    experience_years=request.experience_years,
    experience_months=request.experience_months,
    industry_id=request.industry_id,
    cv=request.cv,
    cover_letter=request.cover_letter,
    job_id=request.job_id,
    remarks=request.remarks,
    status=request.status,
    current_ctc=request.current_ctc,
    expected_ctc=request.expected_ctc,
    notice_period=request.notice_period,
    open_to_relocate=request.open_to_relocate,
    city_id=request.city_id,
    country_id=request.country_id,
    country_calling_code_id=request.country_calling_code_id,
    current_ctc_currency_id=request.current_ctc_currency_id,
    expected_ctc_currency_id=request.expected_ctc_currency_id,
    first_name=request.first_name,
    last_name=request.last_name,
    other_industry=request.other_industry,
    salutation=request.salutation,
    state_id=request.state_id,
    submitted_datetime=request.submitted_datetime,
    job_change_reason_id=request.job_change_reason_id,
    cv_displayname=request.cv_displayname,
    exported=request.exported,
    mail_response=request.mail_response,
    mail_send=request.mail_send,
    transaction_error=request.transaction_error,
    middle_name=request.middle_name,
    father_name=request.father_name,
    gender=request.gender,
    permanent_address=request.permanent_address,
    communication=request.communication,
    emergency_contact=request.emergency_contact,
    emergency_contact_name=request.emergency_contact_name,
    emergency_contact_relationship=request.emergency_contact_relationship,
    blood_group=request.blood_group,
    uan_number=request.uan_number,
    passport=request.passport,
    passport_validity=request.passport_validity,
    adhaar_number=request.adhaar_number,
    pan_number=request.pan_number,
    Education=request.Education,
    bank_name=request.bank_name,
    branch=request.branch,
    account_name=request.account_name,
    account_number=request.account_number,
    ifsc_code=request.ifsc_code,
    old_bank_name=request.old_bank_name,
    old_bank_branch=request.old_bank_branch,
    old_account_name=request.old_account_name,
    old_account_number =request.old_account_number,
    old_ifsc_code=request.old_ifsc_code,
    prf_department=request.prf_department,
    prf_joining_date=request.prf_joining_date,
    prf_group_health_insurance=request.prf_group_health_insurance,
    prf_acenet_asset=request.prf_acenet_asset,
    prf_client_asset=request.prf_client_asset,
    prf_form_16=request.prf_form_16,
    prf_covid_certificate=request.prf_covid_certificate,
    prf_bgv_certificate=request.prf_bgv_certificate,
    prf_inititation_date=request.prf_inititation_date,
    prf_report_date=request.prf_report_date,
    prf_client_name=request.prf_client_name,
    prf_agency=request.prf_agency,
    prf_submission_date=request.prf_submission_date,
    )
    db.add(Post_Candidate)
    db.commit()
    db.refresh(Post_Candidate)
    return Post_Candidate
