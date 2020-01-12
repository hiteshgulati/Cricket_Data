import yaml
import sys
sys.setrecursionlimit(4000)


file_address = "225171_1.yaml"
file = open(file_address, 'r')
match_data = yaml.load(file)

print(match_data)


def get_last(data,stack=[], header="", who="baby", bro_index=0):
    if who == "baby":
        call_index = 0
    elif who == "bro":
        call_index = bro_index + 1
    if isinstance(data, dict):
        header = header + ">" + str(list(data)[call_index])
        stack.append((data, call_index))
        get_last(data[list(data)[call_index]], header=header, stack=stack)
    elif isinstance(data, list):
        # print(data)
        header = header + ">" + str(call_index+1)
        stack.append((data, call_index))
        get_last(data[call_index], header=header, stack=stack)
    else:
        print(header, "-->", data)
        (stack, header) = adjust_stack_for_pop(stack.copy(), header)
        if len(stack) >= 1:
            new_data = stack.pop()
            get_last(new_data[0], header=(header.rsplit(">",1))[0],stack=stack, who="bro", bro_index=new_data[1])


def adjust_stack_for_pop(stack, header):
    if len(stack) >= 1:
        new_data = stack.pop()
        if new_data[1] == len(new_data[0])-1:
            (surplus_stack, header) = adjust_stack_for_pop(stack, (header.rsplit(">",1))[0])
        else:
            stack.append(new_data)
    return (stack, header)


get_last(match_data)