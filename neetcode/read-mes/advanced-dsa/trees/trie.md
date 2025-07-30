## trie
let's give some motivation behind why we need a trie.

imagine we had a big box filled with different vegetables like cucumbers, cauliflower, tomatoes etc. if we wanted to 
organize them by their name, we would want to start by getting smaller boxes and label each one of the boxes with each
letter of the alphabet. so all the vegetables that start with `"A"` will go into the box labelled `"A"`, so on and so
forth.

but, there are vegetables that share a first letter or even first few characters such as `"cauliflower"` and `"cabbage"`. 
instead of creating new boxes for every prefix, we can create new boxes inside our original box such that each new box 
is used to denote each additional letter in our vegetable's name.

so now that we have extra boxes inside, say, `"c"` box, labelled with the second letter of each vegetable's name, we 
can now put `"cauliflower"` and `"cabbage"` in the same box and so on and so forth. we can keep doing this for each 
letter of the alphabet, until we have a bunch of smaller boxes inside bigger boxes.

a trie allows us to organize words based on the first few characters (prefix). in the case of a trie, each vegetable 
box will be represented as a node and the edges are used to represent the characters that connect them.

a trie, often referred to as a prefix tree, as that explains its purpose better, is a tree data structure that can be 
used to find words, given a prefix. It can do so in `O(w)` time, where `w` is the length of the word. this is because 
we only need to traverse the trie for each character in the word.

one real-world application of tries is **search auto-completion**. autocomplete matches the prefix characters to predict
the word or phrase you are going to type. and since searching a prefix is `O(w)`, it is fast and efficient.

## time complexities
the brute-force way of performing search, if we did not have a prefix tree, would be to iterate over all the words and 
check which ones match. This gives us a time complexity of `O(n * m)`, where `n` is the number of words and `m` is the 
average length of each word.

tries allow us to do it in `O(m)` time. this is because we iterate a single time for each character in the target word.

we want to be able to insert, search, such that we have the following complexities:

- insert word: `O(w)`
- search word: `O(w)`
- search prefix: `O(w)`