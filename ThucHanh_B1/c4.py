import json

def load_data():
    with open("fileData/hello.json", encoding='utf-8') as f:
        return json.load(f)


def display(employee=[]):
    for em in employee:
        for k, v in em.items():
            if k.__eq__('ma_nv'):
               print(f"Ma nhan vien: {v}")
            elif k.__eq__('ten_nv'):
                print(f"Ten nhan vien: {v}")


def add_employee(employees, id, name):
    e = {
        'ma_nv': id,
        'ten_nv': name
    }
    employees.append(e)
    with open("fileData/hello.json", mode='w', encoding='utf-8') as f:
        json.dump(employees, f, ensure_ascii=False, indent=4)


def delete_em(empployee, ma_nv):
    for indx, em in enumerate(employee):
        if em['ma_nv'] == ma_nv:
            del employee[indx]
    with open("fileData/hello.json", mode='w', encoding='utf-8') as f:
        json.dump(employee, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    employee = load_data()
    display(employee)
    add_employee(employee, 2, "Nguyen Van A")
    print("Sau khi them vao danh sach")
    display(employee)
    delete_em(employee,2)
    print("Sau khi xoa ma nhan vcien 2 thi")
    display(employee)