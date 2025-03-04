from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        maxID = 1
        if self.soluongsinhvien() > 0:
            maxID = max(sv._id for sv in self.listSinhVien) + 1
        return maxID

    def soluongsinhvien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh: ")
        major = input("Nhap nganh hoc: ")
        try:
            diemTB = float(input("Nhap diem trung binh: "))
        except ValueError:
            print("Diem trung binh phai la so!")
            return

        sv = SinhVien(svID, name, sex, major, diemTB)
        self.xeploaihocluc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            sv._name = input("Nhap ten moi: ")
            sv._sex = input("Nhap gioi tinh moi: ")
            sv._major = input("Nhap nganh hoc moi: ")
            try:
                sv._diemTB = float(input("Nhap diem trung binh moi: "))
            except ValueError:
                print("Diem trung binh phai la so!")
                return
            self.xeploaihocluc(sv)
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai!")

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        return [sv for sv in self.listSinhVien if keyword.lower() in sv._name.lower()]

    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xeploaihocluc(self, sv):
        if sv._diemTB >= 9:
            sv._hocluc = "Xuat sac"
        elif sv._diemTB >= 8:
            sv._hocluc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocluc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocluc = "Trung binh"
        else:
            sv._hocluc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "Sex", "Major", "DiemTB", "HocLuc"))
        for sv in listSV:
            print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocluc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
