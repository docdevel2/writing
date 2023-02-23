# Music Database APIs

## Overview

If you are a developer who wants to integrate network-based services into your applications, an application programming interface (API) can be an appealing solution. An application programming interface allows your client application to interact with a server using a common interface. Network-base APIs are becoming increasingly popular for web applications in industries such as banking, e-commerce, internet of things (IoT), and music.  

Many network-based web services offer APIs that comply with the REpresentational State Transfer (REST) design style which is defined by a set of constraints. APIs that comply with REST constraints are called RESTful. REST APIs operate in two modes, request and response. The client sends a request to the server for data, and the server responds with a status code, and if appropriate, the requested data.

In this article, I will show how you can access a RESTful API database with Python. I will deconstruct the data sent by the client to the server, and the corresponding response received by the client from the server. To illustrate the mechanics of the process, I will use a Python HTTP module to connect to a RESTful music database API.

> **Insert client-server model graphic here.**

## Why REST?

A RESTful API allows the client to retrieve data from the server without the need to know details about the server back-end implementation. There is no need for the client to know which server or database management software is being used. In addition, the API enhances security by restricting who can access data and also, selectively restrict the data that can be accessed.

In a RESTful Web service, requests made to a resource's URI elicit a response with a payload formatted in HTML, XML, JSON, or some other format. The most common protocol for these requests and responses is HTTP, which provides operations (HTTP methods) such as GET, POST, PUT, PATCH and DELETE.

Abbreviated descriptions the REST constraints are: 
 
* identification of resources
* manipulation of resources through representations
* self-descriptive messages
* hypermedia as the engine of the application state 

(This means that HTTP is the primary transfer protocol. See "Stateless".)

Note: While protocols like ftp and others are supported, they cannot be considered RESTful unless they conform to REST constraints.

(See [2] for more details.)


## Benefits

> (Ref. RFC 9110) "... uniform interfaces provide for better visibility and reuse in network-based systems."

An API isolates the client from the server, only allowing communication through a uniform interfaces provide for better visibility and reuse in network-based systems. As a result, implementation changes on either client-side or server-side can be made without either affecting the other, as long as the interface protocol is followed.

A RESTful API benefits developers because it allows developers to connect client components to a server through a standard interface. This allows replaceable components to be swapped without changing code on either side of the interface. As an analogy, consider USB devices that connect to a computer. Mutiple USB devices, with the same or different functions, can connect to the same USB port and still function properly.

RESTful APIs are widely accepted because they leverage existing HTTP infrastructure, the same infrastructure and protocols that browsers use. As a result, lots of tools (applications, libraries, developers, etc.) are available. 

From an end user perspective, you can use your existing browser as a client to access server databases. From a developer perspective, you can easily integrate server data and resources into your applications. From a service provider perspective, it allows you to make their services readily accessible to a wider audience. 

I previously mentioned identifiers to identify target resources. In a REST API, these identifiers are referred to as representations. By design, a REST API never manipulates server resources directly. Instead, it only manipulates their representations, the identifiers. You will see, in the upcoming examples, how these representations are communicated between client and server.

## Music APIs
Several well known music services provide REST API database access to both directly to musicians and to partners who want to integrate their content and/or music into commercial products. 

Spotify for example, provides an API that allows hardware partners to develop applications for home audio systems, music players, headphones, and other internet-enabled devices. 
> Spotify Web API endpoints return JSON metadata about music artists, albums, and tracks, directly from the Spotify Data Catalogue.
> (Note: The preceding sentence was copied verbatum from "Web API | Spotify for Developers". Need to massage before including i article.)

SoundCloud is a music service that allows musicians to share their music with a community of artists and listeners. Musicians can use the API to upload upload and manage their music for their listeners.

MusicBrainz view themselves as an open encyclopedia for music metadata, modeled after Wikipedia in that it is community-driven. It's metadata content is primarily, but not exclusively targeted at music player and tagger applications. In this article, I will use the MusicBrainz API as an example.

Before we interact with a live API, we need to better understand the role that HTTP plays in web applications. 

## HTTP Primer

In order to understand REST APIs, it is essential to understand the role that HTTP plays. The Hypertext Transfer Protocol (HTTP) is a stateless application-level protocol for distributed, collaborative, hypertext information systems. It is the predominant protocol used on the internet today. It was designed, from its beginning in 1990, to support the client-server model, sending a request in the form of a message from a client to a server, then delivering the response message and status code from the server to the client. 

An HTTP client is a program that establishes a connection to a
server for the purpose of sending one or more HTTP requests. An HTTP server is a program that accepts connections in order to service HTTP requests by sending HTTP responses back to the client.

When HTTP was first introduced (1990), the only method used to send requests was the GET method. It has since evolved to include additional methods to allow requests to modify and delete content on the server. Among these other methods are: GET, POST, PUT, and DELETE. You will see how some of these methods are used later when I get to the Python code described in this article. [1]

> **Put the methods and descriptions into a table to improve appearance.**

**GET**
Asks the server to send the target resource based on an identifier (representation).

**POST**
Asks the server to have the target resource process the enclosed content specified by an identifier.

**PUT**
Asks the server to have the target resource create or replace the enclosed content specified by an identifier.

