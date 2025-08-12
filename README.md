# PapyriBot – ULMFit-based Ancient Greek Text Generator

## The complete codebase, along with the technologies used, is available by request — feel free to contact me for access and collaboration opportunities.

## Overview

This project involved the design and training of a language model from scratch using the ULMFit (Universal Language Model Fine-tuning) architecture, following the methodology developed by [Jeremy Howard](https://docs.fast.ai/tutorial.text.html). The objective was to generate plausible ancient Greek documentary text from a curated corpus of papyri. The project was developed collectively as one of the technical demonstrations presented by the Lab-HD during the Madrid Science Week (IFEMA), as part of the CSIC’s science communication activities.

## Corpus

The dataset was extracted from the [Duke Collaboratory for Classics Computing (DC3)](https://papyri.info/browse/ddbdp/), using TEI `.xml` transcriptions available on [GitHub](https://github.com/papyri/idp.data/tree/master/DDB_EpiDoc_XML). These texts are documentary in nature — administrative, legal, and epistolary — not literary.

The initial conversion to `.txt` and cleaning was carried out by **Sabine Arnaud-Thuillier** (Lab-HD technician), preserving editorial tags that reflect omitted, damaged, added, or illegible segments due to papyrus deterioration or scribal corruption.

## Preprocessing

After obtaining the raw files, **Nadège Rollet**, **Sabine**, and I performed a second round of deep cleaning using regular expressions (Regex) and the NLTK library. I wrote Python scripts to process the dataset, enabling effective tokenization and use as training material in machine learning workflows.

This initial training phase focused on capturing semantic, syntactic, and morphological relationships specific to ancient Greek documentary papyri.

## My Role

I worked primarily on the **preprocessing, dataset encoding**, and **training** phases of the model:

- Tokenization and creation of training and validation datasets.
- Configuration of the learner and encoder using `fast.ai`.
- Management of training stages: callbacks, learning rates, layer freezing.
- Hyperparameter tuning to balance semantic accuracy with linguistic complexity.

The model was trained in a high-performance GPU environment (NVIDIA), supported by Lab-HD infrastructure.

## Output Demo

While Nadège designed the LED panels and user interface shown at the Science Fair, my contribution ensured that the trained model could dynamically generate textual output based on one or more seed words. This demonstrated how a model trained only on documentary Greek could reproduce stylistically and grammatically plausible sentence structures.

## Team

The project was developed by:

- Nadège Rollet (Project Lead)
- Sabine Arnaud-Thuillier
- María Isabel Cobos
- Javier de la Rosa (myself)

It integrated computational linguistics, Python programming, machine learning, and open science principles.

## Outcomes

From both a technical and academic perspective, this project allowed me to:

- Understand the full pipeline of creating and training a generative AI model.
- Collaborate with diverse technical profiles using reproducible, modular code.
- Contribute to a science communication initiative using AI in the digital humanities.

## Next Steps

The project is currently **on hold**, pending a **second phase** aimed at fine-tuning the model for editorial variant classification. This next step will rely on a **MongoDB**-based database with annotated editorial interventions (e.g., omissions, additions, conjectures). The ultimate goal is to specialize this pre-trained model into a classifier capable of identifying unmarked editorial variants — paving the way for automated critical edition workflows of ancient texts.
