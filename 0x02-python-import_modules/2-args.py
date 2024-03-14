#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    b = len(sys.argv) - 1

    if b == 0:
        print("{} arguments.".format(b))
    elif b == 1:
        print("{} argument:".format(b))
    else:
        print("{} arguments:".format(b))

    if b >= 1:
        b = 0
        for arg in sys.argv:
            if b != 0:
                print("{}: {}".format(b, arg))
            b += 1
