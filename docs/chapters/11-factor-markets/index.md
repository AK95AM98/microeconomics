# Chapter 11: Factor Markets

## Learning Objectives

After completing this chapter, you will be able to:

1. Explain why the demand for labor and other inputs is a *derived demand*
2. Calculate marginal revenue product (MRP) and use it to find a firm's profit-maximizing hiring level
3. Derive a firm's labor demand curve and explain what shifts it
4. Analyze the labor supply decision as a work-leisure trade-off
5. Determine the equilibrium wage and employment level in a competitive labor market
6. Contrast competitive labor markets with monopsony and explain why monopsony depresses wages and employment
7. Explain how interest rates allocate capital, and distinguish economic rent from other factor payments

---

!!! mascot-welcome "Same Marginal Logic, Brand New Markets"
    ![Professor Owl waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Every choice has a trade-off — and up to now, you've mostly analyzed that trade-off from the seller's side of an output market. This chapter flips the lens: firms become *buyers*, hiring workers and renting capital, and the same marginal reasoning you already mastered — set marginal benefit equal to marginal cost — explains wages, interest rates, and rents too. You already know more of this chapter than you think.

## 11.1 Input Markets and Derived Demand

So far we have studied markets for *output* — the goods and services firms sell to consumers. This chapter turns to markets for the **inputs**, or **factors of production**, that firms use to produce that output: labor, capital, land, and entrepreneurship. The prices of these factors — wages, interest rates, rents, and profits — determine how income is distributed across the economy.

Input markets differ from output markets in one crucial way: **nobody wants an input for its own sake.** A firm does not hire a worker because it enjoys having workers around; it hires a worker because that worker helps produce a good the firm can sell. This gives rise to the concept of **derived demand**: the demand for an input is *derived from* the demand for the output it helps produce.

!!! note "Derived demand in practice"
    When consumer demand for new housing rises, the demand for construction workers, lumber, and land for development all rise with it — not because anyone values carpenters or two-by-fours intrinsically, but because they are necessary to produce houses. When housing demand collapses (as in 2008), derived demand for construction labor collapses too.

This linkage means every input market is connected to some output market. To understand the labor market for software engineers, you must understand the demand for software; to understand the market for farmland, you must understand the demand for food.

!!! mascot-thinking "Every Input Curve Has an Output Market Hiding Inside It"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Here's the mental model to carry through this whole chapter: nobody ever demands an input for its own sake. Every curve you draw for labor, capital, or land secretly has an output market baked into it — shift the demand for houses, and you've just shifted the demand for construction workers, lumber, and land, whether or not you drew that connection explicitly.

---

## 11.2 Marginal Revenue Product

### Defining MRP

How many workers should a profit-maximizing firm hire? The key concept is **marginal revenue product (MRP)**: the additional revenue a firm earns from employing one more unit of an input.

$$MRP_L = MP_L \times MR$$

where $MP_L$ is the **marginal product of labor** (the extra output produced by one more worker) and $MR$ is the **marginal revenue** the firm earns from selling one more unit of output. In a perfectly competitive output market, $MR = P$, so:

$$MRP_L = MP_L \times P$$

MRP tells the firm exactly what an additional worker is worth to it in dollar terms.

### A Worked Numerical Example

Consider a competitive bakery selling bread at $P = \$4$ per loaf. The table below shows how output responds as the bakery adds workers, holding its ovens (capital) fixed.

| Workers ($L$) | Total Product (loaves/day) | Marginal Product ($MP_L$) | MRP ($MP_L \times \$4$) |
|---|---|---|---|
| 0 | 0 | — | — |
| 1 | 20 | 20 | \$80 |
| 2 | 36 | 16 | \$64 |
| 3 | 48 | 12 | \$48 |
| 4 | 56 | 8 | \$32 |
| 5 | 60 | 4 | \$16 |
| 6 | 60 | 0 | \$0 |

Notice that marginal product falls as more workers are added — this is **diminishing marginal returns** (Chapter 5), which arises because the fixed number of ovens means each additional worker has less capital to work with.

### The Hiring Rule

A profit-maximizing firm keeps hiring workers as long as each additional worker adds more to revenue than to cost. The firm hires up to the point where:

$$MRP_L = w$$

where $w$ is the wage rate. If $MRP_L > w$, the worker generates more revenue than they cost — hire them. If $MRP_L < w$, the worker costs more than they generate — do not hire them (or lay them off).

!!! example "Applying the hiring rule"
    Suppose the market wage for bakery workers is $w = \$50$/day. Using the table above:

    - Hiring the 3rd worker: $MRP_L = \$48 < \$50$. Not worth it — stop before the 3rd worker.
    - Hiring the 2nd worker: $MRP_L = \$64 > \$50$. Worth it — hire the 2nd worker.

    The bakery hires **2 workers**, since that is the largest $L$ for which $MRP_L \geq w$. At $w = \$32$, the bakery would hire 4 workers instead ($MRP_L = \$32$ at $L=4$).

This is the same logic as the MR = MC rule from Chapter 6, applied to an input rather than an output: hire inputs up to the point where the marginal benefit (MRP) equals the marginal cost (the wage).

---

## 11.3 Labor Demand

### The Labor Demand Curve

Because the hiring rule says "hire until $MRP_L = w$," the **MRP curve is the firm's labor demand curve.** It is downward-sloping because $MP_L$ diminishes as more labor is added (holding capital fixed).

$$Q_L^d = f(w), \quad \frac{\partial Q_L^d}{\partial w} < 0$$

A market labor demand curve is the horizontal sum of all firms' individual MRP curves in that labor market.

### What Shifts Labor Demand?

| Determinant | Effect on Labor Demand |
|---|---|
| **Increase in output price ($P$)** | Demand increases (MRP = $MP_L \times P$ rises) |
| **Increase in productivity ($MP_L$)**, e.g., better technology or training | Demand increases |
| **More capital** (complementary input) | Demand increases, if capital and labor are complements |
| **Automation that substitutes for labor** | Demand decreases |
| **Increase in demand for the final good** | Demand increases (derived demand) |

!!! example "Technology and labor demand: two directions"
    A new software tool that lets each accountant process twice as many tax returns *raises* each accountant's $MP_L$, shifting labor demand for accountants to the **right** (more accountants demanded at every wage, assuming the firm cannot shrink too much). But self-checkout kiosks are a direct substitute for cashiers, shifting labor demand for cashiers to the **left**.

---

## 11.4 Labor Supply: The Work-Leisure Trade-off

### The Individual's Decision

Workers must decide how to divide their 24 hours between **labor** (which earns income to buy goods) and **leisure** (unpaid time, which they also value). The wage rate $w$ is the **opportunity cost of leisure** — every hour not worked is an hour of wages foregone.

A higher wage has two competing effects on how many hours a person chooses to work:

1. **Substitution effect:** A higher wage raises the opportunity cost of leisure, inducing people to work *more* hours (substitute away from leisure toward labor).
2. **Income effect:** A higher wage raises income at any given number of hours, making people feel richer and want *more* leisure (assuming leisure is a normal good), inducing them to work *fewer* hours.

### The Backward-Bending Labor Supply Curve

At low wages, the substitution effect typically dominates — as wages rise, people work more. But past some wage level, the income effect can dominate — people are rich enough that they "buy back" leisure time by working less even as wages continue to rise. This produces a labor supply curve that slopes upward at first, then bends backward.

!!! example "Backward-bending supply in practice"
    A surgeon earning \$500/hour may choose to work fewer hours than one earning \$300/hour, if at the higher wage she can meet her desired income target more quickly and prefers additional leisure. Many lottery winners also reduce hours worked, consistent with a pure income effect with no change in the wage at all.

!!! mascot-warning "Don't Confuse the Individual Curve With the Market Curve"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A common mix-up: assuming every worker's supply curve bends backward, and then confusing that backward-bending *individual* curve with the upward-sloping *market* curve covered next. Most workers, most of the time, sit on the ordinary upward-sloping portion — the backward bend is a high-wage phenomenon that shows up for only some workers at some wage levels.

### Market Labor Supply

While an individual's supply curve may bend backward, the **market** labor supply curve is typically upward-sloping: a higher wage draws new workers into the labor force (increasing labor force participation) even if some existing workers choose to work fewer hours.

---

## 11.5 Equilibrium in Competitive Labor Markets

### Finding the Equilibrium Wage

In a competitive labor market — many buyers (firms) and many sellers (workers), none with market power — the equilibrium wage $w^*$ and employment level $L^*$ are found just as in Chapter 2, by setting labor demand equal to labor supply:

$$L^d(w) = L^s(w)$$

!!! example "Solving for equilibrium"
    Suppose the labor market for baristas in a city has:

    $$L^d = 2000 - 100w \qquad L^s = -400 + 150w$$

    Setting $L^d = L^s$:

    $$2000 - 100w = -400 + 150w$$
    $$2400 = 250w$$
    $$w^* = \$9.60/\text{hour}, \qquad L^* = 2000 - 100(9.60) = 1040 \text{ workers}$$

!!! mascot-tip "A Ten-Second Check on Any Labor-Market Equilibrium"
    ![Professor Owl with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    After solving for $w^*$, plug it back into the demand equation *and* the supply equation separately. If they don't land on the same $L^*$, you made an algebra error somewhere upstream — this quick check catches most mistakes before they cost you the whole problem.

### Why Wages Differ Across Markets

Competitive labor markets predict a single wage for a *homogeneous* type of labor. In reality, wages differ enormously across occupations because:

- **Differences in MRP:** workers with higher skill or productivity command higher MRP and thus higher wages.
- **Human capital** (Section 11.9): education and training raise $MP_L$.
- **Compensating differentials:** unpleasant, dangerous, or inconvenient jobs (night-shift work, offshore oil rigs) must pay more to attract workers, compensating for the non-wage disadvantages.
- **Labor market frictions and discrimination:** barriers to entry, imperfect information, and discrimination can prevent wages from equalizing even for similarly productive workers.

---

## 11.6 Monopsony: A Single Buyer of Labor

### What Is Monopsony?

A **monopsony** is a market with only one (or a dominant) *buyer* of an input — the mirror image of a monopoly, which has only one seller of output. Classic examples include a single large factory or hospital that is the overwhelmingly dominant employer in an isolated town, or historically, company towns where one firm owned the mine, the housing, and the store.

Because a monopsonist is the only buyer, it faces the entire upward-sloping market labor supply curve, not a flat wage set by the market. To hire one more worker, it must raise the wage *for all its workers*, not just the marginal hire. This means the monopsonist's **marginal cost of labor (MCL)** exceeds the wage:

$$MCL > w$$

!!! mascot-thinking "Monopsony Is Monopoly's Mirror Image"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Notice the symmetry: a monopolist's marginal revenue falls below price because selling one more unit forces the price down on *all* units sold. A monopsonist's marginal cost of labor rises above the wage because hiring one more worker forces the wage up for *all* workers already employed. Same underlying mechanic, opposite side of the market.

### The Monopsony Hiring Rule

A profit-maximizing monopsonist hires where $MRP_L = MCL$ (marginal benefit equals true marginal cost) — but then pays only the wage on the labor supply curve at that quantity, which is *less* than $MRP_L$.

| Market Structure | Hiring Rule | Wage Paid |
|---|---|---|
| Competitive labor market | $MRP_L = w$ | $w = MRP_L$ |
| Monopsony | $MRP_L = MCL$ | $w < MRP_L$, read off the supply curve |

!!! warning "Monopsony depresses both wages and employment"
    Relative to a competitive labor market, a monopsonist hires **fewer** workers and pays a **lower** wage than the competitive outcome. Just as monopoly creates deadweight loss in output markets by restricting output, monopsony creates deadweight loss in input markets by restricting employment.

### Numerical Example

Suppose a monopsonist faces labor supply $w = 10 + 0.02L$ (so the wage it must pay rises as it hires more).

!!! mascot-encourage "Three Small Moves, Not One Big One"
    ![Professor Owl encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If deriving MCL from total labor cost feels like a lot at once, break it into three small moves: multiply wage by $L$ to get total cost, take one derivative, then set the result equal to $MRP_L$. It's the same three-move pattern as the Cournot derivation back in Chapter 9 — you've already done this.

Its total labor cost is $TLC = wL = (10 + 0.02L)L = 10L + 0.02L^2$, so:

$$MCL = \frac{d(TLC)}{dL} = 10 + 0.04L$$

Suppose $MRP_L = 100 - 0.04L$. Setting $MRP_L = MCL$:

$$100 - 0.04L = 10 + 0.04L$$

$$90 = 0.08L$$

$$L^* = 1125$$

The wage paid is read off the *supply* curve at $L = 1125$:

$$w^* = 10 + 0.02(1125) = \$32.50$$

But the value of the marginal worker is $MRP_L = 100 - 0.04(1125) = \$55$. The gap between $MRP_L = \$55$ and $w^* = \$32.50$ is the hallmark of monopsony power — the firm pays workers less than the value they create. Had this been a competitive market (hiring where $MRP_L = w$ directly), employment and wages would both have been higher.

### Policy Responses

A **minimum wage** set between the monopsony wage and the competitive wage can, in a pure monopsony model (unlike in a competitive market), *increase* both the wage and employment simultaneously, because it forces the monopsonist closer to the competitive outcome rather than creating a surplus of unhired workers. This is one reason labor economists' views on minimum-wage effects depend heavily on how competitive they believe local labor markets actually are.

---

## 11.7 Capital Markets and Interest Rates

### Capital as a Factor

**Capital** refers to produced inputs used to make other goods — machinery, buildings, and equipment. Firms "rent" capital in the sense of paying for its use, whether they lease it or purchase it with borrowed funds. The **interest rate** ($r$) is the price of capital — more precisely, the price of loanable funds used to finance capital investment.

### The Investment Decision

A firm invests in a piece of capital if the expected return exceeds the cost of financing it. Formally, a firm should invest in a project as long as:

$$\text{Expected Marginal Rate of Return} \geq r$$

This means capital, like labor, has its own downward-sloping demand curve — the lower the interest rate, the more investment projects become profitable, so the quantity of capital demanded rises as $r$ falls.

### Present Value

Because capital investments pay off over time, firms must compare a dollar today with a dollar in the future. The **present value (PV)** of a future payment $FV$ received in $t$ years, discounted at rate $r$, is:

$$PV = \frac{FV}{(1+r)^t}$$

!!! example "Should the firm buy the machine?"
    A firm can buy a machine today for \$10,000. The machine will generate \$11,500 in revenue one year from now, and then be worthless. The market interest rate is 10%.

    $$PV = \frac{\$11{,}500}{(1+0.10)^1} = \frac{\$11{,}500}{1.10} = \$10{,}454.55$$

    Since the present value of the machine's payoff (\$10,454.55) exceeds its \$10,000 cost, the firm should buy the machine — the net present value is positive ($\$454.55$).

### Loanable Funds Market

The equilibrium interest rate is determined by the supply of loanable funds (household saving) and the demand for loanable funds (firm investment and government borrowing), exactly analogous to the supply-and-demand framework of Chapter 2, with $r$ playing the role of price.

---

## 11.8 Economic Rent and Land Markets

### Land Supply Is (Nearly) Fixed

**Land**, in the economic sense, refers to natural resources whose total supply cannot be increased by human effort — most importantly, the physical land itself. Because the aggregate supply of land is essentially fixed regardless of price, the **supply curve for land is vertical (perfectly inelastic)**.

### Economic Rent

**Economic rent** is the payment to any factor of production whose supply is fixed (or nearly fixed) — a payment determined entirely by demand, since supply cannot respond. Because supply is vertical, any payment above the bare minimum needed to keep the resource in its current use is pure economic rent; the entire price paid for the use of the land is, in effect, rent.

$$\text{Rent} = \text{entire market-clearing payment, since } Q_s \text{ is fixed}$$

!!! example "Economic rent for prime farmland"
    Prime farmland near a growing city has a fixed supply. As the city's population grows, demand for that land rises (both for farming and for development), pushing up the rental price — but no more of this specific land can ever be created. The entire increase in rental price is economic rent: it rewards owning a scarce, fixed resource, not any new cost of production.

The concept of economic rent generalizes beyond literal land: any payment to a resource in excess of what is needed to keep it in its current use — a star athlete's salary beyond what would keep them playing, a uniquely located retail storefront — is also called economic rent.

---

## 11.9 Human Capital Theory

### Education and Training as Investment

**Human capital** is the stock of skills, education, training, and experience embodied in workers that raises their productivity ($MP_L$) and therefore their MRP and wages. **Human capital theory** treats education and training as an *investment* decision, analogous to a firm's capital investment decision in Section 11.7: incur a cost now (tuition, foregone wages while studying) in exchange for higher earnings later.

A rational worker invests in education as long as the present value of the additional future earnings exceeds the cost of acquiring the education:

$$PV(\text{additional lifetime earnings}) > \text{Cost of education (tuition + foregone wages)}$$

!!! example "The college decision as human capital investment"
    A student forgoes four years of full-time wages (say \$35,000/year = \$140,000 total opportunity cost) and pays tuition (say \$40,000) to earn a college degree, for a total cost of \$180,000. If the degree raises her expected lifetime earnings by a present value of \$500,000, human capital theory predicts she should make the investment — the returns substantially exceed the costs.

### Why Does Education Raise Wages?

Two leading explanations exist, and they are not mutually exclusive:

1. **Human capital (productivity) view:** Education directly raises a worker's skills and productivity ($MP_L$), raising MRP and therefore wages.
2. **Signaling view:** Education may not raise productivity much directly, but completing a rigorous degree *signals* to employers that a worker is capable, disciplined, and intelligent — traits employers cannot observe directly but value highly.

Both views predict that educated workers earn more; they differ on *why*, with important policy implications for how much a given investment in education will raise economy-wide productivity versus merely reshuffling who gets which job.

#### Diagram: Labor Market MRP Explorer

<details markdown="1">
<summary>Labor Market MRP Explorer</summary>
Type: microsim
**sim-id:** labor-market-mrp-explorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** determine<br/>
**Learning Objective:** The learner will determine the profit-maximizing number of workers to hire at a given market wage, using the chapter's bakery MRP schedule and the hiring rule MRP=w.

**Prerequisites:** marginal revenue product, marginal product of labor, the hiring rule MRP=w (Section 11.2).

**Evidence of Mastery:** For 2 challenge wages, in fixed order, the learner determines L* using the hiring rule and the given table. Correct when it matches exactly. Mastery is 2 of 2 correct.

**Misconceptions:** (1) Hiring only until MRP exactly equals the wage, rather than the largest L where MRP is still at or above the wage. (2) Using total product or marginal product directly as the hiring criterion instead of MRP (=MP×P). (3) Believing a lower wage means hiring fewer workers.

**Instructional Rationale:** An Apply-level task needs the learner to execute the stated hiring rule on new wage values, mirroring the chapter's own two worked wage examples before independent practice.

**Content:**

The chapter's own bakery MRP schedule (Section 11.2), at output price P=\$4/loaf:

| Workers (L) | Total Product | Marginal Product | MRP |
|---|---|---|---|
| 0 | 0 | — | — |
| 1 | 20 | 20 | \$80 |
| 2 | 36 | 16 | \$64 |
| 3 | 48 | 12 | \$48 |
| 4 | 56 | 8 | \$32 |
| 5 | 60 | 4 | \$16 |
| 6 | 60 | 0 | \$0 |

Chapter's own worked wages: w=\$50 → hire 2 workers; w=\$32 → hire 4 workers. Scored challenges: w=\$70 → hire 1 worker; w=\$10 → hire 5 workers.

**Provenance:** From the chapter's own "A Worked Numerical Example" and "Applying the hiring rule" in Section 11.2.

**Rules:** Hire the largest L (0–6) such that MRP at L is greater than or equal to the wage w. MRP values are fixed exactly per the table above; the output price (\$4/loaf) is fixed throughout. Market wage w: min \$0, max \$90, step \$5, default \$50.

**Learner Activity:**

1. The learner sets the wage to the chapter's own \$50 example and watches the sim confirm L*=2.
2. The learner sets the wage to \$70 and types the predicted L* before the sim reveals it.
3. The sim checks the answer against the table and shows the MRP bars with the wage line marking the cutoff.
4. The learner repeats for wage \$10.

**Feedback:** 2 scored challenges, fixed order, two attempts each. Correct: "Correct: L* = <value> workers." Incorrect (first attempt): "Find the largest number of workers for which MRP is still at or above the wage line." After the second wrong attempt, the correct L* is shown with the MRP table highlighted. A running count "Challenges correct: n of 2" is shown.

**Starting State:** The wage is set to \$50, the MRP bars (80, 64, 48, 32, 16, 0 for L=1–6) are plotted, and a horizontal wage line at \$50 is drawn with L*=2 marked as a worked demonstration. The question on screen before the first challenge is "If the wage rises to \$70, how many workers should the bakery hire?"

**Chapter Anchors:** The chapter's Section 11.2 states that at w=\$50/day the bakery hires 2 workers, and at w=\$32/day it hires 4 workers, using the MRP values 80, 64, 48, 32, 16, 0 for L=1–6; the sim's table and both worked wage cases reproduce the chapter's values exactly.
</details>

---

## Key Terms

| Term | Definition |
|---|---|
| **Derived Demand** | Demand for an input that arises from demand for the output it helps produce |
| **Marginal Revenue Product (MRP)** | The additional revenue from employing one more unit of an input; $MRP_L = MP_L \times MR$ |
| **Marginal Product of Labor ($MP_L$)** | The additional output produced by one more unit of labor |
| **Hiring Rule** | A firm hires an input up to the point where $MRP = $ input price |
| **Labor Demand Curve** | Equivalent to the MRP curve; shows quantity of labor demanded at each wage |
| **Work-Leisure Trade-off** | The decision of how to divide time between paid labor and unpaid leisure |
| **Substitution Effect (labor supply)** | A higher wage raises the opportunity cost of leisure, inducing more work |
| **Income Effect (labor supply)** | A higher wage raises income, inducing more leisure (fewer hours worked) |
| **Backward-Bending Labor Supply** | An individual supply curve that slopes up then bends backward at high wages |
| **Monopsony** | A market with a single (or dominant) buyer of an input |
| **Marginal Cost of Labor (MCL)** | The monopsonist's true marginal cost of hiring one more worker, exceeding the wage |
| **Interest Rate ($r$)** | The price of loanable funds; the cost of financing capital investment |
| **Present Value (PV)** | The value today of a future payment, discounted at the interest rate |
| **Economic Rent** | Payment to a factor in fixed supply, determined purely by demand |
| **Human Capital** | The stock of skills, education, and experience that raises worker productivity |

---

## Practice Problems

### Problem 1 — Marginal Revenue Product

A furniture shop sells chairs at a competitive price of $P = \$60$. Labor is the only variable input.

| Workers | Total Chairs/Week | $MP_L$ | $MRP_L$ |
|---|---|---|---|
| 1 | 10 | — | — |
| 2 | 18 | — | — |
| 3 | 24 | — | — |
| 4 | 28 | — | — |

**a)** Fill in the $MP_L$ and $MRP_L$ columns.
**b)** If the wage is \$360/week, how many workers should the shop hire?
**c)** If the wage falls to \$240/week, how many workers should the shop hire?

