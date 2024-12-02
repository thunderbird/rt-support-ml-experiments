# rt-support-ml-experiments
adventures in ml :-) All data used in my experiments is publicly available data.
## 3. 2024-12-02 Some prompts and results
### Prompt 1
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
### Prompt 2
Please repeat the above analysis but add a link to the posts using the "question_link" field

### Reply 2
Here’s the analysis of the posts with links to the relevant discussions included:

### Categories and Links
- **Authentication Issues (21 posts)**: Issues related to logging in, OAuth, password errors, and connection failures.
  - [Post 1](https://support.mozilla.org/en-US/questions/1472314)
  - [Post 2](https://support.mozilla.org/en-US/questions/1472321)
  - [Post 3](https://support.mozilla.org/en-US/questions/1472391)
  - [Post 4](https://support.mozilla.org/en-US/questions/1472544)
  - [Post 5](https://support.mozilla.org/en-US/questions/1472666)
  - [Post 6](https://support.mozilla.org/en-US/questions/1472939)
  - [Post 7](https://support.mozilla.org/en-US/questions/1473244)
  - [Post 8](https://support.mozilla.org/en-US/questions/1473328)
  - [Post 9](https://support.mozilla.org/en-US/questions/1473349)
  - [Post 10](https://support.mozilla.org/en-US/questions/1473400)
  - [Post 11](https://support.mozilla.org/en-US/questions/1474328)
  - [Post 12](https://support.mozilla.org/en-US/questions/1475332)
  - [Post 13](https://support.mozilla.org/en-US/questions/1475310)
  - [Post 14](https://support.mozilla.org/en-US/questions/1475399)
  - [Post 15](https://support.mozilla.org/en-US/questions/1475632)
  - [Post 16](https://support.mozilla.org/en-US/questions/1475746)
  - [Post 17](https://support.mozilla.org/en-US/questions/1475644)
  - [Post 18](https://support.mozilla.org/en-US/questions/1476606)
  - [Post 19](https://support.mozilla.org/en-US/questions/1475806)
  - [Post 20](https://support.mozilla.org/en-US/questions/1476406)
  - [Post 21](https://support.mozilla.org/en-US/questions/1474318)

- **Email Sync Problems (19 posts)**: Issues related to syncing emails across devices, server connection problems, and folder synchronization.
  - [Post 1](https://support.mozilla.org/en-US/questions/1472533)
  - [Post 2](https://support.mozilla.org/en-US/questions/1472544)
  - [Post 3](https://support.mozilla.org/en-US/questions/1473035)
  - [Post 4](https://support.mozilla.org/en-US/questions/1473334)
  - [Post 5](https://support.mozilla.org/en-US/questions/1473400)
  - [Post 6](https://support.mozilla.org/en-US/questions/1473500)
  - [Post 7](https://support.mozilla.org/en-US/questions/1474322)
  - [Post 8](https://support.mozilla.org/en-US/questions/1475034)
  - [Post 9](https://support.mozilla.org/en-US/questions/1475644)
  - [Post 10](https://support.mozilla.org/en-US/questions/1476555)
  - [Post 11](https://support.mozilla.org/en-US/questions/1476583)
  - [Post 12](https://support.mozilla.org/en-US/questions/1475600)
  - [Post 13](https://support.mozilla.org/en-US/questions/1475655)
  - [Post 14](https://support.mozilla.org/en-US/questions/1476415)
  - [Post 15](https://support.mozilla.org/en-US/questions/1475322)
  - [Post 16](https://support.mozilla.org/en-US/questions/1475832)
  - [Post 17](https://support.mozilla.org/en-US/questions/1475242)
  - [Post 18](https://support.mozilla.org/en-US/questions/1476494)
  - [Post 19](https://support.mozilla.org/en-US/questions/1476250)

- **Email Display Issues (8 posts)**: Concerns about font size, themes, or text readability.
  - [Post 1](https://support.mozilla.org/en-US/questions/1472318)
  - [Post 2](https://support.mozilla.org/en-US/questions/1472559)
  - [Post 3](https://support.mozilla.org/en-US/questions/1473528)
  - [Post 4](https://support.mozilla.org/en-US/questions/1476255)
  - [Post 5](https://support.mozilla.org/en-US/questions/1473035)
  - [Post 6](https://support.mozilla.org/en-US/questions/1475602)
  - [Post 7](https://support.mozilla.org/en-US/questions/1473252)
  - [Post 8](https://support.mozilla.org/en-US/questions/1476345)

- **Notifications Problems (7 posts)**: Problems with missing or unreliable email notifications.
  - [Post 1](https://support.mozilla.org/en-US/questions/1472894)
  - [Post 2](https://support.mozilla.org/en-US/questions/1473036)
  - [Post 3](https://support.mozilla.org/en-US/questions/1475632)
  - [Post 4](https://support.mozilla.org/en-US/questions/1473500)
  - [Post 5](https://support.mozilla.org/en-US/questions/1475495)
  - [Post 6](https://support.mozilla.org/en-US/questions/1475612)
  - [Post 7](https://support.mozilla.org/en-US/questions/1476418)

- **Address Book and Contacts (5 posts)**: Questions about using or syncing contacts.
  - [Post 1](https://support.mozilla.org/en-US/questions/1472560)
  - [Post 2](https://support.mozilla.org/en-US/questions/1475467)
  - [Post 3](https://support.mozilla.org/en-US/questions/1473123)
  - [Post 4](https://support.mozilla.org/en-US/questions/1476406)
  - [Post 5](https://support.mozilla.org/en-US/questions/1475432)

- **Spam Management (8 posts)**: How to manage or mark spam/junk emails.
  - [Post 1](https://support.mozilla.org/en-US/questions/1472471)
  - [Post 2](https://support.mozilla.org/en-US/questions/1475823)
  - [Post 3](https://support.mozilla.org/en-US/questions/1476483)
  - [Post 4](https://support.mozilla.org/en-US/questions/1473254)
  - [Post 5](https://support.mozilla.org/en-US/questions/1475765)
  - [Post 6](https://support.mozilla.org/en-US/questions/1475447)
  - [Post 7](https://support.mozilla.org/en-US/questions/1475635)
  - [Post 8](https://support.mozilla.org/en-US/questions/1475784)

- **Message Filters (2 posts)**: Questions about creating or managing filters.
  - [Post 1](https://support.mozilla.org/en-US/questions/1472881)
  - [Post 2](https://support.mozilla.org/en-US/questions/1475536)

- **General Configuration and Setup (15 posts)**: Issues with settings, importing accounts, or general setup.
  - [Post 1](https://support.mozilla.org/en-US/questions/1472543)
  - [Post 2](https://support.mozilla.org/en-US/questions/1473023)
  - [Post 3](https://support.mozilla.org/en-US/questions/1473295)
  - [Post 4](https://support.mozilla.org/en-US/questions/1473023)
  - [Post 5](https://support.mozilla.org/en-US/questions/1476222)
  - [Post 6](https://support.mozilla.org/en-US/questions/1474334)
  - [Post 7](https://support.mozilla.org/en-US/questions/1476424)
  - [Post 8](https://support.mozilla.org/en-US/questions/1476162)
  - [Post 9](https://support.mozilla.org/en-US/questions/1473282)
  - [Post 10](https://support.mozilla.org/en-US/questions/1476342)

### Mentions
- **Posts mentioning Microsoft** (6 posts):
  - [Post 1](https://support.mozilla.org/en-US/questions/1472321)
  - [Post 2](https://support.mozilla.org/en-US/questions/1473244)
  - [Post 3](https://support.mozilla.org/en-US/questions/1473314)
  - [Post 4](https://support.mozilla.org/en-US/questions/1474291)
  - [Post 5](https://support.mozilla.org/en-US/questions/1475322)
  - [Post 6](https://support.mozilla.org/en-US/questions/1475541)

- **Posts mentioning Google** (6 posts):
  - [Post 1](https://support.mozilla.org/en-US/questions/1472314)
  - [Post 2](https://support.mozilla.org/en-US/questions/1472939)
  - [Post 3](https://support.mozilla.org/en-US/questions/1472534)
  - [Post 4](https://support.mozilla.org/en-US/questions/1476226)
  - [Post 5](https://support.mozilla.org/en-US/questions/1474546)
  - [Post 6](https://support.mozilla.org/en-US/questions/1476182)

Let me know if you'd like further details on any of these categories!

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
