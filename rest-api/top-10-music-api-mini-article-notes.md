# Top 10 Music API Mini Article Notes 
## (And how to retrieve music metadata)

Article—X DevAPI Notes
(NoSQL/MySQL Python API)

Music APIs encompass a variety of services, including online song streaming,  [concert information](https://www.programmableweb.com/api/eventful) ,  [download stores](https://www.programmableweb.com/api/discogs) , song lyrics, artist, label, song, and album data & metadata, reviews,  [playlist services](https://www.programmableweb.com/api/musicovery) ,  [music theory](https://www.programmableweb.com/api/hooktheory) , music composition, free music, band operations, and touring bands information. 


## Focus
* Goal: Use Python to automate the *process* of retrieving music metadata 
* Message: There are two common formats, and XML.
* JSON simplicity, and widespread availability of metadata in JSON format. Using a  Python API facilitates that process of migrating, updating, and expanding library metadata. Emphasize term *Document Store*.
* NoSQL database documents are comprised of JSON objects that are easily parsed and correlates well with Python dictionary objects (is correlate the best term or is mapping better?)
* discuss common use of json or xml for music sources like Amazon, Apple Music, Spotify, SoundCloud, and others
* Compare Create, Read, Update, Delete (CRUD) methods to standard (traditional) SQL statements.

## Narrative: (TBD) 
* Why? More flexible JSON database 
* Why? Create a local MySQL database from XML or JSON metadata from sources like music apps and online database 
 * SQL + NoSQL via X API facilitates migration 
* >> JSON-based is more flexible 
* >> Table-based is rigid (all fields—schema—must be pre-defined)
* >> Document-based is object-based/unstructured 
* CRUD methods compared to standard SQL statements 
* >> programmatic vs. text string 


## Outline sub-topics 
* What is an API? What is an API?
	* An[API](https://en.m.wikipedia.org/wiki/API) is a type of software interface, offering a service to other pieces of  software. 
	* An API, or Application Programming Interface, is a server that you can use to retrieve and send data to using code. APIs are most commonly used to retrieve data. [Ref. 12]
* Why use an API?
	* [Web API](https://www.programmableweb.com/news/how-api-principles-abstraction-benefit-api-providers/analysis/2015/12/03)
	* growth is thusly driven by service providers
	* greater developer productivity by packaging commodity and, often, complex functionality into easily reused API-based components
	* applications that can take advantage of the functionality abstracted by an API’s endpoint is limited only by the imaginations of developers and the capacity of the API provider’s infrastructure
	* Facebook API that allowed Instagram users to broadcast their latest photos
	* Examples: credit card processing, mapping, navigation and translation
	* support the HTTP command structure are often said to be “Web APIs.”
* Components/elements?
	* File format 
	* Authentication 
	* the majority of API providers make such connections possible over the HTTP protocol (Hypertext Transfer Protocol) [HTTP](https://www.programmableweb.com/news/why-did-they-put-web-web-apis/analysis/2015/12/03)
* How can I use a music API?
	* composite applications are sometimes called “mashups”
* Benefits?
	*  [Benefits](https://www.programmableweb.com/news/how-api-principles-abstraction-benefit-api-providers/analysis/2015/12/03)
	* why use an API instead of a static CSV dataset you can download from the web? APIs are useful in the following cases:
		* The data is changing quickly. An example of this is stock price
data. It doesn’t really make sense to regenerate a dataset and download it every minute — this will take a lot of bandwidth, and
be pretty slow. 
		* You want a small piece of a much larger set of data. Reddit comments are one example. What if you want to just pull your own comments on Reddit? It doesn’t make much sense to download
the entire Reddit database, then filter just your own comments.
		* There is repeated computation involved. **Spotify has an API that can tell you the genre of a piece of music. You could theoretically create your own classifier, and use it to compute music categories, but you’ll never have as much data as Spotify does.** In cases like the ones above, an API is the right solution. In this blog post, we’ll be querying a simple API to retrieve data about the
International Space Station (ISS).

* List top 10
* Pros & cons of each 


## Music metadata APIs

**Questions to answer for each API**

1. Is it RESTful?
2. Response format?
3. Authentication method?
4. Metrics? (Popularity, usage, etc.)
5. Pythonic?
6. Limits? (e.g. The number of results to fetch per page (defaults to 50).)

* >> SoundCloud API
	* ()
* >> Last.fm API
	* (  [https://www.dataquest.io/blog/last-fm-api-python/](https://www.dataquest.io/blog/last-fm-api-python/)  )
* >> Musixmatch API
	* ()
* >> Spotify Web API
	* ()
* >> Unofficial Shazam API
	* ()
* >> kanye.rest API
	* ()
* >> Apiseeds Lyrics API
* ()
* >> SHOUTcast Radio API
	* ()
* >> ChartLyrics Lyric API
	* ()
* >> MetroLyrics API
	* ()
* >> Opensong API
	* ()
* >> Discogs
	* ()


## From reading list 
* PEP 249 ( [https://peps.python.org/pep-0249/](https://peps.python.org/pep-0249/) )
* psycopg ( [https://www.psycopg.org/docs/usage.html](https://www.psycopg.org/docs/usage.html)  )
* DB-API ( [https://docs.python-guide.org/scenarios/db/](https://docs.python-guide.org/scenarios/db/) )
* PyMySQL ( [https://pypi.org/project/PyMySQL/](https://pypi.org/project/PyMySQL/) )
* Python Wiki/Database Programming 
	* ( [https://wiki.python.org/moin/DatabaseProgramming](https://wiki.python.org/moin/DatabaseProgramming) )
* Python Wiki/Db API FAQ 
	* ( [https://wiki.python.org/moin/DbApiFaq](https://wiki.python.org/moin/DbApiFaq) )

## API Basics

* Basic interactions [Ref 12]
	- Request (Get)
	- Response
		+ Response data
		+ Response code
* Endpoints [Ref 12]
	- Often there will be multiple APIs available on a particular server. Each of these APIs are commonly called endpoints.

## DB-API
Some examples of parameter passing [Ref 10]:
	* 	a list: .execute ("... col = ?", ["value"]) 
	* 	a tuple: .execute ("... col = ?", ("value")) 
	* 	variable arguments: .execute ("... col = ?", "value") 
	* 	a dictionary: .execute ("... col = :arg", {'arg': "value"}) 
	* 	keyword args: .execute ("... col = :arg", arg = "value")

* This API has been defined to encourage similarity between the Python modules that are used to access databases. By doing this, we hope to achieve a consistency leading to more easily understood modules, code that is generally more portable across databases, and a broader reach of database connectivity from Python. [Ref 5]

### Objects 
Connection objects 
Created when connection is opened.

Cursor objects
These objects represent a database cursor, which is used to manage the context of a fetch operation.

> Connection methods   
.close() to close the connection

.cursor()
Return a new Cursor Object using the connection.

> Cursor methods  
.close() to close the cursor object 

.execute()
Prepare and execute a database operation (query or command).

.fetchone()
Fetch the next row of a query result set, returning a single sequence, or None when no more data is available.

.fetchall()
Fetch all (remaining) rows of a query result, returning them as a sequence of sequences (e.g. a list of tuples).

## Create collection index
TBD

## JSON Path Syntax 
(Source: MySQL-refman-8.0, sec.11.5 p.2194)

For paths used in MySQL JSON functions, the scope is always the document being searched or otherwise operated on, represented by a leading  $  character. Path legs are separated by period characters (.). In MySQL, the scope of the path is always the document being operated on, represented as  $. You can use  '$'  as a synonym for the document in JSON path expressions.

fetchOne()  and fetchAll()  follow forward-only iteration semantics.

## Results and datasets 
(Source: XDevAPI, ch9)
Collection.find()  returns a data set with documents and  Table.select()  respectively Session.sql()  return a data set with rows.

Fetched dataset operations
>> find().execute() [for document operations]
(Note: Use double quotes for key and value strings as apostrophes may be interpreted as single quotes.)
>> select.execute() [for row operations]

## JSON Benefits 
> Schema-less database offers more flexibility; schema-less means that you can have documents with a different set of  [fields](https://en.wikipedia.org/wiki/Field_(computer_science))  in the same collection, without the need for satisfying a rigid table schema.  

> Document-based key:value dictionaries which are more native to programming languages   

> JavaScript Object Notation. It’s a file format with a human-readable structure consisting of key-value pairs that can be nested arbitrarily deep.  


# Market share
SQL databases are 60% 
NoSQL 40%
(2022 ScaleGrid survey:  [https://scalegrid.io/blog/2019-database-trends-sql-vs-nosql-top-databases-single-vs-multiple-database-use/](https://scalegrid.io/blog/2019-database-trends-sql-vs-nosql-top-databases-single-vs-multiple-database-use/)  )

> Source: 2022 ScaleGrid Database Trends Report  
(  [https://www.datamation.com/big-data/current-database-trends/](https://www.datamation.com/big-data/current-database-trends/)  )

> ScaleGrid is a database hosting company   
( https://ScaleGrid.io )

> Python   
2021 Statista report; 3rd most used programming language behind JavaScript and HTML/CSS
(  [https://www.statista.com/statistics/793628/worldwide-developer-survey-most-used-languages/](https://www.statista.com/statistics/793628/worldwide-developer-survey-most-used-languages/)  )

# Terminology 
	* 	Collection: A container that is used to store JSON documents in a MySQL database. Applications usually run operations against a collection of documents, for example to find a specific document. Collections contain JSON documents.
	* 	CRUD: Create, Read, Update, Delete
	* 	Data models: SQL is relational, NoSQL is non-relational
	* 	Document-based
	* 	document-oriented database
	* 	Document store 
	* 	document store model
	* 	Key-value pairs (check JSON & Python documentation)
	* 	JSON: “name/value pair”
	* 	Python: “key:value pair” (explicit python syntax)
	* 	MySQL References: key-value pair *USE THIS*
	* 	Mapping: NoSQL objects map to OOP objects (like Python)
	* 	MySQL Document Store allows developers to work with SQL relational tables and schema-less JSON collections.
	* 	NoSQL database: schema-less, allows mixed field types 
	* 	Object-based, object-oriented (NoSQL)
	* 	Relational database,  relational model 
	* 	Schema
	* 	Document model: Schema-less database, flexible schema, table fields/columns not predetermined 
	* 	Relational model: table fields/columns must be predetermined
	* 	SQL database: structured, table-based, same fields for all rows
	* 	Table-based
	* 	X DevAPI: MySQL Connector/Python provides a client library for the X DevAPI protocol that was introduced in MySQL 8.0

# Study references
[Ref 4, p.1 Supported Languages]
[Ref 4, p.1 Supported APIs]
[Ref 4, p.3 Global Session]
[Ref 4, p.15 MySQL Shell Sessions]
[Ref 1, p.3 “config.py” for security]
[Ref 1, p.3-4 Guidelines for Python Developers]
[Ref 1, p.13 Connecting to MySQL Using Connector/Python]
[Ref 2, p.420 Chapter 6.5 MySQL Connector/Python Coding Examples]
[Ref 4, p.34-37, Ch. 4.4-4.5 Password configuration] *Note: This may be a separate future project.*
[Ref 3, p.]
[Ref #, p.]
[Ref #, p.]
[Ref #, p.]
[Ref #, p.]


# References
1. MySQL-connectors-Python [MySQL Connector/Python Developer Guide] (Acrobat)
2. MySQL-connectors [Connectors and APIs] (Acrobat) 
3. MySQL-shell-Python-x-devapi-userguide [X DevAPI User Guide  for  MySQL Shell in Python Mode] (Acrobat)
4. MySQL-Shell-8.0 [MySQL Shell 8.0] (Acrobat) 
5. Python Database API Specification v2.0 (PEP 249) 
( [https://peps.python.org/pep-0249/](https://peps.python.org/pep-0249/) )
6. psycopg (URL)
7. DB-API (URL)
8. PyMySQL (URL)
9. Python Wiki/Database Programming (URL)
10. Python Wiki/Db API FAQ (URL)
11. Novice’s Guide to the Python 3 DB-API 
( [https://philvarner.github.io/pages/novice-python3-db-api.html](https://philvarner.github.io/pages/novice-python3-db-api.html) )
12. [Python API Tutorial: Getting Started with APIs](https://www.dataquest.io/blog/python-api-tutorial/)



###
	◦	


###