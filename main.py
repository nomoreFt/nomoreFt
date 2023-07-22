import feedparser, time

URL="https://nomoreft.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=7

markdown_text = """
![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&height=250&section=header&text=nomoreFt%20&fontSize=90)

<h1>🌱 I’m currently learning ... 🌳</h1>

<p align="center">
#알고리즘 #이펙티브 자바 #Axon CQRS #WebFlux #MultiModule #Spring Cloud #Heroku #AWS #Go #Docker, K8s, Jenkins 
</p>

<br>

<h1>🛠 Tech Stack ⚒️</h1>

<p align="center">
 <img src="https://img.shields.io/badge/Go-00599C?style=flat&logo=Go&logoColor=1EDDFF"/>
 <img src="https://img.shields.io/badge/Java-black?style=flat&logo=Java&logoColor=FF0000"/>
 <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=JavaScript&logoColor=white"/>
 <img src="https://img.shields.io/badge/SpringBoot-47A248?style=flat&logo=Spring Boot&logoColor=#1EDDFF"/>
 <img src="https://img.shields.io/badge/Docker-00599C?style=flat&logo=Docker&logoColor=#1EDDFF"/>
 <img src="https://img.shields.io/badge/Kubernetes-00599C?style=flat&logo=Kubernetes&logoColor=8B4513"/>
 <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=MySQL&logoColor=white"/></a> &nbsp 
 
                   
</p>
<br>
<br>

<h1>✨ Status</h1>


ㅤㅤ![nomoreFt's github stats](https://github-readme-stats.vercel.app/api/top-langs/?username=nomoreFt&show_icons=true&hide_border=false&title_color=004386&icon_color=004386&layout=compact)ㅤㅤㅤㅤㅤㅤ
![Solved.ac 프로필](http://mazassumnida.wtf/api/v2/generate_badge?boj=hy2wo2) 

<br>
<br>

ㅤㅤ![nomoreFt's github stats](https://github-readme-stats.vercel.app/api?username=nomoreFt&show_icons=true)

<br>
<br>

<h1>🎇 Recent blog posts</h1>

<!--
**nomoreFt/nomoreFt** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.
Here are some ideas to get you started:
- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->
""" # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        markdown_text += "![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FnomoreFt&count_bg=%231F0303&title_bg=%23BBB8C6&icon=exercism.svg&icon_color=%23000000&title=hits&edge_flat=false)<br>"
        markdown_text += "![footer](https://capsule-render.vercel.app/api?type=soft&color=gradient&height=30&section=header&text=&fontSize=90) <br><br><br>\n"
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
       
       

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
