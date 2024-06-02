import json
import random

BOX_SIZE = 360


class Delivery:
    def __init__(self):
        pass

    def get_from_json(self, path):
        with open(path) as fh:
            data = json.load(fh)
            return data

    def dump_to_file(self, data, path):
        full_path = "output_jsons/" + path
        with open(full_path, "w") as fh:
            json.dump(data, fh)

    def create_box(self, product, type):
        dict = {}
        dict["type"] = type
        dict["id"] = random.randrange(100000)
        dict["product_type_name"] = product["product_name"]
        for key, value in random.choice(product["names_manufacturers"]).items():
            dict["product_name"] = key
            dict["manufacturer_name"] = value
        dict["price"] = random.randrange(product["min_price"], product["max_price"])
        dict["size"] = product["size"]
        dict["product_count"] = BOX_SIZE / product["size"]
        if BOX_SIZE % product["size"] != 0:
            raise Exception("Invalid size", product["product_name"])
        return dict

    def get_boxes(self, in_data, type, num):
        boxes = []
        products = in_data.get("products")
        while num > 0:
            boxes.append(self.create_box(random.choice(products), type))
            num -= 1

        return boxes

    def create_delivery(self, size: int, type1, type2="", type3=""):
        boxes = []
        sizes = {"size": size}
        out_data = {"size": sizes, "boxes": boxes}

        in_data = self.get_from_json(f"ProductTypes/{type1}.json")
        in_data2 = None
        in_data3 = None

        type1_num = size
        if type2 != "":
            in_data2 = self.get_from_json(f"ProductTypes/{type2}.json")
            min2_count = int(in_data2.get("min_count", 0))
            max2_count = int(in_data2.get("max_count", 0))
            type1_num = random.randrange(size // 2, size)

        if type3 != "":
            in_data3 = self.get_from_json(f"ProductTypes/{type3}.json")
            min3_count = int(in_data3.get("min_count", 0))
            max3_count = int(in_data3.get("max_count", 0))

            type2_num = random.randrange(type1_num, size)
            type3_num = size - type1_num - type2_num
        else:
            type2_num = size - type1_num

        sizes[f"{type1}"] = type1_num
        boxes += self.get_boxes(in_data, type1, type1_num)
        if type2 != "":
            sizes[f"{type2}"] = type2_num
            boxes += self.get_boxes(in_data2, type2, type2_num)

            if type3 != "":
                sizes[f"{type3}"] = type3_num
                boxes += self.get_boxes(in_data3, type2, type3_num)
        return out_data

    def get_products(self, in_data, size, type):
        dict = {}
        products = in_data.get("products")
        Size = {"small": (1, 3), "medium": (3, 6), "big": (8, 15)}
        product = random.choice(products)
        dict["type"] = type
        dict["product_type_name"] = product["product_name"]
        for key, value in random.choice(product["names_manufacturers"]).items():
            dict["product_name"] = key
            dict["manufacturer_name"] = value
        dict["quantity"] = random.randrange(Size[size][0], Size[size][1])
        return dict

    def create_request(self, items, size, type):
        products = []
        out_data = {"products": products}
        in_data = self.get_from_json(f"ProductTypes/{type}.json")
        while items != 0:
            products.append(self.get_products(in_data, size, type))
            items -= 1
        return out_data
