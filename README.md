# ccomploj.github.io

1. To run locally (requires Jekyll/Ruby installed locally) 
bundle exec jekyll serve
2. Open browser
http://localhost:4000/

# Keeping the site online with a private repo
GitHub Pages visibility is controlled in the repository settings, not by files in this repo. To keep the website online while making the source private, you must use one of these options:

1. **GitHub Pages for private repos (requires a paid plan)**: Make the repo private, then in **Settings → Pages** choose **GitHub Actions** as the source to keep the site public.
2. **Separate public publish repo**: Keep a public `ccomploj.github.io` repo for the published site and move your source to a private repo, then deploy the built site to the public repo via GitHub Actions (requires a personal access token).

This repo alone cannot change its visibility; the steps above must be done in GitHub.

# Notes
The google html is the Google ownership file (to make the site searchable on Google). Change ownership on Google Search Console. The same needs to be done separately for Bing Console 
Special Thanks to Huang's repo
