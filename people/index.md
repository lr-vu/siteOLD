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
