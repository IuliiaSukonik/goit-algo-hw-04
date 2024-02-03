def get_cats_info(path):
    new_list = []
    try:
        with open(path) as cat:
            cats = [line.strip() for line in cat]
            for el in cats:
                a = el.split(",")
                new_list.append({"id": a[0], "name": a[1], "age": a[2]})
            return(new_list)
    except Exception:
        print(f"Document {path} not correct")

cats_info = get_cats_info("cats_file.txt")
print(cats_info)
