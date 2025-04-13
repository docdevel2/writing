# pred-logic-notes.md  

## Definitions  

* Predicate (in DBMS): represent properties or relations among objects, and is an expression that resolves to TRUE, FALSE, or NULL  
* Predicate logic: Applies propositional logic to programming and software engineering; it is the main mathematical tool in programming and software engineering; [PRED10]  
* Proposition: a statement that is either true or false [PRED10]  
* Propositional logic: a formal language for making logical
inferences [PRED10]  

## Predicate in SQL queries  

The SELECT statement is used to pull information from a table. The general form of the statement is:  
SELECT what_to_select  
FROM which_table  
WHERE conditions_to_satisfy;  

You can use a WHERE clause to combine row selection with column selection. For example, to get birth dates for dogs and cats only, use this query:  

mysql> SELECT name, species, birth FROM pet  
WHERE species = 'dog' OR species = 'cat';  

## Predicate examples  

**Example 3 [A2]**  

1.5. SOME LINGUISTIC ASPECTS  
The adoption of a relational model of data, as described above, permits the development of a universal data sub-language based on an applied predicate calculus. A first-order predicate calculus suffices if the collection of relations is in normal form.  

**Example 4 [A3]**  

Re: PointBase SQL  
(RDBMS written in the Java)  

A search condition specifies a condition of "TRUE", "FALSE", or "UNKNOWN"
about a specific row. It is comprised of predicates associated with the
logical operators: AND, OR, and NOT. The syntax for a search condition is
as follows:  

[NOT] {predicate | (search_condition)}  
[{AND | OR} [NOT] {predicate | (search_condition)}...]  

**Example 5 [A3]**  

