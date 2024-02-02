path_to_file = "files\\dev_salarys.txt"


def total_salary(path):
    try:
        with open(path, 'r', encoding="UTF-8", errors="strict") as file:
            salary_info = [el.strip().split(",") for el in file.readlines()]
            sum = 0
            count = 0
        for _, salary in salary_info:
            sum += int(salary)
            count += 1
        average = sum/count
        result = (sum, int(average))

        return result

    except Exception as error:
        print(f"Error: {error}")


total, average = total_salary(path_to_file)
print(
    f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
