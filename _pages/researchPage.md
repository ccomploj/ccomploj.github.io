---
title: "Research"
permalink: /research/
---

My research primarily examines behavioral and health responses to public policies. I previously used retirement data from China, the US and Europe to estimate my models. I employ microeconometrics methods and causal inference, and am proficient in Stata, Python, R and LaTeX.

{% if site.data.papers.working_papers.size > 0 %}
## Working Papers

{% for paper in site.data.papers.working_papers %}
### {{ paper.title }}
{% if paper.solo %}*Solo-authored{% if paper.status and paper.status != "" %} | {{ paper.status }}{% endif %}*{% elsif paper.authors.size > 0 %}*joint with {% for author in paper.authors %}{% if author.url %}[{{ author.name }}]({{ author.url }}){% else %}{{ author.name }}{% endif %}{% unless forloop.last %}{% if forloop.rindex == 2 %} and {% else %}, {% endif %}{% endunless %}{% endfor %}{% if paper.status and paper.status != "" %} | {{ paper.status }}{% endif %}*{% endif %}

{% if paper.abstract and paper.abstract != "" %}
<details>
<summary>Abstract</summary>

{{ paper.abstract }}

</details>
{% endif %}

{% endfor %}
{% endif %}

{% if site.data.papers.work_in_progress.size > 0 %}
## Work in Progress

{% for paper in site.data.papers.work_in_progress %}
### {{ paper.title }}
{% if paper.solo %}*Solo-authored{% if paper.status and paper.status != "" %} | {{ paper.status }}{% endif %}*{% elsif paper.authors.size > 0 %}*joint with {% for author in paper.authors %}{% if author.url %}[{{ author.name }}]({{ author.url }}){% else %}{{ author.name }}{% endif %}{% unless forloop.last %}{% if forloop.rindex == 2 %} and {% else %}, {% endif %}{% endunless %}{% endfor %}{% if paper.status and paper.status != "" %} | {{ paper.status }}{% endif %}*{% endif %}

{% if paper.abstract and paper.abstract != "" %}
<details>
<summary>Abstract</summary>

{{ paper.abstract }}

</details>
{% endif %}

{% endfor %}
{% endif %}







