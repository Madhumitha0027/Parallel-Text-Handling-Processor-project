import time
import multiprocessing

from database.db_manager import create_table, insert_result
from modules.text_loader import split_text, parallel_process
from modules.rule_engine import calculate_sentiment


def process_chunk(chunk):
    score, tag = calculate_sentiment(chunk)
    return (chunk, score, tag)


if __name__ == "__main__":

    create_table()

    text = """
    Today is a good day. I feel happy.
    Sometimes coding gives error and makes me sad.
    But learning is excellent and I love solving problems.
    """

    # Split text into chunks
    chunks = split_text(text)

    total_reviews = len(chunks)
    chunk_size = 1   # each sentence is treated as a chunk
    total_chunks = len(chunks)

    print("\n===== TEXT PROCESSING PERFORMANCE =====\n")

    print(f"Total reviews processed : {total_reviews}")
    print(f"Chunk size used         : {chunk_size}")
    print(f"Total chunks created    : {total_chunks}")

    print("\nParallel processing     : Enabled (multiprocessing)")
    print("CPU cores available     :", multiprocessing.cpu_count())

    # Start timer
    start_time = time.time()

    results = parallel_process(chunks, process_chunk)

    for chunk, score, tag in results:
        insert_result(chunk, score, tag)

    # End timer
    end_time = time.time()
    execution_time = end_time - start_time

    print(f"\nExecution time          : {execution_time:.2f} seconds")

    print("\nProcessing Completed Successfully!")
