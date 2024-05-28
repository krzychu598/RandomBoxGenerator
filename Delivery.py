import json
import random


# max delivery - 500
class Delivery:
    def __init__(self):
        pass

    def get_from_json(self, path):
        with open(path) as fh:
            data = json.load(fh)
            return data

    def dump_to_file(self, data, path):
        with open(path, "w") as fh:
            json.dump(data, fh)

    def create_box(self, product, type, min_count, max_count):
        dict = {}
        dict["type"] = type
        dict["id"] = random.randrange(100000)
        dict["product_name"] = product["product_name"]
        dict["full_product_name"] = random.choice(product["potential_names"])
        dict["manufacturer_name"] = random.choice(
            product["potential_manufacturer_names"]
        )
        dict["price"] = random.randrange(product["min_price"], product["max_price"])
        dict["product_count"] = random.randrange(min_count, max_count)
        return dict

    def get_boxes(self, in_data, type, num, min_count, max_count):
        boxes = []
        products = in_data.get("products")
        while num > 0:
            boxes.append(
                self.create_box(random.choice(products), type, min_count, max_count)
            )
            num -= 1

        return boxes

    def create_delivery(self, size: int, type1, type2="", type3=""):
        boxes = []
        out_data = {"size": size, "boxes": boxes}

        in_data = self.get_from_json(f"ProductTypes/{type1}.json")
        min1_count = int(in_data.get("min_count", 0))
        max1_count = int(in_data.get("max_count", 0))

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

        boxes += self.get_boxes(in_data, type1, type1_num, min1_count, max1_count)
        if type2 != "":
            boxes += self.get_boxes(in_data2, type2, type2_num, min2_count, max2_count)

            if type3 != "":
                boxes += self.get_boxes(
                    in_data3, type2, type3_num, min3_count, max3_count
                )
        return out_data
