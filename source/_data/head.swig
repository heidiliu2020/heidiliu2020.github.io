<link rel="preconnect" href="https://pagead2.googlesyndication.com" crossorigin>
<link rel="preconnect" href="https://giscus.app" crossorigin>
<link rel="dns-prefetch" href="https://giscus.app">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4274798044223706"
    crossorigin="anonymous"></script>

{# Fallback og:image：open_graph() 只在內文有圖時輸出 og:image，這裡補上全站預設分享圖 #}
{%- if not (page.photos and page.photos.length) and (not page.content or page.content.indexOf('<img') == -1) %}
<meta property="og:image" content="{{ config.url }}/images/og-default.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
{%- endif %}

{%- if page.layout == 'post' and page.permalink %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": {{ page.title | json }},
  {%- if page.description %}
  "description": {{ page.description | json }},
  {%- endif %}
  "image": "{{ config.url }}/images/og-default.jpg",
  "author": {
    "@type": "Person",
    "name": "{{ config.author }}",
    "url": "{{ config.url }}/about/"
  },
  "datePublished": "{{ page.date.toISOString() }}",
  "dateModified": "{{ (page.updated or page.date).toISOString() }}",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{ page.permalink }}"
  },
  "inLanguage": "zh-TW"
}
</script>
{%- endif %}
