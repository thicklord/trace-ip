# trace-ip

[![asciicast](https://asciinema.org/a/aEjjnfE9QU7yqxtXW7nwLouLK.svg)](https://asciinema.org/a/aEjjnfE9QU7yqxtXW7nwLouLK)
The need for this script was found when needing to parse apache access logs and gather access attempts, along with other IP data. The program works simply by calling this program `python3 main.py ‘/path/to/access_log’` or specifying the access log path in the `main.py` file.
The IPs are collected from the log data and put through an API loop to tell where the IP traffic is originating from. The data gets processed and put into a JSON dump, ordered by most talkers to least.
