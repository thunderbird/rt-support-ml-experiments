# rt-support-ml-experiments
adventures in ml :-) All data used in my experiments is publicly available data.
## 3. 2024-12-02 Some prompts and results
### Prompt
`The file uploaded to Knowledge is a JSON file of posts on a support forum for November 2024. Tell me how many posts there are, and group them by what their complaint is about, roughly speaking. Tell me how many posts are in each group. Make sure one of the groups is "authentication issues" and include anything that talks about being unable to get into their email account, a password issue, or some sort of connection error to a server that is likely to be authentication-related. Also, call out the total number of posts that mention "Microsoft" or "Google" at the end.  Please link to the posts using the "question_link" field in the JSON file.`
### Answer 1:
There are a total of 154 posts in the dataset. Here is the grouping of posts by complaint category along with the number of posts in each group:
Categories and Counts

    Authentication Issues: 21
    Email Sync Problems: 19
    Email Display Issues: 8
    Notifications Problems: 7
    Address Book and Contacts: 5
    Spam Management: 8
    Message Filters: 2
    General Configuration and Setup: 15
    Others: 69

Mentions

    Posts mentioning Microsoft: 6
    Posts mentioning Google: 6

If you want to see the specific posts in any category or mentions, let me know! ​
​

## 2. 2024-12-02 Upload the data to ChatGPT
* https://github.com/thunderbird/rt-support-ml-experiments/blob/main/all_thunderbird_android_questions_november2024.json
## 1. 2024-12-02 Thunderbird for Android November 2024
* Big Query to get all the TB Android November 2024 questions. Output in
    * CSV Google Sheet: [PUBLIC DOCUMENT: all_thunderbird_android_questions_november2024-results-20241201-210209](https://docs.google.com/spreadsheets/d/1nD-qQY-5Q-YT6VY4Z8FsLfnvQ5awSHDOdhhO0th1A00/edit?gid=1276710460#gid=1276710460) and
    * JSON: https://github.com/thunderbird/rt-support-ml-experiments/blob/main/all_thunderbird_android_questions_november2024.json
```sql
SELECT
  question_id,
  question_link,
  title,
  question_content,
  created_date
FROM
  moz-fx-data-sumo-prod.mzla.metrics_thunderbird_questions
WHERE
  product LIKE 'thunderbird-android'
  AND is_spam = FALSE
  AND EXTRACT(YEAR
  FROM
    DATETIME(created_utc)) = 2024
  AND EXTRACT(MONTH
  FROM
    DATETIME(created_utc)) = 11
ORDER BY
  question_id ASC
LIMIT
  500000;
```
## 6. 2024-11-18 you don't need 'tostring' since it's already a string! You also don't need the brackets around the first conditional
```bash
cat questions-plus-original-poster-answers-and-tags-link_epoch_time_yyyy_mm_dd_iso_week_2023-2024-yearly-thunderbird-questions.json \
| jq   '.[] | select(.yyyy_mm_dd > "2024-11-03" and .yyyy_mm_dd < "2024-11-17")'  > /tmp/foo.json
```
## 5. 2024-11-18 boolean expression to get questions after November 11 and before November 17
```bash
 cat questions-plus-original-poster-answers-and-tags-link_epoch_time_yyyy_mm_dd_iso_week_2023-2024-yearly-thunderbird-questions.json \
| jq   '.[] | select((.yyyy_mm_dd|tostring>"2024-11-03") and .yyyy_mm_dd < "2024-11-17")'  > /tmp/foo.json
```
## 4. 2024-11-18 Filter by date e.g. greater than November 3, 2024 using yyyy_mm_dd (better than 3.
```bash 
cat questions-plus-original-poster-answers-and-tags-link_epoch_time_yyyy_mm_dd_iso_week_2023-2024-yearly-thunderbird-questions.json \
| jq   '.[] | select(.yyyy_mm_dd|tostring>"2024-11-03")'  > /tmp/foo.json
```
## 3. 2024-11-18 Filter by date e.g. greater than November 3, 2024 23:59:59 using unix time equivalent
```bash
cat questions-plus-original-poster-answers-and-tags-link_epoch_time_yyyy_mm_dd_iso_week_2023-2024-yearly-thunderbird-questions.json | \
jq   '.[] | select(.created_epoch|tostring>"1730678399")'  > /tmp/foo.json
```
## 2. 2024-11-18 Create JSON file just for November 4-17, 2024 i.e. last two weeks ChatGPT
* 1st prompt is: `This is a JSON file of posts on a support forum. Tell me how many posts there are, and group them by what their complaint is about, roughly speaking. Tell me how many posts are in each group. Make sure one of the groups is "authentication issues" and include anything that talks about being unable to get into their email account, a password issue, or some sort of connection error to a server that is likely to be authentication-related. Also, call out the total number of posts that mention "Microsoft" or "Google" at the end.  Please link to the posts using the link field in the JSON file.`
* Using this file: https://github.com/thunderbird/rt-support-ml-experiments/blob/main/2024-11-04-2024-11-17-yearly-thunderbird-questions-id-link-yyyymmdd-title-content.json
* 2nd prompt is: `Please provide the links to the specific posts.`
* ChatGPT session is: https://chatgpt.com/share/e/673b6871-f304-8002-9567-a6620301d77d
* * 3rd prompt is: `What are the differences between the week of November 4, 2024 to November 10, 2024 and the week of November 11, 2024 to November 17, 2024?`

## 1. 2024-11-18 Create JSON file just for November 4-17, 2024 i.e. last two weeks
* Edit the file and delete anything before november 4, 2024, have to figure out how to do this using jq or mlr :-)
* file 2024-11-04-2024-11-17-yearly-thunderbird-questions-id-link-yyyymmdd-title-content.json
```bash
cp 2023-2024-yearly-thunderbird-questions-id-link-yyyymmdd-title-content.json 2024-11-04-2024-11-17-yearly-thunderbird-questions-id-link-yyyymmdd-title-content.json
```
and then edit to remove prior to november 4, 2024
## 1. 2024-11-17 try create JSON and then cut id, link, yyyy_mm_dd, title, content

```bash
./create-json-from-question-and-original-poster-answer.rb \
link_epoch_time_yyyy_mm_dd_iso_week_2023-2024-yearly-thunderbird-questions.csv 2023-2024-yearly-thunderbird-answers.csv
jq '[.[] | {id: .id, link: .link, yyyy_mm_dd: .yyyy_mm_dd, title: .title, content: .content}]' \
questions-plus-original-poster-answers-and-tags-link_epoch_time_yyyy_mm_dd_iso_week_2023-2024-yearly-thunderbird-questions.json /
> 2023-2024-yearly-thunderbird-questions-id-link-yyyymmdd-title-content.json
```
## 1. 2024-11-04 I tried my CSV file
* See https://chatgpt.com/share/e/6728f078-f578-8002-b6ea-13be4b63c509
* CSV file is here: https://github.com/thunderbird/rt-support-ml-experiments/blob/main/2024-07-01-2024-07-31-id-created-link-title-content.csv 
## 2. 2024-11-03 I tried a few prompts
* See: https://chatgpt.com/share/e/6728613c-257c-8002-871b-ddea272f94e1 for my session with a JSON file which was weird because it didn't read all 1000 posts?!?
* JSON file is here: https://github.com/thunderbird/rt-support-ml-experiments/blob/main/2024-07-01-2024-07-31-id-created-link-title-content.json
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
