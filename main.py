# vazifa 1
import asyncio

async def cheek_password(password):
    updated_password = ""
    i = 0

    while i < len(password):
        char = password[i]
        if not char.isdigit():
            updated_password += char
        i += 1
        await asyncio.sleep(0.1)

    return updated_password

async def main():
    password = "P4s5w0rd123"
    result = await cheek_password(password)
    print(f"Yangilangan parol: {result}.")


asyncio.run(main())

# ==================================================================

# vazifa 2
import asyncio

async def harf_kesib_olish(text):
    result = ""
    i = 0

    while i < len(text) and i < 10:
        result += text[i]
        i += 1
        await asyncio.sleep(0.1)

    return result

async def main():
    text = "Hello, World!"
    truncated_text = await harf_kesib_olish(text)
    print(f"Birinchi 10 belgi: {truncated_text}")

asyncio.run(main())

# ==================================================================

# vazifa 3
import asyncio

async def remove_digits_from_name(name):
    clean_name = ""
    i = 0

    while i < len(name):
        char = name[i]
        if not char.isdigit():
            clean_name += char
        i += 1
        await asyncio.sleep(0.1)

    return clean_name

async def main():
    name = "A23si1lb3ek32"
    clean_name = await remove_digits_from_name(name)
    print(f"Tozalangan ism: {clean_name}")

asyncio.run(main())

# ==================================================================

# vazifa 4
import asyncio

async def process_text(text):
    processed_text = ""
    i = 0

    while i < len(text):
        char = text[i]
        if not char.isspace():
            processed_text += char.lower()
        i += 1
        await asyncio.sleep(0.1)

    return processed_text

async def main():
    text = "Hello, World!"
    result = await process_text(text)
    print(f"Qayta ishlangan matn: {result}")

asyncio.run(main())

# ==================================================================

# vazifa 5
import asyncio

async def extract_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    i = 0

    while i < len(text):
        char = text[i]
        if char in vowels:
            result += char
        i += 1
        await asyncio.sleep(0.1)

    return result

async def main():
    text = "Hello, World"
    vowel_text = await extract_vowels(text)
    print(f"Unli harflar: {vowel_text}")

asyncio.run(main())

# ==================================================================

# vazifa 6
import asyncio

async def replace_ab_with_hash(word):
    result = ""
    i = 0

    while i < len(word):
        if i < len(word) - 1 and word[i] == "a" and word[i + 1] == "b":
            result += "#"
            i += 2
        else:
            result += word[i]
            i += 1
        await asyncio.sleep(0.1)

    return result

async def main():
    word = "abdulloh, abstrakt"
    modified_word = await replace_ab_with_hash(word)
    print(f"Yangilangan so'z: {modified_word}")

asyncio.run(main())

# ==================================================================

# vazifa 7
import asyncio


async def reverse_numeric_text(text):
    if not text.isdigit():
        return "Matnda faqat raqamlar bo'lishi kerak!"

    reversed_text = ""
    i = len(text) - 1

    while i >= 0:
        reversed_text += text[i]
        i -= 1
        await asyncio.sleep(0.1)

    return reversed_text


async def main():
    numeric_text = "408069588"
    result = await reverse_numeric_text(numeric_text)
    print(f"Teskari matn: {result}")


asyncio.run(main())

# ==================================================================

# vazifa 8
import asyncio

async def remove_middle_character(word):
    if len(word) == 0:
        return "So'z bo'sh bo'lmasligi kerak!"

    middle_index = len(word) // 2
    result = ""
    i = 0

    while i < len(word):
        if i != middle_index:
            result += word[i]
        i += 1
        await asyncio.sleep(0.1)

    return result

async def main():
    word = "Asilbek"
    modified_word = await remove_middle_character(word)
    print(f"O'rtasidan olingan so'z: {modified_word}")

asyncio.run(main())

# ==================================================================

# vazifa 9
import asyncio

async def process_name(name):
    result = ""
    i = 0

    while i < len(name):
        result += name[i]
        i += 1
        await asyncio.sleep(0.1)

    if result.endswith("a"):
        result = result.lower()

    return result

async def main():
    name = "Muxilsa"
    processed_name = await process_name(name)
    print(f"Yangilangan ism: {processed_name}")

asyncio.run(main())

# ==================================================================

# vazifa 10
import asyncio

async def remove_duplicate_characters(text):
    seen = set()
    result = ""
    i = 0

    while i < len(text):
        char = text[i]
        if char not in seen:
            result += char
            seen.add(char)
        i += 1
        await asyncio.sleep(0.1)

    return result

async def main():
    text = "Hello World"
    unique_text = await remove_duplicate_characters(text)
    print(f"Takrorlanmaydigan harflar: {unique_text}")

asyncio.run(main())

# ==================================================================

# vazifa 11
import asyncio

async def process_vowel_word(word):
    vowels = "aeiouAEIOU"
    is_vowel_word = True

    i = 0
    while i < len(word):
        if word[i] not in vowels:
            is_vowel_word = False
        i += 1
        await asyncio.sleep(0.1)

    if is_vowel_word:
        return word.upper()
    else:
        return word

async def main():
    word = "eouia"
    modified_word = await process_vowel_word(word)
    print(f"Yangilangan so'z: {modified_word}")

asyncio.run(main())

# ==================================================================

# vazifa 12
import requests
import asyncio
import time

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

API_KEY = "834fd3eb83628ebc7f9367e2591d9328"

async def get_weather(city_name):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=uz"
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            temp = data['main']['temp']
            weather = data['weather'][0]['description']
            print(f"{GREEN}---------------------------------------------")
            print(f"Shahar nomini kiritdingiz: {city_name}")
            print(f"Hozir {city_name} shahrida havo harorati: {temp:.2f} gradus. Havo: {weather}.")
            print(f"---------------------------------------------{RESET}")
        else:
            print(f"{RED}Shahar nomi noto'g'ri kiritildi!!!{RESET}")
    except Exception as e:
        print(f"{RED}Xatolik yuz berdi: {e}{RESET}")

async def main():
    start_time = time.time()
    print(f"{CYAN}Dasturni tugatish uchun 'stop' deb yozing.{RESET}")
    while True:
        city_name = input("Shahar nomini kiriting: ").strip()
        if city_name.lower() == "stop":
            break
        await get_weather(city_name)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{YELLOW}---------------------------------------------")
    print("Dastur to'xtadi!!!")
    print(f"{elapsed_time:.3f} sekund vaqt davomida ishladi!!!")
    print(f"---------------------------------------------{RESET}")

if __name__ == "__main__":
    asyncio.run(main())

