# Music Database APIs

## Overview

For developers interested in integrating network-based services into their applications, an application programming interface (API) can be an appealing solution. An application programming interface allows a client application to interact with a server using a common interface. Network-base APIs are becoming increasingly popular for web applications in industries such as banking, e-commerce, internet of things (IoT), and music.  

Many network-based music APIs comply with the REpresentational State Transfer (REST) design style which is defined by a set of constraints. APIs that comply with REST constraints are called RESTful. REST APIs operate in two modes, request and response. The client sends a request to the server for data, and the server responds with a status code, and if appropriate, the requested data.

In this article, I will show how you can access a RESTful API database with Python. I will deconstruct the data sent by the client to the server, and the corresponding response received by the client from the server. To illustrate the mechanics of the process, I will use Python HTTP module to connect to a RESTful music database API.

> **Insert client-server model graphic here.**


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

## Why REST?

A RESTful API allows the client to retrieve data from the server without the need to know details about the server back-end implementation. There is no need for the client to know which server or database management software is being used. In addition, the API enhances security by restricting who can access data and also, selectively restrict the data that can be accessed.

In a RESTful Web service, requests made to a resource's URI elicit a response with a payload formatted in HTML, XML, JSON, or some other format. The most common protocol for these requests and responses is HTTP, which provides operations (HTTP methods) such as GET, POST, PUT, PATCH and DELETE.

Abbreviated descriptions the REST constraints are: 
 
* identification of resources
* manipulation of resources
* self-descriptive messages
* hypermedia as the engine of the application state (This means that HTTP is the primary transfer protocol. See "Stateless".)

Note: While protocols like ftp and others are supported, they cannot be considered RESTful unless they conform to REST constraints.

(See [2] for more details.)


## Benefits

> (Ref. RFC 9110) "... uniform interfaces provide for better visibility and reuse in network-based systems."

An API isolates the client from the server, only allowing communication through a uniform interfaces provide for better visibility and reuse in network-based systems. As a result, implementation changes on either client-side or server-side can be made without either affecting the other, as long as the interface protocol is followed.

A RESTful API benefits developers because it allows developers to connect client components to a server through a standard interface. This allows replaceable components to be swapped without changing code on either side of the interface. As an analogy, consider USB devices that connect to a computer. Mutiple USB devices, with the same or different functions, can connect to the same USB port and still function properly.

RESTful APIs are widely accepted because they leverage existing HTTP infrastructure, the same infrastructure and protocols that browsers use. As a result, lots of tools (applications, libraries, developers, etc.) are available. 

From an end user perspective, you can use your existing browser as a client to access server databases. From a developer perspective, you can easily integrate server data and resources into your applications. From a service provider perspective, it allows you to make their services readily accessible to a wider audience. 

I previously mentioned identifiers to identify target resources. In a REST API, these identifiers are referred to as representations. By design, a REST API never manipulates server resources directly. Instead, it only manipulates their representations, the identifiers. You will see, in the upcoming examples, how these representations are communicated between client and server.


**Next steps:** Discuss URL syntax, generic & specific.  

```  
<scheme>://<authority><path>?<query>
```

## Music APIs
Several well known music services provide REST API database access to both directly to musicians and to partners who want to integrate their content and/or music into commercial products. 

Spotify for example, provides an API that allows hardware partners to develop applications for home audio systems, music players, headphones, and other internet-enabled devices. 
> Spotify Web API endpoints return JSON metadata about music artists, albums, and tracks, directly from the Spotify Data Catalogue.
> (Note: The preceding sentence was copied verbatum from "Web API | Spotify for Developers". Need to massage before including i article.)

SoundCloud is a music service that allows musicians to share their music with a community of artists and listeners. Musicians can use the API to upload upload and manage their music for their listeners.

MusicBrainz view themselves as an open encyclopedia for music metadata, modeled after Wikipedia in that it is community-driven. It's metadata content is primarily, but not exclusively targeted at music player and tagger applications. In this article, I will use the MusicBrainz API as an example.

## Anatomy of a Request 
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



> Next step: Describe steps the MBZ authentication steps.


## Python urllib module

```
api_root + entity + mbid + inc + format

api_root = "http://musicbrainz.org/ws/2"
entity = "/recording"
mbid = "/b97670e0-08fe-42fe-af39-7367a710c299"
inc = "?inc=artists"
format = “&fmt=json”
```

TBD

```
class urllib.request.Request(url, data=None, headers={}, unverifiable=False, method=None)

.Request will GET or PUT
```

Using a simple code snippet in Python, this section shows you how to send an HTTPS request & capture the response. The API that I'm using  is the MusicBrainz API web service. I will use the GET method to retrieve metadata for a single recording to illustrate the process.


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

MusicBrainz POST requests require a authentication for security reasons since data can be altered. In order to POST, an application must register using either a username/password or OAuth token. For more information on authentication, see "Development / OAuth2 - MusicBrainz"[6].

> Investigate urllib POST vs. MusicBrainz POST.
> 
> urllib will post if POST method is specified or if data argument is passed.
> 
> MBZ: Either user name/password or OAuth token is required.