**DELETE**
Asks the server to have the target resource specified by an identifier to be deleted.

**Requests**

When a request message is sent by a user agent (typically the client application) to a server, the message typically contains header fields that can include metadata such as: method, target host name, content type, content length, and/or other characteristics of the client, host, or message being sent. 

**Responses**
Upon receiving a request from a user agent, the server determines whether it can accept the request. If accepted, the server responds by sending a status code & a message back to the client. Response message content might include metadata and/or the requested target resource.

**Example header**
This is an example of a header in a PUT request. [1]
```
PUT /somewhere/fun HTTP/1.1  
Host: origin.example.com  
Content-Type: video/h264  
Content-Length: 1234567890987  
Expect: 100-continue  
```

Now that we understand the role that HTTP plays in web applications, the constraints that REST imposes in network-base APIs, and the request/response dynamic between client and server, we are now ready to interact with an API. REST constraints demand that the API must be stateless. This means that each request sent by the client to the server must contain all the information the server needs to respond appropriately. As a consequence, everything is contained in the URL.

> ([2] sec. 5.1.3)

**MusicBrainz API**
The MusicBrainz API gives the client access to a wide range of music metadata about artists & their music, including biographical information, release dates, media formats, etc. Requests are in the form of a URL that is comprised of multiple components, some mandatory, some optional. Syntax for the is as follows:

`<api_root><entity><mbid><inc><format>`

where:

* \<api_root> is the partial URL to the API: "https://musicbrainz.org/ws/2/"
* \<entity> is one of multiple categories that include artist, recording, release, etc.
* \<mbid> is the MusicBrainz identifier the is unique to each target resource in the database.
* \<inc> is an optional subquery string
* \<format> is an optional format string that specifies the transfer format which can be either JSON or XML. If not specified, XML is the default format.


## Python urllib module

```
api_root + entity + mbid + inc + format

api_root = "http://musicbrainz.org/ws/2"
entity = "/recording"
mbid = "/b97670e0-08fe-42fe-af39-7367a710c299"
inc = "?inc=artists"
format = “&fmt=json”
```

> Describe urllib and the Request object, followed by a description of what the code is doing.

```
class urllib.request.Request(url, data=None, headers={}, unverifiable=False, method=None)

.Request will GET or PUT
```

Using a simple code snippet in Python, this section shows you how to send an HTTPS request & capture the response. The API that I'm using  is the MusicBrainz API web service. I will use the GET method to retrieve metadata for a single recording to illustrate the process.

> **Next step:** Try running code with backslash breaking URL into 2 lines.

```
import json
import os
import urllib.request
import webbrowser
import pprint


# Justice's Groove URL
api_url = 'https://musicbrainz.org/ws/2/recording/\
b97670e0-08fe-42fe-af39-7367a710c299?&fmt=json'

def mbz_recording(api_url):
    
    request = urllib.request.Request(api_url)
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))
        statcode = response.status
    
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)
    
    webbrowser.open_new_tab(api_url)

    return
```

> Insert screenshot of result.

In this example, the request uses the GET method which, is the default for urllib when no method is specified. A POST request is sent to the server in a similar way, except that either the POST method must be specified and/or a `data` argument must be passed.

**Security**

Web API typically require some sort of authentication to verify that the user submitting a request is authorized to do so. Some of the common authentication protocols include HTTP Digest Access Authentication, JSON Web Token (JWT), and OAuth 2. HTTP Digest Access Authentication uses 256 or 512 hash encrypted username and password to authorize access. JWT and OAuth 2 use tokens, generated by a third party authorization server, that you authorize in advance to give you access to one or more applications. The token approach effectively gives you a single sign-on source so you don't have to repeatedly re-enter your username and password.

MusicBrainz POST requests require authentication for security reasons since data can be altered. In order to submit a POST request, a client application must register using either a username/password or OAuth 2 token. An authorization request must be submitted prior to submitting a POST request. For more information on MusicBrainz authentication, see "Development / OAuth2 - MusicBrainz"[5]. No authentication is required for most GET requests as I demonstrated in my example.


## Summary

We've covered how the ubiquitous HTTP open standard along with well-defined REST architectural constraints enable you to develop client applications that are flexible and secure. Client and server components and be independently updated or migrated more easily than tightly integrated systems. Manipulation of representations rather than resources combined with a variety of authentication options enhance security. Whether REST APIs thrive in the music industry or any other industry remains to be seen. If the REST APIs live to expectations, the future will be bright.


## References
1. [RFC 9110](https://httpwg.org/specs/rfc9110.html)
2. Fielding, R., “Architectural Styles and the Design of Network-based Software Architectures”, Doctoral Dissertation, University of California, Irvine, September 2000, <https://roy.gbiv.com/pubs/dissertation/top.htm>.
3. [URI RFC 2396](https://www.ietf.org/rfc/rfc2396.txt)
4. [MusicBrainz FAQ](https://musicbrainz.org/doc/MusicBrainz_API#General_FAQ)
5. [Development / OAuth2 - MusicBrainz](https://musicbrainz.org/doc/Development/OAuth2)
6. [Guido van Rossum and the Python development team, *The Python Library Reference*, Release 3.10.5, July 21, 2022](https://docs.python.org/3.10/library/urllib.html)


### 