??? success "Solution"
    **a)**

    | Workers | Total Chairs | $MP_L$ | $MRP_L$ |
    |---|---|---|---|
    | 1 | 10 | 10 | \$600 |
    | 2 | 18 | 8 | \$480 |
    | 3 | 24 | 6 | \$360 |
    | 4 | 28 | 4 | \$240 |

    **b)** At $w = \$360$: hire up to where $MRP_L \geq w$. $MRP_L = \$360$ at the 3rd worker, and \$240 < \$360 at the 4th worker, so hire **3 workers**.

    **c)** At $w = \$240$: $MRP_L = \$240$ at the 4th worker, which just covers the wage, so hire **4 workers**.

### Problem 2 — Labor Market Equilibrium

The labor market for registered nurses in a metro area is described by:

$$L^d = 5000 - 100w \qquad L^s = 500 + 150w$$

**a)** Find the equilibrium wage and employment level.
**b)** If a new nursing school graduates an additional cohort, shifting labor supply to $L^s = 1000 + 150w$, find the new equilibrium.
**c)** Explain intuitively why the wage changed as it did.

??? success "Solution"
    **a)** Set $L^d = L^s$: $5000 - 100w = 500 + 150w \Rightarrow 4500 = 250w \Rightarrow w^* = \$18, \; L^* = 5000 - 100(18) = 3200$.

    **b)** Set $5000 - 100w = 1000 + 150w \Rightarrow 4000 = 250w \Rightarrow w^* = \$16, \; L^* = 5000 - 100(16) = 3400$.

    **c)** Labor supply shifted right (more nurses available at every wage), creating a temporary surplus at the old wage of \$18. The wage falls to \$16 to clear the market, and equilibrium employment rises from 3200 to 3400.

