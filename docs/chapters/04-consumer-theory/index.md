# Chapter 4: Consumer Theory

## Learning Objectives

After completing this chapter, you will be able to:

1. Distinguish between total utility and marginal utility, and compute both from a utility schedule
2. Explain and apply the law of diminishing marginal utility
3. Use the equal marginal principle to find a consumer's utility-maximizing bundle of goods
4. Construct and interpret a budget constraint, and explain how price and income changes affect it
5. Read and interpret indifference curves and compute the marginal rate of substitution
6. Find the consumer optimum using the tangency condition and explain why it maximizes utility
7. Decompose a price change into income and substitution effects
8. Explain how the consumer's utility-maximizing choices at different prices generate the market demand curve

---

!!! mascot-welcome "Where Does Demand Really Come From?"
    ![Professor Owl waving hello](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    We've been treating the demand curve as a given fact since Chapter 2 — now we build it from scratch, starting with a single consumer deciding how to spend a limited budget. By the end, you'll see the law of demand isn't an assumption; it's a conclusion. Every choice has a trade-off, and this chapter is about how people make that trade-off rationally.

## 4.1 From Market Demand to Individual Choice

Chapter 2 introduced the demand curve as a market-level relationship between price and quantity demanded. But *why* does an individual consumer buy less of a good when its price rises? **Consumer theory** answers this question by modeling how a rational, self-interested consumer with limited income chooses among goods to make themselves as well off as possible. This chapter builds the micro-foundations of the demand curve from the ground up: first using the simpler language of utility, then using the more general and powerful tool of indifference curves.

---

## 4.2 Total and Marginal Utility

**Utility** is a numerical measure of the satisfaction or happiness a consumer derives from consuming goods and services. **Total utility** ($TU$) is the overall satisfaction from consuming a given quantity of a good. **Marginal utility** ($MU$) is the *additional* utility gained from consuming one more unit:

$$MU_n = TU_n - TU_{n-1}$$

!!! example "Utility schedule for slices of pizza"
    | Slices of Pizza | Total Utility | Marginal Utility |
    |---|---|---|
    | 0 | 0 | — |
    | 1 | 20 | 20 |
    | 2 | 36 | 16 |
    | 3 | 48 | 12 |
    | 4 | 56 | 8 |
    | 5 | 60 | 4 |
    | 6 | 60 | 0 |
    | 7 | 56 | −4 |

    Total utility rises with each additional slice up through slice 6, then falls — the 7th slice makes the consumer feel sick, generating *negative* marginal utility.

---

## 4.3 The Law of Diminishing Marginal Utility

**The Law of Diminishing Marginal Utility:** As a consumer consumes more units of a good within a given period, the marginal utility from each additional unit eventually decreases, holding consumption of other goods constant.

In the pizza example, marginal utility falls steadily from 20 (first slice) to 4 (fifth slice) before turning negative. This pattern — not total utility rising, but the *increments* getting smaller — is the single most important building block of consumer theory. It explains why consumers typically diversify their consumption across many goods rather than spending their entire income on one good: the tenth unit of anything is worth less to the consumer than the first.

!!! note "Diminishing marginal utility vs. negative marginal utility"
    Diminishing marginal utility simply means each additional unit adds *less* satisfaction than the last — marginal utility is still positive, just declining. Marginal utility only becomes *negative* when consuming more actually makes the consumer worse off (e.g., overeating).

!!! mascot-thinking "Why Diminishing Returns Shapes Everything"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    This is the single idea the rest of the chapter builds on: because each extra unit satisfies you less, you naturally spread your budget across many goods instead of binging on one. Keep this in the back of your mind as indifference curves and tangency conditions get more abstract.

---

## 4.4 Utility Maximization: The Equal Marginal Principle

A consumer with a fixed income and two goods ($X$ and $Y$) maximizes total utility by allocating their budget so that the **marginal utility per dollar** spent is equal across all goods:

$$\frac{MU_x}{P_x} = \frac{MU_y}{P_y}$$

subject to the budget constraint $P_x X + P_y Y = I$, where $I$ is income.

**Intuition:** If $\frac{MU_x}{P_x} > \frac{MU_y}{P_y}$, the consumer gets more "bang for the buck" from good $X$. They should buy more $X$ and less $Y$ — shifting spending toward $X$ raises total utility, until the marginal utilities per dollar are equalized.

!!! example "Equal marginal principle: numerical example"
    A consumer has \$10 to spend on candy bars ($P_x = \$2$) and sodas ($P_y = \$1$). Her marginal utility schedule:

    | Units | $MU_x$ (candy) | $MU_x/P_x$ | $MU_y$ (soda) | $MU_y/P_y$ |
    |---|---|---|---|---|
    | 1 | 20 | 10 | 14 | 14 |
    | 2 | 16 | 8 | 12 | 12 |
    | 3 | 12 | 6 | 10 | 10 |
    | 4 | 8 | 4 | 8 | 8 |
    | 5 | 4 | 2 | 6 | 6 |

    To maximize utility, the consumer buys units in order of highest $MU/P$ until the \$10 budget is exhausted: soda #1 (14), candy #1 (10), soda #2 (12), soda #3 (10, tie with candy #1 already bought — continue), candy #2 (8), soda #4 (8). Tracking spending: soda×4 = \$4, candy×2 = \$4, totaling \$8 spent on 6 units... Continuing to allocate the remaining \$2 to the next-highest ratios yields a bundle where $MU_x/P_x = MU_y/P_y$ at the margin — in this schedule, 2 candy bars and 4 sodas spend $2(2) + 1(4) = \$8$, and the next dollar gives equal marginal utility per dollar (4 and 6 respectively) from either additional good, with remaining funds pushing toward soda #5 and candy #3 until the ratios converge near 6.

    The key takeaway is procedural: **rank purchases by $MU/P$, not by $MU$ alone**, and keep buying the next-best-value unit until the budget runs out.

---

## 4.5 Budget Constraints

The **budget constraint** shows all combinations of two goods a consumer can afford given their income and the goods' prices:

$$P_x X + P_y Y = I$$

Solving for $Y$ gives the equation of the **budget line**:

$$Y = \frac{I}{P_y} - \frac{P_x}{P_y}X$$

The vertical intercept ($I/P_y$) is the maximum amount of $Y$ affordable (if all income is spent on $Y$); the horizontal intercept ($I/P_x$) is the maximum amount of $X$ affordable. The slope, $-P_x/P_y$, is the **opportunity cost** of $X$ in terms of $Y$ — how much $Y$ must be given up to buy one more unit of $X$.

!!! example "Budget line example"
    Income $I = \$100$, $P_x = \$5$ (movies), $P_y = \$2$ (snacks).

    $$Y = \frac{100}{2} - \frac{5}{2}X = 50 - 2.5X$$

    If the consumer buys 0 movies, they can afford 50 snacks. If they buy 20 movies, they can afford 0 snacks. The slope is $-2.5$: each additional movie costs 2.5 snacks in forgone consumption.

### Shifts of the Budget Line

- **Income increases:** The budget line shifts **outward** (parallel shift), since both intercepts increase proportionally.
- **Income decreases:** The budget line shifts **inward** (parallel shift).
- **Price of $X$ falls:** The horizontal intercept ($I/P_x$) increases; the line **rotates outward** around the vertical intercept, becoming flatter.
- **Price of $X$ rises:** The horizontal intercept decreases; the line **rotates inward**, becoming steeper.

---

## 4.6 Indifference Curves and the Marginal Rate of Substitution

An **indifference curve** shows all combinations of two goods that give the consumer the *same* level of total utility. The consumer is, by definition, indifferent between any two bundles on the same curve.

### Properties of Indifference Curves

1. **Downward sloping:** To keep utility constant while consuming more of one good, the consumer must give up some of the other.
2. **Convex to the origin (bowed inward):** This reflects a diminishing willingness to trade one good for another as more of it is consumed.
3. **Higher curves represent higher utility:** A consumer prefers any bundle on a curve farther from the origin.
4. **Curves do not intersect:** If they did, it would imply inconsistent preferences.

### The Marginal Rate of Substitution

The **marginal rate of substitution** ($MRS$) is the rate at which a consumer is willing to trade one good for another while remaining equally satisfied — it is the (absolute value of the) slope of the indifference curve:

$$MRS_{xy} = -\frac{\Delta Y}{\Delta X}\bigg|_{\text{along indifference curve}} = \frac{MU_x}{MU_y}$$

Because of diminishing marginal utility, $MRS$ **diminishes** as the consumer moves down an indifference curve (substituting more $X$ for $Y$) — this is the **law of diminishing marginal rate of substitution**, and it is what gives indifference curves their characteristic convex (bowed-in) shape.

!!! example "Diminishing MRS"
    Starting with 1 movie and 20 snacks, a consumer might willingly give up 8 snacks for a 2nd movie ($MRS = 8$). But starting with 4 movies and 4 snacks, she might only give up 1 snack for a 5th movie ($MRS = 1$) — movies have become relatively abundant, snacks relatively scarce, so she is far less willing to sacrifice additional snacks.

!!! mascot-tip "MRS Is Just a Ratio"
    ![Professor Owl sharing a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    No graph needed to find MRS — it's just $MU_x/MU_y$. If a problem hands you marginal utilities, you already have the slope of the indifference curve at that point.

---

## 4.7 Consumer Optimum: The Tangency Condition

The **consumer optimum** is the bundle of goods that maximizes utility subject to the budget constraint. Graphically, it occurs where the **budget line is tangent to the highest attainable indifference curve** — the point where the budget line just touches, but does not cross, an indifference curve.

At this tangency point, the slope of the indifference curve equals the slope of the budget line:

$$MRS_{xy} = \frac{P_x}{P_y} \quad \Longleftrightarrow \quad \frac{MU_x}{MU_y} = \frac{P_x}{P_y} \quad \Longleftrightarrow \quad \frac{MU_x}{P_x} = \frac{MU_y}{P_y}$$

This confirms that the tangency condition is mathematically identical to the equal marginal principle from Section 4.4 — two different ways of describing the same utility-maximizing condition.

!!! tip "Why not buy more of the good with higher MRS relative to price ratio?"
    If $MRS_{xy} > P_x/P_y$, the consumer values an extra unit of $X$ (in terms of $Y$) more than the market requires her to sacrifice. She should buy more $X$ and less $Y$, increasing utility, until the two ratios are equalized at the tangency point.

!!! mascot-encourage "Partial Derivatives, One Variable at a Time"
    ![Professor Owl giving encouragement](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    Taking $MU_x$ and $MU_y$ from a utility function like $U=XY$ looks intimidating, but it's just ordinary differentiation treating the other variable as a constant. Work through the steps below slowly the first time — it gets mechanical fast.

### Worked Example: Finding the Consumer Optimum

Suppose a consumer's utility function is $U(X,Y) = XY$, income is $I = \$120$, $P_x = \$4$, and $P_y = \$6$.

**Step 1:** Compute marginal utilities: $MU_x = Y$, $MU_y = X$ (partial derivatives of $U = XY$).

**Step 2:** Apply the tangency condition:

$$\frac{MU_x}{MU_y} = \frac{P_x}{P_y} \implies \frac{Y}{X} = \frac{4}{6} \implies Y = \frac{2}{3}X$$

**Step 3:** Substitute into the budget constraint:

$$4X + 6Y = 120 \implies 4X + 6\left(\frac{2}{3}X\right) = 120 \implies 4X + 4X = 120 \implies X^* = 15$$

$$Y^* = \frac{2}{3}(15) = 10$$

**Check:** $4(15) + 6(10) = 60 + 60 = 120$. ✓ The optimal bundle is **15 units of $X$ and 10 units of $Y$**.

---

## 4.8 Income and Substitution Effects

When the price of a good changes, the total change in quantity demanded can be decomposed into two distinct effects:

| Effect | Definition |
|---|---|
| **Substitution effect** | The change in quantity demanded due *only* to the change in relative prices, holding the consumer's utility (satisfaction) constant |
| **Income effect** | The change in quantity demanded due to the change in **real purchasing power** caused by the price change, holding relative prices constant |

**Total effect = Substitution effect + Income effect**

!!! mascot-warning "Don't Assume the Income Effect Always Shrinks Demand"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    It's tempting to think the income effect always works against the substitution effect, but that's only true for inferior goods. For a normal good, both effects push quantity demanded in the *same* direction.

When the price of a good *falls*:

- **Substitution effect:** The good becomes relatively cheaper compared to other goods, so the consumer substitutes toward it. This effect is always in the direction of buying **more** of the good whose price fell.
- **Income effect:** The price decrease increases the consumer's real purchasing power (effectively like a raise in income). For a **normal good**, higher real income increases quantity demanded (reinforcing the substitution effect). For an **inferior good**, higher real income decreases quantity demanded (working against the substitution effect).

| Good Type | Substitution Effect (price ↓) | Income Effect (price ↓) | Net Effect |
|---|---|---|---|
| **Normal good** | Quantity ↑ | Quantity ↑ | Quantity ↑ (law of demand holds) |
| **Inferior good** | Quantity ↑ | Quantity ↓ (but smaller) | Quantity ↑ overall (law of demand still holds) |
| **Giffen good** (rare) | Quantity ↑ | Quantity ↓ (dominates) | Quantity ↓ overall (law of demand violated) |

!!! warning "Giffen goods are a theoretical curiosity"
    A **Giffen good** is an extreme case of an inferior good where the negative income effect is so strong it overwhelms the substitution effect, causing quantity demanded to *fall* when price falls — violating the law of demand. Documented Giffen goods are exceedingly rare (some studies point to staple foods like rice or bread among very poor households); nearly all real-world goods obey the law of demand.

!!! example "Graphical decomposition (verbal walkthrough)"
    Suppose the price of bus fare falls. Graphically:
    1. The budget line rotates outward (pivoting on the $Y$-axis intercept, since only $P_x$ changed).
    2. Draw a hypothetical budget line parallel to the *new* budget line, but tangent to the *original* indifference curve — this isolates the substitution effect (same utility, new relative prices). The movement from the original optimum to this hypothetical point is the substitution effect.
    3. The movement from this hypothetical point to the final optimum on the new, higher indifference curve is the income effect.

---

## 4.9 Deriving the Demand Curve from Consumer Theory

Consumer theory lets us derive the market demand curve directly from utility maximization. Holding income and the price of $Y$ fixed, we can trace out the consumer's optimal quantity of $X$ at each possible price of $X$:

1. Start at the consumer optimum for a given $P_x$.
2. Lower $P_x$ — the budget line rotates outward, generating a new tangency point with a higher indifference curve, and (for a normal good) a higher optimal quantity of $X$.
3. Repeat for several prices and plot each price against the corresponding optimal quantity.
4. The resulting locus of points **is** the individual's demand curve for $X$.

This is why the demand curve slopes downward for ordinary (non-Giffen) goods: at every price, the consumer re-optimizes using the tangency condition, and for normal and most inferior goods, a lower price leads to a higher quantity demanded via the combined substitution and income effects.

!!! note "From individual to market demand"
    The market demand curve is the **horizontal summation** of all individual consumers' demand curves — at each price, add up the quantity demanded by every consumer in the market.

---

## Key Terms

| Term | Definition |
|---|---|
| **Utility** | A numerical measure of satisfaction a consumer derives from consumption |
| **Total Utility** | The overall satisfaction from a given quantity of consumption |
| **Marginal Utility** | The additional utility from consuming one more unit of a good |
| **Law of Diminishing Marginal Utility** | Marginal utility decreases as more units of a good are consumed, holding other consumption constant |
| **Equal Marginal Principle** | Utility is maximized when marginal utility per dollar is equal across all goods |
| **Budget Constraint** | The set of all bundles of goods a consumer can afford given income and prices |
| **Indifference Curve** | A curve showing all bundles of goods that yield the same total utility |
| **Marginal Rate of Substitution (MRS)** | The rate at which a consumer will trade one good for another while holding utility constant; equals $MU_x/MU_y$ |
| **Consumer Optimum** | The utility-maximizing bundle, found where the budget line is tangent to the highest attainable indifference curve |
| **Tangency Condition** | $MRS_{xy} = P_x/P_y$; the condition defining the consumer optimum |
| **Substitution Effect** | The change in quantity demanded from a price change, holding utility constant |
| **Income Effect** | The change in quantity demanded from the change in real purchasing power caused by a price change |
| **Giffen Good** | A good for which quantity demanded falls when price falls, violating the law of demand |

---

## Practice Problems

### Problem 1 — Total and Marginal Utility

A consumer's total utility from consuming cups of coffee is given below:

| Cups | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Total Utility | 0 | 30 | 54 | 72 | 84 | 90 |

**a)** Calculate the marginal utility of each cup.  
**b)** Does this schedule display diminishing marginal utility? Explain.  
**c)** At what point (if shown) would marginal utility become negative, based on the pattern?

