# col-tech-drft0.md  

## Column-store techniques article for Medium  

* 	List and expand upon column-store techniques  
	- Describe each architectural technique in 5-10 sentences  
* 	Techniques  
	- 	Late materialization  
	- 	Column-at-a-time query processing  
	- 	Vectorization  
	- 	Column-specific compression  
	- 	Hybrid row/column implementation  
	- 	Database cracking and adaptive indexing  
	- 	Efficient loading  
*	Conclussion  

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

## Hybrid row/column implementation (C-store)  

* A hybrid architecture with a WS component optimized for frequent insert and update and an RS component optimized for query performance  


## Database cracking and adaptive indexing  

A column store with its reduced storage complexity, makes it easier for the system designer to strike a balance between software complexity, maintainability, and performance. In this context two directions within the MonetDB project are being explored: database cracking and recycling.  

Since [coltech-1].[22], the predominant approach in database systems to pay the price for index maintenance during updates is challenged by a simple scheme, called database cracking. The intuition is to focus on a non-ordered table organization, extending a partial index with each query, i.e., the physical data layout is reorganized within the critical path of query processing. We have shown that this approach is competitive over upfront complete table sorting and that its benefits can be maintained under high update load. The approach does not require knobs [coltech-1].[18].  

* “Indexing, which is not a DBA task but happens as a by-product of query execution, i.e., database cracking”  


## Cracking:  
[coltech-1].[22]  

In this paper we explore a different route based on the hypothesis that **access maintenance should be a byproduct of query processing, not of updates**. A query is interpreted as both a request for a particular database subset and as an advice to crack the database store into smaller pieces augmented with an index to access them. [coltech-1].[22]  

... simple query select * from R where R.a <10 and a storage scheme that requires a full table scan, ... an also be **interpreted as a task to fragment the table into two pieces**, i.e. apply horizontal fragmentation.  

This paper’s contributions are threefold: (i) it introduces a database organization scheme based on cracking, (ii) it introduces a multi-query benchmark to analyze the cracking scheme, and (iii) evaluates a prototype implementation of the key algorithms.  

## Table scans  
[coltech-1].[22]  

... lowest denominator of database access, i.e. table scans.  

Table scans form the lowest access level of most database kernels. They involve a sequential read of all tuples followed by predicate evaluation. The qualified tuples are moved to a result table, passed onward to the next operator in a query evaluation pipeline, or sent to a GUI. The expected gross performance is easy to predict. The source operand has to be read once, and the fragment of interest has to be written back to persistent store (or shipped to the application front-end).  

* Aside from very small tables, the performance of materialization is linear in the size of the fragment selected; a key observation used in most cost-models for query optimization.  
* For large tables it [performance] becomes linear in the number of disk IOs.  
* The performance figures also highlight the relative cost of the basic operations.  
* Storing the result of a query in a new system table (a) is expensive, as the DBMS has to ensure transaction behavior.  
* Sending it to the front-end (b) is already faster, although the systems behave quite differently on this aspect.  
* Finally, the cost of finding qualifying tuples itself (c) is cheap in some systems.  

## DB Cracking Architecture  
[coltech-1].[22]  

In this section, we introduce the architecture of a database cracker component. It is positioned between the semantic analyzer and the query optimizer of a modern DBMS infrastructure. As such, it could be integrated easily into existing systems, or used as a pre-processing stage before query processing.  

Informally, database crackers are queries that break a relational table into multiple, disjoint pieces. They are derived during the first step of query optimization, i.e. the translation of an SQL statement into a relational algebra expression.  

The selection predicates and projection list form the first handle for cracking the database. It has been known for a long time, that they can be used to construct a horizontally/vertical fragmented table for distributed processing [coltech-1].[22].[OV91].  

Relational algebra operations, like πattr(R), σpred(R), or R &bowtie; S, suggest natural and intuitive ways to split their input table(s) into two fragments each, on containing the ”interesting” tuples and the other one the ”non-interesting” tuples.  

## 3.4.1 Crackers in a Query Processor  
[coltech-1].[22]  

Cracking can be used in a conventional DBMS where it takes the form of continual data reorganization, e.g. partitioning decisions at each query step.  

Most systems use a Volcano-like query evaluation scheme [coltech-1].[22].[Gra93]. Tuples are read from source relations and passed up the tree through filter-, join-, and projection-nodes. The cracker approach can be readily included in this infrastructure.  

## Application areas  
[coltech-1].[22]  

