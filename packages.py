import urllib
import urllib2
import thread
from datetime import datetime, timedelta

__author__ = "Alexander Liu"

class TestRequest(object):
    """
    Usage:
    >>> test = TestRequest()
    >>> test.thread_request(4 , 100) # means 100 requests for each thread . In total it's 400 rqts.
    >>> test.url="http://duckduckgo.com"
    >>> test.loop_loop()
    Thread 3 finishes a HTTP conversation
    Thread 4 finishes a HTTP conversation
    ...
    ...
    Thread 3 finishes a HTTP conversation
    Thread 2 finishes a HTTP conversation
    Thread 2 finished
    Thread 3 finishes a HTTP conversation
    Thread 4 finishes a HTTP conversation
    Thread 3 finished
    It takes 45.747551 seconds to handle                800 requests with 4 threads for each 200 sub-requests.
    _____SUMMERY_____
    17.487275 requests/second
    
    """
    url = 'http://www.baidu.com'
    # the threshold indicates the end of all loops                      
    threshold=1                                                                                                                                                        

    def __init__(self, threadAmount=4, eachRequestAmount=100):
        self.threadAmount = threadAmount
        self.eachRequestAmount = eachRequestAmount
        self.allRequestAmount = self.threadAmount * self.eachRequestAmount


    def thread_request(self, threadAmount=4, eachRequestAmount=100):
        self.threadAmount = threadAmount
        self.eachRequestAmount = eachRequestAmount
        self.allRequestAmount = self.threadAmount * self.eachRequestAmount


    def url_request(self, threadNumber=0):                                                                                                     
        # The thread number indicates which thread
        post_headers={
                "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0",                                                                            #"Cookie":".99f01315bb0a684d014a66b7ce33c6489=d25ch2i16m80b0s5c1b0k8p1i3; _mkto_trk=id:800-TIV-782&token:_mch-soapui.org-1409086981371-22489; __CT_Data=gpv=6&apv_26362_www02=6; WRUID=0; _jsuid=1176038871",
                }                                                                                                                                                   

        for i in range(self.eachRequestAmount):
            try:
                request = urllib2.Request(self.url, headers=post_headers)
                response = urllib2.urlopen(request)
            except Exception as e:
                print e  
            else: #print response.readlines()
                print "Thread %d finishes a HTTP conversation" % threadNumber

        self.threshold = self.threshold + 1
        print "Thread %d finished" % threadNumber        
        
    def loop_loop(self):
        '''Create new threads
        '''
        start_time = datetime.now()
        # create the threads
        for t in range(self.threadAmount):
            thread.start_new_thread( self.url_request, (t+1,) )
         # To make the script work until all threads finished
        while self.threshold < self.threadAmount:
            pass              
        end_time = datetime.now()
        tdelta = end_time - start_time
        print "It takes " + str(tdelta.total_seconds()) + " seconds to handle " 
                + "%d requests with %d threads for each %d sub-requests." % (self.allRequestAmount, self.threadAmount, self.eachRequestAmount)
        print "_____SUMMERY_____"
        print "%f requests/second for the site: %s" % (self.allRequestAmount/tdelta.total_seconds(), self.url)


__footer__ == "Happy hacking"
