# Chapter 3: Elasticity

## Learning Objectives

After completing this chapter, you will be able to:

1. Calculate the price elasticity of demand using the percentage-change and midpoint formulas
2. Classify demand as elastic, inelastic, or unit-elastic, and interpret the economic meaning of each case
3. Identify the determinants that make demand more or less elastic
4. Use the relationship between elasticity and total revenue to predict how price changes affect firm revenue
5. Calculate and interpret the price elasticity of supply
6. Calculate income elasticity and cross-price elasticity of demand and classify goods using these measures
7. Apply elasticity concepts to real-world problems in taxation, pricing strategy, and public policy

---

!!! mascot-welcome "Let's Measure Responsiveness"
    ![Professor Owl waving hello](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Chapter 2 told you demand curves slope downward — but not by how much. This chapter gives you that missing number, elasticity, and it's one you'll use constantly: in pricing decisions, tax policy, and even your own grocery budget. Every choice has a trade-off, and elasticity tells you how sharply people react to one.

## 3.1 Why Elasticity Matters

The supply and demand model in Chapter 2 tells us the *direction* in which quantity responds to a price change — but not the *magnitude*. If a city raises the transit fare by 10%, does ridership fall by 1% or by 30%? The answer matters enormously: it determines whether the transit agency's revenue rises or falls, and it determines how much of a product tax is passed on to consumers versus absorbed by producers.

**Elasticity** is a general concept in economics measuring the responsiveness of one variable to a change in another, expressed in percentage terms. Because elasticity is a ratio of percentage changes, it is a *unit-free* number — unlike slope, which depends on the units in which price and quantity are measured. This makes elasticity ideal for comparing responsiveness across very different goods, from gasoline to shoes to higher education.

---

## 3.2 Price Elasticity of Demand

### Definition

The **price elasticity of demand** ($E_d$) measures how much the quantity demanded of a good responds to a change in its own price:

$$E_d = \frac{\%\Delta Q_d}{\%\Delta P}$$

Because demand curves slope downward, price and quantity demanded move in opposite directions, so $E_d$ is mathematically negative. By convention, economists report the **absolute value** of $E_d$ and describe demand in terms of its magnitude.

### The Percentage-Change Formula

$$E_d = \frac{\%\Delta Q_d}{\%\Delta P} = \frac{\Delta Q / Q}{\Delta P / P}$$

!!! example "Simple calculation"
    Suppose the price of movie tickets rises from \$10 to \$12 (a 20% increase), and quantity demanded falls from 1,000 to 900 tickets per week (a 10% decrease).

    $$E_d = \frac{-10\%}{20\%} = -0.5 \implies |E_d| = 0.5$$

    Demand is **inelastic**: quantity demanded is relatively unresponsive to the price change.

### The Midpoint (Arc Elasticity) Formula

The simple percentage-change formula has a flaw: the elasticity calculated for a price *increase* from \$10 to \$12 differs from the elasticity calculated for a price *decrease* from \$12 to \$10, because the base used for the percentage differs. The **midpoint formula** solves this by using the average of the two values as the base:

$$E_d = \frac{(Q_2 - Q_1)/\left[(Q_1+Q_2)/2\right]}{(P_2 - P_1)/\left[(P_1+P_2)/2\right]}$$

!!! example "Midpoint formula applied"
    Using the ticket example: $P_1 = 10, P_2 = 12, Q_1 = 1000, Q_2 = 900$.

    $$\%\Delta Q = \frac{900 - 1000}{(1000+900)/2} = \frac{-100}{950} = -10.53\%$$

    $$\%\Delta P = \frac{12 - 10}{(10+12)/2} = \frac{2}{11} = 18.18\%$$

    $$E_d = \frac{-10.53\%}{18.18\%} = -0.58 \implies |E_d| = 0.58$$

    This is close to, but not identical to, the simple-formula answer of 0.5 — the midpoint method gives a consistent answer regardless of the direction of the price change.

!!! tip "When to use which formula"
    Use the midpoint formula for calculations over a discrete price change (a table or a word problem giving two price-quantity pairs). When demand is given as a continuous function, economists often instead compute **point elasticity** using calculus: $E_d = \frac{dQ}{dP}\cdot\frac{P}{Q}$ evaluated at a specific point.

!!! mascot-thinking "The Number Matters More Than the Formula"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Don't get lost memorizing formulas — the real insight is the classification. Whether $|E_d|$ is exactly 0.58 or 0.6, what matters is that it's below 1: this good's buyers barely react to price.

---

## 3.3 Elastic, Inelastic, and Unit-Elastic Demand

| Case | Condition | Interpretation |
|---|---|---|
| **Elastic** | $\lvert E_d \rvert > 1$ | Quantity demanded is highly responsive to price; %Δ$Q$ > %Δ$P$ |
| **Inelastic** | $\lvert E_d \rvert < 1$ | Quantity demanded is relatively unresponsive; %Δ$Q$ < %Δ$P$ |
| **Unit elastic** | $\lvert E_d \rvert = 1$ | %Δ$Q$ exactly equals %Δ$P$ |
| **Perfectly inelastic** | $E_d = 0$ | Quantity demanded does not change at all (vertical demand curve) |
| **Perfectly elastic** | $E_d \to \infty$ | Any price increase drives quantity demanded to zero (horizontal demand curve) |

!!! example "Perfectly inelastic and perfectly elastic demand"
    - A patient with a life-threatening condition who needs a specific insulin dose has (approximately) **perfectly inelastic** demand for that dose — quantity demanded barely changes regardless of price.
    - A wheat farmer selling into a competitive world market faces (approximately) **perfectly elastic** demand for *his own* wheat — if he raises his price even slightly above the world price, buyers switch entirely to other farmers.

---

## 3.4 Determinants of Price Elasticity of Demand

Why is demand for some goods elastic and others inelastic? Four main factors determine elasticity:

1. **Availability of substitutes.** The more and closer the substitutes, the more elastic demand. Demand for "Coca-Cola" is more elastic than demand for "soft drinks" in general, because a Coke drinker can switch to Pepsi.
2. **Necessity vs. luxury.** Necessities (insulin, water) tend to have inelastic demand; luxuries (vacations, jewelry) tend to have elastic demand.
3. **Share of budget.** Goods that take up a large share of a consumer's budget (housing, cars) tend to have more elastic demand than goods that take a tiny share (salt, matches), because a price change has a larger effect on the household budget.
4. **Time horizon.** Demand is more elastic in the **long run** than in the **short run**, because consumers need time to adjust behavior, find substitutes, or change technology. When gasoline prices spike, short-run demand barely falls (people still need to commute), but over several years, people buy fuel-efficient cars, move closer to work, or switch to public transit.

!!! note "Narrow vs. broad category"
    Narrowly defined goods (a specific brand) tend to have more elastic demand than broadly defined categories (the entire product class), because narrow categories have more substitutes available (other brands).

!!! mascot-tip "Four Questions, One Elasticity Estimate"
    ![Professor Owl sharing a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Before crunching any numbers, ask yourself four quick questions: does it have substitutes, is it a necessity, does it eat a big share of the budget, and how much time do buyers have to adjust? Answering those usually tells you elastic-or-inelastic before you ever see data.

---

## 3.5 Total Revenue and Elasticity

For a firm, the relationship between elasticity and **total revenue** ($TR = P \times Q$) is one of the most practically important results in microeconomics.

### The Total Revenue Test

| Demand is... | A price increase causes... | A price decrease causes... |
|---|---|---|
| **Elastic** ($\lvert E_d\rvert > 1$) | Total revenue **falls** | Total revenue **rises** |
| **Unit elastic** ($\lvert E_d\rvert = 1$) | Total revenue **unchanged** | Total revenue **unchanged** |
| **Inelastic** ($\lvert E_d\rvert < 1$) | Total revenue **rises** | Total revenue **falls** |

**Intuition:** When demand is elastic, the percentage drop in quantity outweighs the percentage rise in price, so revenue ($P \times Q$) falls when price rises. When demand is inelastic, the percentage drop in quantity is small relative to the price increase, so revenue rises.

!!! mascot-encourage "The Calculus Isn't the Hard Part"
    ![Professor Owl giving encouragement](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If taking a derivative here feels intimidating, remember: you already know *why* the answer works from the Total Revenue Test above. The calculus is just confirming, with precision, a direction you can already reason out.

### Worked Example

Suppose a transit agency's demand curve is $Q = 200 - 4P$, where $Q$ is daily riders (thousands) and $P$ is the fare in dollars.

**Step 1: Write total revenue as a function of price.**

$$TR(P) = P \times Q = P(200 - 4P) = 200P - 4P^2$$

**Step 2: Find the revenue-maximizing price using calculus.**

$$\frac{d(TR)}{dP} = 200 - 8P = 0 \implies P^* = 25$$

At $P = 25$: $Q = 200 - 4(25) = 100$, and $TR = 25 \times 100 = 2{,}500$ (thousand dollars).

**Step 3: Verify using elasticity.** At the revenue-maximizing price, demand is **unit elastic**. Check:

$$E_d = \frac{dQ}{dP} \cdot \frac{P}{Q} = (-4)\cdot\frac{25}{100} = -1$$

Confirmed: $\lvert E_d \rvert = 1$ exactly where revenue is maximized. For any price below \$25, demand is inelastic ($\lvert E_d\rvert <1$) and raising price increases revenue; for any price above \$25, demand is elastic and raising price decreases revenue.

!!! example "Why airlines and concert venues care"
    Airlines and ticket sellers constantly estimate elasticity to set prices. If demand for a flight is inelastic (e.g., business travelers with no flexibility), raising the price increases revenue. If demand is elastic (e.g., leisure travelers who can delay or skip the trip), cutting the price increases revenue by drawing in enough new volume.

---

## 3.6 Price Elasticity of Supply

The **price elasticity of supply** ($E_s$) measures how responsive quantity supplied is to a change in price:

$$E_s = \frac{\%\Delta Q_s}{\%\Delta P}$$

Because supply curves slope upward, $E_s$ is positive. The same elastic/inelastic/unit-elastic classification applies.

### Determinants of Supply Elasticity

1. **Availability of inputs and spare capacity.** If firms have idle capacity or can easily obtain more inputs, supply is more elastic.
2. **Time horizon.** Supply is more elastic in the long run, since firms can build new factories, and new firms can enter the industry.
3. **Flexibility of production.** Goods that can be produced with easily reallocated resources (e.g., a farmer who can switch between crops) have more elastic supply. Goods tied to a unique, fixed resource (e.g., beachfront land, a famous painting) have highly inelastic — even perfectly inelastic — supply.

!!! example "Perfectly inelastic supply"
    The supply of original Picasso paintings is **perfectly inelastic** ($E_s = 0$): no matter how high the price rises, no more can be produced. The entire burden of any price change falls on the demand side.

### Worked Example

Suppose $Q_s = -20 + 5P$. At $P=10$, $Q_s = 30$. If price rises to $P=12$, $Q_s = 40$.

Using the midpoint formula:

$$\%\Delta Q = \frac{40-30}{35} = 28.57\%, \qquad \%\Delta P = \frac{12-10}{11} = 18.18\%$$

$$E_s = \frac{28.57\%}{18.18\%} = 1.57$$

Supply is **elastic**: producers expand quantity supplied proportionally more than the price increase.

---

## 3.7 Income Elasticity of Demand

**Income elasticity of demand** ($E_I$) measures how quantity demanded responds to a change in consumer income:

$$E_I = \frac{\%\Delta Q_d}{\%\Delta \text{Income}}$$

| Value of $E_I$ | Classification | Example |
|---|---|---|
| $E_I > 1$ | **Luxury good** (income elastic) | Vacations, designer goods |
| $0 < E_I < 1$ | **Normal good**, income inelastic | Groceries, utilities |
| $E_I < 0$ | **Inferior good** | Instant ramen, used clothing |

!!! example "Income elasticity calculation"
    A household's income rises from \$50,000 to \$55,000 (a 10% increase), and their restaurant spending rises from 10 to 13 meals per month (a 30% increase using the simple formula).

    $$E_I = \frac{30\%}{10\%} = 3.0$$

    Restaurant meals are a strongly **luxury** good for this household — demand grows three times faster than income.

---

## 3.8 Cross-Price Elasticity of Demand

**Cross-price elasticity of demand** ($E_{xy}$) measures how the quantity demanded of good $X$ responds to a change in the price of good $Y$:

$$E_{xy} = \frac{\%\Delta Q_x}{\%\Delta P_y}$$

| Sign of $E_{xy}$ | Relationship | Example |
|---|---|---|
| $E_{xy} > 0$ | **Substitutes** | Coffee and tea |
| $E_{xy} < 0$ | **Complements** | Printers and ink |
| $E_{xy} = 0$ | **Unrelated** | Bananas and automobiles |

!!! example "Cross-price elasticity calculation"
    The price of Pepsi rises by 10%, and the quantity demanded of Coca-Cola rises by 4%.

    $$E_{xy} = \frac{4\%}{10\%} = 0.4 > 0$$

    Coke and Pepsi are substitutes, and a moderate positive cross-price elasticity suggests they are only moderately close substitutes (loyal customers of each brand do not switch readily).

---

## 3.9 Real-World Applications

### Tax Incidence

When a government imposes a tax on a good, elasticity determines **who actually bears the burden** of the tax — regardless of who physically pays it. The side of the market that is more inelastic bears a larger share of the tax burden, because that side has fewer options to avoid the tax by changing its quantity.

!!! example "Cigarette taxes"
    Demand for cigarettes is highly inelastic (addictive good, few substitutes). When governments impose cigarette taxes, consumers continue to buy nearly the same quantity — the tax is largely passed through to consumers in the form of higher prices, and tax revenue is high and predictable. This is also why cigarette taxes are an effective tool for raising government revenue, even though they are intended to also discourage smoking.

!!! mascot-warning "Who Pays the Tax Isn't Who Bears It"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    It's easy to assume the side that legally writes the check to the government bears the tax. It doesn't — tax incidence depends entirely on relative elasticities, regardless of which side the law names as the "payer."

### Pricing Strategy and Price Discrimination

Firms use elasticity estimates to maximize revenue: charge a *higher* price to the segment of customers with *inelastic* demand, and a *lower* price to the segment with *elastic* demand.

!!! example "Student and senior discounts"
    Movie theaters offer discounts to students and seniors — groups with more elastic demand (more time, less income, better substitutes like streaming) — while charging full price to working adults attending with limited scheduling flexibility, who have more inelastic demand.

### Agricultural Policy

Farm goods tend to have inelastic demand (necessities with few substitutes) and, in the short run, fairly inelastic supply (crops take a season to grow). A bumper harvest—a rightward shift in supply—can therefore *reduce* total farm revenue, because the resulting price drop is proportionally larger than the quantity increase. This is sometimes referred to as "the paradox of bumper crops," and it motivates agricultural price-support policy.

!!! warning "Elasticity is not fixed"
    A good's elasticity is not an immutable property, but depends on the price range, the time horizon, and how the good's market is defined. Always identify these conditions before applying an elasticity estimate to a new situation.

#### Diagram: Price Elasticity of Demand Explorer

<details markdown="1">
<summary>Price Elasticity of Demand Explorer</summary>
Type: microsim
**sim-id:** elasticity-explorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the price elasticity of demand using the midpoint formula for a given price-quantity change, and classify the result as elastic, unit-elastic, or inelastic.

**Prerequisites:** price elasticity of demand, the midpoint (arc elasticity) formula, elastic/inelastic/unit-elastic classification (Sections 3.2–3.3).

**Evidence of Mastery:** For each of 4 challenges, the learner types the computed |Ed| (within ±0.05) and picks elastic/inelastic/unit-elastic. Correct when both match. Mastery is 4 of 4 correct.

**Misconceptions:** (1) Using the simple percentage formula's base (P1, Q1 only) instead of the midpoint convention. (2) Forgetting to take the absolute value of Ed before classifying. (3) Classifying by the sign of %ΔQ rather than the magnitude of the ratio.

**Instructional Rationale:** Apply-level calculation needs repeated practice applying the exact midpoint formula to new numbers, with immediate numeric feedback, before generalizing to classification language.

**Content:**

| # | P1 | P2 | Q1 | Q2 | %ΔP | %ΔQ | &#124;Ed&#124; | Classification |
|---|---|---|---|---|---|---|---|---|
| 1 | \$10 | \$12 | 1000 | 900 | 18.18% | −10.53% | 0.58 | Inelastic |
| 2 | \$20 | \$22 | 500 | 350 | 9.52% | −35.29% | 3.71 | Elastic |
| 3 | \$50 | \$55 | 200 | 190 | 9.52% | −5.13% | 0.54 | Inelastic |
| 4 | \$9 | \$11 | 110 | 90 | 20.00% | −20.00% | 1.00 | Unit-elastic |

**Provenance:** Challenge 1 is the chapter's own worked example in Section 3.2 ("Midpoint formula applied"). Challenges 2–4 are illustrative numbers built with the same midpoint formula to produce one elastic, one inelastic, and one exactly unit-elastic case; labeled illustrative.

**Rules:** %ΔQ = (Q2−Q1) / ((Q1+Q2)/2); %ΔP = (P2−P1) / ((P1+P2)/2); Ed = %ΔQ / %ΔP. Classification: |Ed| > 1 → elastic; |Ed| < 1 → inelastic; |Ed| = 1 within ±0.05 → unit-elastic. The Challenge selector is discrete, 1 to 4, step 1, default 1.

**Learner Activity:**

1. The learner reads Challenge 1 (the chapter's own ticket numbers) and types the computed |Ed|, then picks a classification.
2. The sim checks the number (±0.05) and the classification and shows the correct value.
3. The learner repeats for Challenges 2–4, in order.
4. After all 4, a free-input mode unlocks: the learner can type any P1, P2, Q1, Q2 and see the computed |Ed| and classification.

**Feedback:** 4 challenges, fixed order, two attempts each. Correct: "Correct: &#124;Ed&#124; = <value>, which is <classification>." Incorrect (first attempt): "Use the average of Q1 and Q2 as the %ΔQ base, not just Q1." After the second wrong attempt, the correct value and classification are shown. A running count "Challenges correct: n of 4" is shown.

**Starting State:** Challenge 1 is shown with P1 = \$10, P2 = \$12, Q1 = 1000, Q2 = 900, and empty answer boxes. The question on screen is "Using the midpoint formula, how elastic is this demand?"

**Chapter Anchors:** The chapter's worked midpoint example states |Ed| = 0.58 for P1=10, P2=12, Q1=1000, Q2=900; the sim's Challenge 1 reproduces this exactly.
</details>

---

## Key Terms

| Term | Definition |
|---|---|
| **Elasticity** | A unit-free measure of the responsiveness of one variable to a percentage change in another |
| **Price Elasticity of Demand ($E_d$)** | % change in quantity demanded divided by % change in price |
| **Midpoint Formula** | Arc-elasticity formula using the average of two values as the base, giving a consistent result regardless of direction |
| **Elastic Demand** | $\lvert E_d \rvert > 1$; quantity demanded is highly responsive to price |
| **Inelastic Demand** | $\lvert E_d \rvert < 1$; quantity demanded is relatively unresponsive to price |
| **Unit-Elastic Demand** | $\lvert E_d \rvert = 1$; % change in quantity equals % change in price |
| **Perfectly Inelastic Demand** | $E_d = 0$; quantity demanded does not change at all |
| **Perfectly Elastic Demand** | $E_d \to \infty$; any price increase drives quantity demanded to zero |
| **Total Revenue Test** | Method for inferring elasticity from how total revenue responds to a price change |
| **Price Elasticity of Supply ($E_s$)** | % change in quantity supplied divided by % change in price |
| **Income Elasticity of Demand ($E_I$)** | % change in quantity demanded divided by % change in income |
| **Cross-Price Elasticity of Demand ($E_{xy}$)** | % change in quantity demanded of good $X$ divided by % change in price of good $Y$ |
| **Tax Incidence** | The division of a tax's burden between buyers and sellers, determined by relative elasticities |

---

## Practice Problems

### Problem 1 — Calculating Price Elasticity of Demand

The price of a bus pass rises from \$40 to \$44. Quantity demanded falls from 10,000 to 9,200 passes per month.

**a)** Calculate the price elasticity of demand using the midpoint formula.  
**b)** Is demand elastic, inelastic, or unit elastic?  
**c)** What will happen to the transit agency's total revenue?

??? success "Solution"
    **a)**

    $$\%\Delta Q = \frac{9200-10000}{(10000+9200)/2} = \frac{-800}{9600} = -8.33\%$$

    $$\%\Delta P = \frac{44-40}{(40+44)/2} = \frac{4}{42} = 9.52\%$$

    $$E_d = \frac{-8.33\%}{9.52\%} = -0.875 \implies |E_d| = 0.875$$

    **b)** Since $\lvert E_d \rvert < 1$, demand is **inelastic**.

    **c)** Revenue before: $40 \times 10{,}000 = \$400{,}000$. Revenue after: $44 \times 9{,}200 = \$404{,}800$. Revenue **rises** — consistent with the total revenue test: a price increase under inelastic demand raises revenue.