The application areas foreseen for database cracking are data warehouses and scientific databases. Datawarehouses provide the basis for data mining, which is characterized by lengthly query sequences zooming into a portion of statistical interest [coltech-1].[22].[BRK98].  

In the scientific domain, the databases may be composed of a limited number of tables with hundreds of columns and multi-million rows of floating point numbers. For example, the tables keep track of timed physical events detected by many sensors in the field [coltech-1].[22].[SBN+99]. In addition, the database contains many derived tables, e.g. to represent model fitting experiments. It is topped with a version scheme to keep track of the lineage of the tables being managed. In practice, a coarse-grain fragmentation strategy is used to break up a terabyte database into pieces of a few tens of gigabytes each.  

## 5.2 Crackers in MonetDB  
[coltech-1].[22]  

A cracker module has been implemented to assess whether the cost structure encountered at the SQL level can be countered. The module implements the Ξ and &diamond; crackers and relies on the systems efficient memory management scheme to guarantee transaction safety during cracking. The cracker index is organized as a decorated interval tree. Each table comes with its own cracker index and they are not saved between sessions. They are pure auxiliary datastructures to speedup processing of queries over selected binary tables.  

... partitioning large tables has become an important technique to reduce index maintenance and to improved query responsiveness. For example, MySQL, DB2 and Oracle advice the DBA to specify range-partitioned tables for large datawarehouses. The cracker scheme extends this practice using a cracker index defined implicitly by query use, rather then by intervention of a DBA.  

## Cracking summary  
[coltech-1].[22]  

The challenge put on the table here is: Let the query users pay for maintaining the access structures. Its realization is the notion of database cracking, where a query is first interpreted as a request to break the database into pieces organized by a cracker index. After cracking the database the query is evaluated using ordinary (distributed) query optimization techniques.  

As the database becomes cracked into many pieces, the query optimizer is in a better position to discard portions of no interest for evaluation.  


## Efficient loading  
(Efficient loading architectures [whycol-1].[41, 88])  

* Efficient loading architectures [41, 88]. Finally, **one concern with column-stores is that they may be slower to load and update than row-stores, because each column must be written separately, and because data is kept compressed.** Since load performance can be a significant concern in data warehouse systems, optimized loaders are important. For example, **in the C-Store system, data is first written into an uncompressed, write-optimized buffer (the “WOS”), and then flushed periodically in large, compressed batches. This avoids doing one disk seek per-attribute, per-row and having to insert new data into a compressed column; instead writing and compressing many records at a time.**  
* Query execution accesses data from ROS and WOS and joining the results [whycol-1]  
* WOS: newly loaded data is stored in a **write-optimized store (“WOS”), where data is uncompressed and not vertically partitioned**. The WOS enables efficient loading of data, and amortizes the cost of compression and seeking. Periodically, data is moved from the WOS into the ROS via a background **“tuple mover” process, which sorts, compresses, and writes re-organized data to disk in a columnar form**.  
* ... every query may access only the columns referenced, thus seeing some savings in terms of I/O but **once all relevant data arrives in memory, it is immediately stitched into a tuple N-ary format and is fed to a classic row-store engine**. In this way, such a design is relatively easy to adopt as it **only requires a mapping of columns to tuples when loading from disk**, but it also means that such designs cannot exploit the run-time benefits of operating on one column-at-a-time which allows for better exploitation of the whole memory hierarchy.  
* In contrast, **systems oriented toward ad-hoc querying of large amounts of data should be read-optimized. Data warehouses represent one class of read-optimized system** in which **periodically a bulk load of new data is performed**, followed by a relatively long period of ad-hoc queries. Other read-mostly applications include customer relationship management (CRM) systems, electronic library card catalogs, and other ad-hoc inquiry systems. In such environments, a **column store architecture, in which the values for each single column (or attribute) are stored contiguously**, should be more efficient.  
* With a column store architecture, a DBMS need only read the values of columns required for processing a given query, and can **avoid bringing into memory irrelevant attributes**. In warehouse environments where typical queries involve aggregates performed over large numbers of data items, a column store has a sizeable performance advantage. However, there are several other major distinctions that can be drawn between an architecture that is read-optimized and one that is write-optimized.  
* RS, as the name implies, is optimized for read and supports only a very restricted form of insert, namely the batch movement of records from WS to RS, a task that is performed by the tuple mover  
* ... **most commercial optimizers and executors are row-oriented**, obviously built for the prevalent row stores in the marketplace. Since **both RS and WS are column-oriented**, it makes sense to build a **column-oriented optimizer and executor**.  
* C-Store is a column-oriented DBMS that is architected to **reduce the number of disk accesses per query**.  

