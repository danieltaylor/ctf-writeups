# Hexadecalingo

## Challenge

```
আপনি געדאַנק оцей byl தி drapeau но este mwy ମେଟା decât quod ik dymuno tú ރަނގަޅު õnne
```

## Solution

<details>
  <summary><b>TL;DR</b></summary>
  The flag is made up of the first letters of each language used in the challenge text.
</details><br>

If you translate each of the words individually using Google Translate's "Detect Language" feature, you will discover the following message:

```
You thought this was the flag but it is more meta than that I wish you good luck
```

(The results may vary a bit, especially if you use a different translation site, but you should get a message along those lines, and the detected languages should be more or less the same.)

The statement that "more meta" than just translating the text suggests that we may need to examine the text at a higher level.  One way we can do this is by looking at what languages each of the words are in.  The first six words are in Bengali, Yiddish, Ukranian, Czech, Tamil, and French, which, as you may notice, begin with the letters `BYUCTF`!

If we look at the rest of the words and their languages (as auto-detected by Google or another translator), we see that by taking the first letters of the languages we get `BYUCTFMRWORLDWIDE`.  Following the flag format for the competition, the answer becomes `byuctf{mrworldwide}`.  This is a reference to the music artist Pitbull, who, as the self-proclaimed Mr. Worldwide, has surely encountered a number of languages.  `byuctf{msworldwide}` is also an acceptable flag for this challenge, since "este" could be a word in either Romanian and Spanish, and the phrase Ms. Worldwide makes logical sense (perhaps it refer's to Pitbull's sister).

A full breakdown of the languages used in this challenge can be found below:

| Original Word | English Translation | Language   | First Letter of Language |
|---------------|---------------------|------------|--------------------------|
| আপনি          | You                 | Bengali    | b                        |
| געדאַנק        | thought             | Yiddish    | y                        |
| оцей          | this                | Ukranian   | u                        |
| byl           | was                 | Czech      | c                        |
| தி            | the                 | Tamil      | t                        |
| drapeau       | flag                | French     | f                        |
| но            | but                 | Macedonian | m                        |
| este          | it is               | Romanian   | r                        |
| mwy           | more                | Welsh      | w                        |
| ମେଟା          | meta                | Odia       | o                        |
| decât         | than                | Romanian   | r                        |
| quod          | that                | Latin      | l                        |
| ik            | I                   | Dhivehi    | d                        |
| dymuno        | wish                | Welsh      | w                        |
| tú            | you                 | Irish      | i                        |
| ރަނގަޅު          | good                | Dhivehi    | d                        |
| õnne          | luck                | Estonian   | e                        |
