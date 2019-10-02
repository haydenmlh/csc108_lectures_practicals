def marathon_time(half_marathon_time: int, is_hilly: bool) -> int:
    '''Returns total marathon time given the half marathon time and whether or not the marathon is hilly
    >>> marathon_time(300, True)
    630
    >>> marathon_time(250, False)
    510
    >>> marathon_time(0, True)
    30
    '''
    if is_hilly:
        return half_marathon_time * 2 + 30
    else:
        return half_marathon_time * 2 + 10

REGULAR_TICKET_PRICE = 3.99
STUDENT_TICKET_PRICE = 2.99

def total_ticket_price(number_regular_tickets: int, number_student_tickets: int, is_holiday: bool) -> float:
    '''Returns total price for a given number of regular and student tickets and whether or not it is a holiday
    >>> total_ticket_price(1, 1, True)
    6.98
    >>> total_ticket_price(4, 6, True)
    32.205000000000005
    >>> total_ticket_price(4, 6, False)
    30.510000000000005
    '''
    if (number_regular_tickets + number_student_tickets >= 10):
        if is_holiday:
            return (number_regular_tickets * REGULAR_TICKET_PRICE + number_student_tickets * STUDENT_TICKET_PRICE) * 0.95
        else:
            return (number_regular_tickets * REGULAR_TICKET_PRICE + number_student_tickets * STUDENT_TICKET_PRICE) * 0.9
    else:
        return number_regular_tickets * REGULAR_TICKET_PRICE + number_student_tickets * STUDENT_TICKET_PRICE

def british_time(toronto_time: float, toronto_dst: bool, london_dst: bool) -> float:
    '''Return the British time given the time in toronto and whether or not toronto has dst and london has dst
    >>> british_time(0.0, True, True)
    6.0
    >>> british_time(12.0, True, False)
    17.0
    >>> british_time(12.0, False, True)
    19.0
    >>> british_time(12.0, False, False)
    18.0
    >>> british_time(23.0, False, False)
    5.0
    '''
    if toronto_dst and london_dst:
        british_time = toronto_time + 6
    elif toronto_dst and not london_dst:
        british_time = toronto_time + 5
    elif not toronto_dst and london_dst:
        british_time = toronto_time + 7
    else:
        british_time = toronto_time + 6

    # if british_time > 24:
    #     british_time = british_time - 24
    # return british_time

    return british_time % 24


if __name__ == '__main__':
    import doctest
    doctest.testmod()