import csv
import matplotlib.pyplot as plt
from datetime import datetime

def calculate_employer_age(DateBirth):
    today = datetime.today()
    employer_age = today.year - DateBirth.year - ((today.month, today.day) < (DateBirth.month, DateBirth.day))
    return employer_age

def generate_employee_statistics():
    try:
        with open('file_exp1.csv', mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            age_categories = {
                "younger_18": {"male": 0, "female": 0},
                "18-45": {"male": 0, "female": 0},
                "45-70": {"male": 0, "female": 0},
                "older_70": {"male": 0, "female": 0}
            }
            gender_count = {"male": 0, "female": 0}

            for row in csv_reader:
                birthdate = datetime.strptime(row["Дата народження"], '%d.%m.%Y')
                age = calculate_employer_age(birthdate)
                if age < 18:
                    age_category = "younger_18"
                elif 18 <= age <= 45:
                    age_category = "18-45"
                elif 45 < age <= 70:
                    age_category = "45-70"
                else:
                    age_category = "older_70"

                if row["Стать"] == "Чоловіча":
                    gender_category = "male"
                    gender_count["male"] += 1
                elif row["Стать"] == "Жіноча":
                    gender_category = "female"
                    gender_count["female"] += 1
                else:
                    continue

                age_categories[age_category][gender_category] += 1

            print("\nРозподіл за статтю:")
            print(f"Чоловіки: {gender_count['male']}")
            print(f"Жінки: {gender_count['female']}")

            show_gender_chart(gender_count)  # Перша діаграма
            show_age_distribution_chart(age_categories)  # Друга діаграма
            show_gender_age_stacked_bar_chart(age_categories)  # Третя діаграма

            print("\nРозподіл за віком:")
            for category, counts in age_categories.items():
                print(f"{category}: {counts['male'] + counts['female']}")

            print("\nРозподіл за статтю та віком:")
            for category, counts in age_categories.items():
                print(f"{category}: Чоловіки - {counts['male']}, Жінки - {counts['female']}")

            print("Ok")

    except FileNotFoundError:
        print("Повідомлення про відсутність, або проблеми при відкритті файлу CSV.")
    except Exception as e:
        print("Помилка:", str(e))


def show_age_distribution_chart(age_categories):
    categories = list(age_categories.keys())
    total_counts = [counts["male"] + counts["female"] for counts in age_categories.values()]
    plt.figure()
    plt.bar(categories, total_counts, color='grey')
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.title('Розподіл за віком')
    plt.xticks(rotation=45)

def show_gender_age_stacked_bar_chart(age_categories):
    categories = list(age_categories.keys())
    male_counts = [counts["male"] for counts in age_categories.values()]
    female_counts = [counts["female"] for counts in age_categories.values()]
    bar_width = 0.35
    index = range(len(categories))
    plt.figure()
    plt.bar(index, male_counts, bar_width, label='Чоловіки', color='blue')
    plt.bar(index, female_counts, bar_width, label='Жінки', color='pink', bottom=male_counts)
    plt.xlabel('Вікова категорія')
    plt.ylabel('Кількість співробітників')
    plt.title('Розподіл за віком та статтю')
    plt.xticks(index, categories, rotation=45)
    plt.legend()

def show_gender_chart(gender_counts):
    labels = 'Чоловіча стать', 'Жіноча стать'
    sizes = [gender_counts["male"], gender_counts["female"]]
    colors = ['blue', 'pink']
    plt.figure()
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Розподіл за статтю')

generate_employee_statistics()
plt.show()