print("Sinh vien : Lê Văn Bình")
print("MSSV : 235752020710002")

def get_sum(*num):
    tmp = 0
    # Duyệt các tham số
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print(result)
