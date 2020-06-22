---
layout: post
title:  "DB Learning Material Recomendation"
date:   2020-06-20 21:26:29
categories: jekyll update
---

Originally the reason I started this site is to record all my learning experience for MySQL. But sadly, only after working for one half in FB MySQL team, I decided to leave the team. This is not because I don’t like DB. In fact, I really enjoyed the DB learning experience. The reason I left the team is more about personal growth and the way people lead that team. If I have time, I will write more details in future. 

Okay, if you want to learn how DB is working, here are materials I recommend 



*   [Database Internals](https://www.amazon.com/Database-Internals-Deep-Distributed-Systems/dp/1492040347/ref=sr_1_2?crid=3F7FA3K3JHKTQ&dchild=1&keywords=database+internals&qid=1592800995&sprefix=Database%2Caps%2C231&sr=8-2) I tried several books like MySQL internals, high performance MySQL. But all those books are more about MySQL, and lack of concepts introduction. Database Internals is different. This book explains all kinds of concepts like BTree, LSM Tree, transactions and how the DB applies those technologies. What’s more, it gives the paper references for those of people who want to go deeper. If you only want to read one book about DB, my recommendation is this book. 
*   Andy Pavlo’s DB course. This professor is one of the coolest professors in my opinion. His has two courses on YouTube
    *   [Intro to Database system](https://www.youtube.com/playlist?list=PLSE8ODhjZXjbohkNBWQs_otTrBTrjyohi) Just like its name. This is an entry level course. Even though some people suggest I should skip it. But in fact, this class explained lots of useful things like indexing, buffer pool, table join. When I took the advanced course, I realized that Andy just assumed that you knew all those things at the beginning. Highly recommend this course. However, one of the problems is that since this is a video course, compared to reading books, watching video can take a long time. 
    *   [Advanced Database System](https://www.youtube.com/playlist?list=PLSE8ODhjZXja7K1hjZ01UTVDnGQdx5v5U) This is the advance course. It covers lots of researching topics. If you want to work for DB or do research, definitely take this course. But again, the same problem, watching video can take a long time. Sometimes, to save time, I just directly read the paper on the  reading list instead of watching videos. 
*   [High performance MySQL](https://www.amazon.com/High-Performance-MySQL-Optimization-Administrators-ebook/dp/B0026OR31W/ref=sr_1_5?dchild=1&keywords=High+performance+MySQL&qid=1592802744&sr=8-5). This book is more about tuning DB performance. If your job is more like a DBA. This book is worth reading. 
*   [Designing Data-Intensive Application ](https://www.amazon.com/Designing-Data-Intensive-Applications-Reliable-Maintainable/dp/1449373321/ref=sr_1_1?dchild=1&keywords=Designing+Data-Intensive+Application&qid=1592802925&sr=8-1)This is a great book! Compared to Database internals, this book is more focused on distributed systems. In fact, if you want to know more distributed systems, this is a really good book. But compared to Database internals, it lacks some core DB topics, like LSM tree, B-Tree. This is why I recommend it less compared to Database internals. 

That’s all. Thanks for reading. 

