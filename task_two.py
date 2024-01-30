path_to_file = "files\\cats.txt"


def get_cats_info(path):
    try:
        with open(path, "r", encoding="UTF-8", errors="strict") as file:
            cats = [el.strip().split(',') for el in file.readlines()]
            cats_list = []
        if not cats:
            raise ValueError("Файл з даними порожній")
        for id, name, age in cats:
            cat_dict = {"id": id, "name": name, "age": age}

            cats_list.append(cat_dict)

        return cats_list

    except Exception as error:
        print(f"Error: {error}")


print(get_cats_info(path_to_file))
