# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.

# Чтение исходного файла
with open("user_data.txt", "r") as file:
        print(file.read())
# Ввод текста
my_text1 =input("введите строку 1 : ")
my_text2 =input("введите строку 2 : ")

# Текст с переводом строки
my_text = "Съешь же ещё этих мягких \n французских булок да выпей чаю"
# with open("user_data.txt", "w", encoding="utf-8") as file:
print("")
# Запись текста
with open("user_data.txt", "w") as file:
    file.write(my_text1)
    file.write("\n")
    file.write(my_text2)
    file.write("\n")
    file.write("\n")
    file.write(my_text)
# Вывод результата
file = open("user_data.txt")
text = file.read( )
print(text)
file.close()
