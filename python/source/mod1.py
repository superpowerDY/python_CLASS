def sum(a,b):
    return a+b

def safe_sum(a,b):
    if type(a)  !=type(b):
        print("자료형이 다르기때문에 연산을 할수가 없습니다.!")
        return
    else:
        result = sum(a,b)
    return result