??? success "Solution"
    **a)** $MU_1 = 30, MU_2 = 24, MU_3 = 18, MU_4 = 12, MU_5 = 6$.

    **b)** Yes — marginal utility falls steadily from 30 to 6 with each additional cup, which is the definition of diminishing marginal utility.

    **c)** The marginal utilities are falling by 6 each time (30, 24, 18, 12, 6), so the 6th cup would have $MU_6 = 0$, and the 7th cup would have $MU_7 = -6$ (negative) if the pattern continues.

### Problem 2 — Equal Marginal Principle

A consumer has \$18 to spend on apples ($P = \$2$) and oranges ($P = \$3$). Marginal utility schedules:

| Units | $MU$ apples | $MU$ oranges |
|---|---|---|
| 1 | 24 | 27 |
| 2 | 20 | 21 |
| 3 | 16 | 15 |
| 4 | 12 | 9 |
| 5 | 8 | 6 |
| 6 | 4 | 3 |

Find the utility-maximizing combination of apples and oranges that exhausts the \$18 budget.

??? success "Solution"
    Compute $MU/P$ for each unit:

    | Units | $MU_a/P_a$ (÷2) | $MU_o/P_o$ (÷3) |
    |---|---|---|
    | 1 | 12 | 9 |
    | 2 | 10 | 7 |
    | 3 | 8 | 5 |
    | 4 | 6 | 3 |
    | 5 | 4 | 2 |
    | 6 | 2 | 1 |

    Rank and purchase in order of highest $MU/P$ until \$18 is spent: apple#1 (12, \$2), apple#2 (10, \$2), orange#1 (9, \$3), apple#3 (8, \$2), orange#2 (7, \$3), apple#4 (6, \$2) — running total: 2+2+3+2+3+2 = \$14. Next highest is orange#3 (5, \$3) → total \$17. Next highest remaining is apple#5 (4) but only \$1 left, not enough for apple (\$2) or another orange (\$3). 

    Final bundle: **4 apples and 3 oranges**, spending $4(2) + 3(3) = 8 + 9 = \$17$ (the remaining \$1 cannot buy another unit of either good, so it is unspent or saved).

