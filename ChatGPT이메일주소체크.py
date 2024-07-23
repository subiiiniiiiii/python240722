import re

def is_valid_email(email):
    # 이메일 주소의 정규 표현식 패턴
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

# 샘플 이메일 주소
sample_emails = [
    "example@example.com",
    "user.name+tag+sorting@example.com",
    "user_name@sub.example.co.uk",
    "user-name@example.com",
    "user@com",
    "user@.com",
    "user@com.",
    "user@domain.com"
    "@example.com",
    "user@-example.com"
]

# 이메일 주소 유효성 검사
for email in sample_emails:
    print(f"{email}: {'Valid' if is_valid_email(email) else 'Invalid'}")
