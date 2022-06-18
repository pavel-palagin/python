import calc
import logger
from calc import for_log

def calc_answer():
    answer = calc.answer
    print(f'{for_log} = {answer}')
    return answer
result = calc_answer()

log = logger.read_log()