def max_binary_num(num_bits):
    """Вычисляем максимальное число, заданное num_bits битами"""
    return ~(~0 << num_bits)

def add_without_overflow(x, y, num_bits):
    """Складываем два числа, предотвратив переполнение"""
    max_num = max_binary_num(num_bits)
    result = x + y
    if result <= max_num:
        return result
    return result & max_num

def twos_complement(n, num_bits):
    """Вычисляем двоичное дополнение"""
    mask = 1
    i = 0
    while i < num_bits:
        mask = (mask << 1) | 1
        i += 1
    return add_without_overflow((~n) & mask, 1, num_bits)

def subtract_using_twos_complement(bigger, smaller):
    """Вычитание чисел с использованием двоичного дополнения"""
    num_bits = bigger.bit_length()
    if smaller.bit_length() > num_bits:
        num_bits = smaller.bit_length()
    num_bits_plus_2 = num_bits
    i = 0
    while i < 2:
        num_bits_plus_2 += 1
        i += 1
    smaller_comp = twos_complement(smaller, num_bits_plus_2)
    result = add_without_overflow(bigger, smaller_comp, num_bits_plus_2)
    if result & (1 << num_bits_plus_2):
        return twos_complement(result, num_bits_plus_2)
    return result