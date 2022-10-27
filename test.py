
import statistics

def myFunc():
    number_list = []
    integer_list = []
    float_list = []
    n = int(input("Enter the list size "))

    print("\n")
    for i in range(0, n):
        print("Enter number at index", i, )
        item = float(input())
        if item.is_integer():
            item = int(item)
            integer_list.append(item)
        else:
            float_list.append(item)

    if len(integer_list) !=0 and len(float_list) !=0:
        even_nos = [num for num in integer_list if num % 2 == 0]
        x = statistics.mean(even_nos)
        y=max(float_list)
        return x,y
    elif len(integer_list) == 0 and len(float_list) !=0:
        y=max(float_list)
        return y
    elif len(integer_list) !=0 and len(float_list) == 0:
        even_nos = [num for num in integer_list if num % 2 == 0]
        x = statistics.mean(even_nos)
        return x
    else:
        return 0
myFunc()