# Caesar Cipher

<hr />

## Background
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 

It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 

For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 

The method is named after Julius Caesar, who used it in his private correspondence.

<br>

## Instructions
Inside the file, you'll use three lists already saved to a corresponding variable: ```alphabet```.
```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

<br>

## Example Input 1
```
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
```
```
Type your message:
hello
```
```
Type the shift number:
3
```

## Example Output 1
```
Here's the encodeed result: khoor
Type 'yes' if you want to go again. Otherwise type 'no'.
```

## Example Input 2
```
yes
```
Or
```
no
```

## Example Output 2
```
Type 'encode' to encrypt, type 'decode' to decrypt:

< ... continue >
```

Or

```
Goodbye
```

<br>

## And vice versa
```
Type 'encode' to encrypt, type 'decode' to decrypt:
decode
```
```
Type your message:
khoor
```
```
Type the shift number:
3
```

<br>

```
Here's the encodeed result: hello
Type 'yes' if you want to go again. Otherwise type 'no'.
```

<br>

## More Advanced
Also, a shift number, 100 or -100, is available.  