The following are examples of using the comparison predicates. The results (TRUE, FALSE, or UNKNOWN) of the predicates are based on the values of the column.  

    emp_id = 200 ---> TRUE if emp_id is 200
    emp_manager <> `Jones' ----> TRUE if the manager is not JONES
    salary > 50000 ----> TRUE if salary is greater than $50,000 

**Example 6 [A3]**  

BETWEEN  

The BETWEEN predicate determines if a value is between a range of values. The BETWEEN predicate is a short hand notation. It is equivalent to saying the value is greater than or equal to the beginning range and less than or equal to the ending range. For example, value1 BETWEEN value2 AND value3 is equivalent to the following search_condition:  

value1 >= value2 AND value1 <= value3  

The following is the syntax for a between predicate:  

expression [NOT] BETWEEN literal AND literal  

**Example 7 [A3]**  

LIKE  

The LIKE predicate searches a string to determine if the string has a particular pattern. The pattern is a string with a combination of the following special characters: underscore character, _ and percent sign, %. If the value of any of the arguments is NULL, then the result is UNKNOWN. The following is the syntax for the LIKE predicate:  

match_expression [NOT] LIKE pattern  
match_expression  

The match_expression is a string that will be searched to determine if the pattern specified can be found.  

NOTE: The LIKE predicate is case-sensitive.  

**Example 8 [A3]**  

EXISTS | NOT EXISTS  

These quantified operators verifies the existence of rows. The boolean result of an EXISTS or NOT EXISTS predicate is determined by the number of rows returned by the subquery. For EXISTS, the boolean result is TRUE if the subquery returns at least one row and FALSE if the subquery does not return any rows. For NOT EXISTS, the boolean result is TRUE if the subquery does not return any rows and FALSE if the subquery returns at least one row.  

This example retrieves all cities, in which at least one sales representative works.  

SELECT a.city  
FROM office_tbl a  
WHERE EXISTS  
( SELECT *  
FROM sales_rep_tbl b  
WHERE a.office_num = b.office_num);  

**Example 9 [A3]**  

IN | NOT IN  

You can use these predicate keywords to return a value list or a subquery.  

Value List  

The IN predicate determines if a value is TRUE for a list of values. The following is the syntax for an IN predicate. The NOT IN predicate also follows the same format as the IN predicate.  

SELECT|UPDATE|DELETE FROM table  
WHERE expression [NOT] IN (list_of_values)  

The list_of_values can be represented only by literals with the IN predicate. The NOT IN predicate returns a TRUE value only when it does not find the list_of_values specified.  

Example  

In the following example, the IN predicate returns TRUE if the "emp_deptid" is any of the values 10, 100, or 1000.  
emp_deptid IN (10,100,1000)  


**Example 10 [A3]**  

IN | NOT IN  
(Subquery)  

IN or NOT IN can compare a single value of each row of a table to a value from potentially multiple result rows from a subquery. IN returns TRUE, if at least one of the resultant subquery row values is equal to the expression; it returns FALSE otherwise. NOT IN returns TRUE if all of the resultant subquery row values are not equal to the expression.  

Example  

This example retrieves the names of all sales reps working in the western region.  
SELECT a.first_name, a.last_name  
FROM sales_rep_tbl a  
WHERE a.office_num IN  
( SELECT b.office_num  
FROM office_tbl b  
WHERE b.region = 'Western');  

**Example 11 [A3]**  

NULL  

The NULL predicate determines if a column in a selected row contains the SQL value: NULL. If the column value is NULL, then PointBase returns TRUE. The following is the syntax for the NULL predicate:  

column_name IS [NOT] NULL

Examples  

In the first example, the NULL predicate looks for any row where the column contains a NULL value. In the second example, the NULL predicate looks for all rows that do not contain a NULL value for a column.  

        emp_dept IS NULL  
        emp_manager IS NOT NULL   

## SQUARE  

* SQUARE user does not need the mathematical sophistication of the predicate calculus to make relatively simple references to tables.  
* [In the SQUARE] syntax we have attempted to keep in mind the notions of top-down structured programming  
* The resulting [SQUARE] syntax can best be described as a block-structured English keyword syntax.  

## Predicate logic symbols

connectives: ∧,∨,¬,→
quantifiers: ∀,∃

Universal quantifier: ∀
Existential quantifier: ∃

∀: Universal quantifier [PRED8]  

* Decimal value: &#8704;  
* Named value:  &forall;

∃: Existential quantifier [PRED8]  

* Decimal value: &#8707;  
* Named value: &exist;  

∧: AND [PRED8]  

* Decimal value: &#8743;  
* Named value: &and;  

∨: OR [PRED8]  

* Decimal value: &#8744;  
* Named value: &or;  

¬: NOT [PRED8]  

* Decimal value: &#172;  
* Named value: &not;  

→: ASSIGN TO [A5]  

* Decimal value: &#8594;  
* Named value: &rarr;  



## Logic and sets  

Example 1.5.3 [PRED9] We indicate the empty set by ∅, that is, ∅={} is the set without any elements. Note well that ∅≠{∅}: the first contains nothing, the second contains a single element, namely the empty set.  

The logical operations ¬,∧,∨ translate into the theory of sets in a natural way using truth sets.  

If A is a set, define Ac={x:x∉A}, called the complement of A. If B is a second set, define  

A∩B={x:x∈A∧x∈B}, called the intersection of A and B, 

and  

A∪B={x:x∈A∨x∈B}, called the union of A and B.  

Finally, it is occasionally useful to have a notation for the difference of A and B:  

A∖B={x:x∈A∧x∉B}=A∩Bc.  

Note that this operation is not commutative: A∖B and B∖A are usually quite different. 

## Addendum  

Codd Article Notes 11/8/23  
Focus: predicate logic in RDBMS  

* Problem  
* Prior methods  
* Math background  
* Predicate logic  
* Obstacles to adoption  
* SQL result  

## New Notes 11/9/23  

* Dependence on host language [PRED1]
* CODASYL
	- Network model [PRED1]
	- Procedure-oriented language; host-dependent [PRED1]
* System R
	- IBM research project
	- RDBMS
	- Relational data model
	- ALPHA sublanguage [PRED1]
* data models: the logical views of data [PRED1]
* CODASYL: procedure-oriented [PRED1]
* Codd introduced two relational query languages, called Relational Algebra and Relational Calculus (also known as the Data Sublanguage Alpha) [PRED5]
* ALPHA sublanguage
	- Founded on relational model and on relational calculus [PRED1]
* Relational calculus proposes an applied predicate calculus with tuple variables, subscripts and the concept of range separability.
* range-separable formula of the relational calculus [PRED6]

## Data model

The principal motivations of the relational data model were (and are):  

1. data independence
2. the simplest possible structure consistent with semantic considerations
3. provision of a unifying principle which would simplify a) the
language needed for interaction and b) statement analysis needed for authorization of access and optimization of search
	- (Chamberlin extension - language encompasses both query and administrative tasks)
4. relatively easy analysis for consistency. [PRED1]

## Data independence

* Permits hardware change with no affect on query logic (i.e. physical representation may change without affecting application logic) [PRED1]
* Simplifies query (no hardware-dependencies) [PRED1]

## ALPHA characteristics

1. The full power of the relational calculus - an applied predicate calculus with tuple variables;  
2. The capability of specifying any of the operations:  
	1) fetch value or set of values  
	2) change value or set of values  
	3) insert element (i.e., tuple) or set thereof into a relation  
	4) delete element (i.e., tuple) or set thereof from a relation  
	5) declare a relation and its domains for inclusion in the established set of data base relations  
	6) drop a relation from the data base.  
3. The capability (through the RANGE statements) of interaction between a user or his program on the one hand and the data base on the other  
4. A variable binding capability to permit use in either an interactive or batch environment.  

[PRED1]
The language is accordingly more than a query or search language. In this author's opinion the frequent separation of query languages from other aspects of retrieval is usually artificial. The proposed language is intended to be a sublanguage (in a semantic rather than syntactic sense) of the languages used by all terminal users of a shared, formatted data base, except those users who have such narrow needs that their re- quirements can be more efficiently satisfied by a set of pre-structured (or canned) queries and/or updates.

## Chamberlin  

Codd’s Relational Calculus was based on a notation used in formal logic, using an existential quantifier 9 (meaning "for each") and a universal quantifier 8 (meaning "for all"). Similar to Relational Algebra, Relational Calculus could represent the well-paid employee query compactly. [PRED5]  

* In his research papers, Codd introduced two relational query languages, called Relational Algebra and Relational Calculus (also known as the Data Sublanguage Alpha). Relational Algebra consists of several operators, usually represented by symbols such as those in Figure 1. Using these operators, the query about well-paid employees could be represented as in Figure 2a.  
* The basic concepts of Codd’s languages were adapted from set theory and symbolic logic.  

## IDS  

Integrated Data Store (IDS) was an early network database management system largely used by industry, known for its high performance. IDS became the basis for the CODASYL Data Base Task Group standards. IDS was designed in the 1960s at the computer division of General Electric (which later became Honeywell Information Systems) by Charles Bachman ... [PRED2]    

## Network model  

The network model is a database model conceived as a flexible way of representing objects and their relationships. Its distinguishing feature is that the schema, viewed as a graph in which object types are nodes and relationship types are arcs, is not restricted to being a hierarchy or lattice. [PRED3]  

The Network model: is a formal model for representing attribute relationships of an entity set and the associations between the entity sets. The data model consists of record types and connections amongthem which are represented as links. 'Record types' are used to represent the relationships among the attributes of an entity set and 'links' to specify the associations between entity sets. [PRED4]  

The Relational Model: is a formal model for representing relationships among attributes of an entity set and the associations between entity sets. [PRED4]  

A relation represents an entity set both in terms of its intentions, that is, the entity set name, its attributes and their properties, and in its valid extension, that is, the possible values the attributes may have. [PRED4]  


## Spont Notes 10/22/23  

* Early systems, managing persistent data  
* Problem: Knowledge of implementation required to query database  
* Codd’s model separated data from implementation (This is the key!) [B1]  
* represent a database query in the form of a program that navigated through a network of pointers [B1]  
* CODASYL, the Conference/Committee on Data Systems Languages, was a consortium formed in 1959 to guide the development of a standard programming language [2, 4]  
* In 1965 CODASYL formed a List Processing Task Force [B2, B4]  
* [The CODASYL] name arose because Charles Bachman's IDS system (which was the main technical input to the project) managed relationships between records using chains of pointers [B2, B4]  
* In 1967 the group renamed itself the Data Base Task Group (DBTG) [B2, B4]
* In October 1969 the DBTG published its first language specifications for the network database model which became generally known as the CODASYL Data Model. [B2, B4]  
* In computing, the network model is a database model conceived as a flexible way of representing objects and their relationships [B3]  
* The network model was adopted by the CODASYL Data Base Task Group in 1969 and underwent a major update in 1971. It is sometimes known as the CODASYL model for this reason. A number of network database systems became popular on mainframe and minicomputers through the 1970s before being widely replaced by relational databases in the 1980s. [B3]  

## Market share  

The nonrelational DBMS segment grew by 26.8% to take 21% share of the DBMS market, while the relational DBMS (RDBMS) segment grew by 12.2% for a segment share of 78%. [PRED11]  

## Join  

INNER JOIN and , (comma) are semantically equivalent in the absence of a join condition: both produce a Cartesian product between the specified tables (that is, each and every row in the first table is joined to each and every row in the second table).  

## SQL Range predicate—Harvard summary 

The RANGE function returns the range of values for a numeric column expression argument. It calculates the difference between the maximum and the minimum values, as follows: range(expr) = max(expr) - min(expr); You can apply the RANGE function only to numeric columns.  


## References  

[A1][DR1] E.F. Codd, "A Data Base Sublanguage Founded on the Relational Calculus", Proc. ACM SIGFIDET Workshop on Data Description, Access, and Control, ACM Press, 1971, https://dl.acm.org/doi/10.1145/1734714.1734718  

[A2][DR3] CODD, E.F. "A relational model of data for large shared data banks". Comm. ACM 13, 6 (June 1970), https://dl.acm.org/doi/pdf/10.1145/362384.362685  

[A3] Point Base, "Search Conditions and Predicates", http://www.cs.toronto.edu/~nn/csc309/guide/pointbase/docs/html/htmlfiles/dev_searchcondandpredicates.html  

[A4] Oracle, _MySQL 8.0 Reference Manual_, https://dev.mysql.com/doc/refman/8.0/en/join.html  

[A5] Erik R. Tou (University of Washington Tacoma), "Math Origins: The Logical Symbols", https://maa.org/press/periodicals/convergence/math-origins-the-logical-symbols  

[B1] Chamberlin, Donald D., "Early History of SQL", https://ieeexplore.ieee.org/document/6359709  

[B2] Wiki, CODASYL, https://en.m.wikipedia.org/wiki/CODASYL  

[B3] Wiki, Network Database Model, https://en.m.wikipedia.org/wiki/Network_model  

[B4] Charles Babbage Institute, “Conference on Data Systems Languages records”, https://archives.lib.umn.edu/repositories/3/resources/35  

[PRED1] E.F. Codd, "A Data Base Sublanguage Founded on the Relational Calculus", Proc. ACM SIGFIDET Workshop on Data Description, Access, and Control, ACM Press, 1971, https://dl.acm.org/doi/10.1145/1734714.1734718  

[PRED2] Wikipedia, “IDS”, https://en.m.wikipedia.org/wiki/Integrated_Data_Store  

[PRED3] Wikipedia, “Network Model”, https://en.m.wikipedia.org/wiki/Network_model  

[PRED4] Mirza, Oregon State University, "CODASYL DBTG and System R Approache", 1979  

[PRED5] Chamberlin, Donald D., "Early History of SQL", https://ieeexplore.ieee.org/document/6359709  

[PRED6] CODD, E.F., "A relational model of data for large shared data banks", Comm. ACM 13, 6 (June 1970), https://dl.acm.org/doi/pdf/10.1145/362384.362685  

[PRED7] Chamberlin, Donald D., "System R: Relational Approach to Database Management", https://dl.acm.org/doi/pdf/10.1145/320455.320457  

[PRED8] CODD, E.F., "RELATIONAL COMPLETENESS OF DATA BASE SUBLANGUAGES", 1976, https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6a048dc38250ffce49c5e6a5040b4c91ca05e83d  

[PRED9]  Whitman College, "Logic and Sets", https://www.whitman.edu/mathematics/higher_math_online/section01.05.html  

[PRED10] Milos Hauskrecht, University of Pittsburgh, Department of Computer Science, "Predicate Logic", https://people.cs.pitt.edu/~milos/courses/cs441/lectures/Class3.pdf  

[PRED11] Gartner, "Market Share Analysis: Database Management Systems, Worldwide, 2022", June 2023, https://www.gartner.com/en/documents/4432699  

<style>  
body{  
background-color: lavender;  
}  
</style>  

### End  
