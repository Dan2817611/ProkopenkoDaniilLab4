from faker import Faker
import csv
import random

fake = Faker('uk_UA')
def MiddleNameMale(fake):
    male_middle_names = [
        "Іванович", "Петрович", "Олександрович", "Сергійович", "Михайлович",
        "Дмитрович", "Андрійович", "Миколайович", "Єгорович", "Володимирович"
    ]
    return fake.random_element(male_middle_names)

def MiddleNameFemale(fake):
    female_middle_names = [
        "Іванівна", "Петрівна", "Олександрівна", "Сергіївна", "Михайлівна",
        "Дмитрівна", "Андріївна", "Миколаївна", "Єгорівна", "Володимирівна"
    ]
    return fake.random_element(female_middle_names)

num_records = 2000

records = []

for i in range(num_records):
    if i < num_records * 0.4:
        gender = "Жіноча"
        first_name = fake.first_name_female()
        middle_name = MiddleNameFemale(fake)

    else:
        gender = "Чоловіча"
        first_name = fake.first_name_male()
        middle_name = MiddleNameMale(fake)

    birthdate = fake.date_of_birth(minimum_age=15, maximum_age=85)
    record = {
        "Прізвище": fake.last_name(),
        "Ім’я": first_name,
        "По батькові": middle_name,
        "Стать": gender,
        "Дата народження": birthdate.strftime('%d.%m.%Y'),
        "Посада": fake.job(),
        "Місто проживання": fake.city(),
        "Адреса проживання": fake.address(),
        "Телефон": fake.phone_number(),
        "Email": fake.email()
    }
    records.append(record)

random.shuffle(records)

with open('file_exp1.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    names_field = ["Прізвище", "Ім’я", "По батькові", "Стать", "Дата народження",
                  "Посада", "Місто проживання", "Адреса проживання", "Телефон",
                  "Email"]

    writer = csv.DictWriter(csv_file, fieldnames=names_field)

    writer.writeheader()

    for record in records:
        writer.writerow(record)

print("Файл file_exp1.csv створено.")
