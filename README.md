#PBLog#

This is a simple NSLog() replacement, which can send your logs directly to an HTTP Server.

You need to have your own webserver to listen to your POST requests.

You can use [this](http://fragments.turtlemeat.com/pythonwebserver.php) sample and add these statements in your do_POST()
method before self.end_headers() .

<pre><code>logstring = self.headers.getheader('log')           
            print logstring</code></pre>
            
Feel free to ask any questions and follow me on Twitter [@piet_nbn](https://www.twitter.com/piet_nbn).