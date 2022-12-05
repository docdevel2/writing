# REST Notes
REpresentational State Transfer

## Keywords: Restful API, REST

## Highlights
* Defines a set of rules for web API behavior
* Based on HTTP protocol
* Essential operations are: Get, Put, Update, and Delete
* Typical application: machine to machine headless e-commerce

## Description 
(Source: https://en.m.wikipedia.org/wiki/Representational_state_transfer)

Representational state transfer (REST) is a software architectural style that was created to guide the design and development of the architecture for the World Wide Web. REST defines a set of constraints for how the architecture of an Internet-scale distributed hypermedia system, such as the Web, should behave.

REST has been employed throughout the software industry and is a widely accepted set of guidelines for creating stateless, reliable web APIs. A web API that obeys the REST constraints is informally described as RESTful. RESTful web APIs are typically loosely based on HTTP methods to access resources via URL-encoded parameters and the use of JSON or XML to transmit data.

In a RESTful Web service, requests made to a resource's URI elicit a response with a payload formatted in HTML, XML, JSON, or some other format. 

## Uniform interface 
(Source: https://en.m.wikipedia.org/wiki/Representational_state_transfer)

The uniform interface constraint is fundamental to the design of any RESTful system. It simplifies and decouples the architecture, which enables each part to evolve independently. The four constraints for this uniform interface are:
  
* 	Identification of resources
* 	Manipulation of resources
*	Self-descriptive messages and
* 	Hypermedia as the engine of application state

Generally REST describes a machine to machine interface. In web development REST allows content to be rendered when it is requested, often referred to as Dynamic Content. RESTful Dynamic content uses server-side rendering to generate a web site and send the content to the requesting web browser, which interprets the server's code and renders the page in the user's web browser

In a RESTful Web service, requests made to a resource's URI elicit a response with a payload formatted in HTML, XML, JSON, or some other format. The most common protocol for these requests and responses is HTTP, which provides operations (HTTP methods) such as OPTIONS, GET, POST, PUT, PATCH and DELETE.

Resource identification in requests - Individual resources are identified in requests, for example using URIs in RESTful Web services. The resources themselves are conceptually separate from the representations that are returned to the client. For example, the server could send data from its database as HTML, XML or as JSON—none of which are the server's internal representation.

## Fielding re: REST Architecture 

* 	Roy Fielding developed the REST architectural style
* 	independent of any specific implementation 
* 	unique to REST, the concept of resources
* 	layer of abstraction on the server; resources that encapsulate entities (e.g. files) on the server and so hiding the underlying implementation details (file server, database, etc.)
* 	information that can be named can be a resource: an image, a database query, a temporal service (e.g. “today’s weather in London”), or even a collection of other resources; this approach allows the greatest interoperability between clients and servers
* 	clients can only access resources using URIs
* 	client requests a resource using a URI and the server responds with a representation of the resource
* 	resource is manipulated through hypertext representations transferred in messages between the clients and servers
* 	strong decoupling of client and server together with the text- based transfer of information using a uniform addressing protocol
* 	Benefits: robustness (anarchic scalability), independent deployment of components, large-grain data transfer, and a low-entry barrier for content readers, content authors and developers alike

## Web Architecture 
(REST **Relationship to the World Wide Web and REST Architectures**)

Source: [Web Services Architecture](https://www.w3.org/TR/ws-arch/)

The World Wide Web operates as a networked information system that imposes several constraints: 

Agents identify objects in the system, called *resources*, with Uniform Resource Identifiers (URIs). Agents represent, describe, and communicate resource state via *representations* of the resource in a variety of widely-understood data formats (e.g. XML, HTML, CSS, JPEG, PNG). Agents exchange representations via protocols that use URIs to identify and directly or indirectly address the agents and resources. ~[Web Arch]~

An even more constrained architectural style for reliable Web applications known as *Representation State Transfer* (REST) has been proposed by Roy Fielding and has inspired both the W3C Technical Architecture Group's architecture document ~[Web Arch]~ and many who see it as a model for how to build Web services ~[Fielding]~. The REST Web is the subset of the WWW (based on HTTP) in which agents provide __*uniform interface semantics* -- essentially create, retrieve, update and delete --__ rather than arbitrary or application-specific interfaces, and manipulate resources only by the exchange of *representations*. Furthermore, the REST interactions are "stateless" in the sense that the meaning of a message does not depend on the state of the conversation.

We can identify two major classes of Web services:

* 	REST-compliant Web services,* in which the primary purpose of the service is to manipulate XML representations of Web resources using a uniform set of "stateless" operations; and
* *arbitrary Web services,* in which the service may expose an arbitrary set of operations. 

Both classes of Web services use URIs to identify resources and use Web protocols (such as HTTP and SOAP 1.2) and XML data formats for messaging. (It should be noted that SOAP 1.2 *can* be used in a manner consistent with REST. However, SOAP 1.2 can also be used in a manner that is *not* consistent with REST.)

## REST Protocols 
(Source: https://www.w3.org/2001/tag/2002/0828-archdoc)

### Protocols
As mentioned in the introduction, the Web is designed to create the large-scale effect of a shared information space that scales well and behaves predictably. The architectural style known as **Representational State Transfer** [~REST~] encapsulates this notion of a shared information space. According to Fielding:

>
*REST provides a set of architectural constraints that, when applied as a whole, emphasizes scalability of component interactions, generality of interfaces, independent deployment of components, and intermediary components to reduce interaction latency, enforce security, and encapsulate legacy systems.*

*-- Roy Fielding, Section 5.5 of [~REST]~*

HTTP has been specially designed for REST interactions. HTTP has a variety of ~dereference~ methods, including GET, POST, PUT, and DELETE.
The following sections use the REST model to explain how Web protocols take into account the properties of resources and URIs, as well as real-world time and space constraints, in order to improve the user's Web experience.

### 4.1. REST constraints

The REST constraints are:

**Client/server model**

REST separates rendering concerns from the data model and control logic.

**Stateless protocols**

Each request from client to server contains all the necessary data for a server to understand the request.

**Caching**

Some representations may be cached. Intermediaries may respond on behalf of a server with the cached data.

**Uniform Interface**

The consistent constraints on interface between components, specifically resource identification, resource manipulation through representations, self-describing messages, and messages as the embodiment of application state.

**Layering**

The encapsulation of each component so that components "know" only about the components with which they are interacting.

**Optional Code-on-demand**

Clients may download and execute code (such as Java Applets, ActiveX controls, scripts, and XSLT).

REST focuses on the roles of components, the constraints upon their interaction with other components, and their interpretation of significant data elements. REST ignores the details of component implementation and protocol syntax. REST components communicate by transferring a ~representation of a resource~, selected dynamically based on the capabilities or desires of the recipient and the nature of the resource. Whether the representation is in the same format as the raw source, or is derived from the source, remains hidden behind the interface.
Typical hypertext systems support one of three possible styles of data representation: 

1.	render the data where it is located and send a fixed-format image to the recipient,
2.	encapsulate the data with a rendering engine and send both to the recipient, or
3.	send the raw data to the recipient along with metadata that describes the data type, so that the recipient can choose their own rendering engine.
	
The Web provides a hybrid of all three options by focusing on a shared understanding of data types with metadata, but limiting the scope of what is revealed to a standardized interface.

Web components perform various roles in interactions. User agents, gateways, proxies, and origin servers are the main roles that a component can act in. A component may act in different roles depending upon the interaction.

### 4.2. Ideas and issues

1.	Consistency of media types and message contents (from " [TAG Finding: Internet Media Type registration, consistency of use](http://www.w3.org/2001/tag/2002/0129-mime) "
	
2.	Consistency of communicating character encoding (same source).
	
3.	HTTP as a substrate protocol [ [TAG issue HTTPSubstrate-16](http://www.w3.org/2001/tag/ilist#HTTPSubstrate-16) ]

## Operations

* DELETE method is not safe, but is idempotent 
* GET can use query parameters – and use forms to know how to construct query
* PUT 
* POST 

## Summary 

* 	Comment: REST is a set of rules to make http requests to a web site and receive a payload 
* 	Machine to machine interface: headless commerce 
* 	clients can only access resources using URIs
* 	Benefits: robust, independent components, easy to use, scalable (small to large amounts of data)

## References 

	1. [Representational State Transfer]( [https://en.m.wikipedia.org/wiki/Representational_state_transfer](https://en.m.wikipedia.org/wiki/Representational_state_transfer)
	2. [Web Services Architecture](https://www.w3.org/TR/2004/NOTE-ws-arch-20040211/#relwwwrest)
	3. [Architectural Principles of the World Wide Web](https://www.w3.org/2001/tag/2002/0828-archdoc)
	


###