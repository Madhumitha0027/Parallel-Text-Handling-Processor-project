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

    chunks = split_text(text)

    results = parallel_process(chunks, process_chunk)

    for chunk, score, tag in results:
        insert_result(chunk, score, tag)

    print("Processing Completed!")
