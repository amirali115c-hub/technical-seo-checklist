# Technical SEO Checklist Project: Complete Topic Map

Research date: August 2, 2026
Purpose: Identify every topic needed to make the Technical SEO Checklist a 100% complete package covering every aspect of technical SEO, with no entity skipped.

---

## 1. Current Coverage (10 cluster pages)

| # | Folder | Topic Covered |
|---|--------|---------------|
| 1 | categories/ai-search-geo | AI Search and GEO (12 checks) |
| 2 | categories/audit-checklist | Technical SEO Audit Checklist (freq-based) |
| 3 | categories/core-web-vitals | Google Core Web Vitals / Performance (12 checks) |
| 4 | categories/crawlability | Crawlability and Indexing (20 checks) |
| 5 | categories/for-beginners | Technical SEO for Beginners (15 checks) |
| 6 | categories/mobile-ux | Mobile SEO and UX (12 checks) |
| 7 | categories/schema-markup | Schema Markup and Structured Data (12 types) |
| 8 | categories/security | Security (13 checks) |
| 9 | categories/site-architecture | Site Architecture (12 checks) |
| 10 | categories/tools-comparison | SEO Tools Comparison |

---

## 2. The Full Technical SEO Entity Map

Technical SEO in 2026 breaks down into **14 core entities** (big topic families). A complete package must have at least one cluster per entity. Below, each entity is marked: COVERED (C), PARTIAL (P), or MISSING (M).

| Entity | Status | Notes |
|--------|--------|-------|
| A. Crawling | C | Covered in crawlability |
| B. Indexing & Canonicalization | P | Mentioned in crawlability, deserves its own cluster |
| C. Rendering (JavaScript SEO) | M | Only touched in passing. Major gap. |
| D. Site Architecture & Internal Links | C | Covered in site-architecture |
| E. Mobile-First Indexing | C | Covered in mobile-ux |
| F. Core Web Vitals / Speed | C | Covered in core-web-vitals |
| G. Structured Data / Schema | C | Covered in schema-markup |
| H. Security & HTTPS | C | Covered in security |
| I. International SEO (hreflang) | M | Missing entirely. Major gap. |
| J. Image & Media SEO | M | Only inside CWV mentions. Missing entity. |
| K. On-Page Technical (meta tags, headings) | P | Folded into for-beginners; thin as its own entity |
| L. Content Systems / E-E-A-T | P | Partially in ai-search-geo |
| M. AI Search & GEO | C | Covered in ai-search-geo |
| N. Log Files & Crawl Budget Analysis | M | Missing entirely |

---

## 3. Missing Clusters Needed for 100% Coverage

**Tier 1 - Essential (7 clusters). These are core technical SEO entities that are currently missing. Without them the package is incomplete:**

1. **Indexing & Canonicalization** (`categories/indexing-canonicalization`)
   - noindex / nofollow / indexifembedded
   - rel=canonical best practices and mistakes
   - Duplicate content handling
   - Index coverage reports (Crawled currently not indexed, Discovered currently not indexed)
   - Coverage fix workflows

2. **JavaScript SEO & Rendering** (`categories/javascript-rendering`)
   - CSR vs SSR vs SSG vs ISR vs dynamic rendering
   - Two-wave indexing
   - Why AI crawlers mostly do not render JS (Vercel study: most AI crawlers fetch JS but only 10-25% execute it)
   - Rendering diagnostics in Search Console
   - Hydration and structured data injection issues

3. **International SEO & Hreflang** (`categories/international-seo`)
   - hreflang implementation (head, sitemap, headers)
   - URL structure: ccTLD vs subdomain vs subdirectory vs gTLD+path
   - x-default, self-referencing, return tags
   - International targeting report
   - Language and region targeting pitfalls

4. **Image & Media SEO** (`categories/image-seo`)
   - File naming, alt text, captions
   - WebP/AVIF, lazy loading, srcset
   - Image sitemaps
   - Video SEO basics (schema, transcripts, thumbnails)

