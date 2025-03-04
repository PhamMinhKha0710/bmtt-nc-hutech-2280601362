def chiahetcho5(sonhiphan):
    sothapphan = int(sonhiphan, 2)
    if sothapphan % 5 == 0:
        return True
    else:
        return False
chuoinhiphan = input("Nhap chuoi nhi phan(phan tach boi dau phay): ")
so_nhi_phan_list = chuoinhiphan.split(',')
so_chia_het_cho_5 = [so for so in so_nhi_phan_list if chiahetcho5(so)]
if (so_chia_het_cho_5):
    ket_qua = ','   .join(so_chia_het_cho_5)
    print("So chia het cho 5 la: ", ket_qua)
else:
    print("Khong co so nao chia het cho 5")