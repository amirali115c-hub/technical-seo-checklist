---
layout: default
title: Crawlability and Indexing Checklist
description: Complete guide to crawlability and indexing SEO. Robots.txt, XML sitemaps, redirect chains, broken links, crawl budget, and IndexNow with code examples.
---

<section class="category-page-header">
  <div class="container">
    <h1>Crawlability and Indexing Checklist</h1>
    <p>Ensure search engines and AI systems can discover, crawl, and index every important page on your site. 12 checks with code examples.</p>
  </div>
</section>

<section class="category-content">
  <div class="container">

    <h2>Why Crawlability Matters</h2>
    <p>Before Google, Bing, ChatGPT, or Perplexity can do anything with your content, they must first find it, crawl it, and add it to their index. If any step in this chain breaks, your content is invisible. Crawlability is the most fundamental layer of technical SEO. Without it, nothing else works.</p>

    <h2>The 12 Crawlability Checks</h2>

    <h3>1. Check Index Coverage in Google Search Console</h3>
    <p>Open the Pages report in Google Search Console. Review the total indexed vs. not indexed count. Click each exclusion reason to see which pages are affected. Important pages showing as "Crawled but not indexed" need content improvement.</p>

    <h3>2. Fix Duplicate Website Versions</h3>
    <p>Your site should resolve to one canonical version. Test all four combinations: http/https and www/non-www. Each should redirect to your preferred version with a 301 redirect.</p>
    <pre># Apache: Force HTTPS + WWW
RewriteEngine On
RewriteCond %{HTTPS} off [OR]
RewriteCond %{HTTP_HOST} !^www\. [NC]
RewriteRule ^(.*)$ https://www.yourdomain.com/$1 [R=301,L]

# Nginx: Force HTTPS + WWW
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://www.yourdomain.com$request_uri;
}</pre>

    <h3>3. Optimize Robots.txt</h3>
    <p>Check your robots.txt at yourdomain.com/robots.txt. Ensure it allows Googlebot, Bingbot, GPTBot, and Claude-Web while blocking low-value paths like admin, login, and cart pages.</p>
    <pre>User-agent: *
Allow: /
Disallow: /admin/
Disallow: /login/
Disallow: /cart/
Disallow: /checkout/

User-agent: GPTBot
Allow: /

User-agent: Claude-Web
Allow: /

Sitemap: https://www.yourdomain.com/sitemap.xml</pre>

    <h3>4. Fix Redirect Chains and Loops</h3>
    <p>Use Screaming Frog or Semrush Site Audit to detect redirect chains. Every redirect should point directly to the final URL, not through intermediate URLs.</p>

    <h3>5. Fix Broken Links</h3>
    <p>Internal and external broken links waste crawl budget and frustrate users. Run a full crawl with Screaming Frog and fix all 4xx errors. Restore deleted pages, set up 301 redirects, or update the links to working URLs.</p>
    <pre># Bulk check URLs with curl
for url in $(cat urls.txt); do
  status=$(curl -o /dev/null -s -w "%{http_code}" $url)
  echo "$url - $status"
done</pre>

    <h3>6. Fix Server Errors (5xx)</h3>
    <p>5xx errors completely block crawling. Check GSC for server error reports. Review server logs for patterns. Common causes: overloaded servers, PHP memory limits, database connection failures.</p>

    <h3>7. Submit XML Sitemap to Google Search Console</h3>
    <p>Generate a clean XML sitemap containing only canonical, indexable URLs. Submit it in GSC under Sitemaps. Monitor for errors and warnings.</p>
    <pre>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"&gt;
  &lt;url&gt;
    &lt;loc&gt;https://www.yourdomain.com/&lt;/loc&gt;
    &lt;lastmod&gt;2026-07-15&lt;/lastmod&gt;
    &lt;changefreq&gt;weekly&lt;/changefreq&gt;
    &lt;priority&gt;1.0&lt;/priority&gt;
  &lt;/url&gt;
&lt;/urlset&gt;</pre>

    <h3>8. Find and Fix Orphan Pages</h3>
    <p>Orphan pages have zero internal links. They are invisible to crawlers and users. Cross-reference your sitemap URLs with crawl data to identify orphans, then add contextual internal links.</p>

    <h3>9. Optimize Crawl Budget</h3>
    <p>Google allocates limited crawl resources per site. Block low-value URLs in robots.txt, consolidate thin content, use noindex on unimportant pages, and prioritize your best content in the sitemap.</p>

    <h3>10. Implement IndexNow</h3>
    <p>IndexNow notifies search engines instantly when content changes. Supported by Bing, Yandex, Naver, and Seznam. Send a ping every time you publish or update a page.</p>
    <pre># IndexNow API call
curl -X POST https://bing.com/IndexNow \
  -H "Content-Type: application/json" \
  -d '{"host":"www.yourdomain.com","key":"your-key",
       "keyLocation":"https://www.yourdomain.com/your-key.txt",
       "urlList":["https://www.yourdomain.com/new-page"]}'</pre>

    <h3>11. Check Pagination</h3>
    <p>Paginated series should use rel="next" and rel="prev" tags to signal the relationship between pages. Apply canonical tags pointing to the main series page.</p>

    <h3>12. Monitor Google Search Console Weekly</h3>
    <p>GSC is your early warning system. Check it weekly for index coverage drops, new crawl errors, manual actions, and Core Web Vitals issues. Set up email alerts for critical changes.</p>

    <div class="category-navigation">
      <a href="{{ site.baseurl }}/">&larr; Back to Home</a>
      <a href="{{ site.baseurl }}/categories/core-web-vitals">Next: Core Web Vitals &rarr;</a>
    </div>

  </div>
</section>
