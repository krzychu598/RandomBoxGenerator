from Delivery import Delivery


delivery = Delivery()

delivery.dump_to_file(
    delivery.create_delivery(15, "electronics", "industrial"), "example_output.json"
)
