import time
import requests


def wait_for_elasticsearch(host='http://elasticsearch:9200', timeout=60):
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(host)
            if response.status_code == 200:
                return True
        except requests.RequestException:
            pass
        time.sleep(5)
    return False

if __name__ == '__main__':
    if wait_for_elasticsearch():
        import subprocess
        subprocess.run(["python", "main.py"])