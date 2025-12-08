---

marp: true
title: "Product Documentation — Marp Slides"
author: "Technical Writing Team"
theme: default
paginate: true
class: lead
-----------

<!-- Email: 23f3003674@ds.study.iitm.ac.in -->

<style>
/* Custom theme overrides for Marp (embedded) */
section {
  background: linear-gradient(180deg, #0f172a 0%, #071024 100%);
  color: #e6eef8;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial;
}
h1, h2, h3 { color: #7dd3fc; }
footer { color: #9fb3cf; font-size: 0.8rem }
code { background: rgba(255,255,255,0.04); padding: 0.2rem 0.4rem; border-radius: 4px }
/* Larger preformatted blocks */
pre { font-size: 0.85rem }
</style>

<!-- _footer: 23f3003674@ds.study.iitm.ac.in -->

<!-- _header: **Product Documentation — Marp** -->

<!-- _class: lead -->

# Product Documentation — Overview

Contact: [23f3003674@ds.study.iitm.ac.in](mailto:23f3003674@ds.study.iitm.ac.in)

---

## Table of Contents

1. Introduction
2. Architecture
3. Usage
4. API
5. Algorithms & Complexity

---

<!-- _backgroundImage: url('images/architecture-bg.jpg') -->

## System Architecture

![bg cover](images/architecture-bg.jpg)

> Diagram: High-level system architecture and data flows.

---

## Code Example (Usage)

```javascript
// Initialize client
import { Client } from '@acme/sdk'

const client = new Client({ apiKey: process.env.API_KEY })
const res = await client.get('/v1/health')
console.log(res.status)
```

---

## Algorithm Complexity (Math)

We analyze the ranking algorithm. Let $n$ be the number of items and $k$ the number of top results.

Block complexity:

$$
T(n) = O(n \log n) \quad\text{(full sort)}
$$

If using a selection algorithm for top-$k$:

$$
T(n) = O(n + k\log k)
$$

---

<!-- _class: center, middle -->

## Key Configuration (Directives)

* Use environment variables for secrets
* Enable `--allow-local-files` when exporting locally with Marp CLI to include images

<!-- _footer: *Page footer — product docs* -->

---

## Slide with custom directive and fragments

* Feature A: Fast onboarding <!-- _color: #9ae6b4 -->
* Feature B: Scalable storage <!-- _color: #fbd38d -->
* Feature C: Secure by design <!-- _color: #fccb6e -->

---

## Speaker Notes Example

Notes:

* Start with the product mission and highlight adoption metrics.
* For the architecture slide, point out the async queue and caching layer.

---

## Background Image Slide

![bg fit](images/feature-bg.jpg)

This slide demonstrates a full-slide background image using `![bg fit](path)`.

---

## Closing & Contact

Questions? Reach out:

* Email: <a href="mailto:23f3003674@ds.study.iitm.ac.in">[23f3003674@ds.study.iitm.ac.in](mailto:23f3003674@ds.study.iitm.ac.in)</a>

<!-- Notes: End of presentation -->
