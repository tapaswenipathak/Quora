![](https://img.shields.io/badge/-quora-blueviolet.svg)

quora
======
[![GitHub issues](https://img.shields.io/github/issues/tapaswenipathak/Quora.svg)](https://github.com/tapaswenipathak/Quora/issues)
[![GitHub forks](https://img.shields.io/github/forks/tapaswenipathak/Quora.svg)](https://github.com/tapaswenipathak/Quora/network)
[![GitHub stars](https://img.shields.io/github/stars/tapaswenipathak/Quora.svg)](https://github.com/tapaswenipathak/Quora/stargazers)
[![GitHub license](https://img.shields.io/github/license/tapaswenipathak/Quora.svg)](https://github.com/tapaswenipathak/Quora/blob/master/LICENSE)
[![Twitter](https://img.shields.io/twitter/url/https/github.com/tapaswenipathak/Quora.svg?label=Quora&style=social)](https://twitter.com/intent/tweet?text=Quora:&url=https%3A%2F%2Fgithub.com%2Ftapaswenipathak%2FQuora)


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
