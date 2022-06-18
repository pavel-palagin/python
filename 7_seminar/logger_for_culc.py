from datetime import datetime as dt

from calc import result

def calculator_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('logger_for_calc.csv', 'a') as file:
        file.write('{};calculator;{}\n'.format(time, data))