### Problem 3 — Budget Constraint

Income is \$200, $P_x = \$10$ (concert tickets), $P_y = \$4$ (books).

**a)** Write the equation for the budget line (solve for $Y$ in terms of $X$).  
**b)** Find both intercepts.  
**c)** If the price of concert tickets falls to \$8, how does the budget line change?

??? success "Solution"
    **a)** $10X + 4Y = 200 \implies Y = 50 - 2.5X$

    **b)** Vertical intercept ($X=0$): $Y = 50$ books. Horizontal intercept ($Y=0$): $0 = 50-2.5X \implies X = 20$ tickets.

    **c)** New line: $8X + 4Y = 200 \implies Y = 50 - 2X$. The vertical intercept stays at 50 (books unaffected), but the horizontal intercept rises to $X = 25$. The budget line **rotates outward** around the vertical intercept, becoming flatter (opportunity cost of tickets in terms of books falls from 2.5 to 2).

### Problem 4 — Consumer Optimum (Tangency Condition)

A consumer's utility function is $U(X,Y) = X^2Y$, giving $MU_x = 2XY$ and $MU_y = X^2$. Income is $I = \$300$, $P_x = \$10$, $P_y = \$5$.

**a)** Set up the tangency condition.  
**b)** Solve for the optimal bundle $(X^*, Y^*)$.

