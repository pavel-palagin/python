from datetime import datetime as dt

import calc

def reporting(expression = 0, answer = 0, time = 0):
    expression = calc.for_log
    answer = calc.answer
    time = dt.now().strftime('%H:%M')
    report = (f'{expression} = {answer} at {time} ')
    return report

def log_write(report):
    with open('log.txt', 'a') as log:
        log.write(report + '\n')

def read_log():
    with open('log.txt', 'r') as log:
        log_list = log.read().split()
    return log_list

report = reporting()
log_write(report)