### Problem 2 — Determinants of Elasticity

For each pair, identify which good likely has more elastic demand, and explain why using the determinants of elasticity.

**a)** Insulin vs. a Netflix subscription  
**b)** "Honeycrisp apples" vs. "apples" (any variety)  
**c)** Gasoline demand measured over one month vs. over five years

??? success "Solution"
    **a)** **Netflix subscription** is more elastic — it is a discretionary entertainment good with substitutes (other streaming services, free content), while insulin is a life-necessity with no substitutes for diabetics.

    **b)** **"Honeycrisp apples"** is more elastic — it is a narrowly defined good with many close substitutes (other apple varieties), while "apples" as a category has fewer substitutes (someone who wants apples can't easily substitute oranges for the same culinary purpose).

    **c)** Demand measured over **five years** is more elastic — consumers have time to buy fuel-efficient vehicles, relocate, or switch to public transit; in one month, most consumption patterns are locked in.

### Problem 3 — Total Revenue and Elasticity

A firm's demand curve is $Q = 300 - 5P$.

**a)** Derive the firm's total revenue function.  
**b)** Find the price that maximizes total revenue.  
**c)** Confirm using the elasticity formula that demand is unit elastic at that price.

??? success "Solution"
    **a)** $TR = P \times Q = P(300-5P) = 300P - 5P^2$

    **b)** $\dfrac{d(TR)}{dP} = 300 - 10P = 0 \implies P^* = 30$

    At $P = 30$: $Q = 300 - 5(30) = 150$, so $TR = 30 \times 150 = \$4{,}500$.

    **c)** $E_d = \dfrac{dQ}{dP}\cdot\dfrac{P}{Q} = (-5)\cdot\dfrac{30}{150} = -1$. $\lvert E_d\rvert = 1$, confirming unit elasticity at the revenue-maximizing price.

