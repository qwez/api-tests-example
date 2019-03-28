#### Todoist API tests
[API documentation](https://developer.todoist.com/rest/v8/)

##### Prepare environment
1. install python 3.7
2. `git clone https://github.com/qwez/api-tests-example.git`
3. `cd api-tests-example`
4. `python -m pip install -r requirements.txt`
##### Run tests
`pyhon -m pytest --alluredir=allure_report`
##### Run allure report
1. install allure cmd tool
2. `allure serve allure_report`
##### Run Options
* `-n <thread_number>` - run tests in parallel threads. Not recommended more then 1 thread (default), because there are Internal Server errors returned form API (don't know why)
