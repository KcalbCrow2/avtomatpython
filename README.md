# avtomatpython
тут да я сделяль



Ответ: `B408MX77 черный Kia Ceed `
Фото: https://ibb.co/SwPLj3Qx

Поиск российских номерных знаков в латинской транслитерации...
Поиск с кодами регионов...
🎉 НАЙДЕНО! Номерной знак: B408MX77
~1930.8 тыс возможных результатов
|| B408MX77 ||
Время выполнения функции 1.5684471130371094 сек.
PS C:\Users\KcalbCrow\Documents\program\mat6>






код

import hashlib
import time
import itertools

def solve_problem(target1, target2):
    start_time = time.time()
    
    
    letters = 'ABEKMHOPCTYX'  
    digits = '0123456789'
    
   
    regions = ['77', '97', '99', '177', '197', '199', '777', '50', '90', '150']
    
    counter = 0
    found = None
    
    print("Поиск российских номерных знаков в латинской транслитерации...")
    
    
    for l1 in letters:
        for d1, d2, d3 in itertools.product(digits, repeat=3):
            for l2, l3 in itertools.product(letters, repeat=2):
                plate = f"{l1}{d1}{d2}{d3}{l2}{l3}"
                counter += 1
                
                md5_hash = hashlib.md5(plate.encode()).hexdigest()
                if md5_hash == target1:
                    sha256_hash = hashlib.sha256(plate.encode()).hexdigest()
                    if sha256_hash == target2:
                        found = plate
                        break
            if found:
                break
        if found:
            break
        
        if counter % 100000 == 0:
            elapsed = time.time() - start_time
            print(f"Проверено: {counter} комбинаций, время: {elapsed:.1f}с")
    
    
    if not found:
        print("Поиск с кодами регионов...")
        for region in regions:
            for l1 in letters:
                for d1, d2, d3 in itertools.product(digits, repeat=3):
                    for l2, l3 in itertools.product(letters, repeat=2):
                        plate = f"{l1}{d1}{d2}{d3}{l2}{l3}{region}"
                        counter += 1
                        
                        md5_hash = hashlib.md5(plate.encode()).hexdigest()
                        if md5_hash == target1:
                            sha256_hash = hashlib.sha256(plate.encode()).hexdigest()
                            if sha256_hash == target2:
                                found = plate
                                break
                    if found:
                        break
                if found:
                    break
            if found:
                break
            
            if counter % 100000 == 0:
                elapsed = time.time() - start_time
                print(f"Проверено: {counter} комбинаций, время: {elapsed:.1f}с")
    
    end_time = time.time()
    
    if found:
        print(f"🎉 НАЙДЕНО! Номерной знак: {found}")
       
    else:
        print("❌ Номерной знак не найден")
        print("Возможно, нужно проверить другие форматы:")
        print("- Номера СТС/ПТС")
        print("- VIN российских автомобилей")
        print("- Другие коды регионов")
    
    print(f"~{counter/1000:.1f} тыс возможных результатов")
    if found:
        print(f"|| {found} ||")
    else:
        print("|| Не найдено ||")
    print(f"Время выполнения функции {end_time - start_time} сек.")
    
    return found

if __name__ == "__main__":
    target1 = "743f0ed26d2bff34fb9a335588238ceb"
    target2 = "ef581243eb6f7fa74ce03466b9051464275c6b34017a6f031f2548a6d5d0b711"
    
    solve_problem(target1, target2)
