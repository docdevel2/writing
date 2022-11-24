# Mini REST API

For developers interested in integrating music services into their applications, an application programming interface (API) and corresponding documentation are available. An application programming interface allows a client application to interact with a server using a common protocol.

## Benefits

* uniform interface between separate components

RESTful API benefits developers because it allows developers to connect client components to a server through a standard interface. This allows replaceable components to be swapped without changing code on either side of the interface. As an analogy, consider USB devices that connect to a computer. Mutiple USB devices, with the same or different functions, can connect to the same USB port and still function properly.

* RESTful dynamic content uses server-side rendering which renders the page in a web browser

(Expand on this later.)

* widely accepted so lots of applications, libraries, tools, etc.

RESTful APIs are widely accepted because they leverage existing HTTP infrastructure, the same infrastructure and protocols that browsers use. As a result, lots of tools (applications, libraries, developers, etc.) are available. 

From an end user perspective, I can use my existing browser as a client to access server databases. 

From a developer perspective, I can easily integrate server data and resources into my applications.

From a service provider perspective, it allows them to make their services readily accessible to a wider audience. 

* API Examples
	* Music 
	* Weather  
	* Sports
	* Food
	* Travel
	* Finance

* Security

Security is a significant concern these days. With the proliferation of hacker attacks and viruses, it is critical that web server offer protection against attacks and breaches. To combat these security threats, API providers commonly use a combination of these security measures.

* API security
	* HTTP
	* API Keys (Bearer token, JSON Web Token)
	* 0Auth



* mature infrastructure so no need to worry about support infrastructure
* responses are generally formatted as either JSON or XML, both widely accepted internet data exchange file formats
* RESTful systems aim for:
	- fast performance
	- reliability
	- expandability by reusing components
	- pluggable components facilitate maintenance
* Variety of proven security methods are available
* mature infrastructure

## Value

* Cost savings 
	- no need to develop those components
	- reduced maintenance resources
* Time savings
	- faster development by using existing components
* Flexibility
	- easily swap 

## REST

One such protocol is REpresentational State Transfer (REST). The REST protocol operates in two modes, request and response. The client sends a request to the server for data, and the server responds with a status code, and if appropriate, the requested data. REST is a common protocol used by music API web sites. Web site APIs that employ the REST protocol are referred to as RESTful.

A RESTful API allows the client to retrieve data from the server without the need to details the server backend implementation. There is no need for the client to know which server or database management software is being used. In addition, the API enhances security by restricting who can access data, what data is accessible.

In a RESTful Web service, requests made to a resource's URI elicit a response with a payload formatted in HTML, XML, JSON, or some other format. The most common protocol for these requests and responses is HTTP, which provides operations (HTTP methods) such as OPTIONS, GET, POST, PUT, PATCH and DELETE.

## Request & response

Music APIs are commonly used to retrieve either songs or music metadata such as artist, song title, album name, etc.

API requests are typically some form of an HTTP GET request. 

## References
1. [Rapid API](https://rapidapi.com/hub)
