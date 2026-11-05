# Chapter 9: Oligopoly

## Learning Objectives

After completing this chapter, you will be able to:

1. Identify the characteristics that distinguish oligopoly from the other market structures
2. Solve for the Cournot (quantity-setting) equilibrium in a duopoly
3. Solve for the Bertrand (price-setting) equilibrium and explain the Bertrand paradox
4. Explain why collusion is profitable but unstable, using the OPEC cartel as an example
5. Use the kinked demand curve model to explain price rigidity in oligopoly
6. Calculate and interpret concentration ratios and the Herfindahl-Hirschman Index (HHI)
7. Describe the goals of antitrust law and competition policy

---

!!! mascot-welcome "A Few Big Players, All Watching Each Other"
    ![Professor Owl waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Welcome to the market structure where rivals can't ignore each other! In perfect competition and monopoly, a firm could set its price or quantity without a second thought about what anyone else was doing — not here. Every choice has a trade-off, and in oligopoly your trade-offs are tangled up with your rivals' trade-offs too. Get ready to think like a strategist, not just a profit-maximizer.

## 9.1 Characteristics of Oligopoly

An **oligopoly** is a market structure with a *small number of large sellers*, each of whom has market power and is aware that its own pricing and output decisions affect — and are affected by — the decisions of its rivals.

!!! example "Real-world oligopolies"
    - Commercial aircraft manufacturing (Boeing, Airbus)
    - U.S. wireless carriers (Verizon, AT&T, T-Mobile)
    - Breakfast cereal (Kellogg's, General Mills, Post)
    - Crude oil production (OPEC member states and a handful of non-OPEC producers)

The defining feature of oligopoly is **strategic interdependence**: unlike a perfectly competitive firm (which ignores its rivals because each is too small to matter) or a monopolist (which has no rivals), an oligopolist must explicitly anticipate how its competitors will react to its choices. This is why oligopoly is the market structure in which **game theory** (Chapter 10) becomes indispensable.

| Feature | Perfect Competition | Monopoly | Oligopoly |
|---|---|---|---|
| Number of sellers | Many | One | Few |
| Market power | None | Substantial | Significant, but checked by rivals |
| Awareness of rivals | None needed | No rivals | Essential |
| Barriers to entry | None | High | Usually high |
| Price-setting | Price taker | Price maker | Strategic — depends on rivals |

Entry barriers in oligopoly resemble those in monopoly: economies of scale, high capital requirements, patents, and network effects. What makes oligopoly analytically distinct is not the barrier itself but the fact that *a few* firms, not one, clear the market and interact repeatedly.

!!! mascot-thinking "The Mental Shift: You Can't Optimize Alone Anymore"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Notice what just changed. In every market structure so far, a firm could maximize profit by looking only at its own costs and demand. Here, the right choice depends on a guess about what rivals will do — and their choice depends on a guess about you. That circular reasoning is exactly what game theory, coming up in Chapter 10, was invented to resolve.

---

## 9.2 The Cournot Model: Competing in Quantities

The **Cournot model** (named for French economist Antoine Augustin Cournot, 1838) assumes that firms simultaneously and independently choose *quantities* to produce, each firm correctly anticipating the other's output choice in equilibrium.

Consider a duopoly (two firms, Firm 1 and Firm 2) producing an identical good with inverse market demand:

\[P = a - b(Q_1 + Q_2)\]

!!! mascot-encourage "Yes, There's Calculus Ahead — You're Ready for It"
    ![Professor Owl encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If a derivative-based equilibrium makes your stomach drop a little, that's a completely normal reaction — this is genuinely one of the more demanding derivations in the course. Take it one line at a time: write the profit function, take one derivative, set it to zero. You've already made this exact move in the monopoly chapter; the only new wrinkle is that your rival's quantity sits in the equation as a fixed number you don't control.

Each firm has constant marginal cost $c$. Firm 1's profit is:

\[\pi_1 = [a - b(Q_1 + Q_2)]Q_1 - cQ_1\]

Taking the derivative with respect to $Q_1$ (treating $Q_2$ as given) and setting it to zero gives Firm 1's **best-response function**:

\[Q_1 = \frac{a - c - bQ_2}{2b}\]

By symmetry, Firm 2's best response is $Q_2 = \dfrac{a - c - bQ_1}{2b}$.

!!! example "Numerical Cournot equilibrium"
    Let $P = 100 - (Q_1 + Q_2)$ and $c = 10$ for both firms (so $a = 100$, $b = 1$).

    Firm 1's best response: $Q_1 = \dfrac{90 - Q_2}{2}$. By symmetry, $Q_2 = \dfrac{90 - Q_1}{2}$.

    Substituting the symmetric condition $Q_1 = Q_2 = Q^*$:

    \[Q^* = \frac{90 - Q^*}{2} \implies 2Q^* = 90 - Q^* \implies Q^* = 30\]

    Each firm produces **30 units**; total quantity $Q = 60$; market price $P = 100 - 60 = \$40$.

    Compare this to the **competitive outcome** ($P = MC = 10 \implies Q = 90$) and the **monopoly (collusive) outcome** (a single firm maximizing joint profit produces $Q_m = 45$, $P = \$55$). Cournot duopoly output (60) lies between the competitive output (90) and the monopoly output (45) — more sellers push output up and price down toward the competitive level.

Solving the two best-response equations simultaneously and plotting them on a graph with $Q_1$ on one axis and $Q_2$ on the other produces two downward-sloping lines; their intersection is the **Cournot-Nash equilibrium**, the point where each firm's output is a best response to the other's.

!!! note "More firms, more competition"
    With $n$ symmetric Cournot firms, it can be shown that equilibrium industry output converges toward the competitive level as $n \to \infty$, and price converges toward marginal cost. Cournot competition with a large number of firms behaves increasingly like perfect competition — a useful bridge between the two models.

---

## 9.3 The Bertrand Model: Competing in Prices

The **Bertrand model** (Joseph Bertrand, 1883) assumes firms compete by simultaneously choosing *prices* rather than quantities, with consumers buying entirely from whichever firm charges the lower price (splitting demand if prices are tied).

With identical products and constant marginal cost $c$, consider what happens if Firm 1 sets $P_1 > c$. Firm 2 can capture the *entire* market by setting $P_2$ just below $P_1$, as long as $P_2 > c$ still yields a profit. Each firm has an incentive to undercut the other — a race that stops only when price equals marginal cost.

\[P_1 = P_2 = MC\]

This is the **Bertrand paradox**: with only *two* identical firms, price competition alone (no capacity limits, homogeneous goods) drives price all the way down to the competitive, zero-economic-profit level — the same outcome as perfect competition, even though only two firms exist.

!!! warning "Why the Bertrand paradox rarely holds exactly"
    Real-world duopolies rarely show marginal-cost pricing. The paradox weakens once we introduce:

    - **Product differentiation** (firms are not perfect substitutes, so undercutting doesn't capture 100% of rivals' sales)
    - **Capacity constraints** (a firm cannot always serve the whole market even at the lowest price)
    - **Repeated interaction** (firms can sustain higher prices through implicit cooperation — see Section 9.4 and Chapter 10)

The contrast between Cournot and Bertrand illustrates an important lesson: **the strategic variable firms compete on (quantity vs. price) changes the predicted outcome**, even holding the number of firms and cost structure fixed.

!!! mascot-thinking "Same Firms, Same Costs, Totally Different Outcomes"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Step back and compare the two models: Cournot firms competing on quantity land on a price above marginal cost, but Bertrand firms competing on price crash all the way down to marginal cost — same two firms, same costs, same demand curve, wildly different results. Carry that forward as your mental model: in oligopoly, *how* firms compete matters just as much as *how many* firms there are.

---

## 9.4 Collusion and Cartels

**Collusion** occurs when oligopolists coordinate their pricing or output decisions to behave jointly like a monopolist, raising price above the competitive (or Cournot) level and increasing joint profit. A formal, explicit collusive agreement among firms is called a **cartel**.

!!! example "OPEC: the world's most visible cartel"
    The Organization of the Petroleum Exporting Countries (OPEC) coordinates crude-oil production quotas among member nations to influence the world price of oil. When members comply with assigned quotas, world output falls below the competitive level and price rises — exactly as the cartel model predicts. OPEC's history, however, also illustrates the model's central weakness.

**Why collusion is profitable:** Joint profit is maximized by restricting output to the monopoly level and dividing it (and the associated economic profit) among members — strictly more profit than any member could earn acting alone at the competitive or Cournot output.

**Why collusion is unstable:** Each cartel member faces a powerful incentive to **cheat** — secretly producing more than its assigned quota. If a quota holds price at the monopoly level $P_m$ while a member's marginal cost is well below $P_m$, that member earns extra profit on every unit it sneaks past its quota, *as long as other members don't retaliate*. Because every member faces this same temptation simultaneously, the gains from mutual restriction — the cartel — tend to unravel. This instability is formally a prisoner's dilemma, developed fully in Chapter 10.

- In most countries, cartels among *domestic* firms are **illegal** under antitrust law (Section 9.6) — this is precisely why OPEC, a cartel among sovereign *nations*, can operate openly, while a cartel among U.S. airlines could not.
- Price-fixing conspiracies prosecuted under U.S. antitrust law include historical cases in lysine, vitamins, and electrical equipment manufacturing.

---

## 9.5 The Kinked Demand Curve Model

The **kinked demand curve model** (Paul Sweezy, 1939) explains a puzzling empirical regularity: oligopoly prices often stay unchanged for long stretches even as costs fluctuate modestly — a phenomenon called **price rigidity**.

The model assumes an asymmetric belief about rival behavior:

- If a firm **raises** its price above the current level, rivals will **not** follow — they are happy to keep their own price low and capture the firm's customers. Demand for the price-raising firm is therefore **highly elastic** above the current price.
- If a firm **lowers** its price below the current level, rivals **will** match the cut to avoid losing market share. Demand for the price-cutting firm is therefore **much less elastic** below the current price.

This creates a demand curve with a **kink** at the current price $P^*$ — relatively flat above $P^*$, steeper below it. Because marginal revenue has a discontinuous (vertical) jump at the output level corresponding to the kink, a *range* of marginal costs can all intersect that vertical segment at the same quantity, leaving the firm's profit-maximizing price unchanged even though its costs shifted.

!!! tip "The intuition in one sentence"
    A firm that believes "rivals will match my price cuts but ignore my price increases" has every reason to leave price alone — any price change in either direction loses relative to the status quo.

The kinked demand curve describes *behavior that sustains a price*, not how that price was originally set — it explains rigidity around an existing equilibrium rather than predicting what that equilibrium will be.

---

## 9.6 Measuring Market Concentration

Economists and antitrust regulators quantify how "oligopolistic" an industry is using **concentration measures** computed from each firm's market share.

**Concentration ratio (CR$_n$):** the combined market share of the largest $n$ firms.

\[CR_4 = s_1 + s_2 + s_3 + s_4\]

where $s_i$ is firm $i$'s market share (ranked largest to smallest).

**Herfindahl-Hirschman Index (HHI):** the sum of squared market shares (shares expressed as whole-number percentages, e.g., 25 for 25%), giving more weight to large firms than CR$_n$ does.

\[HHI = \sum_{i=1}^{n} s_i^2\]

| Market Structure | Example $s_i$ | HHI |
|---|---|---|
| Perfect competition (many tiny firms) | 100 firms at 1% each | $100 \times 1^2 = 100$ |
| Duopoly, equal shares | Two firms at 50% each | $50^2 + 50^2 = 5{,}000$ |
| Pure monopoly | One firm at 100% | $100^2 = 10{,}000$ |

!!! mascot-tip "A Quick Way to Sanity-Check Any HHI"
    ![Professor Owl with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Want to catch an arithmetic slip before you report a wrong HHI? The market shares should sum to roughly 100, so the squared terms can never add up anywhere near 10,000 unless one firm is close to a true monopoly. And remember, it's the squaring that punishes a handful of giants — equal shares split among more firms always pulls HHI down.

The U.S. Department of Justice and Federal Trade Commission use HHI thresholds to screen proposed mergers:

- **HHI below 1,500:** unconcentrated market — mergers rarely challenged
- **HHI between 1,500 and 2,500:** moderately concentrated — mergers scrutinized, especially large HHI increases
- **HHI above 2,500:** highly concentrated — mergers face the greatest scrutiny

!!! example "Computing HHI"
    An industry has five firms with market shares of 30%, 25%, 20%, 15%, and 10%.

    \[HHI = 30^2 + 25^2 + 20^2 + 15^2 + 10^2 = 900 + 625 + 400 + 225 + 100 = 2{,}250\]

    An HHI of 2,250 falls in the "moderately concentrated" range — a proposed merger between the two largest firms (which would push HHI well above 2,500) would likely draw regulatory scrutiny.

---

## 9.7 Antitrust Law and Competition Policy

**Antitrust law** (called *competition law* outside the United States) is the body of government policy aimed at preventing monopolization, collusion, and anticompetitive mergers in order to protect consumers and preserve market efficiency.

Key pillars of U.S. antitrust policy:

- **Sherman Antitrust Act (1890):** prohibits contracts, combinations, or conspiracies in restraint of trade (Section 1 — targets price-fixing and cartels) and monopolization (Section 2)
- **Clayton Act (1914):** prohibits mergers and acquisitions that would substantially lessen competition, along with specific practices like price discrimination that harms competition
- **Federal Trade Commission Act (1914):** created the FTC and prohibits "unfair methods of competition"

!!! note "What antitrust enforcement targets"
    - **Horizontal price-fixing** — direct agreements among competitors to set prices or output (per se illegal; no defense is accepted)
    - **Anticompetitive mergers** — combinations that would push concentration and market power too high (evaluated partly using HHI, Section 9.6)
    - **Predatory and exclusionary conduct** — e.g., a dominant firm pricing below cost specifically to drive out rivals, then raising prices once competitors exit

!!! mascot-warning "Bigness Isn't the Crime — Conduct Is"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A common trap: assuming a large market share is itself illegal. It isn't. Antitrust law targets *conduct* — price-fixing agreements, exclusionary tactics, mergers that would substantially lessen competition — not the mere fact that a firm is big or dominant. A monopolist that earned its position through a better product has broken no law; a cartel of modest-sized firms that agreed to fix prices has.

Competition policy reflects the same core trade-off this chapter has developed: a few large firms can achieve scale efficiencies unavailable to many small ones, but without a competitive check, they can also exercise the market power this chapter's models all describe — raising prices above, and restricting output below, the competitive levels that maximize total surplus.

#### Diagram: Cournot Duopoly Best-Response Explorer

<details markdown="1">
<summary>Cournot Duopoly Best-Response Explorer</summary>
Type: microsim
**sim-id:** cournot-best-response<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** compute<br/>
**Learning Objective:** The learner will compute each firm's best-response quantity in successive rounds using the chapter's Cournot best-response functions, and iterate toward the Cournot-Nash equilibrium.

**Prerequisites:** Cournot model, best-response function, Cournot-Nash equilibrium (Section 9.2).

**Evidence of Mastery:** Starting from Q1=0, the learner computes each of the first 4 best-response rounds in order, each checked to within ±0.5 units. Correct when all 4 rounds match. Mastery is 4 of 4 correct.

**Misconceptions:** (1) Updating both firms simultaneously each round using each other's just-computed value, rather than alternating as the chapter's sequential process describes. (2) Believing the iteration converges to the competitive quantity (90) or the monopoly quantity (45) rather than 30,30. (3) Forgetting to divide by 2 in the best-response formula.

**Instructional Rationale:** An Apply-level task needs the learner to execute the given best-response formula repeatedly on new inputs, which is why each round is scored as a distinct computation rather than only the final equilibrium.

**Content:**

The chapter's own numeric case (Section 9.2): P = 100 − (Q1+Q2), c = 10 for both firms, best responses Q1=(90−Q2)/2 and Q2=(90−Q1)/2.

Iteration sequence starting from Q1=0, alternating firms:

| Round | Firm responding | Input | Best response |
|---|---|---|---|
| 1 | Firm 2 responds to Q1=0 | Q1=0 | Q2 = 45 |
| 2 | Firm 1 responds to Q2=45 | Q2=45 | Q1 = 22.5 |
| 3 | Firm 2 responds to Q1=22.5 | Q1=22.5 | Q2 = 33.75 |
| 4 | Firm 1 responds to Q2=33.75 | Q2=33.75 | Q1 = 28.125 |

Equilibrium (after many rounds): Q1=Q2=30, total Q=60, P=\$40. Benchmarks: competitive Q=90 (P=MC=10); monopoly (collusive) Qm=45, P=\$55.

**Provenance:** From the chapter's own "Numerical Cournot equilibrium" example in Section 9.2.

**Rules:** Q1 = (90 − Q2)/2; Q2 = (90 − Q1)/2. Each round, the firm not currently moving holds its quantity fixed at its last chosen value while the other firm best-responds. Firm 1's starting quantity: min 0, max 90, step 5, default 0.

**Learner Activity:**

1. The learner sets Firm 1's starting quantity to 0 and presses "Step" to compute Round 1 (Firm 2's best response to Q1=0), typing the result before it is revealed.
2. The sim checks the value (45) and plots the point.
3. The learner presses "Step" for Round 2 (Firm 1's best response to Q2=45), types the result, and the sim checks it (22.5).
4. The learner continues through Rounds 3 and 4, each checked against the sequence above.
5. After 4 rounds, the learner can keep pressing "Step" to watch the sequence converge toward Q1=Q2=30, compared against the competitive (90) and monopoly (45) benchmarks marked on the same axis.

**Feedback:** 4 rounds, fixed order, two attempts each. Correct: "Correct: Q = <value>." Incorrect (first attempt): "Apply the best-response formula to the other firm's most recently chosen quantity, then divide by 2." After the second wrong attempt, the correct value is shown. A running count "Rounds correct: n of 4" is shown.

**Starting State:** Firm 1's quantity is set to 0, Firm 2's quantity is blank, and the two best-response lines are plotted on a Q1–Q2 graph with their intersection not yet marked. The question on screen is "If Firm 1 produces 0 units, what is Firm 2's best response?"

**Chapter Anchors:** The chapter's Section 9.2 worked example states the Cournot-Nash equilibrium is Q1=Q2=30 (total Q=60, P=\$40), compared to the competitive outcome (Q=90) and the monopoly outcome (Qm=45, P=\$55); the sim's equilibrium and benchmarks reproduce these values exactly.
</details>

---

## Key Terms

| Term | Definition |
|---|---|
| **Oligopoly** | A market with a small number of large, interdependent sellers |
| **Strategic interdependence** | Each firm's optimal decision depends on rivals' decisions |
| **Cournot model** | Firms simultaneously choose quantities, each anticipating the other's output |
| **Best-response function** | A firm's optimal choice given a specific (fixed) choice by its rival |
| **Cournot-Nash equilibrium** | The quantity pair at which each firm's output is a best response to the other's |
| **Bertrand model** | Firms simultaneously choose prices; lowest price captures the market |
| **Bertrand paradox** | Price competition between just two identical firms drives price to marginal cost |
| **Collusion** | Coordination among firms to raise joint profit above the non-cooperative level |
| **Cartel** | A formal, explicit collusive agreement among firms |
| **Kinked demand curve** | A demand curve with a kink at the current price, explaining price rigidity |
| **Concentration ratio (CR$_n$)** | Combined market share of the largest $n$ firms |
| **Herfindahl-Hirschman Index (HHI)** | Sum of squared market shares; used to screen mergers |
| **Antitrust law** | Government policy preventing monopolization, collusion, and anticompetitive mergers |

---

## Practice Problems

### Problem 1 — Cournot Equilibrium

Two firms compete in a Cournot duopoly with market demand $P = 120 - (Q_1 + Q_2)$ and identical marginal cost $c = 20$.

**a)** Find each firm's best-response function.  
**b)** Solve for the Cournot-Nash equilibrium quantities and price.  
**c)** Compare total output to the competitive output ($P = MC$) and the monopoly output.

??? success "Solution"
    **a)** Firm 1 maximizes $\pi_1 = [120 - Q_1 - Q_2]Q_1 - 20Q_1$. Taking $\partial \pi_1/\partial Q_1 = 0$:
    
    $$120 - 2Q_1 - Q_2 - 20 = 0 \implies Q_1 = \frac{100 - Q_2}{2}$$
    
    By symmetry, $Q_2 = \dfrac{100 - Q_1}{2}$.

    **b)** Imposing symmetry $Q_1 = Q_2 = Q^*$: $Q^* = \dfrac{100 - Q^*}{2} \implies 2Q^* = 100 - Q^* \implies Q^* = 33.33$.
    
    Total output $Q = 66.67$; price $P = 120 - 66.67 = \$53.33$.

    **c)** Competitive output: $P = MC \implies 120 - Q = 20 \implies Q = 100$. Monopoly output: maximize $[120-Q]Q - 20Q \implies Q_m = 50$. Cournot output (66.67) lies between monopoly (50) and competitive (100), as expected.

