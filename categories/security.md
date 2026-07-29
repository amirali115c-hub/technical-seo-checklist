---
layout: default
title: Security and HTTPS Checklist for SEO
description: Technical SEO security checklist. SSL certificates, mixed content, HSTS headers, and security headers audit with code examples.
---

<section class="category-page-header">
  <div class="container">
    <h1>Security and HTTPS Checklist</h1>
    <p>Secure your site for users and search engines. 4 checks covering SSL, mixed content, HSTS, and security headers.</p>
  </div>
</section>

<section class="category-content">
  <div class="container">
    <h2>Why Security Matters for SEO</h2>
    <p>HTTPS is a confirmed ranking signal. Browsers mark non-HTTPS sites as "Not Secure," destroying trust. Security breaches can lead to manual actions and complete removal from search results. AI agents also verify security before rendering content.</p>

    <h2>The 4 Security Checks</h2>

    <h3>1. Verify SSL Certificate</h3>
    <p>Ensure your SSL certificate is valid, not expired, and covers all subdomains. Use a free certificate from Let's Encrypt or your hosting provider.</p>
    <pre># Check SSL certificate details
openssl s_client -connect yourdomain.com:443 -servername yourdomain.com 2&gt;/dev/null | openssl x509 -noout -dates</pre>

    <h3>2. Fix Mixed Content</h3>
    <p>Mixed content occurs when an HTTPS page loads HTTP resources (images, scripts, iframes). Browsers block mixed content, breaking functionality. Use a content security policy to enforce HTTPS across all resources.</p>
    <pre># Content-Security-Policy header for HTTPS enforcement
Content-Security-Policy: upgrade-insecure-requests; default-src https:</pre>

    <h3>3. Implement HSTS (HTTP Strict Transport Security)</h3>
    <p>HSTS tells browsers to always connect via HTTPS, preventing downgrade attacks and SSL stripping. Add the HSTS header with a max-age of at least one year.</p>
    <pre># Nginx HSTS configuration
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

# Apache .htaccess
Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"</pre>

    <h3>4. Audit Security Headers</h3>
    <p>Security headers protect against common attacks. Add X-Content-Type-Options, X-Frame-Options, and Referrer-Policy. Use securityheaders.com to audit your current headers.</p>
    <pre># Recommended security headers
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;</pre>

    <div class="category-navigation">
      <a href="{{ site.baseurl }}/categories/schema-markup">&larr; Previous: Schema Markup</a>
      <a href="{{ site.baseurl }}/categories/mobile-ux">Next: Mobile and UX &rarr;</a>
    </div>
  </div>
</section>
