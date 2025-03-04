soluongiolam = float(input("Nhap so luong gio lam: "))
luonggio = float(input("nhap thu lao moi gio lam tieu chuan: "))
giotieuchuan = 44
giovuotchuan = max(soluongiolam - giotieuchuan, 0)
thuclinh = giotieuchuan * luonggio + giovuotchuan * luonggio * 1.5  
print("Thu nhap cua ban la: ", thuclinh)