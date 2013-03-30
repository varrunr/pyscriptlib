import httplib
import socket


__DEBUG__ = True

def procResponse(resp):
    if __DEBUG__ is True:
        print "HTTP %d:%s" % (resp.status, httplib.responses[resp.status])
    
    data = resp.read()
    if __DEBUG__ is True:
        print "Response:\n" , repr(data)

def getRawRequest(reqObj):
    # TODO
    return ''

"""
    Establish a HTTPS connection with a server.
    No certificate validation
"""

def sendHTTPreq(host,secure=True,method='GET',path='/',port=443, headers=None):
    try:
        newConn = None
        
        if secure is True and socket.ssl != None:
            newConn = httplib.HTTPSConnection(host, port)
        else:
            port = 80
            if secure is True and __DEBUG__ is True:
                print "python SSL support absent, defaulting to HTTP. Do NOT send sensitive information"
            newConn = httplib.HTTPConnection(host, port)

        if headers != None:
            newConn.putrequest(method, path)

            for header in headers:
                assert len(header) == 2
                newConn.putheader(header[0],header[1])

            newConn.endheaders() # CRLF
            #newConn.send(body) TODO: POST
        else:
            newConn.request(method, path)
       
        resp = newConn.getresponse()

        return procResponse(resp)

    except httplib.HTTPException:
        print "Error sending request"
        return None
