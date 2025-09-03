- key: baccm
  term: "Business Analysis Core Concept Model (BACCM)"
  definition: >
    A shared mental framework for business analysis built on six equal concepts—
    Change, Need, Solution, Stakeholder, Value, and Context—used to frame any BA task
    regardless of domain or methodology.
  examples:
    - "Framing The Trainer: identify the Need, define the Change and Solution, map Stakeholders, value, and Context"
  see_also: ["change", "need", "solution", "stakeholder", "value", "context", "babok-guide"]
  tags: ["cbap", "framework"]
  orbit: "Delivery & Insight"
  source: { course: "CBAP", module: "Module 2 – BACCM & Techniques" }
  status: "draft"

- key: change
  term: "Change"
  definition: >
    The act of transformation in response to a Need; deliberate and controlled
    through BA activities to improve organizational performance.
  examples:
    - "Introduce GA4 custom events to improve engagement measurement"
  see_also: ["need", "solution", "context", "baccm"]
  tags: ["cbap", "baccm"]
  orbit: "Delivery & Insight"
  source: { course: "CBAP", module: "Module 2" }
  status: "draft"

- key: need
  term: "Need"
  definition: >
    A problem or opportunity that motivates Change; needs can trigger changes and
    new changes can introduce further needs (iterative cycle).
  examples:
    - "Low funnel visibility → add checkout events; later, need for attribution refinement"
  see_also: ["change", "solution", "value", "baccm"]
  tags: ["cbap", "baccm"]
  orbit: "Delivery & Insight"
  source: { course: "CBAP", module: "Module 2" }
  status: "draft"

- key: solution
  term: "Solution"
  definition: >
    A specific way to satisfy one or more Needs by resolving a problem or enabling
    an opportunity.
  examples:
    - "Deploy GTM container with standardized event schema"
  see_also: ["need", "value", "stakeholder", "baccm"]
  tags: ["cbap", "baccm"]
  orbit: "Delivery & Insight"
  source: { course: "CBAP", module: "Module 2" }
  status: "draft"

- key: value
  term: "Value"
  definition: >
    The importance or usefulness of something to a Stakeholder; can be delivered by
    different Solutions and may be tangible (e.g., revenue, cost) or intangible
    (e.g., ease of use, brand loyalty).
  examples:
    - "Faster dashboard load → higher satisfaction (intangible); reduced churn (tangible)"
  see_also: ["stakeholder", "solution", "need", "baccm"]
  tags: ["cbap", "baccm"]
  orbit: "Delivery & Insight"
  source: { course: "CBAP", module: "Module 2" }
  status: "draft"

- key: context
  term: "Context"
  definition: >
    The internal and external circumstances that influence or are influenced by the
    Change; aligns with ISO 9000’s notion of issues affecting how an organization
    pursues its objectives.
  examples:
    - "Regulatory constraints on PII shape event design"
  see_also: ["change", "need", "solution", "baccm"]
  tags: ["cbap", "baccm"]
  orbit: "Delivery & Insight"
  source: { course: "CBAP", module: "Module 2" }
  status: "draft"

- key: concept-modeling
  term: "Concept Modeling"
  definition: >
    A technique to organize a domain’s vocabulary and relationships: start a noun-based
    glossary, add verb relationships, classify/specialize, and visualize for stakeholder
    alignment. Business-friendly, but not a data model and may set unrealistic build
    expectations; benefits from collaborative tools.
  examples:
    - "Map FourTwenty terms: Event → is triggered by → Interaction; Event → belongs to → Module"
  see_also: ["business-glossary", "data-modeling", "requirements-levels", "baccm"]
  tags: ["cbap", "technique"]
  orbit: "Delivery & Insight"
  source: { course: "CBAP", module: "Module 2 – Technique: Concept Modeling" }
  status: "draft"

- key: business-glossary
  term: "Business Glossary"
  definition: >
    A curated list of noun terms and clear definitions for a domain; the first step
    in building a Concept Model and reducing ambiguity.
  examples:
    - "glossary.yml terms for GA4 events, modules, and roles"
  see_also: ["concept-modeling", "data-dictionary"]
  tags: ["cbap", "knowledge"]
  orbit: "Delivery & Insight"
  source: { course: "CBAP", module: "Module 2" }
  status: "draft"

- key: given-when-then
  term: "Given–When–Then (GWT)"
  definition: >
    A behavior-driven format for functional acceptance criteria capturing preconditions,
    action, and expected outcome (e.g., ‘Given on checkout, When user selects BNPL,
    Then open third-party interface’).
  examples:
    - "Define acceptance tests for custom event capture"
  see_also: ["functional-requirements", "solution-requirements"]
  tags: ["cbap", "requirements", "bdd"]
  orbit: "Delivery & Insight"
  source: { course: "CBAP", module: "Module 2 – Requirements Details" }
  status: "draft"
