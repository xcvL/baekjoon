# 알람 시계

q = input("")
q = q.split(" ")

hourl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
match int(q[1]) >= 45:
    case True:
        h = int(q[0])
        m = int(q[1]) - 45
    case False:
        h = hourl[hourl.index(int(q[0])) - 1]
        m = int(q[1]) + 15

print(h, m)