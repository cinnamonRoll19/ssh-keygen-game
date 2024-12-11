from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def gen_k(s):
    pr = rsa.generate_private_key(
        public_exponent=65537,
        key_size=s,
        backend=default_backend()
    )
    
    pub = pr.public_key()
    
    # Сериализация приватного ключа
    pr_pem = pr.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
    )
    
    # Сериализация публичного ключа
    pub_pem = pub.public_bytes(
        encoding=serialization.Encoding.OpenSSH,
        format=serialization.PublicFormat.OpenSSH,
    )
    
    return pr_pem, pub_pem

def main():
    print("Добро пожаловать в игру-генератор SSH ключей!")
    print("Выберите уровень сложности:")
    print("1. Легкий (2048 бит)")
    print("2. Средний (3072 бит)")
    print("3. Сложный (4096 бит)")

    ch = input("Введите номер уровня сложности (1-3): ")
    
    if ch == '1':
        s = 2048
    elif ch == '2':
        s = 3072
    elif ch == '3':
        s = 4096
    else:
        print("Неверный выбор! Попробуйте еще раз.")
        return

    print(f"Генерация SSH ключа размером {s} бит...")
    pr_key, pub_key = gen_k(s)
    
    print("\nВаш сгенерированный приватный SSH ключ:")
    print(pr_key.decode())
    
    print("\nВаш сгенерированный публичный SSH ключ:")
    print(pub_key.decode())

if name == "__main__":
    main()
