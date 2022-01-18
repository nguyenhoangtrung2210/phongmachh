from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from app import db


class User(db.Model):
    __tablename__ = "nhanvien"
    maNhanVien = Column(Integer, primary_key=True,autoincrement=True)
    hoTen = Column(String(50), nullable=False)
    gioiTinh = Column(String(50), nullable=False)
    ngaySinh = Column(Date, nullable=False)
    diaChi = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    contact = Column(String(50), nullable=False)

    def __str__(self):
        return self.hoTen

class Product(db.Model):
    __tablename__= "thuoc"
    maThuoc = Column(Integer, primary_key=True,autoincrement=True)
    tenThuoc = Column(String(50), nullable=False)
    moTa = Column(String(50), nullable=True)
    giaTien = Column(Float,default=0)
    hinhAnh = Column(String(50), nullable=True)

    def __str__(self):
        return self.tenThuoc

class KhamBenh(db.Model):
    __tablename__ = "danhsachkhambenh"
    maKB = Column(Integer, primary_key=True,autoincrement=True)
    hoTen = Column(String(50), nullable=False)
    gioiTinh = Column(String(50), nullable=False)
    ngaySinh = Column(Date)
    diaChi = Column(String(50), nullable=False)

    def __str__(self):
        return self.hoTen


class BenhNhan(db.Model):
    __tablename__ = "danhsachbenhnhan"
    maBN = Column(Integer, primary_key=True,autoincrement=True)
    hoTen = Column(String(50), nullable=False)
    ngayKham = Column(Date)
    loaiBenh = Column(String(50), nullable=False)
    trieuchung = Column(String(50), nullable=False)

    def __str__(self):
        return self.hoTen

class PhieuKhamBenh(db.Model):
    __tablename__ = "phieukhambenh"
    maPKB = Column(Integer, primary_key=True,autoincrement=True)
    hoTen = Column(String(50), nullable=False)
    ngayKham = Column(Date)
    trieuchung = Column(String(50), nullable=False)
    tenThuoc = Column(String(50), nullable=False)
    soLuong = Column(Integer)
    cachDung = Column(String(50), nullable=False)
    maBN = Column(Integer,ForeignKey(BenhNhan.maBN),nullable=False)

    def __str__(self):
        return self.hoTen

class HoaDon(db.Model):
    __tablename__ = "hoadon"
    maHoaDon= Column(Integer, primary_key=True,autoincrement=True)
    ngayBan = Column(Date)
    tienThuoc = Column(Float,default=0)
    tienKham = Column(Float,default=0)
    maPKB = Column(Integer,ForeignKey(PhieuKhamBenh.maPKB),nullable=False)

class ChiTietHoaDon(db.Model):
    __tablename__ = "chitiethoadon"
    maPKB = Column(Integer,ForeignKey(PhieuKhamBenh.maPKB),primary_key=True)
    maThuoc = Column(Integer,ForeignKey(Product.maThuoc),primary_key=True)
    soLuong = Column(Integer)
    cachDung = Column(String(50), nullable=False)



if __name__ == "__main__":
    db.create_all()