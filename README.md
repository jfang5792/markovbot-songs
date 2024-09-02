## It Ends With Us - Markov Chains

Generate 'It Ends with Us' film soundtrack song excerpts by modeling Markov chains with a script to Discord API wrapper library

https://github.com/user-attachments/assets/e3df1c9e-358c-45b2-a52f-e94f416d0d3c

### Future Development

- The longer the sequence of words to the left of the arrow, the closer it becomes to the original text, as well as valid English, because there are fewer and fewer random successors. Bigrams (word pairs) and a successor, but try trigrams or n-grams (sequences of n words). The longer the n-gram, the closer to the source text.

- Modify the program to allow any number of words to use as keys so you can easily choose the size of your n-gram used in your chain rather than always using bi-grams.

- Begin on a capital letter and end only at an instance of sentence punctuation.

- See what happens when you mix two different authors together as a single source. This often works best when they have somewhat similar writing styles; trying to combine Dr. Seuss and the Bible probably wouldn’t work as well as combining two Jane Austen books.
