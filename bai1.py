import random


class GiaSuc:
    def __init__(self, soLuong):
        self.soLuong = soLuong

    def tiengKeu(self):
        pass

    def thongKe(self):
        pass


class Bo(GiaSuc):
    def __init__(self, soLuong):
        super().__init__(soLuong)
        self.sua = [random.randint(0, 20) for _ in range(self.soLuong)]

    def tiengKeu(self):
        print("Bò kêu 'Moo Moo'")

    def thongKe(self):
        return {"loai": "Bò", "soLuong": self.soLuong, "tongSua": sum(self.sua)}


class Cuu(GiaSuc):
    def __init__(self, soLuong):
        super().__init__(soLuong)
        self.sua = [random.randint(0, 5) for _ in range(self.soLuong)]

    def tiengKeu(self):
        print("Cừu kêu 'Baa Baa'")

    def thongKe(self):
        return {"loai": "Cừu", "soLuong": self.soLuong, "tongSua": sum(self.sua)}


class De(GiaSuc):
    def __init__(self, soLuong):
        super().__init__(soLuong)
        self.sua = [random.randint(0, 10) for _ in range(self.soLuong)]

    def tiengKeu(self):
        print("Dê kêu 'Mee Mee'")

    def thongKe(self):
        return {"loai": "Dê", "soLuong": self.soLuong, "tongSua": sum(self.sua)}


# Hàm chạy khi tất cả đói
def tatCaGiaSucDoi(giaSuc):
    for con in giaSuc:
        con.tiengKeu()


# Hàm thống kê thông tin
def thongKe(giaSuc):
    thongTin = [con.thongKe() for con in giaSuc]
    return thongTin


# Khởi tạo số lượng gia súc ban đầu
soLuongBo = int(input("Nhập số lượng bò ban đầu: "))
soLuongCuu = int(input("Nhập số lượng cừu ban đầu: "))
soLuongDe = int(input("Nhập số lượng dê ban đầu: "))

# Tạo đối tượng gia súc
danhsachGiaSuc = [Bo(soLuongBo), Cuu(soLuongCuu), De(soLuongDe)]

print("Tiếng kêu khi tất cả đói:")
tatCaGiaSucDoi(danhsachGiaSuc)

# Sinh con và lược sữa
for giaSuc in danhsachGiaSuc:
    giaSuc.soLuong += random.randint(1, 5)  # Số con sinh ngẫu nhiên
    giaSuc.sua = [
        random.randint(0, 20) for _ in range(giaSuc.soLuong)
    ]  # Lược sữa ngẫu nhiên

print("\nThông tin sau khi sinh con và lược sữa:")
thongTinGiaSuc = thongKe(danhsachGiaSuc)
for thongTin in thongTinGiaSuc:
    print(
        f"{thongTin['loai']}: Số lượng: {thongTin['soLuong']}, Tổng sữa: {thongTin['tongSua']} lít"
    )
