from prometheus_client import start_http_server, Summary, Gauge
import random
import time

total_deliveries = Gauge("total_deliveries", "Total number of deliveries")
pending_deliveries = Gauge("pending_deliveries", "Number of pending deliveries")
on_the_way_deliveries = Gauge("on_the_way_deliveries", "Number of deliveries on the way")
average_delivery_time = Summary("average_delivery_time", "Average delivery time in seconds")


def simulate_delivery():
    pending = 50
    on_the_way = random.randint(5, 20)
    delivered = random.randint(30, 70)
    avg_time = 40

    total = pending + on_the_way + delivered

    print(f"[DEBUG] Total deliveries: {total}")
    print(f"[DEBUG] Pending deliveries: {pending}")
    print(f"[DEBUG] On-the-way deliveries: {on_the_way}")
    print(f"[DEBUG] Average delivery time: {avg_time:.2f} seconds")

    total_deliveries.set(total)
    pending_deliveries.set(pending)
    on_the_way_deliveries.set(on_the_way)
    average_delivery_time.observe(avg_time)


if __name__ == "__main__":
    print("[INFO] Starting the HTTP server on port 8000...")

    start_http_server(8000, addr="0.0.0.0")

    print("[INFO] HTTP server started. Simulating deliveries...")

    while True:
        simulate_delivery()
        print("[INFO] Sleeping for 1 seconds...")
        time.sleep(1)