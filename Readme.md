# Remy Chaput's PhD Thesis

[![](https://img.shields.io/badge/github-Link%20to%20the%20manuscript%20branch-blue?logo=github&style=flat "Link to the manuscript branch")](https://github.com/rchaput/phdthesis/tree/manuscript)
[![](https://img.shields.io/badge/github-Link%20to%20the%20slides%20branch-blue?logo=github&style=flat "Link to the slides branch")](https://github.com/rchaput/phdthesis/tree/slides)

[![](https://img.shields.io/badge/html-View%20the%20HTML%20manuscript-blue?style=for-the-badge "View the HTML manuscript")](https://rchaput.github.io/phdthesis/)
[![](https://img.shields.io/badge/pdf-View%20the%20PDF%20manuscript-blue?style=for-the-badge "View the PDF manuscript")](https://rchaput.github.io/phdthesis/thesis.pdf)

This repository holds the source files (RMarkdown + Bookdown) for the thesis.


## Learning behaviours aligned with moral values in a multi-agent system: guiding reinforcement learning with symbolic judgments

Numerous AI systems are being deployed into our society, and have an impact on
humans. This raises questions about their ability to act in accordance with the
moral values that are important to us. In this thesis, we focus particularly on
the area of Machine Ethics, which is concerned with producing systems that have
the means to integrate ethical considerations. Our aim is thus to propose
systems that are able to learn to exhibit behaviours judged as ethical by humans,
both in situations of non-conflicting ethical stakes, but also in more complex
cases of dilemmas between moral values.

First, we propose a reinforcement learning algorithm, capable of learning to
exhibit behaviours incorporating these ethical considerations from a reward
function. The goal is to learn these ethical considerations in many situations
over time. A multi-agent framework is used, which allows on the one hand to
increase the richness of the environment, and on the other hand to offer a more
realistic simulation, closer to our intrinsically multi-agent human society, in
which these approaches are bound to be deployed.We are particularly interested
in the question of how agents adapt to changes, both to environmental dynamics,
such as seasonal changes, but also to variations in the ethical mores commonly
accepted by society.

Our second contribution focuses on the design of the reward function to guide
the learning of agents. We propose to integrate judging agents, based on
symbolic reasoning, tasked with judging learning agents' actions, and determining
their reward, relatively to a specific moral value. The introduction of multiple
judging agents makes the existence of multiple moral values explicit. Using
symbolic judgment facilitates the design by application domain experts, and
improves the intelligibility of the produced rewards, providing a window into
the motivations that learning agents receive.

Thirdly, we focus more specifically on the question of dilemmas. We take
advantage of the existence of multiple moral values and associated rewards to
provide information to the learning agents, allowing them to explicitly identify
those dilemma situations, when 2 (or more) moral values are in conflict and
cannot be satisfied at the same time. The objective is to learn, on the one hand,
to identify them, and, on the other hand, to decide how to settle them, according
to the preferences of the system's users. These preferences are contextualized,
i.e., they depend both on the situation in which the dilemma takes place, and on
the user. We draw on multi-objective learning techniques to propose an approach
capable of recognizing these conflicts, learning to recognize dilemmas that are
similar, i.e., those that can be settled in the same way, and finally learning
the preferences of users.

We evaluate these contributions on an application use-case that we propose,
define, and implement: the allocation of energy within a smart grid.

**Keywords**:
Machine Ethics &mdash;
Artificial Moral Agents &mdash;
Multi-Agent Systems &mdash;
Multi-Agent Reinforcement Learning &mdash;
Multi-Objective Reinforcement Learning &mdash;
Ethical Judgment &mdash;
Hybrid Neural-Symbolic Learning &mdash;
Moral Dilemmas &mdash;
Human Preferences


## Apprentissage de comportements alignés sur des valeurs morales dans un système multi-agent : guider l'apprentissage par renforcement avec des jugements symboliques

De nombreux systèmes d'IA sont déployés dans notre société, et ont un impact
sur des humains. Des questions se posent ainsi quant à leur capacité d'agir en
accord avec les valeurs (morales) qui nous semblent importantes. Dans cette thèse,
nous nous concentrons particulièrement sur le domaine de l'éthique computationnelle,
qui consiste à produire des systèmes ayant les moyens d'intégrer des considérations
éthiques. Notre but est ainsi de proposer des systèmes, qui soient capables
d'apprendre à exhiber des comportements jugés comme éthiques par les humains, à
la fois dans des situations ayant des enjeux éthiques non en conflit, mais aussi
dans les cas plus complexes de dilemmes entre les valeurs morales.

Premièrement, nous proposons un algorithme d'apprentissage par renforcement,
capable d'apprendre à exhiber des comportements intégrant ces considérations
éthiques à partir d'une fonction de récompense. Le but est ainsi d'apprendre
ces enjeux éthiques dans de nombreuses situations, au fil du temps. Un cadre
multi-agent est utilisé, ce qui augmente d'une part la richesse de
l'environnement, et d'autre part offre une simulation plus réaliste, plus proche
de notre société humaine, intrinsèquement multi-agent, et dans laquelle ces
approches sont vouées à être déployées. Nous nous intéressons particulièrement
à la question de l'adaptation des agents aux changements, à la fois aux
dynamiques de l'environnement, tels que les changements saisonniers, mais aussi
aux variations dans les mœurs éthiques couramment acceptées par la société.

Notre deuxième contribution se concentre sur la conception de la fonction de
récompense, afin de guider l'apprentissage. Nous proposons l'intégration d'agents
juges, se basant sur du raisonnement symbolique, chargés de juger les actions
des agents apprenants et déterminer leur récompense, relativement à une valeur
morale spécifique. L'introduction de multiples agents juges permet de rendre
explicite l'existence de multiples valeurs morales. L'utilisation de jugement
symbolique facilite la conception par des experts du domaine applicatif, et
permet d'améliorer l'intelligibilité des récompenses ainsi produites, ce qui
offre une fenêtre sur les motivations que reçoivent les agents apprenants.

Troisièmement, nous nous focalisons plus précisément sur la gestion des dilemmes.
Nous profitons de l'existence de multiples valeurs morales afin de fournir plus
d'informations aux agents apprenants, leur permettant ainsi d'identifier
explicitement ces situations de dilemme, lorsque 2 valeurs morales (ou plus)
sont en conflit et ne peuvent être satisfaites en même temps. L'objectif est
d'apprendre, d'une part à les identifier, et d'autre part à les trancher, en
fonction des préférences des utilisateurs et utilisatrices du système. Ces
préférences sont contextualisées, elles dépendent ainsi à la fois de la situation
dans laquelle se place le dilemme, et à la fois de l'utilisateur. Nous nous
inspirons des techniques d'apprentissage multi-objectif afin de proposer une
approche capable de reconnaître ces conflits, d'apprendre à reconnaître les
dilemmes qui sont similaires, autrement dit ceux qui peuvent être tranchés de
la même manière, et finalement d'apprendre les préférences des utilisateurs et
utilisatrices.

Nous évaluons ces contributions sur un cas d'application que nous proposons,
définissons et implémentons : la répartition d'énergie au sein d'une smart grid.

**Mots-clés** :
Éthique computationnelle &mdash;
Agents moraux artificiels &mdash;
Systèmes multi-agent &mdash;
Apprentissage par renforcement multi-agent &mdash;
Apprentissage par renforcement multi-objectif &mdash;
Jugement éthique &mdash;
Apprentissage hybride neuro-symbolique &mdash;
Dilemmes moraux &mdash;
Préférences humaines


## Compiling

`make pdf` produces the PDF file (single file) at `_book/thesis.pdf`

`make gitbook` produces a HTML book (multiple files) at `_book/gitbook/index.html`

`make all` produces both the PDF and HTML book at `_book/all/{index.html,thesis.pdf}`

`make serve` can be used to live preview the modifications. The thesis will be
built at `_book/serve/` (similar to the `gitbook` format), and re-built each
time a file is modified. The book can be previewed using either the RStudio
Viewer, or any Web browser (the URL of the server is displayed in the console).

## Requirements

A Python virtual environment must be installed in a `.venv` folder, at this
project's root.
The virtualenv must contain the libraries listed in `python-requirements.txt`, 
e.g., by using `pip install -r python-requirements.txt`.
To avoid using a virtual env, comment the line 
`reticulate::use_virtualenv(file.path(getwd(), ".venv"))` in the `setup`
chunk of `index.Rmd`. However, the `reticulate` library **must** find a
Python version with the required libraries, otherwise the book cannot be
produced.

## Citing

Please cite this work using the following BibTeX entry:

```bibtex
@phdthesis{chaput2022thesis,
  author  = "Chaput, Rémy",
  title   = "Learning behaviours aligned with moral values in a multi-agent system: guiding reinforcement learning with symbolic judgments",
  school  = "Université Claude Bernard Lyon 1",
  year    = "2022"
}
```
