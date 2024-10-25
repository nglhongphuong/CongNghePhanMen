#  Viết chương trình thực hiện việc xử lý từ điển
#  Anh – Việt, chương trình thực hiện
# các chức năng sau
# a) Thêm một từ mới vào từ điển.
# b) Hiển thị từ điển, cho biết từ điển hiện tại cho bao nhiêu từ.
# c) Tìm kiếm từ tiếng Anh, nếu tìm thấy thì hiển thị key và value.
# Nếu không tìm thấy
# thì thông báo không tìm thấy.
# d) Xoá một từ trong từ điển dựa trên key cung cấp
words = {}
def display():
    for k, v in words.items():
        print(f"{k} -> {v}")

def add_value(key, value):
    if key not in words:
        words[key] = value
    else:
        print("Da ton tai !!")
def delete_value(value):
    if value in words:
        del words[value]
        print("Da xoa thanh cong!!")
        display()
    else:
        print("Khong tim thay gia tri can xoa!")

if __name__ == '__main__':
    n = int(input("Nhap n: "))
    for i in range (n):
        print(f"- Nhap dic[{i}] ")
        key = str(input("- Nhap words: "))
        value = str(input("- Nhap means: "))
        add_value(key= key, value=value)

    display()
    del_word = str(input("Nhap tu can xoa: "))
    delete_value(del_word)
