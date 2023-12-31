PROGRAM project_un
  VAR
    PB1 AT %IX0.0 : BOOL;
    PB2 AT %IX0.1 : BOOL;
    LED AT %QX0.0 : BOOL;
  END_VAR

  LED := NOT(PB2) AND (LED OR PB1);
END_PROGRAM


CONFIGURATION Config0

  RESOURCE Res0 ON PLC
    VAR_GLOBAL
      PB1 AT %IX0.0 : BOOL;
      LAMP AT %QX0.0 : BOOL;
      PB2 AT %IX0.1 : BOOL;
    END_VAR
    TASK task0(INTERVAL := T#20ms,PRIORITY := 0);
    PROGRAM instance0 WITH task0 : project_un;
  END_RESOURCE
END_CONFIGURATION
