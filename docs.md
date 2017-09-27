{
  patients {
    patientId
    fname
    mname
    lname
    phonenumber
    address
    registeredBy
    nationality
  }
}

{
  patients {
    patientId
    fname
    mname
    lname
    phonenumber
    address
    registeredBy
    nationality
    insurance{
      enrolleeNumber
      coverageType
      scheme{
        payType
        creditLimit
        schemeName
      }
    }
  }
}


{
  insurances {
    enrolleeNumber
    active
    patient {
      fname
      mname
      lname
      address
      phonenumber
    }
    scheme {
      schemeName
      payType
      creditLimit
    }
  }
}


{
  logAppointments {
    startTime
    attendedTime
    status
    logTime
    trigType
  }
}


Changes Made:
1. set related_name for state, lga and district (res) in FakePatient - Not important as this record doesnt have data
2. change ForeignKey to OneToOneField for patient since at the table level, Unique is True.
3. in insurance table, companyId not used - data mostly null. insuranceScheme is preferred but there is a problem

Feedback
insurance_scheme should be ForeignKey to InsuranceSchemes instead of an integerField, this is required to simplify reporting but seems all patients are presents in insurance, PatientId is unique in insurance
Total Records in Patient Demography: 30657
Total Records in Insurance: 30641

How is the total number of patients not equal to the number of patients in insurance?

Investigation:
SRC: http://www.databasejournal.com/features/mysql/three-ways-to-identify-non-matching-records-in-mysql.html

SELECT p.patient_ID FROM patient_demograph as p WHERE p.patient_ID NOT IN (SELECT i.patient_id FROM insurance as i);

+-------------+
| patient_ID  |
+-------------+
| 00000004507 |
| 00000004509 |
| 00000004513 |
| 00000004529 |
| 00000004530 |
| 00000004532 |
| 00000004533 |
| 00000004534 |
| 00000004538 |
| 00000004502 |
| 00000004510 |
| 00000004514 |
| 00000004516 |
| 00000004518 |
| 00000004521 |
| 00000004525 |
+-------------+

16 rows in set

CHANGES
ALTER TABLE `insurance` ADD CONSTRAINT `insurance_scheme_pk` FOREIGN KEY (`insurance_scheme`) REFERENCES `nisa`.`insurance_schemes`(`id`) ON DELETE SET NULL ON UPDATE RESTRICT;

1. Set insurance_scheme in insurance to foriegn key in model and in table directly through phpmyadmin, set relation as well.
2. renamed insurance_scheme field to scheme in InsuranceModel and adjusting to db_column='insurance_scheme'



ISSUES:
Total records in patient_diagnoses: 78856
Total records in patient_diagnoses with ecounter_id Not Null: 551
Total records in encounter_addendum is: 2424
Based on records, only 551 patients had encounters

{
  patientQueue {
    patientId
    entryTime
    attendedTime
    departmentId
    type
    subType
    tagNo
    status
    amount
  }
}


ISSUES:
Department has cost_centre_id but this field is not primaryKey for cost_centre table

CHANGES:

ALTER TABLE `departments` ADD  CONSTRAINT FOREIGN KEY (`cost_centre_id`) REFERENCES `nisa`.`cost_centre`(`id`);

1. setting cost_centre_id to foriegnKey to cost_centre
2. renamed cost_centre_id field to cost_centre in DepartmentModel and adjusting to db_column='cost_centre_id'


query{
  departments{
    name
    costCentre{
      name
      description
      analyticalCode
    }
  }
}

{
  costCentre{
    name
    description
    analyticalCode
    departmentsSet{
      edges{
        node{
          name
        }
      }
    }
  }
}


ISSUES (ROOM/BED):

Feasibility Study
SELECT * FROM room WHERE ward_id is NULL; <Empty Set>
SELECT * FROM room WHERE type_id is NULL; <Empty Set>
select * from bed_charge where patient_id is NULL; <Empty Set>
select * from bed_charge where in_patient_id is NULL; <Empty Set>

It appears ward_id and type_id are not null, They should be made ForeignKey

