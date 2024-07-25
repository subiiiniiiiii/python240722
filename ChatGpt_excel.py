import openpyxl
import random

# 제품 ID 생성
def generate_product_id(index):
    return f'P{index:03d}'

# 제품명 생성
def generate_product_name():
    product_names = ["Laptop", "Smartphone", "Tablet", "Smartwatch", "Monitor", "Headphones", "Keyboard", "Mouse", "Printer", "Camera"]
    return random.choice(product_names)

# 수량 생성
def generate_quantity():
    return random.randint(1, 100)

# 가격 생성
def generate_price():
    return round(random.uniform(50, 1000), 2)

# 데이터 생성
products = []
for i in range(1, 101):
    product_id = generate_product_id(i)
    product_name = generate_product_name()
    quantity = generate_quantity()
    price = generate_price()
    products.append([product_id, product_name, quantity, price])

# 엑셀 파일 생성
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Products"

# 헤더 추가
headers = ["Product ID", "Product Name", "Quantity", "Price"]
sheet.append(headers)

# 데이터 추가
for product in products:
    sheet.append(product)

# 엑셀 파일 저장
file_name = "products.xlsx"
workbook.save(file_name)

print(f"{file_name} 파일이 생성되었습니다.")
