# why-use-columnar-dbms-draft0.md  

# Why Use a Columnar DBMS  

> (Create *SPICY* intro.)  
> Challenges:  
> 
> * Artificial intelligence, machine learning, and business insights requirements  
> * Query performance  
> * Efficient Data Compression  
> * Enhanced Analytical Capabilities (e.g. complex joins)  
> 

**The challenge.** Data analysis applications like artificial intelligence, machine learning, and business insights present significant challenges for traditional row-based database management systems (DBMS).  

The most widely deployed database management systems are row-oriented, representing data as tables organized by rows and columns&mdash;like spreadsheets. Each row is a record (object) with attributes that represent the corresponding columns for that row. Row-oriented DBMS are best suited for online transaction processing (OLTP) business processes such as sales transactions, customer engagement, banking, e-commerce, etc. These applications typically process records by rows where each record identifies a customer, product, or transaction that has related attributes.  

(Insert example)  

## What is a Columnar DBMS  

In contrast to row-oriented OLTP applications, data analysis applications also known as online analytics processing (OLAP), tend to retrieve data by columns instead of rows. As a result, row-oriented databases are not ideally suited for OLAP applications because potentially every row in a database would need to read to retrieve data from each column. Applications like data mining, machine learning, and artificial intelligence use large volumes of data, on the order of terabytes. While retrieving a single column may be feasible for a relatively  cansmall database, it is not feasible for a large one for performance, cost, complexity, and capacity (compression) reasons.  

For a simple example, consider a sales transaction in which a transaction record consists of six fields: the index, customer name, purchase date, purchase amount, product ID, and product category. If you want to know how many products for a particular category sold on a given day, you would have to read an entire row and scan for that attribute in the row. You can see how large tables could quickly consume a lot of CPU time and storage resources.  

(Insert example)  

## Architectures  

Among the critical challenges that row-oriented databases present are performance and efficiency. To address these challenges, database architects have explored a variety of architectural approaches. Traditional row-oriented relational DBMSs were conceived in the late 1960s and early 1970s when hardware limitations influenced their design.  

* Academic  
	- C-store (> Vertica)  
	- 1996: MonetDB (> VectorWise > Actian Vector)  
	- VectorWise (> Actian Vector)  

* Commercial  
	- Vertica (C-Store)  
	- Actian Vector (VectorWise)  
	- Google BigQuery  
		- ParAccel Analytic Database was a parallel relational database system using a shared-nothing architecture  with a columnar orientation,  adaptive compression, memory-centric design. ParAccel's DBMS engine is built for analytics, initially based on PostgreSQL.  

In recent years, there has been renewed interest in so-called column-oriented systems, sometimes also called column-stores. Early influential efforts include the academic systems MonetDB, VectorWise 1 and C-Store as well as the commercial system SybaseIQ. VectorWise and C-Store evolved into the commercial systems Ingres VectorWise and Vertica, respectively, while by late 2013 all major vendors have followed this trend and shipped column-store implementations in their database system offerings, highlighting the significance of this new technology, e.g., IBM, Microsoft, SAP and Oracle.  


## Architectural features and techniques  

Use these bullets as talking points to describe expand upon description of architectural features and techniques throughout the article.  

* 	Column tuple objects: virtual ID, tuple identifier (e.g., a numeric primary key)  
* 	Vectorization: operating on multiple values simultaneously  
* 	Late materialization: delayed tuple reconstruction  
* 	Column-specific compression  
* 	Direct operation on compressed data  
* 	Efficient join implementations  
* 	Redundant column representation: multiple sort orders  
* 	Database cracking and adaptive indexing  
* 	Efficient loading: slow load and update  

## Vectorization  

>**vector indexing**  

>* a specialized type of index designed to store and manage multidimensional data called vectors.  
* A vector index is a data structure used in computer science and information retrieval to efficiently store and retrieve high-dimensional vector data, enabling fast similarity searches and nearest neighbor queries.  
* A vector index is a data structure that enables fast and accurate search and retrieval of vector embeddings from a large dataset of objects.  

>(Why?)
>
* called “vectorized execution” pioneered in VectorWise, which strikes a balance between full materialization and tuple pipelining  
* model separates query progress control logic from data processing logic  
* operators in vectorized processing are similar to those in tuple pipelining, with the sole distinction that the next() method of each operator returns a vector of N tuples as opposed to only a single tuple  
* Typically, sequential operators (project, selection) work best on vertical vectors (exploiting automatic memory prefetching and SIMD opportunities)  
>
Vector processing advantages/benefits:  
>
(Why?)  
>
* Reduced interpretation overhead: improve performance by two orders of magnitude by reducing function calls  
* Better cache locality: fit all query vectors in the CPU cache  
* Compiler optimization opportunities: vectorized primitives trigger compilers to generate SIMD instructions  
* Block algorithms: give rise to logical algorithm optimizations  
* Parallel memory access: get good memory bandwidth on modern computers  
* Profiling: provides highly detailed performance insight into where CPU cycles are spent (complements adaptive execution)  
* Adaptive execution: tests all alternative implementations and subsequently uses the best performing implementation most of the time (complements profiling)  

