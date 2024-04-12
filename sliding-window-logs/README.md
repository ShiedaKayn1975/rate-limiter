# Python rate limter

A python rate limter, which was created by Thieu Anh Nguyen, using Python and Docker.


## Task 1

To run the code, you should follow these steps.

- Active python virtual env
    ```bash
    source .venv/bin/activate
    ```
- Run file ```rate_limiter.py```
    ```bash
    python3 rate_limter.py
    ```
- You'll see the result like this
    ```
    Time 2022-01-20 00:13:05, accepted = True
    Time 2022-01-20 00:27:31, accepted = True
    Time 2022-01-20 00:45:27, accepted = True
    Time 2022-01-20 01:00:49, accepted = False
    Time 2022-01-20 01:15:45, accepted = True
    Time 2022-01-20 01:20:01, accepted = False
    Time 2022-01-20 01:50:09, accepted = True
    Time 2022-01-20 01:52:15, accepted = True
    Time 2022-01-20 01:54:00, accepted = False
    Time 2022-01-20 02:00:00, accepted = False
    ```

## Task 2

To check the integration of the rate limiter in cluster mode, you should follow these steps.

- Run project
    ```bash
    docker-compose up -d --build
    ```
- Then you access to your browser and access this address ```http://localhost:5660```
- Then you have to refresh your browser three times, after that, you'll see the message "Too many requests" in the next time runnings. 