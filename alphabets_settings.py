import alphabets

def printPattern(sequence, size=5, sym="*"):
    obj = alphabets.Alphas(trow=size, sym=sym)
    letter_methods = {
        "a": obj.a,
        "b": obj.b,
        "c": obj.c,
        "d": obj.d,
        "e": obj.e,
        "f": obj.f,
        "g": obj.g,
        "h": obj.h,
        "i": obj.i,
        "j": obj.j,
        "k": obj.k,
        "l": obj.l,
        "m": obj.m,
        "n": obj.n,
        "o": obj.o,
        "p": obj.p,
        "q": obj.q,
        "r": obj.r,
        "s": obj.s,
        "t": obj.t,
        "u": obj.u,
        "v": obj.v,
        "w": obj.w,
        "x": obj.x,
        "y": obj.y,
        "z": obj.z,
    }
    for letter in sequence:
        method = letter_methods.get(letter.lower())
        if method:
            method()
        else:
            print("None")
        print()
