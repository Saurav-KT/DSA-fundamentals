### Making Words (asked in Fractal Analytics)

Write a function which accepts 2 arguments - one string value called word and another string array called arr.
The function should either return true or false based on whether the word can be made by arranging elements from the arr.

A few things to keep in mind -
Elements from the arr can occur in any order
Elements can be repeated

Examples:

```arr = ["hello", "world", "po", "pu", "lar"]

word = "helloworld";                            // true
word = "worldhello":                            // true
word = "helloworldlar"                          // true
word = "popopopopopopopopolarlarworldlarhello"  // true

word = "hello world"                            // false
word = "helloworld!"                            // false```
