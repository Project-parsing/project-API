from wrapper_for_argon import ArgonHasher

hasher = ArgonHasher()
password = "pass2"

# Генерация хеша
hash1 = hasher.hash(password)
print("Generated hash:", hash1)

# Проверка хеша
print("Verification result:", hasher.verify(hash1, password))  # Должно быть True

# Проверка хеша из вашей БД
db_hash = "$2a$10$qJbKI33WMcxIDCNBYNWj9O1UDRMZbPIC4ITOBAbXJERRrBg31m./2"
print("DB hash verification:", hasher.verify(db_hash, password))  # Должно быть True