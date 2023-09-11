# Ladino Rashi

An implementation of a transcriber for Ladino text between latin letter ortography and Rashi script.

* Create a set of test cases in a yaml file (mapping words in latin letters and words in hebrew letters)
* Use the yaml to generate a web page where people can see latin letters, Rashi, and squared hebrew letters to verify the mapping.
* Create a page where peole can type in hebrew letters and see the text in Rashi - so they can send me more examples for the YAML file.


* Write a two-way converter in JavaScript using the YAML file as test cases.
* Write a two-way converter in Python using the YAML file as test cases.

* [Rashi script](https://en.wikipedia.org/wiki/Rashi_script)

## Development Environment

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

```
python generate.py
```
