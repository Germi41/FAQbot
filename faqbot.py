import requests
import json
import sys


def main():
    lang = sys.argv[1]
    file_name = "queries_en.txt"
    file_name2 = "queries_cs.txt"
    url = "https://kiwi.aicheck.tech/"
    url2 = "https://kiwi2.aicheck.tech/"
    headers = {
        'Content-Type': 'application/json'
    }
    if lang == "en":
        queries = get_queries(file_name)
        answers = get_payload(url, headers, queries)
    else:
        queries = get_queries(file_name2)
        answers = get_payload(url2, headers, queries)
    save_to_txt(answers)
    if answers:
        create_csv(queries, answers)


def get_payload(url, headers, queries):
    answers = []
    username = ""  # deleted
    password = ""  # deleted
    auth = (username, password)

    for query in queries:
        payload = json.dumps({
            "query": query
        })
        response = requests.request("POST", url, headers=headers, data=payload, auth=auth)
        if response.status_code == 200:
            results = json.loads(response.text)
            answers.append(results["answer"])

    return answers


def get_queries(file_name):
    queries = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            else:
                queries.append(line)
    return queries


def save_to_txt(answers):
    with open("answers.txt", "w", encoding="utf-8", newline="\n") as f:
        for line in answers:
            f.write(line)
            f.write("\n")


def create_csv(queries, answers):
    with open('my_file.csv', 'w') as csv_file:
        for i in range(min(len(queries), len(answers))):
            query = queries[i].strip()
            answer = answers[i].strip()
            csv_file.write(f'{query},{answer}\n')


if __name__ == "__main__":
    main()