### Problem 2 — Bertrand Competition

Two firms sell an identical product with marginal cost $c = \$15$. Under Bertrand competition, what price will prevail in equilibrium? Explain why neither firm can profitably deviate.

??? success "Solution"
    Equilibrium price $P_1 = P_2 = \$15 = MC$. If either firm priced above \$15, the other could undercut it by a cent, capture the entire market, and still earn a positive margin — so prices above \$15 cannot be an equilibrium. Neither firm will price below \$15 because that guarantees a loss on every unit sold. The only price from which neither firm wants to deviate is $P = MC = \$15$, the same outcome as perfect competition.

### Problem 3 — HHI and Merger Review

An industry has four firms with market shares 40%, 30%, 20%, and 10%.

**a)** Calculate the industry's HHI.  
**b)** The two smallest firms (20% and 10%) propose to merge. Calculate the post-merger HHI.  
**c)** Would this merger likely draw antitrust scrutiny? Explain using the DOJ/FTC thresholds.

??? success "Solution"
    **a)** $HHI = 40^2 + 30^2 + 20^2 + 10^2 = 1{,}600 + 900 + 400 + 100 = 3{,}000$.

    **b)** Post-merger, the combined firm has $20 + 10 = 30\%$ share, alongside the 40% and 30% firms: $HHI = 40^2 + 30^2 + 30^2 = 1{,}600 + 900 + 900 = 3{,}400$. The HHI increase is $3{,}400 - 3{,}000 = 400$.

    **c)** The market was already "highly concentrated" (HHI > 2,500) before the merger, and the merger increases HHI further (by 400 points). Under DOJ/FTC guidelines, mergers in already highly concentrated markets that increase HHI by more than 100 points are presumed likely to enhance market power — this merger would very likely draw significant antitrust scrutiny.

