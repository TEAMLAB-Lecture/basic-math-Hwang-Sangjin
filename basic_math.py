#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):

    greatest_num=-10000000

    list_size = len(number_list)

    for looper in range(0,list_size):
        if greatest_num == -10000000 or greatest_num < number_list[looper]:
            greatest_num = number_list[looper]
    """
    주어진 리스트에서 가장 큰 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            greatest_number (int): parameter number_list 중 가장 큰 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_greatest(number_list)
            99
    """

    return greatest_number


def get_smallest(number_list):

    smallest_number=10000000

    list_size = len(number_list)

    for looper in range(0,list_size):
        if smallest_number == 10000000 or smallest_number < number_list[looper]:
            smallest_number = number_list[looper]
    """
    주어진 리스트에서 제일 작은 숫자를 반환함

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            smallest_number (int): parameter number_list 중 가장 작은 값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_smallest(number_list)
            11
    """

    return smallest_number


def get_mean(number_list):
    list_num = len(number_list)

    mean = None

    for looper in range(0,list_num):
        mean+=number_list[looper]

    mean = mean/ list_num

    """
    주어진 리스트 숫자들의 평균을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            mean (int): parameter number_list 숫자들의 평균

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_mean(number_list)
            47
    """
    
    return mean


def get_median(number_list):
    """
    주어진 리스트 숫자들의 중간값을 구함.

        Parameters:
            number_list (list): integer로 값으로만 구성된 list
            ex - [10, 33, 22, 99, 33]

        Returns:
            median (int): parameter number_list 숫자들의 중간값

        Examples:
            >>> number_list = [39, 54, 32, 11, 99]
            >>> import basic_math as bm
            >>> bm.get_median(number_list)
            39
            >>> number_list2 = [39, 54, 32, 11, 99, 5]
            >>> bm.get_median(number_list2)
            35.5
    """
    median = None

    number_list.sort()

    list_num = len(number_list)

    if list_num == 0:
        median =None

    else:
        center = int(list_num/2)
        if center%2==1:
            median = number_list[center]
        else:
            median = (number_list[center-1] + number_list[center])/2
    return median