### Problem 3 — Monopsony

A monopsonist coal mine is the only employer in an isolated town. It faces labor supply $w = 15 + 0.01L$ and has $MRP_L = 95 - 0.02L$.

**a)** Derive the marginal cost of labor (MCL) curve.
**b)** Find the profit-maximizing level of employment.
**c)** Find the wage the monopsonist actually pays.
**d)** Compare this wage to the value of the marginal worker's output ($MRP_L$) at that employment level, and explain the gap.

??? success "Solution"
    **a)** $TLC = wL = (15 + 0.01L)L = 15L + 0.01L^2 \Rightarrow MCL = 15 + 0.02L$.

    **b)** Set $MRP_L = MCL$: $95 - 0.02L = 15 + 0.02L \Rightarrow 80 = 0.04L \Rightarrow L^* = 2000$.

    **c)** $w^* = 15 + 0.01(2000) = \$35$.

    **d)** $MRP_L$ at $L = 2000$ is $95 - 0.02(2000) = \$55$. The monopsonist pays workers \$35 but each generates \$55 in value — a \$20 gap per worker. This gap is the essence of monopsony power: because the firm is the only buyer, it can pay workers less than their marginal contribution to revenue, and it also hires fewer workers than a competitive market would.

### Problem 4 — Present Value and Investment

