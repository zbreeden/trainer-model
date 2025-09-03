- key: structured-data
  term: "Structured Data"
  definition: >
    Data with a well-defined schema (rows/columns) that fits relational tables and
    standard analytical methods.
  examples:
    - "Survey response table; GA session table"
  see_also: ["semi-structured-data", "unstructured-data", "relational-database"]
  tags: ["ibm", "data-types"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Data Types & Sources" }
  status: "draft"

- key: semi-structured-data
  term: "Semi-Structured Data"
  definition: >
    Data with organizational properties but no rigid schema; uses tags/metadata (e.g., XML/JSON)
    and is often hierarchical.
  examples:
    - "Webhook JSON payloads for events"
  see_also: ["structured-data", "unstructured-data", "json", "xml", "nosql-database"]
  tags: ["ibm", "data-types"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Data Types & Sources" }
  status: "draft"

- key: unstructured-data
  term: "Unstructured Data"
  definition: >
    Data without a predefined format (text, images, audio/video, PDFs) that does not map cleanly
    to rows/columns.
  examples:
    - "Session recordings, support emails, screenshots"
  see_also: ["semi-structured-data", "data-lake", "nosql-database"]
  tags: ["ibm", "data-types"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Data Types & Sources" }
  status: "draft"

- key: delimited-text-file
  term: "Delimited Text File (CSV/TSV)"
  definition: >
    Plain-text rows where fields are separated by a delimiter (comma, tab, etc.); widely supported,
    schema described by header row.
  examples:
    - "Exported KPI table as CSV for The Trainer"
  see_also: ["xlsx", "json", "data-warehouse"]
  tags: ["ibm", "formats"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – File Formats" }
  status: "draft"

- key: xlsx
  term: "XLSX (Excel Workbook)"
  definition: >
    Open XML spreadsheet format with multiple worksheets; tabular cells with formulas/formatting.
  examples:
    - "Manual backlog tracker with streak metrics"
  see_also: ["delimited-text-file", "data-wrangling"]
  tags: ["ibm", "formats"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – File Formats" }
  status: "draft"

- key: xml
  term: "XML"
  definition: >
    Tag-based markup for structured exchange; human/machine readable; platform/language independent.
  examples:
    - "Survey exports with hierarchical question blocks"
  see_also: ["json", "semi-structured-data"]
  tags: ["ibm", "formats"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – File Formats" }
  status: "draft"

- key: json
  term: "JSON"
  definition: >
    Lightweight text format for structured data (key/value, arrays); common for APIs/web services.
  examples:
    - "GTM → GA4 event payloads"
  see_also: ["xml", "semi-structured-data", "nosql-database"]
  tags: ["ibm", "formats"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – File Formats" }
  status: "draft"

- key: data-sources
  term: "Data Sources"
  definition: >
    Origins of data for analytics: relational/non-relational databases, flat files/spreadsheets,
    APIs/web services, web scraping, data streams, social and sensor feeds.
  examples:
    - "Twitter API for sentiment; Kafka clickstream; CRM DB extract"
  see_also: ["relational-database", "nosql-database", "data-streams", "web-scraping"]
  tags: ["ibm", "sources"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Sources" }
  status: "draft"

- key: data-streams
  term: "Data Streams"
  definition: >
    Continuous, time-stamped event feeds from devices, apps, and services used for real-time analysis.
  examples:
    - "Pageview and engagement events flowing to a stream processor"
  see_also: ["etl", "data-pipeline", "apache-spark"]
  tags: ["ibm", "sources", "streaming"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Sources" }
  status: "draft"

- key: relational-database
  term: "Relational Database (RDBMS)"
  definition: >
    Table-based store with defined schema and SQL querying; supports joins, integrity constraints,
    and ACID properties.
  examples:
    - "Dimensional model for reporting KPIs"
  see_also: ["sql", "nosql-database", "data-warehouse"]
  tags: ["ibm", "repositories"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Databases & Repositories" }
  status: "draft"

- key: nosql-database
  term: "NoSQL Database"
  definition: >
    Non-relational stores with flexible schemas; common models include key-value, document,
    column-family, and graph—optimized for scale/performance.
  examples:
    - "Document store for event payloads; key-value cache for sessions"
  see_also: ["relational-database", "data-lake"]
  tags: ["ibm", "repositories"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Databases & Repositories" }
  status: "draft"

- key: data-warehouse
  term: "Data Warehouse"
  definition: >
    Central, analysis-ready repository integrating cleansed and conformed data for BI/analytics.
  examples:
    - "Conformed sessions, events, and outcomes for portfolio-wide KPIs"
  see_also: ["data-mart", "etl", "data-pipeline"]
  tags: ["ibm", "repositories"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Repositories" }
  status: "draft"

- key: data-mart
  term: "Data Mart"
  definition: >
    Subject-area slice of a warehouse with isolated performance/security for a team or function.
  examples:
    - "Marketing mart with engagement and campaign tables"
  see_also: ["data-warehouse", "data-lake"]
  tags: ["ibm", "repositories"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Repositories" }
  status: "draft"

- key: data-lake
  term: "Data Lake"
  definition: >
    Storage for raw structured, semi-structured, and unstructured data in native formats,
    tagged for later processing.
  examples:
    - "Raw GA4 export + scraped FAQs for feature discovery"
  see_also: ["data-warehouse", "etl", "nosql-database"]
  tags: ["ibm", "repositories"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Repositories" }
  status: "draft"

- key: etl
  term: "Extract, Transform, Load (ETL)"
  definition: >
    Automated process to acquire data from sources, clean/standardize/enrich, and load into a
    target repository; supports batch and streaming variants.
  examples:
    - "Nightly CSV ingest + real-time event transforms for ‘The Trainer’"
  see_also: ["data-pipeline", "data-warehouse"]
  tags: ["ibm", "pipelines"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – ETL & Pipelines" }
  status: "draft"

- key: data-pipeline
  term: "Data Pipeline"
  definition: >
    End-to-end system that moves/processes data (batch, streaming, or hybrid) from sources to
    destinations (lakes, apps, viz), of which ETL is a subset.
  examples:
    - "Event stream → stream processor → lake → dashboard"
  see_also: ["etl", "data-lake", "apache-spark"]
  tags: ["ibm", "pipelines"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – ETL & Pipelines" }
  status: "draft"

- key: big-data-5vs
  term: "Big Data (5 Vs)"
  definition: >
    Large, fast, diverse data where value depends on managing volume, velocity, variety—and
    quality (veracity)—to produce outcomes (value).
  examples:
    - "Clickstream + IoT + social signals for portfolio insights"
  see_also: ["hadoop", "apache-spark", "data-lake"]
  tags: ["ibm", "big-data"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Big Data" }
  status: "draft"

- key: hadoop
  term: "Apache Hadoop"
  definition: >
    Open-source ecosystem for distributed storage/processing of large datasets across clusters;
    often paired with HDFS and Hive.
  examples:
    - "Archive cold data to HDFS-backed storage"
  see_also: ["hdfs", "hive", "apache-spark"]
  tags: ["ibm", "big-data"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Big Data Tools" }
  status: "draft"

- key: hdfs
  term: "Hadoop Distributed File System (HDFS)"
  definition: >
    Fault-tolerant, distributed storage that partitions/replicates files across nodes and lets
    computation run where data resides.
  examples:
    - "Store large raw parquet files with 3x replication"
  see_also: ["hadoop", "apache-spark"]
  tags: ["ibm", "big-data"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Big Data Tools" }
  status: "draft"

- key: hive
  term: "Apache Hive"
  definition: >
    SQL-on-Hadoop data warehouse layer optimized for batch/long scans; unsuitable for low-latency
    transactions.
  examples:
    - "Ad-hoc aggregates on raw clickstream in HDFS"
  see_also: ["hadoop", "apache-spark"]
  tags: ["ibm", "big-data", "sql"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Big Data Tools" }
  status: "draft"

- key: apache-spark
  term: "Apache Spark"
  definition: >
    Distributed processing engine (batch & streaming) with in-memory acceleration and APIs for
    SQL, Python, R, Java/Scala.
  examples:
    - "Process engagement stream to compute rolling WIP/throughput"
  see_also: ["hadoop", "hdfs", "data-streams"]
  tags: ["ibm", "big-data", "streaming"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Big Data Tools" }
  status: "draft"

- key: sql
  term: "SQL"
  definition: >
    Standard query language for creating and manipulating relational data (tables, views, joins,
    DML/DDL, stored procedures).
  examples:
    - "Windowed KPI rollups in a warehouse"
  see_also: ["relational-database", "hive"]
  tags: ["ibm", "languages"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Languages" }
  status: "draft"

- key: python
  term: "Python"
  definition: >
    General-purpose language with rich analytics libraries (NumPy, pandas); readable syntax and
    strong community—common for data prep, ML, and ETL.
  examples:
    - "pandas transform for GA4 event features"
  see_also: ["apache-spark", "sql", "r-language"]
  tags: ["ibm", "languages"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Languages" }
  status: "draft"

- key: r-language
  term: "R (Language)"
  definition: >
    Open-source environment for statistics, visualization, and analysis; extensible ecosystem
    (ggplot2, plotly) and report/app publishing.
  examples:
    - "Exploratory plots for streak patterns"
  see_also: ["python", "sql"]
  tags: ["ibm", "languages"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 2 – Languages" }
  status: "draft"
