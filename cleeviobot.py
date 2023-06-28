import requests
import json


def main():
    file_name = "queries.txt"
    url = "https://ai-faqbot.cs-systems-sandbox.skypicker.com/chat"
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    queries = get_queries(file_name)
    answers = get_payload(url, headers, queries)
    save_to_txt(answers)
    if answers:
        create_csv(queries, answers)


def get_payload(url, headers, queries):
    answers = []

    for query in queries:
        payload = json.dumps({
            "query": query,
            "conversation_id": '8082229f-d0cb-4d42-8fe5-80a66f5fb34d',
            "display_history_limit": 1,
            "ai_history_limit": 1
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            response_text = response.text
            results = json.loads(response_text)
            answers.append(results["answer"].split("\n")[0])

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
            csv_file.write(f'{query};{answer}\n')


if __name__ == "__main__":
    main()