## Column compression  

(What?)  

* The basic notion of compression is assumed to be understood.  
* Can apply to rows, columns, or both  
* Can compress column-at-a-time  
* Compression yields higher performance via CPU & I/O efficiency and potentially lower costs (See Why below)  

(Why?)  

* Columns are more compressible (by algorithms) than rows because the data is similar  
* compression does improve performance (in addition to reducing disk space); if data is compressed, then less time is spent in I/O during query processing as less data is read from disk into memory (and from memory to CPU)  
* as CPUs are getting much faster compared to memory bandwidth, the cost of accessing data costs more in terms of CPU cycles than it did in the past  
* decompressing compressed data fast which is preferable to transferring uncompressed and thus bigger data at slow speeds (in terms of waisted CPU cycles)  

## Late Materialization ([whycol-1] sec. 4.4)  

> “In a column-store, information about a logical entity (e.g., a person) is stored in multiple locations on disk (e.g., name, e-mail address, phone number, etc. are all stored in separate columns), whereas in a row store such information is usually co-located in a single row of a table. However, most queries access more than one attribute from a particular entity. Furthermore, most database output standards (e.g., ODBC and JDBC) access database results entity-at-a-time (not column-at-a-time). Thus, at some point in most query plans, data from multiple columns must be combined together into ‘rows’ of information about an entity. Consequently, this join-like materialization of tuples (also called “tuple construction”) is an extremely common operation in a column store.”

> “Naive column-stores store data on disk (or in memory) column-by-column, read in (to CPU from disk or memory) only those columns relevant for a particular query, construct tuples from their component attributes, and execute normal row-store operators on these rows to process (e.g., select, aggregate, and join) data. Although likely to still outperform the row-stores on analytical workloads like those found in data warehousing, this method of **constructing tuples early in a query plan (“early materialization”)** leaves much of the performance potential of column-oriented databases unrealized.”

* “In a column-store that uses **late materialization, the predicates are applied to the column for each attribute separately**, and a list of positions (ordinal offsets within a column) of values that passed the predicates are produced.”
* “Late materialization means that we always operate on individual columns ...”
* MonetDB is one of the few database systems using full materialization, product of its BAT Algebra designed to make operators and their interactions simpler and thus more CPU efficient. However, MonetDB therefore may cause excessive resource utilization in queries that generate large intermediate results. 
* “‘vectorized execution’ pioneered in VectorWise, which strikes a balance between full materialization and tuple pipelining.”  

Examples:  

* For example, when applying a predicate evaluation operation in the where clause (such as WHERE salary > $100,000), memory bandwidth is not wasted shipping other attributes from the same set of tuples to the CPU, since only the salary attribute is relevant for that particular operator.  
* Despite all the reasoning above, late materialization can sometimes be slower than early materialization (especially if a naive implementation is used). For example, if a predicate is used that is not restrictive (e.g., WHERE salary > $100 AND age > 5 AND ...) on many attributes within a tuple  

**Contrast early materialization.**  
(Source: [whycol-1])

* constructing tuples early in a query plan (“early materialization”) leaves much of the performance potential of column-oriented databases unrealized.  

"This (standards-compliant relational database interface) means they must ultimately stitch together separate columns into tuples of data that are output. Determining the tuple construction point in a query plan is the inverse of the problem of applying projections in a row-oriented database, since rather than deciding when to project an attribute out of an intermediate result flowing through the query plan, the system must decide when to add it in. Lessons from when to apply projection in row-oriented databases (projections are almost always performed as soon as an attribute is no longer needed) suggest a natural **tuple construction policy: at each point where a column is accessed**, add the column to an **intermediate tuple representation** if that column is needed by some later operator or is included in the set of output columns. Then, at the top of the query plan, these intermediate tuples can be directly output to the user. We call this process of adding columns to intermediate results materialization, and call the simple scheme described above **early materialization**, since it seeks to **form intermediate tuples as early as possible**." [whycol-13]  

## VectorWise late materialization  

Balance between full materialization & tuple pipeline

> An additional drawback of the column-at-a-time execution model is its full materialization of intermediate results. For example, if a select operator consumes its complete input column in one go, then it needs to materialize a result which represents all qualifying tuples, resulting in a significant overhead especially as we scale to bigger data inputs. Together, these aspects make MonetDB vulnerable to swapping when its working set starts exceeding RAM.  

The main innovation in VectorWise

> * vectorized execution model  
> * VectorWise processes one **block/vector of a column at a time** as opposed to one column-at-a-time or one tuple-at-a-time.  
> * VectorWise also provides a novel way of handling updates (Positional Delta Trees [41]), and new high-speed compression algorithms  
> * VectorWise does perform explicit I/O, in an advanced way, adaptively finding synergy in the I/O needs of concurrent queries through its Active Buffer Manager (ABM) and Cooperative Scans [98]. VectorWise also provides a novel way of handling updates (Positional Delta Trees [41]), and new high-speed compression algorithms  

**tuple-at-a-time pipelining**

