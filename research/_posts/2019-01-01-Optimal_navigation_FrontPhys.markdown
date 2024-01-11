---
layout: page-no-sidebar
title: "Collective search with finite perception: transient dynamics and search efficiency"
date: 2019-01-01 00:00
categories: [dynamical systems, collective behaviour]
authors: Gosztolai, A., Carrillo, J. A., Barahona, M.
journal: Frontiers in Physics
year: 2019
paperurl: https://www.frontiersin.org/articles/10.3389/fphy.2018.00153/full?ref=https://githubhelp.com
codeurl: https://github.com/agosztolai/optimal_navigation
---

## The role of spatial perception in ecological navigation

Movement, exploration and search are ubiquitous behaviours among many organisms. Low on the tree of life, bacteria have evolved the ability of [chemotaxis](https://en.wikipedia.org/wiki/Chemotaxis) to navigate landscapes of concentrations to find nutrients or to avoid toxins. As another example, pigeons have an exceptional ability to navigate based on visual landmarks, among other cues, to find their way back home. Finally, many mammals have evolved a complex network of neurons including, but not limited to, grid cells and place cells to represent and search physical spaces, or perhaps even the space of memories.

![Fig1](https://adamgosztolai.files.wordpress.com/2018/09/fig1.jpg)
*Illustration of an animal searcher (fly) navigating a heterogeneous environment based on a finite perceptual horizon.*

A common feature among many animal searchers is using information from a *finite perceptual range* about their environments gathered through visual cues or other sensory cues. Studying how such limited spatial awareness facilitates search and exploration is a key step towards a deeper understanding of how more complex internal representations of space leads to efficient navigation.

First, let me provide some intuition. Consider a biased [random walker](https://en.wikipedia.org/wiki/Random_walk) (as it turns out, the movement of many animals can be modeled as a biased random walk) searching for nutrients in a landscape. How much spatial knowledge does the random walker need to find the spot where the nutrient is most abundant? It depends on how much time the random walker devotes to search. If the search time is not limited, knowing the local gradient (which way is up or down) suffices since, eventually, the walker will explore the whole space and find the target. Similarly, if only a very short time is given to the searcher, following the gradient is as good as it can do since it gives the searcher the best shot at reaching the local peak. Many biological systems, however, operate in between these two extremes time-scales, i.e. there is often a limited time to find a nutrient before it diffuses away or perhaps eaten by a lion. In this case, there could be a benefit of having a finite perceptual range; this could allow the random walker to preferentially exploit certain directions since spending energy searching in other directions will likely not result in as much reward.

To understand how limiting it really is to search based on a limited perceptual horizon, we proposed a parsimonious mathematical model based on biased random walks and [optimal control theory](https://en.wikipedia.org/wiki/Optimal_control). In this mathematical framework, finite perception appears naturally as the time horizon over which the searchers optimize their motion. Then, to shed light on the role of spatial perception we studied how quickly searchers found the source of a diffusing stimulant when they were moving alone or as a part of an interacting population.

We found that when searchers were given a limited time for searching they were more efficient at finding their targets when they had finite perceptual range compared to when they were only aware of the local gradient of their search landscape, which most classical studies of ecological search assume. Among all possible "look-around" horizons, there was an optimal one, which was comparable with the spatial scale of the landscape. Perhaps more surprisingly, there was no benefit of being aware of space beyond the optimal horizon; searchers with the optimal horizon could navigate as efficiently as those having complete information about the environment. Finally, we found an advantage of being part of a group; when searchers interacted through a secreted chemical, such as a pheromone, the optimal perceptual horizon further shrunk due to collective sensing.

In follow-up work, we study how even primitive sensory systems, such as the biochemical pathway controlling the chemotaxis of *E. coli*, can encode a finite perceptual range and use it to improve search performance.

---

##### Original publication

**Gosztolai, A**., Carrillo J. A., Barahona, M. Collective search with finite perception: transient dynamics and search efficiency. *Frontiers in Physics, 6, 153 (2019)* [article](https://www.frontiersin.org/articles/10.3389/fphy.2018.00153/full) [code](https://figshare.com/articles/Matlab_code_of_the_optimal_navigation_ON_model/7477568)