### Problem 4 — Price Elasticity of Supply

A supply curve is given by $Q_s = 2P - 10$. At $P=20$, find $Q_s$. If price rises to $P=25$, find the new $Q_s$, and calculate the price elasticity of supply using the midpoint formula. Classify the result.

??? success "Solution"
    At $P=20$: $Q_s = 2(20)-10 = 30$.

    At $P=25$: $Q_s = 2(25)-10 = 40$.

    $$\%\Delta Q = \frac{40-30}{35} = 28.57\%, \qquad \%\Delta P = \frac{25-20}{22.5} = 22.22\%$$

    $$E_s = \frac{28.57\%}{22.22\%} = 1.29$$

    Since $E_s > 1$, supply is **elastic**.

### Problem 5 — Income and Cross-Price Elasticity

A household's income rises by 8%. As a result, their demand for public transit falls by 2%, and their demand for restaurant meals rises by 16%. Separately, when the price of butter rose by 5%, the quantity of margarine demanded by this household rose by 2%.

**a)** Calculate the income elasticity of demand for public transit and classify the good.  
**b)** Calculate the income elasticity of demand for restaurant meals and classify the good.  
**c)** Calculate the cross-price elasticity between butter and margarine and classify the relationship.

??? success "Solution"
    **a)** $E_I = \dfrac{-2\%}{8\%} = -0.25$. Since $E_I < 0$, public transit is an **inferior good** for this household.

    **b)** $E_I = \dfrac{16\%}{8\%} = 2.0$. Since $E_I > 1$, restaurant meals are a **luxury good**.

    **c)** $E_{xy} = \dfrac{2\%}{5\%} = 0.4 > 0$. Butter and margarine are **substitutes**.

