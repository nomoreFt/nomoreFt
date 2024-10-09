import feedparser, time

# RSS 피드 URL
URL = "https://nomoreft.github.io/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 7

# README.md에 들어갈 마크다운 텍스트
markdown_text = """
![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=250&section=header&text=nomoreFt%20&fontSize=90)

### 👋 안녕하세요, 습관의 힘을 믿는 백엔드 개발자 김현우입니다.

> 나는 몇 달이고 몇 년이고 생각하고 또 생각한다. 그러다 보면 아흔아홉 번은 틀리고, 백 번째가 되어서야 비로소 맞는 답을 얻어낸다 - **아인슈타인**

<h1>🌱 I will be learning ... 🌳</h1>

| 📚 **라이브러리**| ☁️ **Cloud & DevOps**| 🏛 **Software Architecture**| 🚀 **Languages**| 📚 **Books**|
|-|-|-|-|-|
| - Spring WebFlux<br>- Spring Cloud| <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=aws,kubernetes,kafka&perline=3" /></a> | - DDD<br>- MultiModule<br> | <a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=go,kotlin&perline=2" /></a> | - [이펙티브 자바](https://product.kyobobook.co.kr/detail/S000001033066)<br>- [단위 테스트](https://product.kyobobook.co.kr/detail/S000001805070)<br>- [JVM 밑바닥까지 파헤치기](https://product.kyobobook.co.kr/detail/S000213057051) |

<h1>🛠 Tech Stack ⚒</h1>

### Languages
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=java,kotlin&perline=5" />
  </a>
</p>

### Frameworks & Libraries
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=spring,hibernate,axon&perline=5" />
  </a>
</p>

### DevOps & Cloud
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=docker,linux,githubactions&perline=5" />
  </a>
</p>

### Tools & Build
<p align="left">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=idea,gradle,postman,git,jenkins&perline=5" />
  </a>
</p>

<h1>✨ Status</h1>

![Solved.ac 프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=hy2wo2) 
![](http://github-profile-summary-cards.vercel.app/api/cards/stats?username=nomoreFt&&theme=slateorange)

<a href="https://github.com/devxb/gitanimals">
    <img src = "https://render.gitanimals.org/farms/{nomoreFt}" width="800" height="300"/>
</a>

<h1>🛠 My Contributions </h1>

- Spring Framework - PR #33625 - [Replace hardcoded "null" with NULL_STRING constant in ObjectUtils.nullSafeConciseToString](https://github.com/spring-projects/spring-framework/pull/33625)

<h1>🎇 Recent blog posts</h1>

"""

# RSS 피드에서 최근 게시물 가져오기
if 'entries' in RSS_FEED and RSS_FEED['entries']:
    for idx, feed in enumerate(RSS_FEED['entries']):
        if idx >= MAX_POST:
            break
        feed_date = feed['published_parsed']
        markdown_text += f"* [{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
else:
    markdown_text += "No recent blog posts found.<br/>\n"

# footer 추가
markdown_text += "<br>![footer](https://capsule-render.vercel.app/api?type=soft&color=gradient&height=30&section=header&text=&fontSize=90) <br><br><br>\n"

# README.md 파일에 쓰기
with open("README.md", mode="w", encoding="utf-8") as f:
    f.write(markdown_text)
