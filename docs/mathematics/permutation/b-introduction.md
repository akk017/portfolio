---
title: Introduction to Permuation
icon: fa-hashtag
---

Given A 4 Letter Word ex. ROSE, all ways that letters that jumbled to form meaningless words are
ROES, RSOE, REOS ... EOSR. In order to find the number of possible arrangements, we use tool called _**Permutation**_.


### 6.3.1 Permuataion where all objects are distinct

**Theorem 1** The number of permutations of $n$ different objects taken $r$ at time, where $0 < r < n$ and objects do not repeat is $(n-1)(n-2) ... (n-r+1)$ which is denoted by ${}^{n}P_{r}$

**Proof** There will be many permuations filling $r$ vancant spaces by $n$ objects. The first place can filled with $n$ ways, secondy place be $n-1$ and so on, the $r^{\text{th}}$ place be $(n - (r-1))$. Therefore, the number of
ways of filling in $r$ vacant places in succession is $(n)(n-1)(n-2) ... (n - r + 1)$.

Similyfying ${}^{n}P_{r}$

$$
{}^{n}P_{r} = \frac{n!}{(n - r)!}
$$

$$
{}^{n}P_{r} =
\begin{cases}
n!, & \text{if } n = r \\
\frac{n!}{(n - r)!}, & \text{else } r < n
\end{cases}
$$

**Theorem 2** Similarly, The number of permutations of n different objects taken r at a time,
where repetition is allowed, is ${n}^{r}$

### 6.3.4 Permutations when all the objects are not distinct objects

Suppose we have to find the number of ways of rearranging the letters of the word ROOT. There are 2 Os, which are of the same kind. Let us treat, temporarily, the 2 $O$ s as different, say, $O_{1}$ and $O_{2}$.

The number of permutations of 4-different letters, in this case, taken all at a time is $4!$.
The number of permutation of 2-apparently-different letters, in this 2 $O$ s, is $2!$, ie, $O_{1}O_{2} O_{2}O_{1}$, all its arrangement are same.

Therefore, the required number of permutataion are = $\frac{4!}{2!} = 12$.

**Theorem 3** The number of permutation of n objects taken n time given p of them are same, then the number of permutations are
$\frac{n!}{p!}$

**Theorem 4** The number of permutations of n objects, where $p_{1}$ objects are of one kind, $p_{2}$ are of second kind, ..., pk are of $k_{th}$ kind and the rest, if any, are of different kind is

$$
\frac{n!}{p_1!p_2!...p_k!}
$$

**Example 14** Find the number of different 8-letter arrangements that can be made from the word $\text{DAUGHTER}$ so that

$$
\text{(i) All vowels are together} \;\;\; \text{(ii) All vowels are not togther}
$$

**Solution**

(i) There are 8 different letter in word $DAUGHTER$, which 3 Vowels $AEU$, For Time Assume, $AUE$ as single letter, so the number of permuation of 6 Letter would be ${}^{6}P{_6} = 6!$ and the number of combination that $AUE$ can rearranged are
${}^{3}P_3 = 3!$. So cummlilative number of permuation given vowels are together are $6! \times 3! = 4320$