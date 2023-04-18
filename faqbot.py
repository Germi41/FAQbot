import requests
import json
import sys


def main():
    file_name = sys.argv[1]
    url = "https://kiwi.aicheck.tech/"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic cGlsb3Q6UDFsMFROb3RTb1ZlcnlMb25nUGFzc3dvcmQ='
    }
    queries = get_queries(file_name)
    print(queries)
    # queriesCount = len(queries)
    # print(queriesCount)
    #get_payload(url, headers, queries)


def get_payload(url, headers, queries):
    answers = []

    for query in queries:
        payload = json.dumps({
            "query": query
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            results = json.loads(response.text)
            answers.append(results["answer"])

    save_to_txt(answers)
    # print(answers)
    # print(type(answers))


def get_queries(file_name):
    queries = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            print(line.rstrip())
            queries.append(line)

    return queries


def save_to_txt(answers):
    with open("queries.txt", "w", encoding="utf-8", newline="\n") as f:
        for line in answers:
            f.write(line)
            f.write("\n")


if __name__ == "__main__":
    main()
