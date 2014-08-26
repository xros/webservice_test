RESTful Webservice Test Tool
=====
* Just read the codes it's so easy
```python
    >>> test = TestRequest()
    >>> test.thread_request(4 , 200) # means 200 requests for each thread . In total it's 800 rqts.
    >>> test.url="http://www.duckduckgo.com"
    >>> test.loop_loop()
    Thread 3 finishes a HTTP conversation
    Thread 4 finishes a HTTP conversation
    ...
    ...
    Thread 3 finishes a HTTP conversation
    Thread 2 finishes a HTTP conversation
    Thread 3 finishes a HTTP conversationThread 4 finishes a HTTP conversation
    Thread 3 finished
    It takes 45.747551 seconds to handle                800 requests with 4 threads for each 200 sub-requests.
    _____SUMMERY_____
    17.487275 requests/second

```
* Happy hacking
