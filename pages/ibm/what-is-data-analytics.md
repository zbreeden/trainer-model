- key: data-ecosystem
  term: "Data Ecosystem"
  definition: >
    Interconnected people, processes, tools, and infrastructure that acquire, store,
    process, and disseminate data from diverse sources so stakeholders can generate and act on insights.
  examples:
    - "Repo → event stream → warehouse/lake → dashboards for stakeholders"
  see_also: ["etl", "governance", "data-wrangling"]
  tags: ["ibm", "foundations"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Intro & Ecosystem" }
  status: "draft"

- key: data-engineer
  term: "Data Engineer"
  definition: >
    Builds and maintains data architectures; integrates data from disparate sources; designs
    and operates repositories to make data accessible and reliable for analytics and applications.
  examples:
    - "Pipeline to collect GA events and land them in a queryable store"
  see_also: ["etl", "data-warehouse", "data-lake"]
  tags: ["ibm", "roles"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Roles" }
  status: "draft"

- key: data-analyst
  term: "Data Analyst"
  definition: >
    Translates data into insights by acquiring, cleaning, analyzing, and visualizing data,
    then communicating findings that inform decisions.
  examples:
    - "Analyze engagement WIP/throughput; publish weekly KPI report"
  see_also: ["descriptive-analytics", "diagnostic-analytics", "data-visualization"]
  tags: ["ibm", "roles"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Roles" }
  status: "draft"

- key: data-scientist
  term: "Data Scientist"
  definition: >
    Uses statistical and machine learning techniques to build predictive or prescriptive models,
    often requiring programming and domain knowledge.
  examples:
    - "Forecast conversion rate from historical session data"
  see_also: ["predictive-analytics", "prescriptive-analytics", "feature-engineering"]
  tags: ["ibm", "roles"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Roles" }
  status: "draft"

- key: bi-analyst
  term: "Business Intelligence (BI) Analyst"
  definition: >
    Organizes and monitors business data, builds standardized reports/dashboards, and explores
    trends to support performance decisions, often with market/external focus.
  examples:
    - "Power BI sales dashboard with daily refresh and drill-downs"
  see_also: ["data-analyst", "kpi", "dashboard"]
  tags: ["ibm", "roles"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Roles" }
  status: "draft"

- key: descriptive-analytics
  term: "Descriptive Analytics"
  definition: >
    Summarizes past data to show what happened over a period; baseline for monitoring KPIs and trends.
  examples:
    - "Weekly pageviews by source in The Trainer"
  see_also: ["diagnostic-analytics", "kpi"]
  tags: ["ibm", "analytics-types"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Analysis Types" }
  status: "draft"

- key: diagnostic-analytics
  term: "Diagnostic Analytics"
  definition: >
    Investigates why an outcome occurred by drilling into segments, correlations, and drivers.
  examples:
    - "Explain a traffic spike by campaign, landing page, and device"
  see_also: ["descriptive-analytics", "root-cause"]
  tags: ["ibm", "analytics-types"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Analysis Types" }
  status: "draft"

- key: predictive-analytics
  term: "Predictive Analytics"
  definition: >
    Uses historical patterns to estimate the likelihood of future outcomes; results are probabilistic.
  examples:
    - "Forecast weekly sessions from seasonal history"
  see_also: ["time-series", "data-scientist"]
  tags: ["ibm", "analytics-types"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Analysis Types" }
  status: "draft"

- key: prescriptive-analytics
  term: "Prescriptive Analytics"
  definition: >
    Evaluates possible actions and their likely outcomes to recommend what to do next.
  examples:
    - "Choose promo variant that maximizes predicted conversions"
  see_also: ["predictive-analytics", "optimization"]
  tags: ["ibm", "analytics-types"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Analysis Types" }
  status: "draft"

- key: data-analysis-process
  term: "Data Analysis Process"
  definition: >
    Define the problem and desired outcome, set evaluation metrics, gather and clean data,
    analyze/mine and interpret, then communicate findings to drive decisions.
  examples:
    - "Overbilling case study: hypotheses → datasets → patterns → stakeholder readout"
  see_also: ["data-wrangling", "kpi", "storytelling"]
  tags: ["ibm", "process"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Process" }
  status: "draft"

- key: analyst-skills
  term: "Analyst Skills (Technical, Functional, Soft)"
  definition: >
    Blend of tool proficiency (spreadsheets, SQL, viz tools, programming), functional capabilities
    (statistics, analytical thinking, problem-solving, probing, project management), and soft skills
    (collaboration, communication, storytelling, curiosity, informed intuition).
  examples:
    - "SQL for joins; Power BI dashboards; stakeholder workshop; narrative readout"
  see_also: ["sql", "data-visualization", "statistics", "storytelling"]
  tags: ["ibm", "skills"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Skills" }
  status: "draft"

- key: generative-ai-for-analysts
  term: "Generative AI for Analysts"
  definition: >
    Models that create new content (text, images, code) and can accelerate analysis via summarization,
    data augmentation, scenario simulation, and automated drafting—used responsibly with awareness of limitations and bias.
  examples:
    - "Draft a findings summary; synthesize scenarios; generate synthetic edge cases"
  see_also: ["predictive-analytics", "ethics", "quality-assurance"]
  tags: ["ibm", "genai"]
  orbit: "Delivery & Insight"
  source: { course: "IBM Data Analytics", module: "Module 1 – Generative AI overview" }
  status: "draft"
