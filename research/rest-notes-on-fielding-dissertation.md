# REST Notes on Fielding Dissertation

## REST goals

"REST emphasizes scalability of component interactions, generality of interfaces, independent deployment of components, and intermediary components to reduce interaction latency, enforce security, and encapsulate legacy systems."

## Terms & highlights
* REST architectural style

* software engineering principles

* constraints chosen to retain those principles

* REST is a hybrid style
	* derived from several of the network-based architectural styles described in Chapter 3 and 
	* combined with additional constraints that define a ***uniform connector interface***

* Stateless: each request from client to server must contain all of the information necessary to understand the request; session state is therefore kept entirely on the client

* Uniform Interface 

* distributed information services

* "REST is defined by four interface constraints:
identification of resources; manipulation of resources through representations; self-descriptive messages; and, hypermedia as the engine of application state."

> ***Note: In short, REST enables a web client and web server to communicate with each other in a common language, without the need for each to know implementation details about the other.***

* The key abstraction of information in REST is a resource. Any information that can be named can be a resource: a document or image, a temporal service ...

* Resources identifiers map to a resource. REST uses a resource identifier to identify the particular resource involved in an
interaction between components.

* A representation is a sequence of bytes, plus representation metadata to describe those bytes. Other commonly used but less precise names for a representation include: document, file, and HTTP message entity, instance, or variant.

* A software architecture is defined by a configuration of architectural elements—components, connectors, and data—constrained in their relationships in order to achieve a desired set of architectural properties.

* A component is an abstract unit of software instructions and internal state that provides a transformation of data via its interface.

* A connector is an abstract mechanism that mediates communication, coordination, or cooperation among components. Examples include shared representations, remote procedure calls, message-passing protocols, and data streams.


## Reference

1. Fielding, 2000, ["Architectural Styles and the Design of Network-based Software Architectures"](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)


### 