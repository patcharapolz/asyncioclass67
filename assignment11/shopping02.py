import time
import asyncio
from asyncio import Queue
from random import randrange

# we first implement the Customer and Product classes, 
# representing customers and products that need to be checked out. 
# The Product class has a checkout_time attribute, 
# which represents the time required for checking out the product.
class Product:
    def __init__(self, product_name: str, checkout_time: float):
        self.product_name = product_name
        self.checkout_time = checkout_time

class Customer:
    def __init__(self, customer_id: int, products: list[Product]): 
        self.customer_id = customer_id
        self.products = products

# we implement a checkout_customer method that acts as a consumer.
# As long as there is data in the queue, this method will continue to loop. 
# During each iteration, it uses a get method to retrieve a Customer instance. 
# 
# If there is no data in the queue, it will wait. 
# 
# After retrieving a piece of data (in this case, a Customer instance), 
# it iterates through the products attribute and uses asyncio.sleep to simulate the checkout process.
# 
# After finishing processing the data, 
# we use queue.task_done() to tell the queue that the data has been successfully processed.
async def checkout_customer(queue: Queue, cashier_number: int):
    cashier_time = 0
    count = 0
    while not queue.empty():
        customer: Customer = await queue.get()
        count += 1
        print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}")
        await asyncio.sleep(0.001)

        for product in customer.products:
            cashier_time += product.checkout_time
            print(f"The Cashier_{cashier_number} will checkout Customer_{customer.customer_id}'s Product_{product.product_name} in {product.checkout_time} secs")
            await asyncio.sleep(product.checkout_time)
        
        # print(f"The Cashier_{cashier_number} finished checkout Customer_{customer.customer_id} in {round(time.perf_counter() - customer_start_time, ndigits=2)} secs")

        queue.task_done()

    return {"type": "Cashier", "name": f"Cashier_{cashier_number}", "count": count, "time": f"{cashier_time:.2f}",}
    # print(f"The Cashier_{cashier_number} take {count} customers total {round(time.perf_counter() - customer_time, ndigits=2)} secs")

# we implement the generate_customer method as a factory method for producing customers.
#
# We first define a product series and the required checkout time for each product. 
# Then, we place 0 to 4 products in each customer’s shopping cart.
def generate_customer(customer_id: int) -> Customer:
    all_products = [Product('beef', 1),
                    Product('banana', 0.4),
                    Product('sausage', 0.4),
                    Product('diapers', 0.2)]
    return Customer(customer_id, all_products)

# we implement the customer_generation method as a producer. 
# This method generates several customer instances regularly 
# and puts them in the queue. If the queue is full, the put method will wait.
async def customer_generation(queue: Queue, customers: int):
    customer_count = 0
    while True:
        customers = [generate_customer(the_id) for the_id in range(customer_count, customer_count + customers)]

        for customer in customers:
            print("Waiting to put customer in line...")
            await queue.put(customer)
            print("Customer put in line...")
        
        customer_count += len(customers)
        await asyncio.sleep(.001)

        return {"type": "Total", "name": "Supermarket", "count": customer_count}

# Finally, we use the main method to initialize the queue, 
# producer, and consumer, and start all concurrent tasks.
async def main():
    queue = 3
    customer = 10
    cashier = 5

    customer_queue = Queue(queue)
    customers_start_time = time.perf_counter()
    customer_producer = asyncio.create_task(customer_generation(customer_queue, customer))
    cashiers = [checkout_customer(customer_queue, i) for i in range(cashier)]

    result = await asyncio.gather(*cashiers, customer_producer)

    print("----------------------------------------------")

    for item in result:
        match item["type"]:
            case "Cashier":
                print(f"The {item["name"]} take {item["count"]} customers total {item["time"]} secs")
            
            case "Total":
                print(f"\nThe {item["name"]} process finished {item["count"]} customers in {round(time.perf_counter() - customers_start_time, ndigits=2)} secs")




if __name__ == "__main__":
    asyncio.run(main())


