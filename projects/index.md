---
title: Projects
---

# Current Projects #

<div class="projects_gallery">
{% for project in site.data.projects.current_projects %}
  {% if project.image != null %}
    <figure>
      <a href="{{project.website}}"
        ><img
          src="{{site.baseurl}}{{project.image}}"
          class="people_gallery__img"
          alt="Image 1"
        />
      </a>
    </figure>
  {% else %}
    <a href="{{project.website}}"><strong>{{project.name}}</strong></a>
  {% endif %}
{% endfor %}
</div>

# Previous Projects #

<ul>
{% for project in site.data.projects.previous_projects %}
  {% if project.website != null %}
    <li><a href="{{project.website}}">{{project.name}}</a></li>
  {% else %}
    <li>{{project.name}}</li>
  {% endif %}
{% endfor %}
</ul>
