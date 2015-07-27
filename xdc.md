---
title: "companyx-dc-redo"
author: "Melody"
date: "July 25, 2015"
output: html_document
---

Hello (R Markdown) World! I had heard of **knitR** before, but never really had a use for it until recently, when I started to work on data challenges as part of the data scientist interview process. Using knitR to weave my analyses and code in an elegant report format is much better than what I was doing before, which was making comments in the code itself or having a separate document file to hold all of my plots and explanations. 

Below, I am going to redo a data challenge that was assigned to me a few weeks ago. I will be using knitR and the **dplyr** package (I was using base functions previously) to get some practice working with both. 

A short introduction to the challenge: I was given 2 large json bz2 files (~5GB total), an explanation of the variables, and several questions to answer. The biggest challenge I faced was trying to import the data into R or Python. After unsuccessfully trying to load the larger data file (~3GB) using **rjson** and **jsonlite**, I switched over to Python's **json** module. I like to do my data analyses in R, so I saved the relevant variables as text files, and loaded them into R. I'm sure this isn't the most efficient way, so let me know if there is a better way to do this. I did try making another json file with the variables I needed, but the resulting file was actually slightly larger than the separate .txt files.

~



The first task was to find the top 5 largest users 


```r
userids = scan("userids.txt", n=5000000, sep="\n", blank.lines.skip=FALSE) 
totals = scan("totals.txt", n=5000000, sep=",", blank.lines.skip=FALSE)
totals = na.omit(totals) # weird trailing NA
df = data.frame(userids, totals)
rm(userids, totals)

grouped = group_by(df, userids)
top5 = summarise(grouped, sumtotal=sum(totals))
top5 = arrange(top5, desc(sumtotal))
head(top5, 5)
```

```
## Source: local data frame [5 x 2]
## 
##   userids  sumtotal
## 1   10032 517321885
## 2  133584 419299045
## 3   56957 100528250
## 4   55449  63637530
## 5  132574  58499855
```

Then, for each user, find the top 5 posts 


```r
urls = scan("urls.txt", n=5000000, what="character", sep="\n", blank.lines.skip=FALSE)
df$urls = urls
rm(urls)

q2 = function(id)
{
  user_grouped = group_by(filter(df, userids==id), urls)
  user_top5 = arrange(summarise(user_grouped, sumtotal=sum(totals)), desc(sumtotal))
  head(user_top5, 5)
}
q2(10032)
```

```
## Source: local data frame [5 x 2]
## 
##                                                                                                             urls
## 1                                 http://www.huffingtonpost.com/2013/01/22/michelle-obama-boehner_n_2529107.html
## 2                                http://www.huffingtonpost.com/2013/01/21/michelle-obama-eye-roll_n_2522136.html
## 3                http://www.huffingtonpost.com/2013/01/15/gene-rosen-sandy-hook-conspiracy-theory_n_2481912.html
## 4 http://www.huffingtonpost.com/2013/01/27/jonbenet-ramsey-case-grand-jury-indictment-alex-hunter_n_2562007.html
## 5                               http://www.huffingtonpost.com/2013/01/25/sarah-palin-fox-news-out_n_2553421.html
##   sumtotal
## 1  1433980
## 2  1377550
## 3  1334570
## 4  1324645
## 5  1221105
```

```r
q2(133584)
```

```
## Source: local data frame [5 x 2]
## 
##                                                                                                                                                    urls
## 1 http://www.dailymail.co.uk/news/article-2265002/Ahmed-Dogan-Heart-stopping-moment-man-pulls-gun-Bulgarian-opposition-leader-makes-speech-live-TV.html
## 2     http://www.dailymail.co.uk/news/article-2262740/Exeter-University-Safer-Sex-Ball-Investigation-CCTV-footage-couple-having-sex-spreads-campus.html
## 3                                http://www.dailymail.co.uk/news/article-2256641/Teenager-left-Marilyn-Monroe-design-like-blow-sex-doll-50-session.html
## 4          http://www.dailymail.co.uk/news/article-2265277/Mikel-Ruffinelli-420lb-mother-worlds-widest-hips-measuring-staggering-8ft-circumference.html
## 5                        http://www.dailymail.co.uk/news/article-2257975/Alarming-trend-teenaged-girls-shame-peers-dressing-slutty-wearing-make-up.html
##   sumtotal
## 1  1338845
## 2  1188525
## 3  1069455
## 4   976360
## 5   847250
```

```r
#and so on for 56957, 55449, 132574
```

Next, make 25 plots of the hourly traffic for each of the above links (I'll just show the ones for the most visited site)


```r
hours = matrix(scan("hours.txt"), ncol=24)
df = cbind(df, hours)
rm(hours)

# key here is that urls are not unique
q3 = function(id)
{
  top5links = as.character(q2(id)$urls) # o.w. levels takes too long
  q3df = filter(df, urls %in% top5links) # should cover userids as well
  q3df_byurl = group_by(q3df, urls)
  summarise_each(q3df_byurl, funs(sum), 4:27)
}

q3plot = function(x)
{
  par(ps=8)
  plot(x[2:25], main=x[1], xlab="Hours", ylab="Views") 
  lines(x[2:25])
}

apply(q3(10032), 1, q3plot)
```

![plot of chunk q3](figure/q3-1.png) ![plot of chunk q3](figure/q3-2.png) ![plot of chunk q3](figure/q3-3.png) ![plot of chunk q3](figure/q3-4.png) ![plot of chunk q3](figure/q3-5.png) 

```r
# etc
```

The next task was to write explanations for why each of the 25 links from previous question had the traffic trends they did. I'm not going to go through each of the link, but here are three potential reasons for why a page could peak at one hour and generate relatively low traffic for another hour: (1) Someone high-profile shared it (ex. if a celebrity shared a link on their twitter page, it would generate high traffic for the hour or so before and after the tweet was posted) or a popular site advertised it on their front page (ex. it rose to the top of the Facebook Trending....area or it was posted to the front page of Yahoo!) (2) In general, pages should get more traffic before/after school or work hours, assuming that non-school/non-work related internet usage is very limited during hours 9-17 (3) As pages are being shared, I think there should be a "tipping point" when the rate that it spreads through a network picks up (and then drops back down again after the large group finishes reading it). And an obvious reason for why a certain site had no traffic for a portion of the day is that the page wasn't posted until the first hour that it had activity.

The final task is to make a plot with the average hourly traffic for all posts with 15k views or greater from all partners with error bars. 


```r
q5df_byurl = group_by(df, urls)
q5df = summarise_each(q5df_byurl, funs(sum), 4:27)
q5df$sumtotals = rowSums(q5df[,2:25])
q5df = filter(q5df, sumtotals>=15000)
res = colSums(q5df[,2:25]) / nrow(q5df)

plot(1:24, res, ylim=c(500, max(res)+500), main="Average Total Hourly Traffic, Posts With >=15k Views", xlab="Hour", ylab="Views")
lines(res)
segments(1:24, res-sd(res), 1:24, res+sd(res))
```

![plot of chunk q5](figure/q5-1.png) 

And done! 
