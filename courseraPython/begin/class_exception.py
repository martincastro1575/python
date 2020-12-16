class B(Exception):
    pass

class C(B):
    pass

class D(Exception):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except B:
        print('BB')
    except C:
        print('C')
    except D:
        print('DD')