## Adaptive indexing  

(Draft)  

Indexing is critical to database search and sort performance during query execution. Using the right data structure can speed up scans by eliminating data that is irrelevant to a query.  

B-tree indexing is a data structure commonly used for searching and sorting databases. It is appealing because of its combination of speed and simplicity. Column are represented as a collection of (v, sk)  pairs in which the data value is v and the storage location key is sk.  

Indexes are traditionally determined prior to query execution, prohibiting on-the-fly tuning. Adaptive indexing allows the query engine to learn from from previous queries and "autonomously create only the indexes it needs" [whycol-1], minimizing the CPU cycles spent on irrelevant data.  

(Draft highlights)  

* Queries can also be used to dynamically create indexes (adaptive indexing, see below)  
* Each projection is represented as a collection of pairs, (v, sk) where v is the data value in the column and sk is the storage location key  
* B-tree indexing to maintain a logical sort-key order; commonly used to search large blocks of data; known for speed and simplicity 
* Indexing strategy: Speed up scans by eliminating non-qualifying tuples  
* Add section from Actian website  
* Add discussion of different indexing approaches by C-Store & MonetDB  
* Add discussion of projections  

**Indexing** 

* Insert into adaptive section, a statement on scan speed gains from selective predicate & reducing tuple reconstruction (See C-Store indexing below.) 
* minimizing the effort needed to search as well as minimizing the effort needed for tuple reconstruction


> **(adaptive indexing)**   
> Such dynamic and online scenarios are the main motivation for adaptive indexing. The main idea is that **the system autonomously creates only the indexes it needs**. Indexes are created (a) adaptively, i.e.,**only when needed**, (b) partially, i.e., **only the pieces of an index needed** are created and (c) **continuously**, i.e., the system continuously adapts.  
> With database cracking, a database system can be used immediately when the data is available; the more the system is used, the more the performance approaches the optimal performance that would be achieved if there was enough idle time and workload knowledge to fully prepare all indexes needed for the current workload.  
> 
> The **main innovation** is that the physical data store is **continuously changing with each incoming query q**, using q as a hint on how data should be stored. [whycol-1]   
> 
> **The Velocity of Data Accrual** – Because data arrives from a variety of sources, it tends to arrive quickly as well. The **consolidation of disparate data sources** is another key to the modern data platform. It is difficult at best to **bring together all of the data into a single repository or format**, so virtual unity through data management and operations is necessary. **One way to accomplish the virtual consolidation is through adaptive indexing** and metadata use. **Replacing or augmenting traditional taxonomies with faceting classifications enables the data to be searched and organized in multiple ways.** This provides the use of different analytics and allows organizations to understand the data. [coltech-4]  
>   
> **B-tree indexing**   
>   
> Since we assume that WS is trivial in size relative to RS, we make no effort to compress data values; instead we represent all data directly. Therefore, **each projection uses B-tree indexing to maintain a logical sort-key order**. [whycol-2]  
>   
> Every column in a WS **projection is represented as a collection of pairs, (v, sk)**, such that v is a value in the column and sk is its corresponding storage key. **Each pair is represented in a conventional B-tree on the second field**. The sort key(s) of each projection is additionally represented by pairs (s, sk) such that s is a sort key value and sk is the storage key describing where s first appears. Again, this structure is represented as a conventional B-tree on the sort key field(s). To perform searches using the sort key, one uses the latter B-tree to find the storage keys of interest, and then uses the former collection of B-trees to find the other fields in the record.  
> [whycol-2]   
>   
> The natural “value-based” way to implement the write-store is to keep track of which tuples were deleted, inserted or modified in a RAM-resident data structure that organizes these items in the sort key (SK) order of the underlying read-store table and contains these keys; for example in a RAM friendly B-tree. [coltech-2]  
> 
> PDT. In this paper, we propose a new data structure called the Positional Delta Tree (PDT). PDTs are similar to counted B-trees [23] but contain differential updates. They are designed to make merging in of these updates fast by providing the tuple positions where differences have to be applied at update time. [coltech-2]  
> 
> The key advantages of the PDT over value-based merging are (i) positional merging needs less I/O than value-based merging, because the sort keys do not need to be read, and (ii) positional merging is less CPU intensive than
value-based merging, especially when the sort-key is a compound key (common in clustering approaches) and/or non-numerical attributes are part of the sort-key. [coltech-2]  
>
> The B-Tree index is a very commonly used database index structure that allows for high-speed searching and sorting of data with minimal storage overhead for the index. [coltech-3]  
> 

