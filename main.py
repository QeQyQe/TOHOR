d = 5
a = float(input("Введди наименьшее число "))
b = float(input("Введди наибольшее число "))
n = int((b - a) // 0.25)
if (a - int(a)) <= 0.25:
    kjh = int(a) + 0.25
if 0.25 < (a - int(a)) <= 0.5:
    kjh = int(a) + 0.5
if 0.5 < (a - int(a)) <= 0.75:
    kjh = int(a) + 0.75
if 0.75 < (a - int(a)):
    kjh = int(a) + 1
sp = []
# kjh=float(input())
asd = 0
for k in range(n+1):
    sp.append(kjh + asd)
    asd = asd + 0.25

if a > b:
    kl = a - b
else:
    kl = b - a
for i in range(n+1):
    if 5<=((sp[i] - a) * d) / kl:
        break
    print(sp[i],((sp[i] - a) * d) / kl)
input()
print('KO')
