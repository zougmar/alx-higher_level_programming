#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for RSLT in dir(hidden_4):
        if RSLT[0] != '_' and RSLT[1] != '_':
            print(RSLT)
