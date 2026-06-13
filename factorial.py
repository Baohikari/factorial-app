# Đây là file để viết hàm tính giai thừa, file này là 1 module dự án

# Factorial functions:
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
# Sử dụng đệ quy để tính toán giai thừa
