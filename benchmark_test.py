import time
import sqlite3
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from modules.rule_engine import calculate_sentiment

DB_NAME = "texts.db"

base_reviews = [
    "excellent product amazing service good support",
    "bad error worst experience terrible quality",
    "happy customer love this excellent item",
    "error happened but good response"
]


def run_single(data):
    for r in data:
        calculate_sentiment(r)


def run_thread(data):
    with ThreadPoolExecutor(max_workers=4) as ex:
        list(ex.map(calculate_sentiment, data))


def run_multi(data):
    with ProcessPoolExecutor(max_workers=4) as ex:
        list(ex.map(calculate_sentiment, data))


def query_test():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    start = time.time()
    cursor.execute("SELECT id FROM texts WHERE tag='positive'")
    cursor.fetchall()
    end = time.time()

    conn.close()
    return round(end-start,3)


if __name__ == "__main__":

    print("\n===== PERFORMANCE COMPARISON =====")

    reviews = base_reviews * 2500

    start = time.time()
    run_single(reviews)
    print("Single:", round(time.time()-start,2),"sec")

    start = time.time()
    run_thread(reviews)
    print("Thread:", round(time.time()-start,2),"sec")

    start = time.time()
    run_multi(reviews)
    print("Multiprocessing:", round(time.time()-start,2),"sec")


    print("\n===== SCALABILITY TEST =====")

    for size in [100, 10000, 100000]:

        dataset = base_reviews * (size // len(base_reviews))

        start = time.time()
        run_multi(dataset)
        end = time.time()

        print("Size:", len(dataset), "| Time:", round(end-start,2),"sec")


    print("\n===== QUERY TIME TEST =====")

    before = query_test()
    print("Query Time (Indexed):", before,"sec")
