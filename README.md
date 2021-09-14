## SQLite3 vs Pandas Query Performance Tests

Simple performance tests that compare the query runtimes of SQLite3 and Pandas. 
These tests were used in my Work Term Report (WKRPT 200) at the University of Waterloo

Tests were performed by creating a test dataset with 3 columns (first name, last name, ID). The dataset is queried 
for a specific ID value (in this case ID = 12) and the query runtime is measured. 

## Results 
Although Pandas performed better with smaller datasets, SQLite3 
performed better with datasets with over ~30,000,000 - 40,000,000 records. When testing 80,000,000 records
SQLite found the records over 2x faster.

See the table below for results. 

| Number of Records       | Pandas Query Runtime (s)          | SQlite3 Query Runtime (s) |
| ------------- |:-------------:| -----:|
| 10,000,000    | 0.8415 | 2.8348 |
| 40,000,000     | 8.5419      |   18.2742 |
| 80,000,000 | 90.7456      |    35.9351 |


## Acknowledgment
[1] [Quick Guide to generating fake data with Pandas](https://www.caktusgroup.com/blog/2020/04/15/quick-guide-generating-fake-data-with-pandas/) <br>

