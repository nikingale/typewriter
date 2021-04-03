import pdfplumber
from processor import process
import time
import argparse

def get_difficult(word_scores, threshold):
    difficult = list()
    for word in word_scores:
        if word_scores[word] > threshold:
            difficult.append(word)
    return difficult

def main(args):
    input = args.input
    threshold = args.threshold
    with pdfplumber.open(input) as pdf:
        page_number = 1
        for page in pdf.pages:
            page_content = page.extract_text()
            if page_content == None:
                continue
            # print(page_content)
            word_scores = process(page_content)
            print('Page {0:3} -'.format(page_number), get_difficult(word_scores, threshold))
            page_number += 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help = 'the readbud command (pdf, url)')
    parser.add_argument('--input',  required = True)
    parser.add_argument('--threshold', type = float, required = True)
    args = parser.parse_args()
    main(args)