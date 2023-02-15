# Music Database APIs

## Overview

* Who provides it?
	- Spotify
	- SoundCloud
	- MusicBrainz
	- Others

* Who needs it? (Find examples of each)
	- Used in consumer electronics products
	- Musicians
	- Social media

* Common features
	- RESTful
	- Authentication for security

* Python request examples
	- Request

## Mini REST API

For developers interested in integrating server-based internet services into their applications, an application programming interface (API) can be an appealing solution. An application programming interface allows a client application to interact with a server using a common interface.

Many music APIs comply with the REpresentational State Transfer (REST) design style which is defined by a set of constraints. APIs that comply with REST constraints are called RESTful. REST APIs operate in two modes, request and response. The client sends a request to the server for data, and the server responds with a status code, and if appropriate, the requested data.

In this article, I will show how you can access a RESTful API database with Python. I will deconstruct the data sent by the client to the server, and the corresponding response received by the client from the server. To illustrate the mechanics of the process, I will use a RESTful music database API.

## Why REST?

A RESTful API allows the client to retrieve data from the server without the need to know details about the server back-end implementation. There is no need for the client to know which server or database management software is being used. In addition, the API enhances security by restricting who can access data and also, selectively restrict the data that can be accessed.

In a RESTful Web service, requests made to a resource's URI elicit a response with a payload formatted in HTML, XML, JSON, or some other format. The most common protocol for these requests and responses is HTTP, which provides operations (HTTP methods) such as OPTIONS, GET, POST, PUT, PATCH and DELETE.

## Music API
Several well known music services provide REST API database access to both directly to musicians and to partners who want to integrate their content and/or music into commercial products. 

Spotify for example, provides an API that allows hardware partners to develop applications for home audio systems, music players, headphones, and other internet-enabled devices. 
> Spotify Web API endpoints return JSON metadata about music artists, albums, and tracks, directly from the Spotify Data Catalogue.
> (Note: The sentence above was copied verbatum from "Web API | Spotify for Developers". Need to massage before including i article.)

SoundCloud is a music service that allows musicians to share their music with a community of artists and listeners. Musicians can use the API to upload upload and manage their music for their listeners.

MusicBrainz view themselves as an open encyclopedia for music metadata, modeled after Wikipedia in that it is community-driven. It's metadata content is primarily, but not exclusively targeted at music player and tagger applications.

> Next steps: Principles of HTTP Requests/Responses.

## Benefits

An API solves these problems by isolating the client from the server, only allowing communication through via a pre-defined and fixed interface. As a result, implementation changes on either client-side or server-side can be made without either affecting the other, as long as the interface protocol is followed.

A RESTful API benefits developers because it allows developers to connect client components to a server through a standard interface. This allows replaceable components to be swapped without changing code on either side of the interface. As an analogy, consider USB devices that connect to a computer. Mutiple USB devices, with the same or different functions, can connect to the same USB port and still function properly.
* widely accepted so lots of applications, libraries, tools, etc.

RESTful APIs are widely accepted because they leverage existing HTTP infrastructure, the same infrastructure and protocols that browsers use. As a result, lots of tools (applications, libraries, developers, etc.) are available. 

From an end user perspective, you can use my existing browser as a client to access server databases. 

From a developer perspective, you can easily integrate server data and resources into my applications.

From a service provider perspective, it allows them to make their services readily accessible to a wider audience. 

## API Examples

(Expand on this. Give more details on examples and put it in sentence and paragraph form.)

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



## Request & response

Music APIs are commonly used to retrieve either songs or music metadata such as artist, song title, album name, etc.

API requests are typically some form of an HTTP GET request. 

## References
1. [Rapid API](https://rapidapi.com/hub)
