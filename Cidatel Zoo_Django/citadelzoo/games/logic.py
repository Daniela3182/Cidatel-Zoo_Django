import random

def level_range(level:int):
    ranges = {
        1: (0, 10),
        2: (0, 20),
        3: (0, 50),
        4: (0, 100),
        5: (0, 200),
    }
    return ranges.get(level, (0, 10))

def gen_sumas(level, n=10):
    lo, hi = level_range(level)
    for _ in range(n):
        a, b = random.randint(lo, hi), random.randint(lo, hi)
        yield f"{a} + {b} =", a + b

def gen_restas(level, n=10):
    lo, hi = level_range(level)
    for _ in range(n):
        a, b = random.randint(lo, hi), random.randint(lo, hi)
        if a < b: a, b = b, a
        yield f"{a} - {b} =", a - b

def gen_mult(level, n=10):
    table = {1:(0,5),2:(0,8),3:(0,10),4:(0,12),5:(0,12)}
    lo, hi = table.get(level,(0,10))
    for _ in range(n):
        a, b = random.randint(0,12), random.randint(lo, hi)
        yield f"{a} × {b} =", a * b

def gen_div(level, n=10):
    table = {1:(1,5),2:(1,8),3:(1,10),4:(1,12),5:(1,12)}
    lo, hi = table.get(level,(1,10))
    for _ in range(n):
        b = random.randint(lo, hi)
        a = b * random.randint(0,12)
        yield f"{a} ÷ {b} =", a // b

def generator_for(game_type):
    return {
        'sumas': gen_sumas,
        'restas': gen_restas,
        'multiplicacion': gen_mult,
        'division': gen_div,
    }.get(game_type, gen_sumas)
