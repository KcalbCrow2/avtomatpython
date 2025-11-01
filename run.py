import hashlib
import time

# Целевые хеши, которые нужно найти
TARGET_MD5 = "743f0ed26d2bff34fb9a335588238ceb"
TARGET_SHA384 = "ef581243eb6f7fa74ce03466b9051464275c6b34017a6f031f2548a6d5d0b711"

# Функции для вычисления хеша
def md5_hex(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

def sha384_hex(s):
    return hashlib.sha384(s.encode('utf-8')).hexdigest()

with open('your_dictionary.txt', 'r', encoding='utf-8') as f:
    dictionary = [line.strip() for line in f]

start_time = time.time()

found = False
result_word = None

print("Начинаем перебор слов...")

for word in dictionary:
    m_hash = md5_hex(word)
    s_hash = sha384_hex(word)

    # Проверка совпадения
    if m_hash == TARGET_MD5 and s_hash == TARGET_SHA384:
        result_word = word
        found = True
        break

# Время выполнения
elapsed_time = time.time() - start_time

if found:
    print("Ответ найден:")
    print(f"Строка: {result_word}")
else:
    print("Совпадений не найдено в данном словаре.")

print(f"Время выполнения: {elapsed_time:.2f} сек")