# Qlik, BI and SQL Notes

## Star Schema

A star schema is a common data-modeling pattern used in business intelligence and analytics. It contains a central fact table connected to several dimension tables.

The fact table usually stores measurable business events such as sales amount, quantity, cost, profit, or number of transactions. It often contains foreign keys that connect each row to related dimensions.

Dimension tables store descriptive information used to filter, group, and analyze the facts. Common examples include Date, Product, Customer, Store, Supplier, and Employee.

For example, a Sales fact table may contain DateID, ProductID, CustomerID, StoreID, Quantity, and SalesAmount. The Product dimension may contain ProductID, ProductName, Brand, Category, and Department.

A star schema is popular because it is relatively simple for users to understand and often performs well for analytical queries. Instead of storing all descriptive attributes in one large transactional table, the model separates business events from descriptive context.

## Fact and Dimension Tables

A fact table represents events or measurements. Each row usually corresponds to a business event at a defined level of detail, also called the grain of the table.

For example, if the grain of a sales fact table is one row per item per receipt line, then every row represents a specific item sold in a specific transaction.

A dimension table describes the entities related to those events. A Product dimension describes products, while a Store dimension describes stores.

Defining the grain correctly is important. Mixing multiple grains in one fact table can make measures difficult to interpret and can create incorrect aggregations.

## Qlik Associative Model

Qlik uses an associative data model. Tables are associated automatically when they share fields with the same name.

For example, if both Sales and Products contain a field named ProductID, Qlik can associate the two tables through that field.

This makes field naming important. Two fields with the same name will create an association even if the developer did not intend them to be related.

Developers often rename fields deliberately to control associations and avoid accidental relationships.

## Synthetic Keys in Qlik

A synthetic key can appear when two or more tables share more than one field with the same names.

For example, if Sales and Inventory both contain StoreID and ProductID, Qlik may create a synthetic key that represents the combination of those shared fields.

A synthetic key is not always an error, but it is often a sign that the data model should be reviewed.

Possible solutions include creating a single composite key, renaming fields that should not associate, or redesigning the model so that the relationship between the tables is explicit.

A common composite key might be:

StoreID & '_' & ProductID as StoreProductKey

The same key must be created consistently in every table that should be linked through it.

## Qlik Set Analysis

Set Analysis allows a Qlik measure to calculate over a specific set of data, independent of some or all current selections.

A basic example is:

Sum({<Year={2026}>} SalesAmount)

This expression sums SalesAmount only for records where Year is 2026.

Set Analysis can also ignore a selection. For example:

Sum({<Store=>} SalesAmount)

This clears the Store selection for that calculation while keeping other selections.

Another common use is comparison between current and previous periods, such as current year versus previous year.

Set Analysis is evaluated once per chart calculation and is generally not row-by-row logic.

## ApplyMap in Qlik

ApplyMap is used to look up a value from a mapping table.

A mapping table is created using the MAPPING keyword. For example:

ProductCategoryMap:
MAPPING LOAD
    ProductID,
    Category
FROM ...;

The mapping can then be applied:

ApplyMap('ProductCategoryMap', ProductID, 'Unknown') as Category

The first argument is the mapping table name, the second is the lookup value, and the third is an optional default value.

ApplyMap is often more efficient and simpler than joining a small lookup table into a large fact table when only one mapped value is needed.

## Join in Qlik

Qlik supports joins such as LEFT JOIN, INNER JOIN, RIGHT JOIN, and OUTER JOIN.

A LEFT JOIN keeps all rows from the existing table and adds matching fields from the joined table.

Joins should be used carefully in Qlik because an incorrect join can increase the number of rows and create duplicated facts.

If both tables contain multiple rows for the same join key, the result can become a many-to-many join and multiply records.

For simple one-field lookups, ApplyMap is often safer than a join.

## Incremental Load

An incremental load processes only new or changed data instead of reloading the full dataset every time.

A common design is:

1. Load existing historical data from a QVD.
2. Query the source database only for new or updated rows.
3. Combine the new data with the historical data.
4. Remove duplicates if necessary.
5. Store the updated result back into the QVD.

Incremental loading can significantly reduce reload time and source-database load.

A field such as UpdatedAt, ModifiedDate, or an increasing transaction ID is commonly used to identify new or changed records.

The logic must also handle updates to existing rows. If an existing transaction changes, the old version should normally be replaced rather than duplicated.

## QVD Files

QVD is Qlik's native data storage format.

QVD files are commonly used to separate extraction from transformation and presentation layers.

A typical architecture may have:

1. Extract layer: load data from SQL or APIs and store raw QVDs.
2. Transform layer: clean, enrich, and combine the extracted data.
3. Application layer: load prepared QVDs into the analytical application.

QVDs can improve reload performance and reduce repeated queries against source systems.

## SQL JOIN

SQL JOIN combines rows from two or more tables based on a related field.

An INNER JOIN returns only matching rows from both tables.

A LEFT JOIN returns every row from the left table and matching rows from the right table. If no match exists, the right-side fields contain NULL.

Example:

SELECT
    s.SaleID,
    s.ProductID,
    p.ProductName
FROM Sales s
LEFT JOIN Products p
    ON s.ProductID = p.ProductID;

This returns every sale even if a matching product record is missing.

## SQL ROW_NUMBER

ROW_NUMBER is a SQL window function that assigns a sequential number to rows within a defined partition and order.

Example:

SELECT
    CustomerID,
    OrderDate,
    ROW_NUMBER() OVER (
        PARTITION BY CustomerID
        ORDER BY OrderDate DESC
    ) AS RowNum
FROM Orders;

In this example, the most recent order for each customer receives RowNum = 1.

This pattern is useful for retrieving the latest record per customer, product, or other entity.

## ROW_NUMBER, RANK and DENSE_RANK

ROW_NUMBER always assigns a unique sequence number to each row.

RANK assigns the same rank to tied values and leaves gaps after ties.

DENSE_RANK also assigns the same rank to tied values but does not leave gaps.

For example, values 100, 90, 90, 80 would receive:

- ROW_NUMBER: 1, 2, 3, 4
- RANK: 1, 2, 2, 4
- DENSE_RANK: 1, 2, 2, 3

The correct function depends on whether ties should share a position and whether rank gaps are acceptable.

## Data Quality in BI

Data quality is critical in business intelligence because dashboards and KPIs are only as reliable as their underlying data.

Common data-quality problems include missing values, duplicated records, inconsistent identifiers, invalid dates, and incorrect mappings.

Validation should be performed as early as possible in the pipeline.

Useful checks include row counts, uniqueness checks, reconciliation against source totals, null-rate checks, and comparisons between expected and actual values.

A technically correct dashboard can still be misleading if the data feeding it is incomplete or inconsistent.

## Grounded Answers

A grounded answer is an answer based only on information available in the provided source material.

If a document does not contain enough information to answer a question, the model should not invent an answer using outside knowledge.

For a grounded question-answering system, it is useful to return both the answer and the exact supporting passage from the source document.

This makes the result easier to verify and helps reduce hallucination.
