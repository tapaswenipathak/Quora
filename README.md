# quora

## Implemented

- [X] Questions Stats
- [X] Answer Stats
- [X] User Stats
- [X] Blog Stats
- [X] Spaces Stats
- [X] QnA
- [X] Posts
- [X] User Profile - Stats
- [X] User Activity

## Installation

`pip install quora`

## Code Samples

```python
from quora import Quora

userStats = Quora.getUserStats(<username>)

# answers
# questions
# shares
# spaces
# posts
# blogs
# followers
# following

questionStats = Quora.getQuestionStats(<question>)

# followers
# views
# date_asked
# tags
# url

answerStats = Quora.getAnswerStats(<answer>)

# upvotes
# upvoters
# text
# url

blogStats = Quora.getBlogStats(<blog_name>)

# followers
# posts

qna = Quora.getAnswer(<question>)

# answer

profile = Quora.getUserProfile(<username>)

# knows_about
# credential_highlights
# profile_picture

activity = Quora.getUserActivity(<username>)

# activity
```

## API

[quora-api](https://github.com/tapaswenipathak/quora-api).

`quora` performs unofficial Quora parsing.
