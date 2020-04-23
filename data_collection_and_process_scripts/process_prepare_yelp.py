from data_collection_and_process_scripts.preprocessing_tools import strip_down_comment
import json


def main():
    with open('../review.json', encoding="utf-8") as review_file, \
            open('../yelp_reviews.txt', 'w', encoding='utf-8') as write_file:
        line = review_file.readline()
        line_count = 0
        while line:
            print(line_count)
            review = json.loads(line)
            text = review['text']
            rating = review['stars']
            print(f"__label__{int(rating)} {strip_down_comment(text)}", file=write_file)
            line = review_file.readline()
            line_count += 1


if __name__ == '__main__':
    main()
