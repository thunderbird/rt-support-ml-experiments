# rt-support-ml-experiments
adventures in ml
## 1. 2024-11-03 setup
* Copy the questions file
```bash
 cp ../rt-tb-regular-expression-scanner/link_epoch_time_yyyy_mm_dd_iso_week_2023-2024-yearly-thunderbird-questions.csv .
```
**get essential fields: id, link, title, post, content and july 1-31, 2024 English only CSV:**
```bash
mlr --csv --from link_epoch_time_yyyy_mm_dd_iso_week_2023-2024-yearly-thunderbird-questions.csv \
filter \
'$created_epoch > 1719817199 && $created_epoch < 1722495600 && $locale == "en-US"' \
then cut -f id,created,link,title,content \
> 2024-07-01-2024-07-31-id-created-link-title-content.csv
```
**get essential fields: id, link, title, post, content and july 1-31, 2024 English only JSON:**
```bash
 mlr --icsv --ojson --from link_epoch_time_yyyy_mm_dd_iso_week_2023-2024-yearly-thunderbird-questions.csv
\
filter \
'$created_epoch > 1719817199 && $created_epoch < 1722495600 && $locale == "en-US"' \
then cut -f id,created,link,title,content \
> 2024-07-01-2024-07-31-id-created-link-title-content.json
```
