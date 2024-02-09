from colorama import Fore, Style, init
import sys
import os
from pathlib import Path

def directory(path):
    try:
        directory_name = Path(path)
        for new_path in directory_name.iterdir():  # Перебираємо всі файли та папки у каталозі
            if new_path.is_dir():  # Перевіряємо, чи є це папка
                print(Fore.RED + str(new_path))  # Виводимо червоний колір для папок

        for new_path in directory_name.iterdir():  # Знову перебираємо всі файли та папки у каталозі
            if new_path.is_dir():  # Перевіряємо, чи є це папка
                print(Fore.GREEN + str(new_path))  # Виводимо зелений колір для папок
                directory(new_path)  # Рекурсивно викликаємо функцію для папки

    except Exception as e:
        print("ERROR:", e)

if __name__ == "__main__":


    name = sys.argv[1]
    print(name)
