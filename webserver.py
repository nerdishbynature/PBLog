#Copyright Jon Berg , turtlemeat.com

import string
import cgi
import time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    
    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


class MyHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        try:
            if self.path.endswith(".html"):
                f = open(curdir + sep + self.path)
                
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
            if self.path.endswith(".esp"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write("hey, today is the" +
                                 str(time.localtime()[7]))
                self.wfile.write(" day in the year " +
                                 str(time.localtime()[0]))
                return
            
            return
        
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
    
    def do_POST(self):
        global rootnode
        try:
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query = cgi.parse_multipart(self.rfile, pdict)
            self.send_response(200)
            
            logstring = self.headers.getheader('log')
            
            print bcolors.WARNING + logstring + bcolors.ENDC
            
            upfilecontent = query.get('upfile')
            print "filecontent", upfilecontent[0]
            self.wfile.write("<HTML>POST OK.<BR><BR>")
            self.wfile.write(upfilecontent[0])
            
            self.end_headers()
        except:
            pass


def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
