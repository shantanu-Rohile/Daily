# 7. Handle KeyboardInterrupt Exception When Reading Input

def k_e():
    try:
        while(True):
            print("running ...")
    except KeyboardInterrupt:
        print("Exccution forecefully stopped")

k_e()
