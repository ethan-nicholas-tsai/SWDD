# Sina Weibo Depression Dataset (SWDD)

## Introduction

- SWDD contains normal user sampels and depressed user samples collected by a [crawler](https://github.com/YiChengCai1999/SinaWeiboCrawler) using the crawling API provided by Sina Weibo. 
- The dataset is stored in the form of JsonLines, with `depressed.jsonl` for the depressed users and `control.jsonl` for none-depressed users. It can be download from [Google Driver](https://drive.google.com/file/d/1fNKtoo4SP98OAhalMjNRZfFqmQZsQ0fh/view?usp=sharing) or [Baidu Netdisk (Verification Code: gdq6)](https://pan.baidu.com/s/1V8S_a_GoFFRzRG542eRcSg)
- As of Dec 31, 2021, the candidate samples collected by the crawler and the various information of the samples in SWDD are shown in the following table. Once new data is updated later, the statistics in this table will be updated.

| Dataset    | Category      | User   | Tweet      |
| ---------- | ------------- | ------ | ---------- |
| Candidates | Depressed     | 64,513 | 11,610,155 |
|            | Non-depressed | 31,085 | 5,144,688  |
|            | Total         | 95,598 | 16,754,843 |
| SWDD       | Depressed     | 3,711  | 785,689    |
|            | Non-depressed | 19,526 | 4,068,732  |
|            | Total         | 23,237 | 4,854,421  |

- The detailed information fields of `user profile` include:

|     Field Name      |                         Description                          |                           Example                            |
| :-----------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|     avatar_url      |                  Link of user avatar image                   | https://tvax4.sinaimg.cn/crop.0.0.664.664.180/007VF8oFly8gbdxiv1hoyj30ig0igjrr.jpg?KID=imgbed,tva&Expires=1611228212&ssig=3MUKhB2a5q |
|   cover_image_url   |                   Link of user cover image                   | https://tva1.sinaimg.cn/crop.0.0.640.640.640/549d0121tw1egm1kjly3jj20hs0hsq4f.jpg |
|     description     |          A sentence of the user's self-introduction          |                     锦鲤也拯救不了的女孩                     |
|    follow_count     |                The number of user followings.                |                              26                              |
|   followers_count   |                The number of user followers.                 |                              11                              |
|       gender        |         User gender（`f` for female, `m` for male）          |                              f                               |
|     screen_name     |                        User nickname                         |                        一条自由的海豚                        |
|     tweet_count     |                   The number of all tweets                   |                              68                              |
|      user_rank      | Liveness of user on Sina Weibo（Bigger number represents for more user activities on Sina Weibo） |                              3                               |
|      verified       |    If user has passed certain verification of Sina Weibo     |                            false                             |
|   verified_reason   |  The reason of why the user pass verification of Sina Weibo  |                              -                               |
|      vip_rank       |                Vip rank of user on Sina Weibo                |                              1                               |
| private_tweet_count | The number of tweets that can only be seen by the user itself |                              0                               |

- The detailed information fields of `tweet` include:

|   Field Name    |                         Description                          |                           Example                            |
| :-------------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|       id        |                       Tweet id of user                       |                       4466236706001635                       |
| comments_count  |                    The number of comments                    |                              2                               |
|     edit_at     |               Last modified time of the tweet                |                              -                               |
|   edit_count    |               Modification times of the tweet                |                              0                               |
|  is_long_text   | Whether the tweet is a long tweet (Judged by Sina Weibo offical) |                             true                             |
|    is_origin    |         Whether the tweet is written by user itself          |                             true                             |
|    pics_url     | Links of pictures in the tweet content (delimited by comma)  |                              -                               |
|    post_time    | The posting time of the tweet (weekday month day hour:minute:second timezone year) |                Thu Jan 30 01:01:11 +0800 2020                |
|  publish_place  |       The current place of user when posting the tweet       |                              -                               |
|  publish_tool   | Use what kind of device to post the tweet or Under what supertopic the user post the tweet |                      vivo Y3 闪充强续航                      |
|  reposts_count  |                 Reposting times of the tweet                 |                              0                               |
|      text       | Text content of tweet (raw html, including emotion icons, mentions, topic of the tweet classified by Sina Weibo) | 该怎么说，许多人都说抑郁症就像感冒发烧可能熬过去了就会好了，也有许多人说是你自己想得太多，这都是屁话。许多人都不会理解我们，深夜痛苦得要死，被全身疼痛折磨，它是不是病就得看自己了，因为它无时无刻都存在，就像沼泽一样越陷越深，我尝试过如何摆脱它，但是我输了，它是不会走的。就像没有灵魂的空壳，没有了快乐，感受不到外界的爱，活在自己的世界里，想要的就只是解脱。 <a data-url=\"http://t.cn/AiD3iByL\" href=\"https://weibo.com/p/2313474450604943540609?\" data-hide=\"\"><span class='url-icon'><img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2016/11/23/433/wenda_icon_default.png'></span><span class=\"surl-text\">你了解抑郁症吗   知道抑郁症是一种病吗?</span></a> |
| thumb_ups_count |             The number of people favor the tweet             |                              1                               |
|    video_url    |                  Link of video in the tweet                  |                              -                               |
|   article_url   |           Link of front page headline in the tweet           |                              -                               |
|     topics      | Topics of the tweet (classified by Sina Weibo, delimited by comma) |                              -                               |
|    at_users     |     Mention of users of Sina Weibo (delimited by comma)      |                              -                               |

- The detailed information fields of `symptoms(labeled by us)` include:

|      Field Name       |                         Description                          | Example |
| :-------------------: | :----------------------------------------------------------: | :-----: |
|     self_reported     | If the user directly self-report of suffering from depression |  false  |
|     interest_loss     | If the user show signs of `Nothing can raise its interest ` in tweet |  false  |
|     pleasure_loss     | If the user show signs of `Feel no pleasure in normally enjoyable activities` in tweet |  true   |
|      energy_loss      |    If the user show signs of `Get tired easily` in tweet     |  true   |
|        sadness        | If the user show signs of `Feel sad without any reason` in tweet |  false  |
|  sympathetic arousal  | If the user describes of`Palpitation, chest distress, etc.` in tweet |  false  |
| concentration problem | If the user describes of `Can hardly concentract on most things` in tweet |  false  |
|         panic         | If the user show signs of `Feel terrified without any reason` in tweet |  false  |
|   appetite_problem    | If the user describes of `Frequently have nausea and vomiting` |  false  |
|       insomnia        | If the user describes of `Have insomnia` or have big portion of tweet posted during 0 am and 6 am |  true   |
|        anxious        |    If the user describes of `Often feel anxious` in tweet    |  false  |
|      self_blame       | If the user show signs of `Low self-esteem, or lay the blame for every wrongs to himself` in  tweet |  true   |
|      retardation      | If the user describes of `Feel slow on the draw  ` in tweet  |  false  |
|   suicidal ideation   | If the user describes of `Self-harm or thought of death` or post pictures of self-harm in tweet |  true   |
|    weight_problem     | If the user describes of `Lose weight or gain weight in a short time` in tweet |  false  |
|       agitation       |    If the user describes of `Easy to get angry` in tweet     |  false  |
|      hypersomnia      | If the user describes of `Feel sleepy at daytime and feel hard to get up` |  false  |

## Explanations and Issues

- In order to protect the privacy of depressed users, we have deleted the user IDs in SWDD.

- The depressed user is labeled in our self-implemented web-system based on a set of labeling criteria proposed by us. **We have uploaded the annotation system to [DepressionAnnotator Repo](https://github.com/YiChengCai1999/DepressionAnnotator)**

- **We have uploaded the crawler script to [SinaWeiboCrawler Repo](https://github.com/YiChengCai1999/SinaWeiboCrawler)**. Researchers can further collect user samples based on our scripts. 

- We don't clean the text content of tweet in the dataset, for we think emotion icons, mentions, topic of the tweet may be useful for feature extraction. **Instead, We have offered the scripts for data preprocessing ** in the folder `SWDD_preprocessing`, you can use our scripts for data cleaning or write your own scripts. An example of our `clean_text.py` is shown below:

  - raw html of a tweet in the dataset

    ```
    该怎么说，许多人都说抑郁症就像感冒发烧可能熬过去了就会好了，也有许多人说是你自己想得太多，这都是屁话。许多人都不会理解我们，深夜痛苦得要死，被全身疼痛折磨，它是不是病就得看自己了，因为它无时无刻都存在，就像沼泽一样越陷越深，我尝试过如何摆脱它，但是我输了，它是不会走的。就像没有灵魂的空壳，没有了快乐，感受不到外界的爱，活在自己的世界里，想要的就只是解脱。 <a data-url=\"http://t.cn/AiD3iByL\" href=\"https://weibo.com/p/2313474450604943540609?\" data-hide=\"\"><span class='url-icon'><img style='width: 1rem;height: 1rem' src='https://h5.sinaimg.cn/upload/2016/11/23/433/wenda_icon_default.png'></span><span class=\"surl-text\">你了解抑郁症吗   知道抑郁症是一种病吗?</span></a>
    ```

  - after cleaning using `get_raw_text`

    ```
    该怎么说，许多人都说抑郁症就像感冒发烧可能熬过去了就会好了，也有许多人说是你自己想得太多，这都是屁话。许多人都不会理解我们，深夜痛苦得要死，被全身疼痛折磨，它是不是病就得看自己了，因为它无时无刻都存在，就像沼泽一样越陷越深，我尝试过如何摆脱它，但是我输了，它是不会走的。就像没有灵魂的空壳，没有了快乐，感受不到外界的爱，活在自己的世界里，想要的就只是解脱。
    ```

  - after cleaning using `get_cleaned_text`

    ```
    该怎么说 许多人都说抑郁症就像感冒发烧可能熬过去了就会好了 也有许多人说是你自己想得太多 这都是屁话 许多人都不会理解我们 深夜痛苦得要死 被全身疼痛折磨 它是不是病就得看自己了 因为它无时无刻都存在 就像沼泽一样越陷越深 我尝试过如何摆脱它 但是我输了 它是不会走的 就像没有灵魂的空壳 没有了快乐 感受不到外界的爱 活在自己的世界里 想要的就只是解脱 你了解抑郁症吗 知道抑郁症是一种病吗
    ```

- If `encoding='utf-8'` doesn't work, try: `encoding='utf-8-sig'` when using `Python` to load the Jsonl file.

- Other issues will be updated soon...
