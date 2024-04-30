import csv


def csv_to_list(file_name):
    copy_list = []
    with open(file_name, 'r', newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for i in csv_reader:
            copy_list.append(i)
    return copy_list


def write_csv(File_name, col_names):
    with open(File_name, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(col_names)


def add_data(file_name, products):
    with open(file_name, "a", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([products])


def show_products(id):
    copy_list = csv_to_list("product.csv")
    return copy_list[id]


def show_products_csv():
    print("-" * 36)
    counter = 1
    print("|", "ID"
               "|", csv_to_list("product.csv")[0][1],
          "|", csv_to_list("product.csv")[0][2],
          "|", csv_to_list("product.csv")[0][3])
    print("-" * 36)

    for i in csv_to_list("product.csv"):
        if i[0] == "Pr_id":
            continue
        print("|", counter, " "
                            "|", i[1], " " * (6 - len(i[1])),
              "|", i[2], " " * (4 - len(i[2])),
              "|", i[3], " " * (7 - len(i[3])), "|")
        counter += 1
    print("-" * 36)


def show_basket_csv():
    print("-" * 37)
    print("|", csv_to_list('basket.csv')[0][0],
          "|", csv_to_list("basket.csv")[0][1],
          "|", csv_to_list("basket.csv")[0][2],
          "|", csv_to_list("basket.csv")[0][3], "|")
    print("-" * 37)

    for i in csv_to_list("basket.csv"):
        if i[0] == "Product":
            continue
        if len(i[0]) > 1:
            i = i[0].split(',')
            print("|", i[0], "",
                  "|", i[1], " "*(7-len(i[1])),
                  "|", i[2], " ",
                  "|", i[3], " "*(7-len(i[3])), "|")

    print("-" * 37)


col_names = ["Product", "Price", "Amount", "Total"]
write_csv("basket.csv", col_names)

while True:
    print("1-Show product")
    print("2-Show me basket")
    print("3-Quit")
    menu = input("Enter your choice: ")

    if menu == "1":
        show_products_csv()
        user = input("Do you want to buy anything(1-yes/2-no)? ")
        if user == "1":
            products = []
            user_choice = int(input("Enter product Id"))
            product = show_products(user_choice)
            products.append(str(product[1]))
            price = show_products(user_choice)[2]
            products.append(str(price))
            amount = int(input(f"Enter product {product[1]} quantity"))
            products.append(str(amount))
            if amount < float(product[3]):
                total = float(price) * amount
                products.append(str(total))
                add_data("basket.csv", ','.join(products))
            else:
                print(f'This product hav only {product[3]} quantity')
    elif menu == "2":
        if csv_to_list("basket.csv")[1:]:
            show_basket_csv()
        else:
            print("No products")

    else:
        break