A firm is considering a machine costing \$50,000 today. It will produce a single payoff of \$58,000 one year from now.

**a)** If the interest rate is 8%, should the firm buy the machine? Show the present value calculation.
**b)** If the interest rate rises to 20%, should the firm buy the machine?
**c)** Explain, in words, why rising interest rates reduce investment.

??? success "Solution"
    **a)** $PV = \dfrac{58{,}000}{1.08} = \$53{,}703.70$. Since $PV > \$50{,}000$ cost, the firm **should buy** the machine (positive NPV of \$3,703.70).

    **b)** $PV = \dfrac{58{,}000}{1.20} = \$48{,}333.33$. Since $PV < \$50{,}000$ cost, the firm **should not buy** the machine (negative NPV of -\$1,666.67).

    **c)** A higher interest rate raises the opportunity cost of tying up funds in a project (or raises the cost of borrowing to finance it), so it discounts future payoffs more heavily. Projects that were profitable at a low interest rate become unprofitable at a higher one, so investment demand falls as interest rates rise.

### Problem 5 — Economic Rent

A unique beachfront lot can only be used for one restaurant. Three restaurant chains bid for the annual lease: Chain A values it at \$200,000/year, Chain B at \$150,000/year, Chain C at \$90,000/year. The lot has no alternative use and costs the owner nothing to maintain.

