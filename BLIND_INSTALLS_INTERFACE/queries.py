from string import Template


"""
[CALL TEMPLATE]
QUERY
    TABLE
        OPERATION
            UNIQUE


[LAYOUT OF CLASS]
QUERY
    CUSTOMER
    JOB
    DESIGNER
    INSTALLER
    INSTALLER_PAY
"""

class QUERY:
    class CUSTOMER:
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

            def ALL_NEW_BOX_NEEDS_BY_CUSTOMER_NAME(self, F_NAME, L_NAME):
                return Template('SELECT F_NAME, L_NAME, DESIGNER, JOB_ID FROM CUSTOMER WHERE F_NAME="$F_NAME" AND L_NAME="$L_NAME";').substitute(
                    F_NAME = F_NAME,
                    L_NAME = L_NAME
                )
                


            class WHOLE_TABLE:
                def WITHOUT_JOBID(self):
                    return "SELECT F_NAME, L_NAME, ADDRESS, EMAIL, PHONE, AVAILABILITY, DESIGNER FROM CUSTOMER;"

        class UPDATE:
            def JOB_ID_TO_COMPLETE(self, F_NAME, L_NAME):
                return Template('UPDATE CUSTOMER SET JOB_ID = "COMPLETE" WHERE F_NAME = "$F_NAME" AND L_NAME = "$L_NAME";').substitute(
                        F_NAME = F_NAME,
                        L_NAME = L_NAME
                    )
    class JOB:


        class INSERT:
            def NEW_JOB(self, JOB_ID, PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE):
                return Template('INSERT INTO JOB \
                (JOB_ID, PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE, BARCODES) VALUES \
                    ("$JOB_ID", "$PAYS", "$CUSTOMER", "$DESIGNER", "$INSTALLER", "$BOXES_IN", "$TOTAL_BOXES", "$BLINDS_ON_HAND", "$BLIND_COUNT", "$SCOPE", "$READY_TO_SCHEDULE", "$BARCODES");').substitute(
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
                        READY_TO_SCHEDULE = READY_TO_SCHEDULE,
                        BARCODES = "None"
                        )
        class DELETE:
            def BY_JOB_ID(self, _hash):
                return Template('DELETE FROM JOB WHERE JOB_ID = "$_hash";').substitute(
                _hash = _hash
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
            

            class UNIQUE_COLUMNS:
                class PAY_AND_INSTALLER:
                    def BY_JOB_ID(self, _hash):
                        return Template('SELECT PAYS, INSTALLER FROM JOB WHERE JOB_ID = "$_hash";').substitute(
                                _hash = _hash
                            )
                            
            class WHOLE_TABLE:
                def WITHOUT_JOBID(self):
                    return "SELECT PAYS, CUSTOMER, DESIGNER, INSTALLER, BOXES_IN, TOTAL_BOXES, BLINDS_ON_HAND, BLIND_COUNT, SCOPE, READY_TO_SCHEDULE FROM JOB;"


        class UPDATE:
            def BOX_AND_BLIND_COUNT_MANUALLY(self, BOXES_IN, BLINDS_ON_HAND, READY_TO_SCHEDULE, _hash):
                return Template('UPDATE JOB SET BOXES_IN = "$BOXES_IN",\
                                                  BLINDS_ON_HAND="$BLINDS_ON_HAND",\
                                                  READY_TO_SCHEDULE="$READY_TO_SCHEDULE" \
                                                  WHERE JOB_ID = "$_hash";').substitute(
                                                      BOXES_IN = BOXES_IN,
                                                      BLINDS_ON_HAND = BLINDS_ON_HAND,
                                                      READY_TO_SCHEDULE = READY_TO_SCHEDULE,
                                                      _hash = _hash
                                                  )


    class DESIGNER:
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
            class WHOLE_TABLE:
                def ALL_COLUMNS(self):
                    return "SELECT * FROM DESIGNER;"
    class INSTALLER:
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
            class WHOLE_TABLE:
                def ALL_COLUMNS(self):
                    return "SELECT * FROM INSTALLER;"

        class DELETE:
            def BY_NAME(self, F_NAME, L_NAME):
                return Template('DELETE FROM INSTALLER WHERE F_NAME = "$F_NAME" AND L_NAME = "$L_NAME";').substitute(
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
        class SELECT:
            def PAY(self, INSTALLER):
                return Template('SELECT PAY FROM INSTALLER_PAY WHERE INSTALLER = "$INSTALLER";').substitute(
                    INSTALLER = INSTALLER
                )
        class UPDATE:
            def PAY(self, PAY, INSTALLER: tuple) -> tuple:
                return Template('UPDATE INSTALLER_PAY SET PAY = "$PAY" WHERE INSTALLER = "$INSTALLER";').substitute(
                        PAY = PAY,
                        INSTALLER = INSTALLER
                    )
            def PAY_SET_TO_ZERO(self, INSTALLER: tuple) -> tuple:
                return Template('UPDATE INSTALLER_PAY SET PAY = 0.0 WHERE INSTALLER = "$INSTALLER";').substitute(
                    INSTALLER = INSTALLER
                )
    
    class BOX:
        class INSERT:
            def NEW_BOX(self, JOB_ID, CUSTOMER, DESIGNER, BARCODE):
                return Template('INSERT INTO BOX (JOB_ID, CUSTOMER, DESIGNER, BARCODE) VALUES ("$JOB_ID", "$CUSTOMER", "$DESIGNER", "$BARCODE");').substitute(
                    JOB_ID = JOB_ID,
                    CUSTOMER = CUSTOMER,
                    DESIGNER = DESIGNER,
                    BARCODE = BARCODE
                )
                # TODO: Additional logic that updates box_count under JOB_ID and alerts when ready to schedule