> In tuple-at-a-time pipelining, one tuple-at-a-time is pushed through the query plan tree. The next() method of each relational operator in a query tree produces one new tuple at-a-time, obtaining input data by calling the next() method on its child operators in the tree. Apart from being elegant in the software engineering sense, this approach has the advantage that materialization of intermediate results is minimized.  

**Full materialization**

> In full materialization, on the other hand, each query operator works in isolation, fully consuming an input from storage (disk, or RAM) and writing its output to storage. MonetDB is one of the few database systems using full materialization, product of its BAT Algebra designed to make operators and their interactions simpler and thus more CPU ecient. However, MonetDB therefore may cause excessive resource utilization in queries that generate large intermediate results.

**Vectorized execution.**

> This model separates query progress control logic from data processing logic. Regarding control flow, the operators in vectorized processing are similar to those in tu- ple pipelining, with the sole distinction that the next() method of each operator returns a vector of N tuples as opposed to only a single tuple. Regarding data processing, the so-called primitive functions that oper- ators use to do actual work (e.g., adding or comparing data values) look much like MonetDB’s BAT Algebra, processing data vector-at-a-time. Thus, vectorized execution combines pipelining (avoidance of material- ization of large intermediates) with the array-loops code patterns that make MonetDB fast.  


## BAT Algebra  
(Source: [whycol-1])  

> "The reason behind the efficiency of the BAT Algebra is its hard-coded semantics, causing all operators to be predicate-less. For comparison, in the relational algebra in traditional systems, the Join and Select operators take an arbitrary Boolean column expression that determines which tuples must be joined and selected. The fact that this Boolean expression is arbitrary, and specified at query time only, means that the RDBMS must include some expression interpreter in the critical runtime code-path of the Join and Select operators. Such predicates do not occur in BAT Algebra; therefore we also say it has “zero degrees of freedom”. This absence of freedom means the interpreter is removed from inside the operator; all BAT algebra operators perform a fixed hard-coded action on a simple array. As such, complex expressions in a query must be mapped into multiple subsequent BAT Algebra operators. Expression interpretation in MonetDB effectively occurs on the granularity of whole column-at-a-time BAT Algebra operators, which much better amortizes interpretation overhead."  
> 
> "The column-at-a-time processing is realized through the BAT Algebra, which offers operations that work only on a handful of BATs, and produce new BATs. BAT stands for Binary Association Table, and refers to a two-column \<surrogate,value> table as proposed in DSM. The surrogate is just a Virtual ID; it effectively is the array index of the column and is not materialized. Both base data and intermediate results are always stored in BATs, and even the final result of a query is a collection of BATs. MonetDB hence takes late tuple materialization to the extreme. BATs are essentially in-memory (or memory mapped) arrays. The BAT algebra operators consume and produce BATs."  
>
> The absence of tuple reconstruction fits another goal of MonetDB,
namely using a single internal data representation (BATs) to manipulate data of widely different data models.  

## C-Store Tech  

* Compressed columns  
* On disk data representation (projection) is a compressed set of column files  
* Each column can be copied and stored in different sort orders  
* A hybrid architecture with a WS component optimized for frequent insert and update and an RS component optimized for query performance. [whycol-2]  

## MonetDB Tech  

* "Execution engine, which uses a column at-a-time-algebra" [whycol-1]  
* BAT algebra  
* Full materialization  

## VectorWise Tech  

* Vectorized execution engine; processes vectors of N tuples  
* Vector-at-a-time query  

## Glossary  

