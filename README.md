# Site Map Parser


## Requirements

Handle sitemaps according to: https://www.sitemaps.org/protocol.html
   
1. Sitemap Index
1. Sitemap
1. Url

## Usage

### Basic Usage

```python
sm = SiteMapper(url)
if sm.has_sitemaps():
    sitemap_list = sm.getSitemaps()
else:
    url_list = sm.getUrls()
```

