# https://lr.cs.vu.nl/

This repo hosts the source code of the website. It's built with Jekyll.
This README is an onboarding document. If you find anything to be updated, including
this README, please make a branch and a pull request (PR).

By building a website with Jekyll and hosting as a Github page, we don't have to worry
about traditional web development. Ideally, we only have to modify markdown files.

Although at the moment some people are more active in the web development, it shouldn't
anyone can make changes / contributions by creating a branch and making a PR to the main
branch. For example, adding / modifying your profile should be easily done by you.

## Prerequisites

1. [Install Ruby, Jekyll, and Bundler](https://jekyllrb.com/docs/)
1. In the root repo directory, install the necessary gems by running `bundle install`.

## Run the website locally

1. Run `bundle exec jekyll serve --baseurl /`
1. Type http://127.0.0.1:4000/ on your web browser.

## Adding or modifying a user profile at https://lr.cs.vu.nl/people/

1. Create a new branch (e.g., `git checkout -b add-bob`)
1. Add your profile image in [`./images/members/`](./images/members/).
1. Add your entry in [`./_data/members.yml`](./_data/members.yml). The names are ordered
   in an alphabetical order.
1. [Test locally if it works](#run-the-website-locally).
1. Push your code to Github (e.g., `git push --set-upstream origin add-bob`)
1. [Create a PR to the main branch](https://github.com/lr-vu/site/pulls). Add reviewers who can check your code (e.g., Taewoon Kim).

## Adding or modifying a project at https://lr.cs.vu.nl/projects/

This is the same as [Adding or modifying a user profile](#adding-or-modifying-a-user-profile-at-httpslrcsvunlpeople), except that some paths are
different (e.g., `./images/projects/` instead of `./images/members/`,
and `./_data/projects.yml` instead of `./_data/members.yml`.