* BAT: Binary Association Table; refers to a two-column \<surrogate,value> table as proposed in DSM  
* DSM: DECOMPOSITION STORAGE MODEL; stores a single attribute for all tuples contiguously in a block of data. Sometimes also called vertical partitioning.  
* early materialization: constructing tuples early in a query plan  
* late materialization: form tuples after some part of the (query) plan has been processed [whycol-13]  
* materialization: tuple construction  
* query plan: A query plan (or query execution plan) is a sequence of steps used to access data in a SQL relational database management system. This is a specific case of the relational model concept of access plans. [Wikipedia-Query Plan](https://en.wikipedia.org/wiki/Query_plan) The (C-Store) query optimizer will accept a SQL query and construct a query plan [whycol-2]  

## References  

[whycol-1] Abadi, D., Boncz, P., Harizopoulos, S., Idreos, S., & Madden, S. (2013). "The design and implementation of modern column-oriented database systems." Foundations and Trends® in Databases, 5(3), 197-280., https://stratos.seas.harvard.edu/files/stratos/files/columnstoresfntdbs.pdf  

[whycol-2] Michael Stonebraker, et al., “C-Store: A Column-oriented DBMS”, Proceedings of the 31st VLDB Conference, Trondheim, Norway, 2005, https://web.stanford.edu/class/cs345d-01/rl/cstore.pdf  

[whycol-3] Microsoft, “Columnstore indexes: Overview”, https://learn.microsoft.com/en-us/sql/relational-databases/indexes/columnstore-indexes-overview  

[whycol-4] Oracle, “MySQL 8.0 Reference Manual”, 12.20.2  

[whycol-6] Oracle, “Database In-Memory Guide”, https://docs.oracle.com/en/database/oracle/oracle-database/21/inmem/database-memory-guide.pdf  

[whycol-7] "MySQL 8.0 Reference Manual", https://dev.mysql.com/doc/refman/8.0/en/join.html  

[whycol-8] "MySQL 8.0 Reference Manual", sec. 3.3.4.9, https://dev.mysql.com/doc/refman/8.2/en/multiple-tables.html  

[whycol-9] Peter Boncz. Monet: A next-generation DBMS kernel for query- intensive applications. University of Amsterdam, PhD Thesis, 2002, https://pure.uva.nl/ws/files/3551242/21018_Thesis.pdf  

[whycol-10] Marcin Zukowski and Peter A. Boncz. Vectorwise: Beyond column stores. IEEE Data Eng. Bull., 35(1):21–27, 2012  

[whycol-11]  “What is the projection operation in DBMS?”, https://www.educative.io/answers/what-is-the-projection-operation-in-dbms   

[whycol-12] “PROJECT Operation in Relational Algebra”, https://www.geeksforgeeks.org/project-operation-in-relational-algebra/ 

[whycol-13] "Materialization Strategies in a Column-Oriented DBMS", https://dspace.mit.edu/bitstream/handle/1721.1/34929/MIT-CSAIL-TR-2006-078.pdf  

[whycol-14] Carnagie Mellon, "Storage Models & Data Layout", https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwil7ojri5aEAxVpgYQIHQU_ChkQFnoECA4QAw&url=https%3A%2F%2F15721.courses.cs.cmu.edu%2Fspring2018%2Fslides%2F10-storage.pdf&usg=AOvVaw3dZhOcIFwNiKa0vO2kNPFj&opi=89978449  

---  

---  

## Random notes below  

>NOTE: Decomposition Storage Model or DSM–a predecessor to column-
stores (Source: "Harvard Column Stores")


## The problem 
* *Bandwidth* 
* **Solution:** Columnar 

## Timeline 
* MonetDB: 2002 [16]
* C-Store: 2005  [CS-1]
* VectorWise: 2012 [99]

## Products  

* Academic  
	- C-store (> Vertica)  
	- MonetDB (> VectorWise > Actian Vector)  
	- VectorWise (> Actian Vector)  

* Commercial  
	- Vertica (C-Store)  
	- Actian Vector (VectorWise)  
	- Google BigQuery  
		- ParAccel Analytic Database was a parallel relational database system using a shared-nothing architecture  with a columnar orientation,  adaptive compression, memory-centric design.[20] ParAccel's DBMS engine is built for analytics, initially based on PostgreSQL  


## Column architecture notes

* Column tuple objects: virtual ID, tuple identifier  
* Vectorization: operating on multiple values simultaneously   
* Late materialization: delayed tuple reconstruction  
* Column-specific compression  
* Direct operation on compressed data  
* Efficient join implementations  
* Redundant column representation: multiple sort orders  
* Database cracking and adaptive indexing  
* Efficient loading: slow load and update  
* column-at-a-time processing is realized through BAT Algebra  

## Common architectural features and techniques 

* Compression 
* Column objects: each column is stored independently as a separate data object
* Column operators 
* Vectorization 
* Late materialization  

## C-Store [1]  

* On disk data representation is a compressed set of column files  
* WOS speeds load operation  
* Each column can be copied and stored in different sort orders  
* Sparse indexes for column values and tuple  
* Query execution accesses data from ROS and WOS and joining the results  

## C-Store features/benefits 

See [whycol-2] sec. Conclusions, “update-240203”, and “columnar-update-240203-v2.md”  

---

> **Abstract**   
>   
> "This paper presents the design of a **read-optimized relational DBMS** that contrasts sharply with most current systems, which are write-optimized. Among the many differences in its design are: storage of data by column rather than by row, careful **coding and packing of objects into storage including main memory during query processing**, storing an overlapping collection of **column-oriented projections**, *rather than the current fare of tables and indexes*, a non-traditional implementation of transactions which includes high availability and **snapshot isolation for read-only transactions**, and the extensive use of bitmap indexes to complement B-tree structures. We present preliminary performance data on a subset of TPC-H and show that the system we are building, C-Store, is substantially faster than popular commercial products. architecture looks very encouraging."  

---  

> The innovative features of C-Store include:  
> 
1. A hybrid architecture with a WS component optimized for frequent insert and update and an RS component optimized for query performance.  
2. Redundant storage of elements of a table in several overlapping projections in different orders, so that a query can be solved using the most advantageous projection.  
3. Heavily compressed columns using one of several coding schemes.  
4. A column-oriented optimizer and executor, with different primitives than in a row-oriented system.  
5. High availability and improved performance through K-safety using a sufficient number of overlapping projections.  
6. The use of snapshot isolation to avoid 2PC and locking for queries.  

* “[C-Store combines] in a single piece of system software, both a read-optimized column store and an update/insert-oriented writeable store, connected by a tuple mover” (hybrid architecture)

**Data Model**

> “C-Store supports the standard relational logical data model, where a database consists of a collection of named tables, each with a named collection of attributes (columns). As in most relational systems, attributes (or collections of attributes) in C-Store tables can form a unique primary key or be a foreign key that references a primary key in another table. The C-Store query language is assumed to be SQL, with standard SQL semantics. **Data in C-Store is not physically stored using this logical data model.** Whereas most row stores implement physical tables directly and then add various indexes to speed access, **C-Store implements only projections.** Specifically, a C-Store projection is anchored on a given logical table, T, and contains one or more attributes from this table. In addition, a projection can contain any number of other attributes from other tables, as long as there is a sequence of n:1 (i.e., foreign key) relationships from the anchor table to the table containing an attribute.” [whycol-2]   

* “[Each projection] contains one or more attributes from this table”  
* “The C-Store query language is assumed to be SQL”  
* A projection is simply a set of columns with the same cardinality and ordering.  
* C-Store query operators accept predicates (Pred), join indexes (JI), attribute names (Att), and expressions (Exp) as arguments.  

---  

**C-Store Indexing (sec. 2)**  

>"C-Store proposed the concept of *projections*, i.e., to replicate each table multiple times and each replica may be ordered by a different attribute. In addition, each *replica* does not necessarily have to contain all of the table’s attributes. A query may use a single covering projection which is ordered (ideally) by the attribute which participates in the query’s most selective predicate, thus minimizing the effort needed to search as well as minimizing the effort needed for tuple reconstruction. Given that columns compress very well, materializing these extra projections does not bring a significant storage overhead when compared to a traditional row-store system."  

---
**Projections**  

> "C-Store physically stores a collection of columns, each sorted on some attribute(s). Groups of columns sorted on the same attribute are referred to as *“projections”*; the same column may exist in multiple
projections, possibly sorted on a different attribute in each."

---

## C-Store Query Execution

The **query optimizer** will accept a SQL query and **construct a query plan** of execution nodes. In this section, we describe the nodes that can appear in a plan and then the architecture of the optimizer itself. [whycol-2] 

**C-Store storage.** “Since everything is a column, storage is simply the persistence of a collection of columns.” [whycol-2] 

## C-Store conclusions
(Source: [whycol-2])

This paper has presented the design of C-Store, a radical departure from the architecture of current DBMSs. Unlike current commercial systems, it is aimed at the “read-mostly” DBMS market. The innovative contributions embodied in C-Store include:  

* A column store representation, with an associated query execution engine.  
* A hybrid architecture that allows transactions on a column store.  
* A focus on economizing the storage representation on disk, by coding data values and dense-packing the data.  
* A data model consisting of overlapping projections of tables, unlike the standard fare of tables, secondary indexes, and projections.  
* A design optimized for a shared nothing machine environment.
* Distributed transactions without a redo log or two phase commit.
* Efficient snapshot isolation.  

## MonetDB features/benefits  

“The philosophy behind the BAT Algebra can also be paraphrased as “the RISC approach to database query languages”: by **making the algebra simple**, the opportunities are created for implementations that **execute the common case very fast.**” ([whycol-1], sec. 3.2)  

“The reason behind the efficiency of the BAT Algebra is its hard-coded semantics, causing all operators to be predicate-less.” ([whycol-1], sec. 3.2) This eliminates the need for expression interpreters to be built into the critical paths of the SELECT and  JOIN operators.  
(For front-end/back implementation description, see “Spontaneous 
Notes 10/6/23”)  

## MonetDB 
(Source: [whycol-1])

* “MonetDB works by performing simple operations column-at-a-time instead tuple-at-a-time”
* “Query optimization, which is done at run-time, during query incremental execution”
* “uses memory mapping to provide the BAT Algebra operations direct access to it”
* MonetDB stores data one column-at-a-time both in memory and on disk
* Late materialization  

## MonetDB  architecture [whycol-1]  

* “Execution engine uses a column at-a-time-algebra”
* “Indexing, which is not a DBA task but happens as a by-product of query execution, i.e., database cracking”
* “Query optimization, which is done at run-time, during query incremental execution”
* “Transaction management, which is implemented using explicit additional tables and algebraic operations, so read-only workloads can omit these and avoid all transaction overhead”
* Basis for VectorWise architecture 
* “MonetDB works by performing simple operations column-at-a-time instead tuple-at-a-time” 
* “column-at-a-time primitives not only get much more work done in fewer instructions - primarily thanks to eliminating tuple-at-a-time iterator function calls - but its instructions also run more efficiently in modern CPUs”
* “uses memory mapping to provide the BAT Algebra operations direct access to it, unhindered by any API. The absence of a buer manager means MonetDB must rely on providing virtual memory access advice to the OS, which means the system does not have absolute control over I/O scheduling.”

MonetDB is designed from scratch focusing on handling analytical workloads efficiently on modern hardware. MonetDB stores data one column-at-a-time both in memory and on disk and exploits bulk processing and late materialization. It solely relies on memory mapped files avoiding the overhead and complexity of managing a buffer pool. MonetDB differs from traditional RDBMS architecture in many aspects, such as its:  

* Execution engine, which uses a column at-a-time-algebra,  
* Processing algorithms, that minimize CPU cache misses rather than IOs,  
* Indexing, which is not a DBA task but happens as a by-product of query execution, i.e., database cracking,
* Query optimization, which is done at run-time, during query incremental execution and  
* Transaction management, which is implemented using explicit additional tables and algebraic operations, so read-only workloads can omit these and avoid all transaction overhead.
* first major column-store project in the academic community
* original motivation behind MonetDB, which was ini- tially developed as a main-memory only system, was to address the **memory-bandwidth problem** and also improve computational **efficiency** by avoiding an expression interpreter  

## Predicate-less 
(Note: Absence of a predicate violates Codd’s rules for relational databases. Discuss Codd’s predicate rules as a sidebar.)

> “[Traditional] RDBMSs must include some expression interpreter in the critical runtime code-path of the Join and Select operators. Such predicates do not occur in BAT Algebra; therefore we also say it has “zero degrees of freedom”. This absence of freedom means **the interpreter is removed from inside the operator**; all BAT algebra operators perform a fixed hard-coded action on a simple array. As such, **complex expressions** in a query must be mapped into **multiple subsequent BAT Algebra operators**. Expression interpretation in MonetDB effectively occurs on the granularity of **whole column-at-a-time BAT Algebra operators**, which much better amortizes interpretation overhead.” [whycol-1]  

## VectorWise features/benefits

“The main innovation in VectorWise is its vectorized execution model”  

(For other benefits, see “Vectorization” in draft0. Also, [whycol-1] sec.4.1)  

## VectorWise 
(Source: [whycol-1])

* “stores columns uncompressed on disk”
* “vectorized execution model which strikes a balance between full materialization of intermediate results in MonetDB and the high functional overhead of tuple-at-a-time iterators in traditional systems”
* “processes one block/vector of a column at a time as opposed to one column-at-a-time or one tuple-at-a-time” (a vector is a set of multiple tuples)
* vectorized execution combines pipelining (avoidance of materialization of large intermediates) with the array-loops code patterns that make MonetDB fast  

## VectorWise  architecture [whycol-1]  

* “VectorWise architecture was derived from MonetDB” 
* “stores columns uncompressed on disk” 
* “vectorized execution model which strikes a balance between full materialization of intermediate results in MonetDB and the high functional overhead of tuple-at-a-time iterators in traditional systems”  
* “processes one block/vector of a column at a time as opposed to one column-at-a-time or one tuple-at-a-time”  
* “perform explicit I/O, in an advanced way, adaptively finding synergy in the I/O needs of concurrent queries through its Active Buffer Manager (ABM) and Cooperative Scans”  
* “provides a novel way of handling updates (Positional Delta Trees [41]), and new high-speed compression algorithms”  
* the operators in vectorized processing are similar to those in tuple pipelining, with the sole distinction that the next() method of each
operator returns a vector of N tuples as opposed to only a single tuple

(For architecture details, see ch. 3, Harvard-columnstoresfntdbs.pdf)

## Two main architectures [whycol-1]  

* **Column-store only.** “The first approach involves storing data one column-at-a-time on disk but relies on a standard row-store execution engine to process queries. “
* **Native Column-store.** “adopt the full column-store model, providing both a columnar storage layer and an execution engine which is tailored for operating on one column-at-a-time with late tuple reconstruction. Then, this new engine is integrated with a traditional row-oriented execution engine.”

## IBM BLU/BLINK [whycol-1]  

“A prime example of [an integrated native column-store] is IBM BLU  which originated from the IBM BLINK project. Essentially, IBM BLU sits on the side of the standard row-store DB2 engine and becomes responsible for part of the data.”

## Microsoft SQL Server Column Indexes [whycol-1] (Confirm source)  

"Server provides native support for columnar storage and column-oriented execution, adopting many of the critical design features that are common in column-stores, such as vectorized processing and heavily exploiting compression. These features have been integrated with the traditional row-store design of SQL Server, providing the flexibility of choosing the appropriate physical design depending on the workload."

## Data stores  

(TBD)  

## Data pipeline   

(TBD)  

## Summary  

(TBD)  

## [whycol] References  
(See columnar-ext-references.md)

[whycol-1] Abadi, D., Boncz, P., Harizopoulos, S., Idreos, S., & Madden, S. (2013). "The design and implementation of modern column-oriented database systems." Foundations and Trends® in Databases, 5(3), 197-280., https://stratos.seas.harvard.edu/files/stratos/files/columnstoresfntdbs.pdf  

[whycol-2] Michael Stonebraker, et al., “C-Store: A Column-oriented DBMS”, Proceedings of the 31st VLDB Conference, Trondheim, Norway, 2005, https://web.stanford.edu/class/cs345d-01/rl/cstore.pdf  

[whycol-3] Microsoft, “Columnstore indexes: Overview”, https://learn.microsoft.com/en-us/sql/relational-databases/indexes/columnstore-indexes-overview  

---  

## Project operator  

The projection operator π is one of the unary operators in relational algebra (RA) and is used to **project columns from a relation**. It can select specific columns from a given relation and hide all the other columns. This relational operator is a base for SQL (Structured Query Language) and is used to write queries. [Proj-1]  

Project operation selects (or chooses) certain attributes discarding other attributes. The **Project operation is also known as vertical partitioning** since it partitions the relation or table vertically discarding other columns or attributes. [Proj-2]  

## References

[whycol-1] Abadi, D., Boncz, P., Harizopoulos, S., Idreos, S., & Madden, S. (2013). "The design and implementation of modern column-oriented database systems." Foundations and Trends® in Databases, 5(3), 197-280., https://stratos.seas.harvard.edu/files/stratos/files/columnstoresfntdbs.pdf 

[whycol-2] Michael Stonebraker, et al., “C-Store: A Column-oriented DBMS”, Proceedings of the 31st VLDB Conference, Trondheim, Norway, 2005, https://web.stanford.edu/class/cs345d-01/rl/cstore.pdf 

[Proj-1]  “What is the projection operation in DBMS?”, https://www.educative.io/answers/what-is-the-projection-operation-in-dbms 

[Proj-2] “PROJECT Operation in Relational Algebra”, https://www.geeksforgeeks.org/project-operation-in-relational-algebra/   

---  

# Generating query plans

A given database management system may offer one or more mechanisms for returning the plan for a given query. Some packages feature tools which will generate a graphical representation of a query plan. Other tools allow a special mode to be set on the connection to cause the DBMS to **return a textual description of the query plan.** Another mechanism for retrieving the query plan involves querying a virtual database table after executing the query to be examined. In Oracle, for instance, this can be achieved using the EXPLAIN PLAN statement. (Source: [Wikipedia-Query Plan](https://en.wikipedia.org/wiki/Query_plan))

To be able to **execute queries**, the SQL Server **Database Engine** must analyze the statement to determine an efficient way to access the required data and process it. This analysis is handled by a component called the **Query Optimizer.** The input to the Query Optimizer consists of the query, the database schema (table and index definitions), and the database statistics. The Query Optimizer builds one or more query execution plans, sometimes referred to as query plans or execution plans. The Query Optimizer chooses a query plan using a set of heuristics to balance compilation time and plan optimality in order to find a good query plan. (Source: [MS Query](https://learn.microsoft.com/en-us/sql/relational-databases/performance/execution-plans?view=sql-server-ver15))  

---  


A list of leading data warehouses [7]:  

* AWS data warehouse (Amazon Redshift)  
* Azure data warehouse  
* BigQuery data warehouse (Google BigQuery)  
* Google Cloud Storage   
* Snowflake data warehouse  

CRM example:  
Customer data is critical for businesses to grow and thrive. For that reason, a customer relationship management (CRM) application is a good example of a typical business-related REST API application. In our example, we will use the HubSpot REST API to access a CRM database.  

> **Note:** The main components of the HubSpot CRM are objects, records, and properties. [10]  
> 
> Objects: represent the different types of relationships and processes your business has. All HubSpot accounts use four standard objects: contacts, companies, deals, and tickets. There are additional objects, such as conversations, products, quotes, and depending on your HubSpot subscription, calls, payments and custom objects. All objects use the same framework, which enables you to segment or report on them.  
> 
> Record: a single instance of an object, where you can store information in properties and track interactions. You can associate records between objects to understand how they are related.  
> 
> Properties:  the different fields where you can store information on a record. There are default properties included in your account for each object, but you can also create custom properties based on your business needs.  

> 
> **Note:** HubSpot has four standard objects (contacts, companies, deals, and tickets) in addition to other non-standard objects. Each object contains records which are a single instance of an object containing data within properties. **Those properties are fields stored on a record.** [8]  
> 
> Sample of contact properties. [9]  
> 
> * email  
> * phone  
> * company  
> * lastname  
> * firstname  

## Example database description 

(Derive scenario from HubSpot API article.)

* CRM customer engagement scenario 
	- Contact date 
	- Type (call, email, website)
* Product table 
	- Product ID 
	- Description 
	- Price 
* Customer table 
	- Customer ID 
	- Company
	- Contact name 
	- Contact email

## Join [3] [4]
mysql> SELECT pet.name,  
TIMESTAMPDIFF(YEAR,birth,date) AS age,  
remark  
FROM pet INNER JOIN event  
ON pet.name = event.name  
WHERE event.type = 'litter';  

```
+--------+------+-----------------------------+  
| name   | age  | remark 					|  
+--------+------+-----------------------------+  
| Fluffy |  2   | 4 kittens, 3 female, 1 male |  
| Buffy  |  4   | 5 puppies, 2 female, 3 male |  
| Buffy  |  5   | 3 puppies, 3 female			|  
+--------+------+-----------------------------+  
```

There are several things to note about this query:  

* The FROM clause joins two tables because the query needs to pull information from both of them.  

* When combining (joining) information from multiple tables, you need to specify how records in one table can be matched to records in the other. This is easy because they both have a name column. The query uses an ON clause to match up records in the two tables based on the name values.  

## Joins ([1] sec. 4.5)  

* “several alternative algorithms can be used with a late materialization strategy”  
* “The most straightforward way to implement a column-oriented join is for (only) the columns that compose the join predicate to be input to the join”  
* Algorithm improvements  
* If an early materialization strategy is used relative to a join, tuples have already been constructed before reaching the join operator, so the join functions as it would in a standard row-store system and outputs tuples (yielding the same performance profile as a row-store join). However, several alternative algorithms can be used with a late materialization strategy.  
	- input only columns that form the predicate  
	- sort or repartition both sets of input  
	- efficient main-memory joins  

## Join operator  
(Source: [whycol-9])

Join is the most complex relational operator and much research has been devoted too its most common variant: equi-join. INGRES used nested-loop algorithms for joinn that scan over the outer relation and perform index loop into the inner. System R has sort-merge as its main algorithm, in which both relations are first sorted
onn the join attribute, and subsequently merged. Later research into join algorithms showed, however, that hash-join algorithms perform at least as good, if not better than the algorithms employed by INGRES and System R. Specifically, the hybrid hash-join algorithm, proposed in 1984, is still considered the best general purpose join
method [DKO+84].  

[DKO+84]] D. DeWitt, R. Katz, F. Olken, L. Shapiro, M. Stonebraker, and D. Wood. Implementationn Techniques for Main Memory Database Systems. In Proc. of thethe ACM SIGMOD Int'l. Conf. on Management of Data, pages 1-8, Boston, MA, USA, June 1984  

## Predicate examples  

* (e.g., WHERE salary > $100 AND age > 5 AND ...)  
* WHERE salary > $100,000  

# From AI "columnar-database.docx"  

**Introduction: Understanding the Basics of Columnar Databases**  

columnar database, column-oriented database, database architecture, data storage, data retrieval  

## The Key Advantages of Using Columnar Databases for Data Storage and Analytics  

columnar database benefits, faster query performance, compression techniques, data compression, column-store indexing  

**Improved Query Performance:**  

columnar database query performance, analytical queries, query optimization  

**Efficient Data Compression:**  

columnar database compression techniques, storage efficiency, disk space savings  

**Enhanced Analytical Capabilities:**  

analytical queries in columnar databases, aggregation functions, complex joins  

## The Various Use Cases Where Columnar Databases Excel  

columnar databases use cases, big data analytics, time-series analysis, suitable workloads for column-store databases

**Big Data Analytics:** Data processing for large datasets efficiently using column-store databases. Analyzing trends and patterns in large volumes of data. Data warehousing and business intelligence applications. Data exploration and ad hoc querying. Distributed computing with column-oriented systems.  

**Time-Series Analysis:** Column-based storage optimizes time-series analysis tasks like sensor readings, ticker prices or logs from IoT devices. Faster filtering and aggregation operations over time stamps or date ranges. Efficient storage and retrieval of time-stamped data in chronological order.  

**Suitable Workloads for Column-Store Databases:** Database workloads with a high number of read operations. Data analytics scenarios that require complex queries with multiple filters and aggregations, especially on large datasets.  

## Conclusion: Leveraging the Power of Columnar Databases for Efficient Data Storage and Analysis  

columnar database conclusion, benefits of column-store databases, improved performance, optimized storage  

## The Advantages of Using a Columnar Database over a Relational Database: A Comprehensive Comparison  

**Introduction: Understanding the Difference between Columnar and Relational Databases**  

columnar database, relational database, database management system, data storage, data organization  

**Efficient Data Retrieval: Faster Query Performance with Columnar Databases**  

columnar database advantages, faster query performance, improved data retrieval, query optimization  

**Data Compression and Storage Savings: Reducing Disk Space Usage with Columnar Databases**  

columnar databases compression, storage savings, disk space optimization, data compression techniques  

**Analytical Capabilities: Enhanced Data Analysis with Columnar Databases**  

columnar databases analytics features, advanced analytical functions, real-time analytics  

**Data Scalability and Flexibility: Handling Large Volumes of Data with Ease in Columnar Databases**  

columnar databases scalability, handling big data, flexible schema design in columnar databases  

**Data Aggregation and Summarization: Simplifying Complex Queries with Columnar Databases**  

column-oriented databases aggregation capabilities, complex query simplification  

**Conclusion.** Choosing the Right Database for Your Specific Needs - Is a Columnar Database the Right Choice?  

## References  

1. Abadi, et.al, "Harvard-Columnstores..."  
2. Oracle, “Database In-Memory Guide”, https://docs.oracle.com/en/database/oracle/oracle-database/21/inmem/database-memory-guide.pdf  
3. "MySQL 8.0 Reference Manual", https://dev.mysql.com/doc/refman/8.0/en/join.html  
4. "MySQL 8.0 Reference Manual", sec. 3.3.4.9, https://dev.mysql.com/doc/refman/8.2/en/multiple-tables.html  
5. Microsoft, “Columnstore indexes: Overview”   
6. Stanford, “C-Store: A Column-oriented DBMS” (In Books)  
7. Oracle, “MySQL 8.0 Reference Manual”, 12.20.2  

(Also see ./Writing-Tech/Articles/Column-store/columnar-ext-references.md)  

### End  