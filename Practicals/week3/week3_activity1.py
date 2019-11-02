
def is_rich(my_account: float) -> bool:
    return my_account >= 1000000

def is_close(my_account: float) -> bool:
    return my_account < min_balance + 30

def can_join_CSC267(g: float, CSC108: bool, MAT102: bool) -> bool:
    return (g >= 2.7) and (CSC108 or MAT102)

def can_join_CSC267_2(g:bool, CSC108: bool, MAT102: bool) -> bool:
    return g and (CSC108 or MAT102)



