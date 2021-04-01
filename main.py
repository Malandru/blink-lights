import RPi.GPIO as GPIO
import datetime
import argparse
import time


def main():
    setup()
    on, off = parse_arguments()
    current_hour = datetime.datetime.now().hour

    sleep_time = 1
    if current_hour >= on:  # current_hour should be on
        turn_on()
        sleep_time = calculate_sleep_time(off)
    elif current_hour >= off:
        turn_off()
        sleep_time = calculate_sleep_time(on)
    # Sleep 1 second or the hours until off
    print 'First sleep of:', sleep_time
    print '_____________________________'
    time.sleep(sleep_time)

    try:
        blink()
    except:
        print 'Shutting down program...'
        turn_off()
        print 'Done!'


def blink():
    print 'Blinking...'
    while True:
        turn_off()
        sleep_time = calculate_sleep_time(on)
        print '_____________________________'
        time.sleep(sleep_time)

        turn_on()
        sleep_time = calculate_sleep_time(off)
        print '_____________________________'
        time.sleep(sleep_time)


def setup():
    print 'Setting up GPIO'
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)


def calculate_sleep_time(to_hour):
    current_hour = datetime.datetime.now().hour
    diff = abs(current_hour - to_hour)
    if to_hour <= current_hour:
        diff = 24 - diff
    sleep_time = to_seconds(diff)
    print 'Current hour', current_hour
    print 'To hour:', to_hour
    print 'Sleep time:', sleep_time
    return sleep_time


def turn_off():
    print 'Turning lights OFF'
    GPIO.output(8, GPIO.LOW)


def turn_on():
    print 'Turning lights ON'
    GPIO.output(8, GPIO.HIGH)


def to_seconds(hours):
    return hours * 60 * 60  # hour * [60 minute/hour] * [60 second/minute]


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--on', type=int, required=True, help='Hour to turn on the lights')
    parser.add_argument('--off', type=int, required=True, help='Hour to turn off the lights')
    args = parser.parse_args()
    on, off = args.on, args.off
    print 'Configured ON hour:', on
    print 'Configured OFF hour:', off
    print '_____________________________'
    return on, off


if __name__ == '__main__':
    main()
