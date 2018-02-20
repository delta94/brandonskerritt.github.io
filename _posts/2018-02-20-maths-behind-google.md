---
title: "Maths behind Google"
categories:
  - University
---

When Google first started out in the 90s the one thing that set them apart from their competitors is that its search results always seem to show the most relevant and helpful results. Google's *page ranking* algorithm was at least 10 times better than any other search engine at the time.

Search engines typically have 3 main objectives:
1. Crawl the web and find all the web pages with public access
2. Index the data from step 1 so the pages can be searched efficiently
3. Rate the importance of each page in the database.

Here is an image of a very small web

![img](https://screenshotscdn.firefoxusercontent.com/images/8507a511-57fd-42f7-b2ee-8910f830f4f0.png)
Taken from [here](https://www.rose-hulman.edu/~bryan/googleFinalVersionFixed.pdf).

We will have an importance score that will represent how important a webpage is. One of the core ideas of assigning a score is that the page's score is derived from the links made to the page from other web pages. The links to a given page are called the _backlinks_ for that page.

In such a scoring system a democracy is created where web pages "vote" for the importance of web pages by lniking to them.

The web seen in the imaeg is an example of a _directed graph_, a graph that holds direction. A typical graph will consist of a set of vertices (in this context, they are called the web pages) and a set of edges. Each edge joins a pair of vertices (webpages). The graph is considered directed because each edge has a direction.

An approach one could make is to take $$x_k$$ as the number of backlinks for any page, k. In  the image above we then have:

$$x_1 - 2, x_2 = 1, x_3 = 3, x_4 = 2 $$

As can be seen here the most "important" web page is $$x_3$$ since it is linked to by 3 pages.

This approach ignores a large problem, mainly that a link from an already important page should have more weight to it than a link from a non-important page. In the image above pages 1 and 4 both have two backlinks: each links to the other, but page 1's backlink is from an important web page, page 3. While page 4's backlink is from an unimportant page 1.

In our new and improved version we don't want pages to be able to "vote" for themselves. We don't want a page to gain popularity by linking to lots of other pages. If page j contains $$x_j$$ links, one of them linking to page k, then we will boost page k's score by $$\frac{x_j}{n_j}$$.

In this version each webpage gets a total of one vote, weighted by that web page's score that is evenly divided up among all of its outgoing links.