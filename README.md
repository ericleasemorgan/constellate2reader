# JSTOR Constellate to Distant Reader

The Python script in this distribution reads JSONL files from JSTOR's [Constellate](https://constellate.org) platform, and outputs a zip file suitable for input to the [Distant Reader](https://distantreader.org).


## Quick start

   ``python constellate2reader.py thoreau.jsonl thoreau``

The result ought to include a file named thoreau.zip which can be submitted to the Distant Reader at [https://distantreader.org/create/zip2carrel](https://distantreader.org/create/zip2carrel).


## Usage

   1. Use Constellate to search JSTOR's collection. Do what ever sort of search you desire, but be sure to limit Download Availability to "Full text only". While this is not necessary, ``constellate2reader.py`` will only extract full text items from your dataset.
   
   2. Submit your dataset for building and wait patiently.
   
   3. When you dataset is finished building, download the whole of the dataset, not just the sampled data. The result ought to be a file with a long, ugly-looking name with a ``.jsonl`` file extension.
   
   4. As per above, use ``constellate2reader.py`` where the first argument is the name of the ``.jsonl`` file, and the second argument is the name of a directory where the full texts (and their associated metadata.csv file) are to be saved.
   
   5. The result ought to be a ``.zip`` file, and you can use it as input to the Reader.

## Discussion

The purpose of this script is build upon -- not replace -- the good work of Constellate. Given a corpus, a system called the Distant Reader is capabile of extracting parts-of-speech, named-entities, noun phrases, and even sentences matching a select number of grammars from a text. These sorts of things are not possible sans full text. Within the limitations of JSTOR's license agreements, some full texts are available. The script ``constellate2reader.py`` takes advantage of this fact and enables the student, researcher, or scholar to create a corpus of full text, and use the Reader to go to another level when it comes to reading a body of literature.

This distribution was written in a fit of creativity, which happens to me often. I'm sure there are some errors. When you find them, please bring them to my attention.

---
Eric Lease Morgan &lt;emorgan@nd.edu&gt;  
September 1, 2021

