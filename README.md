# dollarstreet-deeplearning

Analyzing the dollarstreet images from gapminder using deep learning.

The .txt files in the metadata folder were scraped from the dollarstreet website:

```
https://www.gapminder.org/dollar-street/matrix
```

Using the javascript console in a web browser I ran the following code and saved the console output to a text file.

```javascript
$(".cell-inner").each((index, element) => {
    console.log(element.style.backgroundImage)
    value_span = $(element).find(".place-image-box-income")
    console.log(value_span.text())
    console.log(index)
```

To regenerate the `data.tsv` file you can run the `generate_tsv.py` script (expects to be run with python 3.6+):

```
$ cd metadata
$ python generate_tsv.py *.txt
```

To download the data just run the script:

```
$ scripts/download
```