CHANGES:
ALTER TABLE `room` ADD FOREIGN KEY (`ward_id`) REFERENCES `nisa`.`ward`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT; ALTER TABLE `room` ADD FOREIGN KEY (`type_id`) REFERENCES `nisa`.`room_type`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `ward` ADD FOREIGN KEY (`cost_centre_id`) REFERENCES `nisa`.`cost_centre`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `bed` ADD FOREIGN KEY (`room_id`) REFERENCES `nisa`.`room`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

1. setting ward_id to foriegnKey to ward
2. setting type_id to foriegnKey to room_type
3. renamed ward_id field to ward in RoomModel and adjusting to db_column='ward_id'
4. renamed type_id field to room_type (type is a reserved python keyword) in RoomModel and adjusting to db_column='type_id'
6. renamed cost_centre_id field to cost_centre in WardModel and adjusting to db_column='cost_centre_id'
7. renamed room_id field to room in RoomModel and adjusting to db_column='room_id'

query{
  rooms{
    name
    ward{
      name
    }
    roomType{
      label
      billingCode
    }
  }
}

query{
  wards{
    name
    billingCode
    roomSet{
      edges{
        node {
          name
          roomType{
            label
          }
        }
      }
    }
  }
}


query{
  wards{
    name
    billingCode
    costCentre{
      name      
    }
    roomSet{
      edges{
        node {
          name
          roomType{
            label
          }
        }
      }
    }
  }
}


query{
  beds{
    name
    description
    available
    room{
      name
      ward{
        name
      }
      roomType{
        label
      }
    }
  }
}


ISSUES procedures/ patient_procedures
Feasibility Study
describe `procedure`
category_id in `procedure` table has Null: No, should be made ForeignKey
SELECT * FROM patient_procedure WHERE request_id is NULL; <Empty Set> Why make it null as default.

CHANGES:

ALTER TABLE `procedure` ADD FOREIGN KEY (`category_id`) REFERENCES `nisa`.`procedure_category`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `patient_procedure` ADD FOREIGN KEY (`patient_id`) REFERENCES `nisa`.`patient_demograph`(`patient_ID`) ON DELETE RESTRICT ON UPDATE RESTRICT; ALTER TABLE `patient_procedure` ADD FOREIGN KEY (`procedure_id`) REFERENCES `nisa`.`procedure`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;
ALTER TABLE `patient_procedure_note` ADD FOREIGN KEY (`patient_procedure_id`) REFERENCES `nisa`.`patient_procedure`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;

1. renamed room_id field to room in RoomModel and adjusting to db_column='room_id'


query{
  procedures{
    name
    category{
      name
    }
  }
}


query{
  procedureCategories{
    name
    procedureSet{
      edges{
        node{
          name
          billingCode
        }
      }
    }
  }
}

query{
  patientProcedures{
    inPatientId
    requestId
    requestDate
    billed
    timeStop
    timeStart
    closingText
    requestNote
    patient{
      fname
      mname
      lname
      address
    }
    procedure{
      name
      category{
        name
      }
    }    
  }
}


query{
  patientProcedureNotes{
    note
    staffId
    noteTime
    noteType
    patientProcedure{
      requestDate
    }
  }
}

query{
  patientProcedures{
    requestDate
    requestNote
    encounterId
    timeStart
    timeStop
    procedure{
      name
      billingCode
      category{
        name
      }
    }
    patient{
      fname
      email
    }
    patientprocedurenoteSet{
      edges{
        node {
          staffId
          note
        }
      }
    }
  }
}



doctors note, (diagnoses)
lab investigation ()
phamacy (dispensing)
patient procedure (sugeries)


ALTER TABLE `patient_procedure` ADD FOREIGN KEY (`patient_id`) REFERENCES `nisa`.`patient_demograph`(`patient_ID`) ON DELETE RESTRICT ON UPDATE RESTRICT;

ALTER TABLE `patient_procedure` ADD FOREIGN KEY (`procedure_id`) REFERENCES `nisa`.`procedure`(`id`) ON DELETE RESTRICT ON UPDATE RESTRICT;


BILLS

select * from bills where patient_id is NULL; yields 7 records