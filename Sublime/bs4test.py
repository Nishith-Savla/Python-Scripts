from bs4 import BeautifulSoup

response = """
<div class="overview">
<i class="fa fa-instagram"></i>
<div class="overflow-h">
<small>Value #1 here</small>
<small>131,390,555</small>
<div class="progress progress-u progress-xxs">
<div style="width: 13%" aria-valuemax="100" aria-valuemin="0" aria-valuenow="92" role="progressbar" class="progress-bar progress-bar-u">
</div>
</div>
</div>
</div>

<div class="overview">
<i class="fa fa-facebook"></i>
<div class="overflow-h">
<small>Value #2 here</small>
<small>555</small>
<div class="progress progress-u progress-xxs">
<div style="width: 13%" aria-valuemax="100" aria-valuemin="0" aria-valuenow="92" role="progressbar" class="progress-bar progress-bar-u">
</div>
</div>
</div>
</div>
"""

soup = BeautifulSoup(response, 'html.parser')
overview_div = soup.findAll('div', class_ = 'overview')
small_tag_2 = overview_div[0].findAll('small')[1]
print(small_tag_2)
