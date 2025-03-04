def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhap danh sach cac so, cach nhau boi dau phay: ").split(',')
numbers = list(map(int, input_list))
reversed_numbers = dao_nguoc_list(numbers)
print("Danh sach sau khi dao nguoc: ", reversed_numbers)