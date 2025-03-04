def truy_cap_phan_tu_cuoi_cung(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
input_tuple = eval(input("Nhập một tuple: "))
first, last = truy_cap_phan_tu_cuoi_cung(input_tuple)
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)