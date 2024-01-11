---
layout: page-no-sidebar
title: "Cellular memory enhances bacterial chemotactic navigation in rugged environments"
date: 2020-01-01 00:00
categories: [dynamical systems, collective behaviour]
authors: Gosztolai, A., Barahona, M.
journal: Communications Physics
year: 2020
paperurl: https://www.sciencedirect.com/science/article/pii/S0959438822000265
codeurl: https://github.com/barahona-research-group/Chemotaxis-In-Rugged-Landscapes
---

## How memory helps microscopic swimmers to navigate

Life at the microscale is constantly on the move. However static a glass of seawater, lump of soil, or drop of blood appears to the naked eye, magnified several dozen times we find myriads of microscopic life forms buzzing with activity. At first sight, their motion appears haphazard, chaotic, or disorganized. However, decades of research have shown that the movement of microbes has been fine-tuned through the evolutionary pressures of searching for nutrients, avoiding toxins, or escaping microscopic predators. These migratory responses to environmental cues are known as [chemotaxis](https://en.wikipedia.org/wiki/Chemotaxis).

![Swimming *E. coli* cells under a microscope. Courtesy of Howard Berg (www.rowland.harvard.edu).](https://adamgosztolai.files.wordpress.com/2021/06/1q1lzv-seoh2yqw1jggpgkg-1.gif?w=320)

Since the development of microscopy, biologists have uncovered a great deal about the complex molecular interactions that regulate chemotaxis. As a result, in several bacterial species such as *E. coli*, we have a good understanding of the underlying biochemical processes. The major stages of processing include the sensing of environmental chemicals, relaying these signals via a series of subsequent reactions, and finally regulating molecular motors. The role of the motors is to turn a set of whip-like appendages called flagella propelling the microbe forward.

This is where the story begins. These scientific leaps have inspired physicists and mathematicians to understand how these seemingly random molecular interactions give rise to ordered, coordinated swimming. Indeed, objectives such as searching for nutrients do not immediately follow from merely turning a molecular motor. Rather, these behaviors emerge from the dynamics of reaction pathways, regulated by feedback loops. If this is not complicated enough, the presence of other cells and the fluid dynamics at the microscale also shapes this motion - but this is a topic for another article.


## Biochemical Memory

So what do I mean by ‘dynamics of reaction pathways’ and ‘feedback loops’ and what is their significance? Let me explain with a simple example. Millions of protein complexes called receptors crowd on the surface of bacteria (and other cells). Different receptor types are sensitive to different types of small molecules floating in the environment, also known as ligands. When the ligand is in the proximity of the receptor they can bind starting a chain of chemical reactions inside the cell. Now suppose that some of the chemical reactions are slower than others. This means that exposure to ligands over periods of time (seconds to minutes) leads to the accumulation of intermediate signaling molecules. Reversing the direction of cause and effect, an accumulated pool of signaling molecules means that ligands must have been present in the environment in the past. In other words, the concentration of the intermediate molecule forms a *memory* of the environmental concentration.

Now, the story is somewhat more involved. How much the concentration of the signaling molecule changes relative to a baseline assigns a weight or importance to the stimulus. Moreover, the level of signaling molecules eventually tends to return to the baseline, meaning the intracellular state no longer contains information about past events. This reflects the memory length of the cell. Importantly, both the length and strength of this memory, i.e. what relative importance is given to concentrations at various times in the past, can be shaped by the timescale of reactions and the presence of positive or negative feedback. One very interesting case is when the concentration of the signaling molecule fluctuates up and down (relative to a baseline concentration) in response to a stimulus before returning back to the baseline level. This response allows the cell to give positive weighting to recent stimuli and negative weight to those in the more distant past, in effect making a temporal comparison.

![Consider a cell in an environment where the concentration of a chemical at the location x(t) of the cell is S(x(t)). The ligand molecules (green) bind specific receptors on the cell membrane and activate internal chemical reaction pathways (y1, y2, y3). Some reactions are faster than others which causes the accumulation of intermediate products. This cascade ultimately controls a molecular motor, which rotates a flagellum λ(t) to propel the cell forward.](https://adamgosztolai.files.wordpress.com/2021/06/1qbqdxewwfza9nx0ewdoi9w.png?w=708)


## Random Walks and Gradient-Sensing

Although simple, biochemical memory is fundamental to generating sophisticated behaviors such as navigating a landscape of chemicals. Indeed, when microbes swim, they have no way of ‘looking around’ in their chemical environment and deciding which way to swim. Likewise, the sperm cell has no way of knowing where the egg lies and quickly zaps to the finish line. Instead, they explore their environment randomly and, over time, bias their swimming in favorable directions. In essence, for a host of species, their flagella have two modes of rotation: turn it one direction and the cell will move straight, turn it the other and it will tumble in one place randomizing its orientation. This ‘random walk’ is typical for many microorganisms, although some have more fancy swimming patterns, which are subject to current research.

Now, whenever the cell swims in a straight line, it gets a chance to use its memory to compare the concentration it currently senses to that which it found some short time in the past. This is also known as gradient-sensing. If it senses an increase, thus a positive gradient, it can make straight-line runs slightly longer, and vice versa, to bias its motion over many exploratory runs towards hotspots in the chemical landscape.

## Exploration in Complex Environments

The gradient-sensing model is a simple description of cellular navigation and it performs well when the chemical landscape changes very slowly along the path of the cell, in what is called a shallow gradient. However, chemicals in the microbial environments typically unevenly diffuse due to the porosity of the medium (in soil) or turbulence (in water). From the cell’s perspective, such a landscape could appear as a rugged gradient at a scale that is inherent to the structure of the medium. The question we asked was whether the gradient-sensing mechanism is sufficient to describe how cells swim in environments that more realistically mimic natural microbial habitats. Interestingly, in rugged landscapes, we noticed that cells swam faster than predicted by the gradient-sensing mechanism.

![Individual cell trajectories (top) and drift of cell population (bottom) in a shallow gradient (left) and rugged (right) chemical landscapes. The figure shows that in a shallow gradient the gradient-sensing model gives a good prediction of the cell velocity, but this prediction breaks down in rugged landscapes. This means that there are unaccounted-for effects of memory in sensing.](https://adamgosztolai.files.wordpress.com/2021/06/1j-byxfkzihjk5tg0jvpfqq.jpeg?w=1024)

One way to accept this is to realize that the role of biochemical memory goes beyond merely sensing the gradient; it modulates chemical signals perceived during swimming. When the perceived stimuli fluctuate rapidly, for example, due to molecular collisions, the memory acts as a buffer to ‘average-out’ these fluctuations. This helps the cell to discern the underlying gradient and to approach the velocity predicted by gradient-sensing. In contrast, the fluctuations caused by ruggedness in the landscape do not necessarily appear rapid to the cell and therefore are not averaged out. Instead, we showed that under this scenario, the gradient-sensing model is an incomplete approximation because the cell can exploit these fluctuations to achieve higher swimming speeds.

Another way to understand this phenomenon is to note that an accurate assessment of the shallow gradient does not depend on the length of the memory, as long as it is short enough such that the cell does not change direction while the gradient measurement takes place. Our theory extends this viewpoint by showing that when the memory length is comparable to the characteristic scale of the perceived fluctuations, it extracts more information than the gradient. Our results precisely quantify the advantage of using memory by the increased swimming speed upwards rugged gradients. Since the swimming speed can be accurately measured in experiments, we hope that our results will spur future research in quantifying the relevance of memory in different physical scenarios.

## Memory in a Broader Context

**This form of cellular memory might seem too simple to have relevance for higher-order or multicellular organisms. However, this could be far from the truth. One area where we think our findings have implications is visual search. This is the process by which our eyes navigate a visual scene using random-walk-like saccadic eye movements. This process relies on specific neurons in the early visual cortex which respond to light very similarly to how microbes respond to chemicals. From this perspective, saccadic eye movements could be thought of as navigation over the image with neurons using their memory to integrate the spatial features as explored during the visual search. We think this is a theoretically and experimentally tractable and very interesting direction that could shed light on how connected multicellular systems integrate memory in individual cells as building blocks of sophisticated navigation strategies.**

---

## References

- **Gosztolai, A**., Barahona, M. Cellular memory enhances bacterial chemotactic navigation in rugged environments. *Communications Physics* **3,** 47 (2020) [article](https://www.nature.com/articles/s42005-020-0312-8) [code](https://doi.org/10.6084/m9.figshare.6973706.v5)

- **Gosztolai, A**., Carrillo J. A., Barahona, M. Collective search with finite perception: transient dynamics and search efficiency. *Frontiers in Physics, 6, 153 (2019)* [article](https://www.frontiersin.org/articles/10.3389/fphy.2018.00153/full) [code](https://figshare.com/articles/Matlab_code_of_the_optimal_navigation_ON_model/7477568) [summary](https://adamgosztolai.wordpress.com/2017/04/25/first-blog-post/)
