from sqlalchemy import DateTime, Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from saleapp import db, app
from datetime import  datetime

class BaseModel(db.Model):
    __abstract__=True# khong  tao bang
    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    __tablename__ = 'category'

    name = Column(String(20), nullable=False)
    products = relationship('Product', backref='category', lazy=True)
    #backref: tự động trong đối tượng product sẽ thêm thuộc tính category
    # mà attribute category agent cho nguyên đối tượng category_id mà product phụ thuộc
    #Lazy: Truy vấn lấy thư mục thì nó chỉ lấy đúng thông tin của danh mục, chưa thực hiện truy vấn products,
    # -> đến khi nào mình tác động lên thì nó mới làm -> tăng hiệu năng
    def __str__(self):
        return self.name

class Product(BaseModel):# Sản phẩm  thuộc nhiều thư mục
    __tablename__ = 'product'

    name=Column(String(50), nullable=False)
    description = Column(String(255))
    price = Column(Float, default=0)
    image = Column(String(100))
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False) #cac khac 'category.id' -> bang du lieu
    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        c1 = Category(name='Dien thoai')
        c2 = Category(name='May tinh bang')
        c3 = Category(name='Dong ho thong minh')

        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)

        db.session.commit()
    #     db.create_all()
