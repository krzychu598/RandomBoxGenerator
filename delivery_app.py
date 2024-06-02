from Delivery import Delivery


delivery = Delivery()
if 1 == 0:
    boxes = delivery.create_delivery(20, "electronics")
    delivery.dump_to_file(boxes, "electronics_delivery.json")

    boxes = delivery.create_delivery(20, "food_and_drinks")
    delivery.dump_to_file(boxes, "food_and_drinks_delivery.json")

    boxes = delivery.create_delivery(20, "industrial")
    delivery.dump_to_file(boxes, "industrial_delivery.json")

    boxes = delivery.create_delivery(20, "industrial", "electronics")
    delivery.dump_to_file(boxes, "mixed_delivery.json")

    boxes = delivery.create_request(5, "small", "food_and_drinks")
    delivery.dump_to_file(boxes, "request1.json")


boxes = delivery.create_request(3, "small", "electronics")
delivery.dump_to_file(boxes, "request2.json")
