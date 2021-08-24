from string import Template

class QUERY:
    class CUSTOMER:
        class WHOLE_TABLE:
            def WITHOUT_JOBID(self):
                return "SELECT F_NAME, L_NAME, ADDRESS, EMAIL, PHONE, AVAILABILITY, DESIGNER FROM CUSTOMER;"
        class INSERT:
            def NEW_CUSTOMER(self, F_NAME, L_NAME, ADDRESS, EMAIL, PHONE, AVAILABILITY, DESIGNER, JOB_ID):
                return Template('INSERT INTO CUSTOMER \
                                (F_NAME, L_NAME, ADDRESS, EMAIL, PHONE, AVAILABILITY, DESIGNER, JOB_ID) VALUES \
                                    ("$F_NAME", "$L_NAME", "$ADDRESS", "$EMAIL", "$PHONE", "$AVAILABILITY", "$DESIGNER", "$JOB_ID");').substitute(
                                        F_NAME = F_NAME,
                                        L_NAME = L_NAME, 
                                        ADDRESS = ADDRESS, 
                                        EMAIL = EMAIL, 
                                        PHONE = PHONE, 
                                        AVAILABILITY = AVAILABILITY, 
                                        DESIGNER = DESIGNER, 
                                        JOB_ID = JOB_ID
                                        )
        class SELECT:
            def BY_NAME(self, F_NAME, L_NAME):
                return Template('SELECT F_NAME, L_NAME, ADDRESS, EMAIL, PHONE, AVAILABILITY FROM CUSTOMER WHERE F_NAME="$F_NAME" AND L_NAME="$L_NAME";').substitute(
                    F_NAME = F_NAME,
                    L_NAME = L_NAME
                )
    class JOB:
        class WHOLE_TABLE:
            def WITHOUT_JOBID(self):
                return "SELECT PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE FROM JOB;"
        class INSERT:
            def NEW_JOB(self, JOB_ID, PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE):
                return Template('INSERT INTO JOB \
                (JOB_ID, PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE) VALUES \
                    ("$JOB_ID", "$PAYS", "$CUSTOMER", "$DESIGNER", "$INSTALLER", "$BOXES_IN", "$TOTAL_BOXES", "$BLINDS_ON_HAND", "$BLIND_COUNT", "$SCOPE", "$READY_TO_SCHEDULE");').substitute(
                        JOB_ID = JOB_ID, 
                        PAYS = PAYS,
                        CUSTOMER = CUSTOMER, 
                        DESIGNER = DESIGNER, 
                        INSTALLER = INSTALLER, 
                        BOXES_IN = BOXES_IN, 
                        TOTAL_BOXES = TOTAL_BOXES,
                        BLINDS_ON_HAND = BLINDS_ON_HAND, 
                        BLIND_COUNT = BLIND_COUNT, 
                        SCOPE = SCOPE, 
                        READY_TO_SCHEDULE = READY_TO_SCHEDULE
                        )
        class SELECT:
            def BY_CUSTOMER_NAME(self, CUSTOMER):
                return Template('SELECT CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE FROM JOB WHERE CUSTOMER = "$CUSTOMER";').substitute(
                    CUSTOMER = CUSTOMER
                )
            def BY_READY_TO_SCHEDULE(self):
                return "SELECT PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE FROM JOB WHERE READY_TO_SCHEDULE = 1;"

            def BY_INSTALLER(self, INSTALLER):
                return Template('SELECT PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE FROM JOB WHERE INSTALLER = "$installer";').substitute(
                    installer = INSTALLER
                )
            def BY_JOB_ID(self,_hash):
                return Template('SELECT CUSTOMER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT FROM JOB WHERE JOB_ID = "$_hash";').substitute(_hash = _hash)

    class DESIGNER:
        class WHOLE_TABLE:
            def ALL_COLUMNS(self):
                return "SELECT * FROM DESIGNER;"
        class INSERT:
            def NEW_DESIGNER(self, F_NAME, L_NAME, EMAIL, PHONE, COMPANY, AREA):
                return Template('INSERT INTO DESIGNER \
                                (F_NAME, L_NAME, EMAIL, PHONE, COMPANY, AREA) VALUES \
                                    ("$F_NAME", "$L_NAME", "$EMAIL", "$PHONE", "$COMPANY", "$AREA");').substitute(
                                        F_NAME = F_NAME,
                                        L_NAME = L_NAME,
                                        EMAIL = EMAIL,
                                        PHONE = PHONE,
                                        COMPANY = COMPANY,
                                        AREA = AREA
                                    )
        class SELECT:
            def BY_NAME(self, F_NAME, L_NAME):
                return Template('SELECT F_NAME, L_NAME, EMAIL, PHONE, COMPANY, AREA FROM DESIGNER WHERE F_NAME = "$F_NAME" and L_NAME = "$L_NAME";').substitute(
                    F_NAME = F_NAME,
                    L_NAME = L_NAME
                )
    class INSTALLER:
        class WHOLE_TABLE:
            def ALL_COLUMNS(self):
                return "SELECT * FROM INSTALLER;"
        class INSERT:
            def NEW_INSTALLER(self, F_NAME, L_NAME, PHONE, EMAIL):
                return Template('INSERT INTO INSTALLER\
                                    (F_NAME, L_NAME, PHONE, EMAIL) VALUES \
                                    ("$F_NAME", "$L_NAME", "$PHONE", "$EMAIL");').substitute(
                                        F_NAME = F_NAME,
                                        L_NAME = L_NAME,
                                        PHONE = PHONE,
                                        EMAIL = EMAIL
                                    )
        class SELECT:
            def BY_NAME(self, F_NAME, L_NAME):
                return Template('SELECT * FROM INSTALLER WHERE F_NAME="$F_NAME" AND L_NAME="$L_NAME";').substitute(
                    F_NAME = F_NAME,
                    L_NAME = L_NAME
                )
    class INSTALLER_PAY:
        class INSERT:
            def NEW_INSTALLER(self, L_NAME, F_NAME):
                return Template('INSERT INTO INSTALLER_PAY (INSTALLER, PAY) VALUES ("$INSTALLER", "$PAY");').substitute(
                            INSTALLER = (L_NAME, F_NAME),
                            PAY = 0.0
                        )