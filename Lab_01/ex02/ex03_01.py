def tinh_tong_so_chan(lst):
    tong = 0   
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong
input_list = input("Nhap danh sach cac so, cach nhau boi dau phay: ")
numbers = [int(x) for x in input_list.split(',')]
result = tinh_tong_so_chan(numbers)
print("Tong cac so chan trong danh sach la:", result)