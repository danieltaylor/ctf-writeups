# Stone Moon


## Challenge

I came across this malicious code, but I'm not quite sure what language it's written in... can you help me?

[stone.txt](./stone.txt)


## Solution

I started by taking a look at [stone.txt](./stone.txt), which appears as follows:

```
Let tanner be 15
Let cougar be 14
Let kevin be 12
Let cosmo be 13
Let byu be 16
Let getrektathirdtime be 10
Let the flag be "abcfgkorstuy0{}_!"
Let ian be 2
Let albert be 0
Let kate be 7
Let anna be 6
Let ctf be 17
Let justin be 3
Let bet be 11
Let derek be 5
Let micheal be 4
Let getrektagain be 9
Let your basement be 1
Let getrekt be 8
Let your face be the flag at bet
Let my mom be the flag at getrektathirdtime
Let my love be the flag at ian
Let your favorite be the flag at justin
Let getrickrolled be the flag at getrektagain
Let your mom be the flag at your basement
Shout your mom
Shout your face
Shout my mom
Shout my love
Shout getrickrolled
Shout your favorite
Shout the flag at cosmo
Shout the flag at micheal
Shout the flag at anna
Shout the flag at tanner
Shout the flag at kate
Shout the flag at kevin
Shout the flag at ian
Shout the flag at derek
Shout the flag at getrekt
Shout the flag at getrektagain
Shout the flag at albert
Shout the flag at kate
Shout the flag at byu
Shout the flag at cougar
```

A good approach to CTF problems usually starts with considering whether you've run across anything similar in the past.  This challenge reminded me of [Kattis's Metaprogramming challenge](https://open.kattis.com/problems/metaprogramming).  For the Kattis problem, it was necessary to write an interpreter for the language since the input could change.  In this situation, we only have to deal with one set input, so this problem should be a piece of cake!

Rather than try to write an interpreter for this new language, I instead elected to simply treat it as pseudocode and translate it into actual code (with the assistance of find-and-replace of course).

These are the changes I applied in order to convert [stone.txt](./stone.txt) into [stone.py](./stone.py):

- remove `Let `
- replace ` be ` with ` = `
- replace spaces in variable names with `_`
- replace ` at variable_name` with `[variable_name]`
- replace ` Shout variable_name[optional]` with `print(variable_name[optional], end = '')`

Applying all of these changes results in the following, which reveals the flag when run!

```python
tanner = 15
cougar = 14
kevin = 12
cosmo = 13
byu = 16
getrektathirdtime = 10
the_flag = "abcfgkorstuy0{}_!"
ian = 2
albert = 0
kate = 7
anna = 6
ctf = 17
justin = 3
bet = 11
derek = 5
micheal = 4
getrektagain = 9
your_basement = 1
getrekt = 8
your_face = the_flag[bet]
my_mom = the_flag[getrektathirdtime]
my_love = the_flag[ian]
your_favorite = the_flag[justin]
getrickrolled = the_flag[getrektagain]
your_mom = the_flag[your_basement]
print(your_mom, end='')
print(your_face, end='')
print(my_mom, end='')
print(my_love, end='')
print(getrickrolled, end='')
print(your_favorite, end='')
print(the_flag[cosmo], end='')
print(the_flag[micheal], end='')
print(the_flag[anna], end='')
print(the_flag[tanner], end='')
print(the_flag[kate], end='')
print(the_flag[kevin], end='')
print(the_flag[ian], end='')
print(the_flag[derek], end='')
print(the_flag[getrekt], end='')
print(the_flag[getrektagain], end='')
print(the_flag[albert], end='')
print(the_flag[kate], end='')
print(the_flag[byu], end='')
print(the_flag[cougar], end='')
```
