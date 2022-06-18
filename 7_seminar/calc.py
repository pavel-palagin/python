import request

def exp_to_list(expression):
    expression_list = []
    for i in expression:
        expression_list.append(i)
    # print(expression_list)
    new_expression_list = []
    value = ''
    for i in range(len(expression_list)):
        if expression_list[i].isdigit():
            value+= expression_list[i]
        else:
            if expression_list[i] == '(' or expression_list[i] == ')':
               new_expression_list.append(expression_list[i])
            else:
                new_expression_list.append(value)
                new_expression_list.append(expression_list[i])
                value = ''
        if(i == len(expression_list)-1):
            new_expression_list.append(value)
    # print(new_expression_list)
    return new_expression_list

def calcul(user_expression):
    result = 0
    if user_expression[1] == '+':
        result = summ(user_expression[0], user_expression[2])
    elif user_expression[1] == '-':
        result = sub(user_expression[0], user_expression[2])
    elif user_expression[1] == '*':
        result = power(user_expression[0], user_expression[2])
    elif user_expression[1] == '/':
        result = div(user_expression[0], user_expression[2])
    return result

summ = lambda x,y: float(x)+float(y)
sub = lambda x,y: float(x)-float(y)
power = lambda x,y: float(x)*float(y)
div = lambda x,y: float(x)/float(y)

user_expression = request.user_expression()
for_log = user_expression
user_expression = exp_to_list(user_expression)
answer = calcul(user_expression)
# print(answer)