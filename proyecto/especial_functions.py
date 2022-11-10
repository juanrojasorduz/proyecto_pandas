import os

def conditions_function(condition_name,condition_input,condition_body):
    if condition_name == 'file_name_extension':
        condition = condition_body == os.path.splitext(condition_input)[1].lstrip('.')
        return condition


def input_validation(rule_type,input_type,options_list,condition_name,condition_body,input_message,error_message,menu):
    if rule_type == 'options_list':
        print(input_message)
        if menu == False:
            for option in options_list:
                print(option)
        else:
            print(options_list)
    elif rule_type == 'condition':
        print(input_message)
    while True:
        try:
            if input_type == 'int':
                selected_option = int(input(': '))
            elif input_type == 'float':
                selected_option = float(input(': '))
            elif input_type == 'string':
                selected_option = input(': ')
            if rule_type == 'options_list' and selected_option not in options_list:
                raise ValueError(error_message)
                if menu == False:
                    for option in options_list:
                        print(option)
                else:
                    print(options_list)
            elif rule_type == 'condition' and conditions_function(condition_name,selected_option,condition_body) == False:
                raise ValueError(error_message)
            else:
                break
        except ValueError:
            if rule_type == 'options_list':
                print(error_message)
                if menu == False:
                    for option in options_list:
                        print(option)
                else:
                    print(options_list)
            elif rule_type == 'condition':
                print(error_message)
    return selected_option
