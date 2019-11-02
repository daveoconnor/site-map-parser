# Site Mapper


## Requirements

Handle sitemaps according to: https://www.sitemaps.org/protocol.html
   
1. Sitemap Index
1. Sitemap
1. Url

## Usage

### Basic Usage

```python
sm = SiteMapper(url)
if sm.is_sitemap_index():
    sitemap_list = sm.getSitemaps()
else:
    url_list = sm.getUrls()
```

