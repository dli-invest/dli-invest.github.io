---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Tasklist


Acting under the assumption that tasklists will be implemented pretty quickly.

```{todo}
Move content to 2020 when done
```


**Vacation**
Get reddit data integrated and analysed - can have angular site that reads from faunadb via streaming and shows the latest reddit tweets
Also consider getting bigquery hooked up to the subreddits of interest.


**12/07 - 12/14**
Dash technical analysis minute by minute with data from yahoo finance. In depth day by day decision making.
Finish testing the zipline environment
- [x] Setup pyfolio using github codespaces and jupyter notebook.
- [ ] Youtube transcription of videos via url. Need to get webhook implementation to have it work on gae (whatever spin up codespace) or use google cloud run (need better docker file). Ehh agoracom has transcripts now, no need to not auto nlp it.
- [ ] Add social media data golang api.
	- [x] twitter data
	- [ ] linkedin data (via company)
	- [ ] reddit data


**12/01 - 12/06**
- [x] Get notifications on each cron job on failure via github actions. See https://github.community/t/if-expression-with-context-variable/16558.
	- [x] youtube nlp kinda working
	- [x] earnings report generation hook working
- [x] Fixed youtube nlp with docker embeds.



## Future Projects


#### Twitter data
TODO

- [ ] Stream data from twitter using the v2 api and/or v1 api.
- [ ] Notifications when events happen
- [ ] Use golang or python for this
- [ ] Store data in faunadb with discord notifications
- [ ]

#### Sedar documents

The sedar documents site is horribly outdated, I can automatically grab and download documents


Steps:
Seleinum based.

1. Go to inputted sedar url
2. Click on given link 
3. capcha reading using ocr downloading 5 images
4. entering data into input field
5. visiting all the other links now that authentication has occured.
