def total_salary(path):
    total = 0
    average = 0
    new_list = []
    try:
        with open(path) as worker:
            workers = [line.strip() for line in worker]
            for el in workers:
                a = el.split(",")
                new_list.append({"name": a[0], "salary": a[1]})
            for dict in new_list:
                total += float(dict.get("salary"))
            average = float(total/len(new_list))
            return total, average

    except Exception:
        print(f"Document {path} not correct")


total, average = total_salary("salary.txt")
print(
    f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
