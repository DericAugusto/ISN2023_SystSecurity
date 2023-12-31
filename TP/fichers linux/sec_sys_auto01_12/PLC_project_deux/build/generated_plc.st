PROGRAM program2
  VAR
    START_BUTTON AT %QX0.0 : BOOL := 0;
    LEVEL_SENSOR AT %QX0.1 : BOOL := 0;
    CONTACT_SENSOR AT %QX0.2 : BOOL := 0;
    MOTOR AT %QX0.3 : BOOL := 0;
    NOZZLE AT %QX0.4 : BOOL := 0;
    RUN AT %QX0.5 : BOOL := 0;
  END_VAR

  RUN := START_BUTTON;
  MOTOR := (LEVEL_SENSOR OR NOT(CONTACT_SENSOR)) AND RUN;
  IF NOT(CONTACT_SENSOR) AND RUN AND LEVEL_SENSOR AND RUN THEN
    NOZZLE := FALSE; (*reset*)
  END_IF;
  NOZZLE := NOT(LEVEL_SENSOR) AND CONTACT_SENSOR AND RUN;
  IF NOT(LEVEL_SENSOR) AND CONTACT_SENSOR AND RUN THEN
    MOTOR := FALSE; (*reset*)
  END_IF;
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : program2;
  END_RESOURCE
END_CONFIGURATION
