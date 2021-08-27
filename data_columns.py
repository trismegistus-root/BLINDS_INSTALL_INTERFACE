# Columns to be used for Pandas Dataframes
class COLUMN:
    _installers = ['FIRST NAME', 'LAST NAME', 'PHONE', 'EMAIL']
    _job_without_jobID = ['PAYS', 'CUSTOMER', 'DESIGNER', 'INSTALLER', 'BOXES_IN', 'TOTAL_BOXES', 'BLINDS_ON_HAND', 'BLIND_COUNT', 'SCOPE', 'READY_TO_SCHEDULE']
    _job = ['JOB_ID', 'PAYS', 'CUSTOMER', 'DESIGNER', 'INSTALLER', 'BOXES_IN', 'TOTAL_BOXES', 'BLINDS_ON_HAND', 'BLIND_COUNT', 'SCOPE', 'READY_TO_SCHEDULE']
    _customers = ['F_NAME', 'L_NAME', 'ADDRESS', 'EMAIL', 'PHONE', 'AVAILABILITY', 'DESIGNER', 'JOB_ID']
    _customer_without_jobID = ['F_NAME', 'L_NAME', 'ADDRESS', 'EMAIL', 'PHONE', 'AVAILABILITY', 'DESIGNER']
    _designers = ['F_NAME', 'L_NAME', 'EMAIL', 'PHONE', 'COMPANY', 'AREA']