## C-store indexing  

> A query may use a single covering projection which is ordered (ideally) by the attribute which participates in the query’s most selective predicate, thus minimizing the effort needed to search as well as minimizing the effort needed for tuple reconstruction. Given that columns compress very well, materializing these extra projections does not bring a significant storage overhead when compared to a traditional row-store system.  

## Hybrid section 

* Add paragraph on C-store, MonetDB, & VectorWise update approach; don’t identify company names 
* MonetDB uses delete/insert to update 
* C-Store uses row format 
* VectorWise uses Positional Delta Tree (PDT) 

> A natural approach to implement the write-store is to store differences (inserts, deletes, and updates) in an in-memory structure. MonetDB uses plain columns, i.e., for every base column in the schema there are two auxiliary columns to store pending inserts and pending deletes; an update is a delete followed by an insert. C-Store proposed that the write optimized store could also use a row-format which speeds up updates even more as only one I/O is needed to write a single new row (but merging of updates in the column format becomes potentially more expensive). [whycol-1]   


## Glossary  

* B-tree: A B-tree is a  [data structure](https://builtin.com/data-science/data-structures)  that provides sorted data and allows searches, sequential access, attachments and removals in sorted order. The B-tree (the B stands for Balanced) is highly capable of storing systems that write large blocks of data. The B-tree simplifies the binary search tree by allowing nodes with more than two children.
* PDT: Positional Delta Tree (PDT), [whycol-1].[41]  
* VDT: Value-based Delta Tree, [whycol-1].[41]  
* tuple N-ary format: A tuple with n fields is called an n-ary tuple., [whycol-1, p.31]



## References  
(See col-tech-references.md for all coltech references.)  


[coltech-1] Stefan Manegold, Martin L. Kersten, Peter Boncz, "Database Architecture Evolution: Mammals Flourished long before Dinosaurs became Extinct"  

[coltech-1].[18] Idreos, Stratos, Martin L. Kersten, and Stefan Manegold. "Self-organizing tuple reconstruction in column-stores." In Proceedings of the 2009 ACM SIGMOD International Conference on Management of data, pp. 297-308. 2009. https://dl.acm.org/doi/abs/10.1145/1559845.1559878  

[coltech-1].[22] Kersten, Martin L., and Stefan Manegold. "Cracking the database store." In CIDR, vol. 5, pp. 4-7. 2005. https://www.cidrdb.org/cidr2005/papers/P18.pdf  

[coltech-2] Héman, Sándor, Marcin Zukowski, Niels J. Nes, Lefteris Sidirourgos, and Peter Boncz. "Positional update handling in column stores." In Proceedings of the 2010 ACM SIGMOD International Conference on Management of data, pp. 543-554. 2010.,https://dl.acm.org/doi/abs/10.1145/1807167.1807227  

[coltech-3] paul.randal, "An Introduction to B-Tree and Hash Indexes in PostgreSQL", Thwack Community, https://thwack.solarwinds.com/groups/data-driven/b/blog/posts/an-introduction-to-b-tree-and-hash-indexes-in-postgresql  

[coltech-4] Acitan Corporation, "What is a Modern Data Platform?", October 9, 2020, https://www.actian.com/blog/uncategorized/what-is-a-modern-data-platform/  

[whycol-1] Abadi, D., Boncz, P., Harizopoulos, S., Idreos, S., & Madden, S. (2013). "The design and implementation of modern column-oriented database systems." Foundations and Trends® in Databases, 5(3), 197-280., https://stratos.seas.harvard.edu/files/stratos/files/columnstoresfntdbs.pdf  

[whycol-1].[41]=[coltech-2]  

[whycol-2] Michael Stonebraker, Daniel J. Abadi, Adam Batkin, Xuedong Chen, Mitch Cherniack, Miguel Ferreira, Edmond Lau, Amerson Lin, Samuel R. Madden, Elizabeth J. O’Neil, Patrick E. O’Neil, Alexander Rasin, Nga Tran, and Stan B. Zdonik. C-Store: A Column-Oriented DBMS. In Proceedings of the International Conference on Very Large Data Bases (VLDB), pages 553–564, 2005.  



### End  