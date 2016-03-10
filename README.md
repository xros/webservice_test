RESTful Webservice Test Tool
=====
* Just read the codes it's so easy

```
    # Getting into the folder
    cd ./webservice_test
    # Fire up the Python console
    python
```

```python
    >>> from packages import TestRequest
    >>> test = TestRequest()
    >>> test.thread_request(4 , 20) # means 20 requests for each thread . In total it's 80 rqts.
    >>> test.url="http://www.duckduckgo.com"
    >>> test.loop_loop()
    Thread 3 finishes a HTTP conversation
    Thread 4 finishes a HTTP conversation
    ...
    ...
    Thread 3 finishes a HTTP conversation
    Thread 2 finishes a HTTP conversation
    Thread 3 finishes a HTTP conversation
    Thread 4 finishes a HTTP conversation
    Thread 3 finished
    Thread 2 finished

    It takes 3.374847 seconds to handle 80 requests with 4 threads for each 20 sub-requests.
    _____SUMMERY_____
    23.704778 requests/second for the site: http://www.duckduckgo.com

```
* Happy hacking
