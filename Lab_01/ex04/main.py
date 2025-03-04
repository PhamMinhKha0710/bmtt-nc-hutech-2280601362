from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nChuong Trinh Quan Ly Sinh Vien")
    print("================MENU================")
    print("1. Them Sinh Vien")
    print("2. Cap nhat thong tin sinh vien")
    print("3. Xoa sinh vien")
    print("4. Tim kiem sinh vien theo ten")
    print("5. Sap xep sinh vien theo diem trung binh")
    print("6. Sap xep sinh vien theo ten chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("8. Thoat")
    print("====================================")
    
    try:
        key = int(input("Nhap lua chon: "))
    except ValueError:
        print("Vui lòng nhập một số hợp lệ!")
        continue

    if key == 1:
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print('\nThem sinh vien thanh cong!')

    elif key == 2:
        if qlsv.soluongsinhvien() > 0:
            print("\n2. Cap nhat thong tin sinh vien")
            try:
                ID = int(input("Nhap ID: "))
                qlsv.updateSinhVien(ID)
                print("\nCap nhat sinh vien thanh cong!")
            except ValueError:
                print("ID phải là số nguyên!")
        else:
            print("Danh sach sinh vien rong!")

    elif key == 3:
        if qlsv.soluongsinhvien() > 0:
            try:
                ID = int(input("\nNhap ID sinh vien can xoa: "))
                if qlsv.deleteByID(ID):
                    print(f"\nSinh vien co ID = {ID} da bi xoa")
                else:
                    print(f"\nSinh vien co ID = {ID} khong ton tai!")
            except ValueError:
                print("ID phải là số nguyên!")
        else:
            print("Danh sach sinh vien rong!")

    elif key == 4:
        keyword = input("Nhap ten sinh vien can tim: ")
        results = qlsv.findByName(keyword)
        if results:
            qlsv.showSinhVien(results)
        else:
            print("Khong tim thay sinh vien!")

    elif key == 5:
        qlsv.sortByDiemTB()
        print("\nDanh sach sinh vien sau khi sap xep theo diem trung binh:")
        qlsv.showSinhVien(qlsv.getListSinhVien())

    elif key == 6:
        qlsv.sortByName()
        print("\nDanh sach sinh vien sau khi sap xep theo ten chuyen nganh:")
        qlsv.showSinhVien(qlsv.getListSinhVien())

    elif key == 7:
        print("\nDanh sach sinh vien hien tai:")
        qlsv.showSinhVien(qlsv.getListSinhVien())

    elif key == 8:
        print("\nThoat chuong trinh!")
        break

    else:
        print("Lua chon khong hop le, vui long nhap lai!")