**a)** What is the equilibrium annual lease payment, assuming competitive bidding?
**b)** How much of this payment is economic rent? Explain why.
**c)** Suppose a new highway exit dramatically increases foot traffic near the lot, raising each chain's valuation by \$50,000. What happens to the rent, and why does supply play no role?

??? success "Solution"
    **a)** Competitive bidding drives the lease price up to the second-highest valuation (since Chain A will outbid Chain B by any amount up to \$150,000, but has no reason to pay more than necessary to win) — approximately **\$150,000/year** (the lot goes to Chain A at a price just above Chain B's valuation).

    **b)** Because the lot's supply is fixed (there is exactly one such lot and no cost of maintaining it), the entire \$150,000 payment is **economic rent** — it does not reflect any production cost, only the value of controlling a scarce resource.

    **c)** All valuations rise by \$50,000 (Chain A to \$250,000, Chain B to \$200,000), so the equilibrium rent rises to approximately **\$200,000/year**. Supply plays no role because the lot's supply curve is vertical — the quantity of this specific lot cannot increase no matter how valuable it becomes; the entire effect of increased demand falls on price (rent), not quantity.

---

!!! mascot-celebration "You Just Priced Every Factor of Production"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Labor, capital, and land each have their own market, their own logic, and their own quirks — monopsony power, present value, fixed supply — and you worked through all of them. You can now explain why wages differ, why interest rates matter for investment, and why a beachfront lot commands a premium that has nothing to do with the cost of building on it.

!!! tip "Next Chapter"
    In [Chapter 12: Market Failures](../12-market-failures/index.md), we step back from well-functioning competitive markets to examine *why* markets sometimes fail to deliver efficient outcomes — and what role government can play in response.