5. **Crawl Budget & Log File Analysis** (`categories/crawl-budget-log-analysis`)
   - What crawl budget is and when it matters (sites under a few thousand pages usually don't need to worry)
   - Robots.txt, sitemaps, internal linking effects
   - Reading server logs (Screaming Frog Log File Analyzer, SEO Logics)
   - Dead-end crawling, thin pages, parameter crawling

6. **HTTP Status Codes & Redirects** (`categories/redirects-status-codes`)
   - 200, 301, 302, 404, 410, 500, 503
   - Redirect chains, redirect loops, 301 vs 302
   - Site migration / URL change best practices
   - Soft 404s and how to avoid them

7. **On-Page Technical Elements** (`categories/on-page-technical`)
   - Title tags, meta descriptions (length, duplicates, dynamism)
   - Heading structure (H1 uniqueness, hierarchy)
   - Meta robots directives
   - Structured content: lists, tables, answer blocks (links to GEO)

**Tier 2 - Completeness (5 clusters). These cover advanced/niche aspects that round out a "100% complete" package:**

8. **Content Delivery & Performance Infrastructure** (`categories/cdn-caching-hosting`)
   - CDN, caching layers, TTFB, hosting choice
   - Preloading, resource hints, HTTP/2 and HTTP/3
   - Static vs dynamic delivery

9. **Faceted Navigation & E-commerce Technical SEO** (`categories/ecommerce-faceted-nav`)
   - Faceted/filter URL parameters, indexing control
   - Product schema, pagination (rel next/prev vs infinite scroll)
   - Thin content traps from filters

10. **Accessibility & Core Web Vitals Intersection** (`categories/accessibility-a11y`)
    - Semantic HTML, alt text, contrast, keyboard nav
    - How a11y signals overlap with SEO and AI agent accessibility

11. **E-E-A-T & Entity Clarity** (`categories/eeat-entities`)
    - Author markup (ProfilePage), Organization, SameAs
    - Entity consistency across the web
    - Trust signals and how they feed AI citation

12. **Site Migrations & Redesigns** (`categories/site-migrations`)
    - Full migration checklist: URL mapping, redirects, sitemaps, robots
    - Domain change, platform migration, redesign preservation
    - Post-migration monitoring in Search Console

---

## 4. Totals

- Existing: **10 clusters**
- Missing Tier 1: **7 clusters** (BUILT)
- Missing Tier 2: **5 clusters** (BUILT)
- **100% complete package: 22 clusters** (10 existing + 12 new) - DONE

All 12 new clusters are built as real `categories/<slug>/index.html` pages, tag-balanced, keyword-optimized, and linked as category cards on `index.html`.

**Consistency pass (complete):**
- All 22 pages now have a standard CTA (Visit Clienvora Homepage + WhatsApp buttons) and an "All Checklists" homepage nav link.
- All 22 pages have a "Related Checklists" section, giving every page at least 2 incoming links and reciprocal interlinking between new and pre-existing clusters.
- All 22 pages have a Tools section styled as `dark-section` with free/paid badges matching the published blogs.
- The 12 new pages were refreshed with real keyword data (volume/KD) in titles, meta descriptions (138-157 chars), hero/intro copy, and FAQ JSON-LD.
- Homepage `index.html` links all 22 category cards to `/categories/<slug>/`.

Remaining suggestion: run a local Jekyll build (or the `scripts/prebuild-check.py` static check) to validate the full site before deploying.

---

## 5. Suggested Build Priority

Phase 1 (highest traffic + biggest gap):
1. javascript-rendering (massive search volume, zero coverage)
2. indexing-canonicalization (foundational, high intent)
3. international-seo (hreflang, high authority topics)
4. redirects-status-codes (site owners search this constantly)

Phase 2:
5. crawl-budget-log-analysis
6. image-seo
7. on-page-technical

Phase 3 (completeness):
8. cdn-caching-hosting
9. ecommerce-faceted-nav
10. accessibility-a11y
11. eeat-entities
12. site-migrations

---

## 6. Notes for Consistency with Existing Structure

Each new cluster should mirror the existing template:
- H1: "[Topic] and the Complete 2026 Checklist"
- H2 structure: Why it matters / The [N] Checks / Deep Dive / Common Mistakes / Tools / FAQ
- A downloadable checklist PDF in assets/pdfs/ (like technical-seo-checklist-2026.pdf)
- Interlinked from index.html and cross-linked with related clusters