## References
1. [RFC 9110](https://httpwg.org/specs/rfc9110.html)
2. Fielding, R., “Architectural Styles and the Design of Network-based Software Architectures”, Doctoral Dissertation, University of California, Irvine, September 2000, <https://roy.gbiv.com/pubs/dissertation/top.htm>.
3. [URI RFC 2396](https://www.ietf.org/rfc/rfc2396.txt)
4. [MusicBrainz FAQ](https://musicbrainz.org/doc/MusicBrainz_API#General_FAQ)
5. [Development / OAuth2 - MusicBrainz](https://musicbrainz.org/doc/Development/OAuth2)
6. [Python Software Foundation, *The Python Library Reference*, Release 3.10.5, July 21, 2022](https://docs.python.org/3.10/library/urllib.html)


## Research Notes

(To be edited)
HTTP Core Specifications

The “core” semantics of the HTTP protocol are defined by:

    RFC9110: HTTP Semantics
    RFC9111: HTTP Caching

Those semantics are expressed “on the wire” in three ways:

    RFC9112: HTTP/1.1
    RFC9113: HTTP/2
    RFC9114: HTTP/3


> Stateless: each request from client to server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Session state is therefore kept entirely on the client. (Ref. Dissertation quote; sec. 5.1.3)

* Authentication (Ref. [5] MusicBrainz FAQ)

All POST requests require authentication. You should authenticate using HTTP Digest, using the same username and password you use to access the main https://musicbrainz.org website. The realm is "musicbrainz.org".

> **Note:** What is "HTTP Digest" in paragraph above? (See "Development / OAuth2 - MusicBrainz". OAuth2 is an alternative to "HTTP Digest")

POST requests should always include a 'client' parameter in the URL (not the body). The value of 'client' should be the ID of the client software submitting data. This has to be the application's name and version number, not that of a client library (client libraries should use HTTP's User-Agent header). The recommended format is "application-version", where version does not contain a - character.


* Security (Ref. Dissertation)

Security is a significant concern these days. With the proliferation of hacker attacks and viruses, it is critical that web servers offer protection against attacks and breaches. To combat these security threats, API providers commonly use a combination of these security measures.

* API security
	* HTTP
	* API Keys (Bearer token, JSON Web Token)
	* 0Auth


* user agent 
	* The term user agent refers to any client program that initiates a request. (Ref. RFC 9110)
	* A user agent uses a client connector to initiate a request and becomes the ultimate recipient of the response. (Source: Fielding Dissertation, 5.2.3)
* origin server
	* The term origin server refers to a program that can originate
authoritative responses for a given target resource.
	* An origin server uses a server connector to govern the namespace for a requested resource. It is the definitive source for representations of its resources and must be the ultimate recipient of any request that intends to modify the value of its resources. (Source: Fielding Dissertation, 5.2.3)
* response status code
* selected representation
	* A target resource might be provided with, or be capable of generating, multiple representations that are each intended to reflect the resource's current state. An algorithm, usually based on content negotiation (Section 12), would be used to select one of those representations as being most applicable to a given request. This **selected representation** provides the data and metadata for evaluating conditional requests (Section 13) and constructing the content for 200 (OK), 206 (Partial Content), and 304 (Not Modified) responses to GET (Section 9.3.1).

> 6.3.2.7 Content Negotiation (Ref. Fielding Dissertation)
All resources map a request (consisting of method, identifier, request-header fields, and sometimes a representation) to a response (consisting of a status code, response-header fields, and sometimes a representation).

```
(Ref. RFC 9110; Extract select info below.)

From 9110 abstract: 
The Hypertext Transfer Protocol (HTTP) is a stateless application-level protocol for distributed, collaborative, hypertext information systems. 

4.2.1. http URI Scheme

The "http" URI scheme is hereby defined for minting identifiers within the hierarchical namespace governed by a potential HTTP origin server listening for TCP ([TCP]) connections on a given port.

  http-URI = "http" "://" authority path-abempty [ "?" query ]

The origin server for an "http" URI is identified by the authority component, which includes a host identifier ([URI], Section 3.2.2) and optional port number ([URI], Section 3.2.3). If the port subcomponent is empty or not given, TCP port 80 (the reserved port for WWW services) is the default. The origin determines who has the right to respond authoritatively to requests that target the identified resource, as defined in Section 4.3.2.

6.2. Control Data
Messages start with control data that describe its primary purpose.
Request message control data includes a request method (Section
9), request target (Section 7.1), and protocol version (Section 2.5).
Response message control data includes a status code (Section
15), optional reason phrase, and protocol version.

(From RFC 2396 URI syntax)
This "generic URI" syntax consists of a sequence of four main components: 

<scheme>://<authority><path>?<query>
```

`statcode = response.status`

## Target audience

    Application (client) developers


## REST benefit highlights

    Development flexibility
        Independent of web server or client implementation
        Implementation independence facilitates migration and/or upgrade
    Security
        Layered components allow security measures to be applied at multiple levels
        Manipulation and transfer of representations restricts direct client access to server resources


## Features that yield benefits

    HTTP open standard
    Well-defined constraints
        Identification of resources
        manipulation of resources through representations
        Self-descriptive messages
        Hypertext explicitly determines the state of the application



