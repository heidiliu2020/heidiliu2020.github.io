{% if page.comments and not page.no_ads %}
{# min-height 預留廣告空間，避免載入時版面位移（CLS） #}
<div class="ad-post-footer" style="margin: 2rem 0; min-height: 280px;">
  <ins class="adsbygoogle"
       style="display:block"
       data-ad-client="ca-pub-4274798044223706"
       data-ad-slot="3472959732"
       data-ad-format="auto"
       data-full-width-responsive="true"></ins>
  <script>
    (adsbygoogle = window.adsbygoogle || []).push({});
  </script>
</div>
{% endif %}