??? success "Solution"
    **a)** Tangency condition: $\dfrac{MU_x}{MU_y} = \dfrac{P_x}{P_y} \implies \dfrac{2XY}{X^2} = \dfrac{10}{5} = 2 \implies \dfrac{2Y}{X} = 2 \implies Y = X$

    **b)** Substitute into budget constraint: $10X + 5Y = 300$. Since $Y = X$: $10X + 5X = 300 \implies 15X = 300 \implies X^* = 20$, and $Y^* = 20$.

    Check: $10(20) + 5(20) = 200 + 100 = 300$. ✓ Optimal bundle: **$X^*=20, Y^*=20$**.

### Problem 5 — Income and Substitution Effects

Classify each scenario by good type and describe the direction of the substitution and income effects.

**a)** The price of name-brand cereal falls, and a normal-good consumer buys more of it.  
**b)** The price of store-brand macaroni (an inferior good) falls, and the consumer buys more of it, but less than the substitution effect alone would predict.  
**c)** A hypothetical Giffen good's price falls, and the consumer buys *less* of it overall.

??? success "Solution"
    **a)** Normal good: substitution effect (quantity ↑, cheaper relative price) and income effect (quantity ↑, higher real income raises demand for normal good) **both point in the same direction** — quantity demanded rises, consistent with the law of demand.

    **b)** Inferior good: substitution effect (quantity ↑) and income effect (quantity ↓, since higher real income reduces demand for an inferior good) work in **opposite directions**, but the substitution effect dominates, so quantity demanded still rises overall — the law of demand still holds.

    **c)** Giffen good: substitution effect (quantity ↑) and income effect (quantity ↓) work in opposite directions, but here the **income effect dominates**, causing quantity demanded to fall when price falls — a violation of the law of demand, confirming this good is a (rare) Giffen good.

