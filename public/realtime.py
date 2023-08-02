import time

# Fungsi untuk menghasilkan data secara realtime
def realtime_data():
    i = 0
    while True:
        i += 1
        yield f"Data ke-{i}"
        time.sleep(1)
