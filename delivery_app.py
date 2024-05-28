from Delivery import Delivery


delivery = Delivery()

boxes = delivery.create_delivery(20, "electronics", "industrial")
delivery.dump_to_file(boxes, "delivery3.json")
