import functools


def find_unique_element(arry_list):
    u_element = functools.reduce(lambda a,b:a^b, arry_list)
    print(u_element)


if __name__== "__main__":
    input_string = list(map(int, input().rstrip().split()))
    find_unique_element(input_string)