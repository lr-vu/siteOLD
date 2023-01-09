---
title: People
---

# Group Members #

<div class="people_gallery">
{% for member in site.data.members.group_members %}
  <figure>
    <a href="{{member.website}}"
      ><img
        src="{{site.baseurl}}{{member.image}}"
        class="people_gallery__img"
        alt="Image 1"
      />
      <figcaption>{{member.name}}</figcaption>
    </a>
  </figure>
{% endfor %}
</div>

# Guests #

<div class="people_gallery">
{% for member in site.data.members.guest_members %}
  <figure>
    <a href="{{member.website}}"
      ><img
        src="{{site.baseurl}}{{member.image}}"
        class="people_gallery__img"
        alt="Image 1"
      />
      <figcaption>{{member.name}}</figcaption>
    </a>
  </figure>
{% endfor %}
</div>

# Alumni #

<div class="people_unordered_list">
{% for member in site.data.members.alumni %}
    {% if member.website == and member.bio == %}
      <li><small>{{member.name}}</small></li>
    {% elsif member.website == and member.bio != %}
      <li><small>{{member.name}} ({{ member.bio | markdownify | remove: '<p>' | remove: '</p>' | strip_newlines}})</small></li>
    {% elsif member.website != and member.bio == %}
      <li><small><a href="{{member.website}}">{{member.name}}</a></small></li>
    {% elsif member.website != and member.bio != %}
      <li><small><a href="{{member.website}}">{{member.name}}</a> ({{ member.bio | markdownify | remove: '<p>' | remove: '</p>' | strip_newlines}})</small></li>
    {% endif %}

{% endfor %}

</div>