### Problem 6 — Tax Incidence Application

The government imposes a new excise tax on gasoline. Demand for gasoline is highly inelastic ($\lvert E_d\rvert = 0.2$) in the short run, while supply is relatively elastic ($E_s = 1.5$).

**a)** Which side of the market — consumers or producers — will bear more of the tax burden? Explain using the concept of elasticity.  
**b)** Suppose instead the government taxed a luxury good with highly elastic demand ($\lvert E_d\rvert = 3$) and inelastic supply ($E_s = 0.3$). Who bears more of the burden now?

??? success "Solution"
    **a)** **Consumers** bear more of the tax burden. Demand is far more inelastic than supply, meaning consumers have few alternatives and will continue buying gasoline even as the price rises to reflect the tax; producers, facing more elastic supply, can more easily adjust quantity and avoid absorbing much of the tax.

    **b)** **Producers** bear more of the burden. Supply is far more inelastic than demand: producers cannot easily reduce the quantity they bring to market (perhaps due to fixed production commitments), while consumers can readily reduce quantity demanded in response to a price increase, shifting the burden back onto sellers.

!!! mascot-celebration "You Can Now Quantify Responsiveness"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now calculate four different elasticities, predict how a price change moves revenue, and explain who really bears a tax. That's a toolkit real firms and policymakers use every day!

---

!!! tip "Next Chapter"
    In [Chapter 4: Consumer Theory](../04-consumer-theory/index.md), we go beneath the demand curve to study how individual consumers choose a utility-maximizing bundle of goods given their budget — providing the micro-foundations for the law of demand and elasticity itself.
