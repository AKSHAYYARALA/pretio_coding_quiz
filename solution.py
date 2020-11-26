import requests
import time
import sys
import json
import csv


class CodingQuiz:

    def __init__(self, auth_token):
        self.headrs = {'Authorization': 'Bearer ' + auth_token}

    def make_call(self, endpoint):

        try:
            response = requests.get(endpoint, headers=self.headrs)

            if response.status_code == 200:
                json_response = response.json()
                rows = json_response['rows']
                rows = sorted(rows, key = lambda i: float(i['payout']))

                fp = open('offers.csv', 'w', encoding='utf-8', errors='ignore')
                csv_writer = csv.writer(fp)

                count = 0
                for row in rows:
                    if count == 0:
                        header = row.keys()
                        csv_writer.writerow(header)
                        count += 1

                    csv_writer.writerow(row.values())

                fp.close()
                return response.status_code
            elif response.status_code == 429:
                time.sleep(60)
                self.make_call(endpoint)
                return response.status_code
            else:
                return response.status_code
        except Exception as ex:
            print(f"Something went wrong. Error: {str(ex)}")


if __name__ == '__main__':
    auth_token = 'LpNe5bB4CZnvkWaTV9Hv7Cd37JqpcMNF'
    cq_obj = CodingQuiz(auth_token)

    endpoint = 'https://atlas.pretio.in/atlas/coding_quiz'
    status_code = cq_obj.make_call(endpoint)

    if status_code == 200:
        print("offers.csv file generated successfully.")
    elif status_code == 429:
        print("Got 429 status code and tried again")
    elif status_code == 401:
        print("Got 401 status code. It's unauthorized call")
        sys.exit()
    elif status_code == 500:
        print("Got 500 status code.")
        sys.exit()
