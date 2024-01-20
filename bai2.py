class Ve:
    def __init__(self, ma_ve, ten_chu_ve, nam_sinh, so_tro_choi):
        self.ma_ve = ma_ve
        self.ten_chu_ve = ten_chu_ve
        self.nam_sinh = nam_sinh
        self.so_tro_choi = so_tro_choi


def nhap_danh_sach_ve():
    danh_sach_ve = []
    so_ve = int(input("Nhập số vé: "))

    for i in range(so_ve):
        ma_ve = input("Nhập mã vé: ")
        ten_chu_ve = input("Nhập tên chủ vé: ")
        nam_sinh = int(input("Nhập năm sinh: "))
        so_tro_choi = int(input("Nhập số trò chơi: "))

        ve = Ve(ma_ve, ten_chu_ve, nam_sinh, so_tro_choi)

        danh_sach_ve.append(ve)

    return danh_sach_ve


def tinh_tong_tien(danh_sach_ve):
    tong_tien = 0

    for ve in danh_sach_ve:
        if ve.so_tro_choi == 30:
            tong_tien += 200000
        else:
            tong_tien += 70000 + 20000 * ve.so_tro_choi

    return tong_tien


def dem_ve_tu_phan(danh_sach_ve):
    dem = 0

    for ve in danh_sach_ve:
        if ve.so_tro_choi != 30:
            dem += 1

    return dem

danh_sach_ve = nhap_danh_sach_ve()
tong_tien = tinh_tong_tien(danh_sach_ve)
so_ve_tu_phan = dem_ve_tu_phan(danh_sach_ve)

print("Tổng tiền vé mà công viên thu được: {} VNĐ".format(tong_tien))
print("Số vé đã bán là vé từng phần: {}".format(so_ve_tu_phan))