### Problem 4 — Cartel Instability

Two firms in a cartel agree to split the market and each charge the monopoly price of \$60, with marginal cost of \$20 for each. Secretly, Firm A considers cutting its price to \$55 while Firm B keeps its price at \$60, capturing all of the market's 100 units.

**a)** What does Firm A earn if it cheats and Firm B does not retaliate?  
**b)** What would Firm A earn if it honored the agreement and received half of the market at \$60?  
**c)** Why is this an unstable arrangement even though both firms are better off than under competition?

??? success "Solution"
    **a)** Cheating profit: $(55 - 20) \times 100 = \$3{,}500$.

    **b)** Honoring the agreement: assume the cartel's total quantity at $P=\$60$ is 50 units; Firm A's half-share profit: $(60-20) \times 25 = \$1{,}000$ (using a 50-unit total split evenly).

    **c)** Even though both arrangements beat the competitive outcome, each firm individually gains far more by secretly undercutting the agreed price while the other complies — exactly the logic of a prisoner's dilemma (Chapter 10). Because *both* firms recognize this incentive, the cartel tends to break down unless firms can detect and punish cheating (e.g., through repeated interaction).

### Problem 5 — Kinked Demand

A firm believes that if it raises its price, no rival will follow, but if it cuts its price, every rival will match the cut. Using this belief, explain why the firm might leave its price unchanged even after a 10% increase in its marginal cost.

??? success "Solution"
    Above the current price, demand is highly elastic (rivals don't follow a price increase, so the firm loses most of its customers to competitors) — raising price loses more in volume than it gains in margin. Below the current price, demand is much less elastic (rivals match the cut, so the firm doesn't gain market share, it just earns less per unit on the same customers) — cutting price loses margin without gaining volume. Because marginal revenue jumps discontinuously at the kink, a range of marginal costs — including the cost both before and after a moderate 10% increase — can all still point to the same profit-maximizing output and price. The firm rationally leaves its price unchanged.

---

!!! mascot-celebration "You Just Tamed Four of the Toughest Models in the Course"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Cournot, Bertrand, cartel instability, and kinked demand — you worked through all four, and you can now calculate equilibria, spot a doomed cartel, and explain why prices sometimes just don't move. That's strategic thinking, and it's exactly what Chapter 10 builds on next.

!!! tip "Next Chapter"
    In [Chapter 10: Game Theory](../10-game-theory/index.md), we formalize the strategic reasoning this chapter relied on informally — dominant strategies, Nash equilibrium, and the prisoner's dilemma — giving us the tools to fully explain why cartels break down and how firms sustain cooperation when they interact repeatedly.
