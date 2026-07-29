---
layout: default
title: AI Search and GEO Checklist for Technical SEO
description: Optimize your site for AI search visibility. AI crawler access, semantic HTML, entity optimization, llms.txt, and agentic commerce readiness with code examples.
---

<section class="category-page-header">
  <div class="container">
    <h1>AI Search and GEO Checklist</h1>
    <p>Prepare your site for AI-powered search engines like ChatGPT, Perplexity, Claude, and Google AI Overviews. 6 checks for Generative Engine Optimization.</p>
  </div>
</section>

<section class="category-content">
  <div class="container">
    <h2>Why AI Search Optimization Matters</h2>
    <p>AI search engines pull content in real time from the web. If your technical SEO is clean, AI systems can access and cite your content. If your robots.txt blocks AI crawlers or your HTML is poorly structured, you are invisible in AI-generated answers.</p>
    <p>GEO (Generative Engine Optimization) is not a separate discipline. It is technical SEO applied to AI retrieval. The same fundamentals that help Google index your pages also help ChatGPT cite them.</p>

    <h2>The 6 AI Search Checks</h2>

    <h3>1. Verify AI Crawler Access in Robots.txt</h3>
    <p>AI retrieval bots need access to your content. Check that GPTBot, Claude-Web, and other AI crawlers are not blocked. Separate training crawlers (which learn from your data) from retrieval crawlers (which fetch content for real-time answers).</p>
    <pre>User-agent: GPTBot
Allow: /
Disallow: /private/

User-agent: Claude-Web
Allow: /

User-agent: Google-Extended
Allow: /</pre>

    <h3>2. Use Semantic HTML Structure</h3>
    <p>AI agents parse HTML to understand content structure. Use semantic tags: header, nav, main, article, section, aside, footer. Proper headings (h1 > h2 > h3) create a clear content outline that AI systems can navigate.</p>
    <pre>&lt;!-- Good: Semantic HTML --&gt;
&lt;header&gt;&lt;nav&gt;...&lt;/nav&gt;&lt;/header&gt;
&lt;main&gt;
  &lt;article&gt;
    &lt;h1&gt;Main Title&lt;/h1&gt;
    &lt;section&gt;
      &lt;h2&gt;Section Title&lt;/h2&gt;
      &lt;p&gt;Content...&lt;/p&gt;
    &lt;/section&gt;
  &lt;/article&gt;
&lt;/main&gt;
&lt;footer&gt;...&lt;/footer&gt;

&lt;!-- Bad: Div soup --&gt;
&lt;div class="header"&gt;...&lt;/div&gt;
&lt;div class="content"&gt;...&lt;/div&gt;</pre>

    <h3>3. Optimize for Entity Recognition</h3>
    <p>AI systems extract entities (people, places, things, concepts) from your content. Use consistent entity names. Include schema markup for entities. Link to Wikipedia or authoritative sources for key entities.</p>

    <h3>4. Implement llms.txt</h3>
    <p>llms.txt is a proposed standard that tells AI systems which content to use for training and retrieval. It is like robots.txt but for LLMs. Create an llms.txt file at the root of your site.</p>
    <pre># llms.txt
https://www.yourdomain.com/
https://www.yourdomain.com/about
https://www.yourdomain.com/technical-seo-guide

# Preferred content for AI training and retrieval
https://www.yourdomain.com/blog/
https://www.yourdomain.com/guides/

# Content to exclude
- https://www.yourdomain.com/private/</pre>

    <h3>5. Ensure Clean HTML for Agent Parsing</h3>
    <p>AI agents parse your HTML when rendering pages. Keep HTML clean, valid, and accessible. Avoid JavaScript-dependent content for critical information. Some agents cannot execute JS and will only see a blank page.</p>

    <h3>6. Test Agentic Commerce Readiness</h3>
    <p>If you run an ecommerce site, test whether an AI agent can complete a purchase. Use ChatGPT's shopping assistant or similar tools. If it stalls at checkout, your technical implementation is blocking AI-driven sales.</p>

    <div class="category-navigation">
      <a href="{{ site.baseurl }}/categories/mobile-ux">&larr; Previous: Mobile and UX</a>
      <a href="{{ site.baseurl }}/categories/audit-checklist">Next: Audit Checklist &rarr;</a>
    </div>
  </div>
</section>
