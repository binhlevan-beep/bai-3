print("Sinh viên : Lê Văn Bình")
print("MSSV : 235752020710002")

def checkValue(n):
    if n % 2 == 0:
        print("số chẵn")
    else:
        print("số lẻ")

n = int(input("Nhập một số nguyên: "))
checkValue(n)