### Problem 6 — Deriving Demand from Consumer Theory

A consumer's utility function is $U(X,Y)=XY$, income is \$100, and $P_y = \$5$. Using the tangency condition and budget constraint (following the method of Section 4.7), find the optimal quantity of $X$ when $P_x = \$5$, and again when $P_x = \$2$. What does this reveal about the shape of the individual's demand curve for $X$?

??? success "Solution"
    For $U=XY$: $MU_x = Y$, $MU_y = X$. Tangency: $\dfrac{Y}{X} = \dfrac{P_x}{P_y} \implies Y = \dfrac{P_x}{P_y}X$.

    **At $P_x = 5$:** $Y = \dfrac{5}{5}X = X$. Budget: $5X + 5Y = 100 \implies 5X+5X=100 \implies X^*=10$.

    **At $P_x = 2$:** $Y = \dfrac{2}{5}X$. Budget: $2X + 5\left(\dfrac{2}{5}X\right) = 100 \implies 2X+2X=100 \implies X^*=25$.

    As $P_x$ fell from \$5 to \$2, the optimal quantity of $X$ rose from 10 to 25. Plotting these price-quantity pairs $(5,10)$ and $(2,25)$ traces out points on a **downward-sloping demand curve** for $X$ — exactly the relationship predicted by the law of demand, now derived rigorously from utility maximization rather than simply assumed.

!!! mascot-celebration "You've Built the Demand Curve From Scratch"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You just derived the law of demand from first principles — utility, a budget, and a tangency condition — instead of simply assuming it. That's real theoretical grounding, and it's what separates an economist from someone who just memorized a downward-sloping line.

---

!!! tip "Next Chapter"
    In [Chapter 5: Production and Costs](../05-production-and-costs/index.md), we turn from the consumer's side of the market to the producer's side, studying how firms transform inputs into output and how their cost structures shape the supply decisions introduced in Chapter 2.
