# Chapter 6: Perfect Competition

## Learning Objectives

After completing this chapter, you will be able to:

1. Identify the four characteristics that define a perfectly competitive market
2. Explain why a competitive firm is a "price taker" and graph its demand and marginal revenue curves
3. Apply the MR = MC rule to find a competitive firm's profit-maximizing output
4. Apply the shutdown rule to determine a firm's short-run supply decision
5. Derive the short-run industry supply curve from individual firms' marginal cost curves
6. Distinguish short-run and long-run equilibrium in a competitive industry
7. Explain why economic profit is driven to zero in long-run competitive equilibrium
8. Use consumer and producer surplus to show that competitive equilibrium is allocatively efficient

---

!!! mascot-welcome "The Benchmark Market"
    ![Professor Owl waving hello](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Perfect competition is the model every other market structure in this book gets compared against. Learn its MR = MC logic well here, in its simplest form, and Chapters 7 through 9 will feel like variations on a theme rather than brand-new material. Every choice has a trade-off, and here you'll see firms make that trade-off with zero power over price.

## 6.1 Characteristics of Perfectly Competitive Markets

**Perfect competition** is a market structure characterized by four conditions:

1. **Many buyers and many sellers**, each too small to individually influence the market price.
2. **A standardized (homogeneous) product** — consumers view every seller's output as identical, so there is no reason to prefer one seller over another based on the product itself.
3. **Free entry and exit** — firms can enter the industry when profits are attractive and exit when losses persist, with no significant barriers.
4. **Perfect information** — buyers and sellers have full knowledge of prices and product quality.

!!! example "Approximations to perfect competition"
    No real-world market perfectly satisfies all four conditions, but several come close: commodity agricultural markets (wheat, corn), foreign exchange markets, and many online markets for standardized goods. Even if imperfect, the competitive model is a powerful benchmark against which to measure other market structures (studied in Chapters 7–9).

---

## 6.2 The Competitive Firm as a Price Taker

Because a competitive firm is one of many sellers of an identical product, it has **no ability to influence the market price** — it is a **price taker**. If a wheat farmer tried to charge above the market price, buyers would simply purchase from any of thousands of other farmers selling identical wheat. If the farmer charged below market price, they would needlessly sacrifice revenue, since they can already sell as much as they want at the market price.

This means the individual competitive firm faces a **horizontal (perfectly elastic) demand curve** at the market price $P^*$, even though the *market* demand curve is downward sloping (recall from Chapter 3 that $E_d \to \infty$ at the firm level).

### Marginal Revenue for a Price Taker

Since the firm can sell every unit at the same price $P^*$, each additional unit sold adds exactly $P^*$ to total revenue:

$$MR = \frac{\Delta TR}{\Delta Q} = P^*$$

For a perfectly competitive firm: $P^* = MR$. This is a special simplification that will *not* hold for the imperfectly competitive firms studied in Chapters 7–9.

!!! mascot-thinking "Price-Taking Is the Special Case"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    $MR = P$ only holds because a competitive firm can sell unlimited units at one fixed price. Remember this carefully — starting next chapter, firms with market power face falling marginal revenue, and this simplification disappears.

---

## 6.3 Profit Maximization: The MR = MC Rule

Every firm, regardless of market structure, maximizes profit by producing the quantity at which **marginal revenue equals marginal cost**:

$$MR = MC$$

**Intuition:** If $MR > MC$, producing one more unit adds more to revenue than to cost — profit rises, so the firm should produce more. If $MR < MC$, the last unit cost more to produce than it earned — profit falls, so the firm should produce less. Only where $MR = MC$ is profit maximized (with the second-order condition that $MC$ is rising at that point).

For a competitive firm, since $MR = P^*$, the rule becomes:

$$P^* = MC$$

### Worked Example

A competitive firm faces a market price of $P^* = \$40$. Its cost schedule is:

| $Q$ | $TC$ | $MC$ | $TR$ ($=40Q$) | Profit |
|---|---|---|---|---|
| 0 | \$50 | — | \$0 | −\$50 |
| 1 | \$80 | \$30 | \$40 | −\$40 |
| 2 | \$105 | \$25 | \$80 | −\$25 |
| 3 | \$135 | \$30 | \$120 | −\$15 |
| 4 | \$170 | \$35 | \$160 | −\$10 |
| 5 | \$210 | \$40 | \$200 | −\$10 |
| 6 | \$255 | \$45 | \$240 | −\$15 |

At $Q=5$, $MC=\$40$ exactly equals $P^*=MR=\$40$ — profit is maximized (tied with $Q=4$ at −\$10, but $Q=5$ is the last unit where $MC \leq MR$; producing the 6th unit would reduce profit since $MC=\$45 > MR=\$40$). The firm maximizes profit (minimizes loss) at $Q^*=5$, earning profit of **−\$10**.

---

## 6.4 Short-Run Supply Decision and the Shutdown Rule

In the short run, a firm has already incurred its fixed costs regardless of whether it produces. The question the firm faces is not "should I exist?" but **"should I produce at all, or shut down (produce zero) this period?"**

**The Shutdown Rule:** A firm should continue to produce in the short run as long as the price it receives covers average variable cost:

$$P^* \geq AVC_{\min} \implies \text{produce } Q \text{ where } P^*=MC$$

$$P^* < AVC_{\min} \implies \text{shut down (produce } Q=0\text{)}$$

!!! mascot-warning "Shutting Down Isn't Going Out of Business"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    "Shut down" here means producing zero *this period* while still paying fixed costs — not permanently closing. A firm can shut down in a slow month and reopen once price recovers.

**Intuition:** If $P^* \geq AVC$, the firm covers all its variable costs and contributes at least something toward fixed costs — producing is better than shutting down, even if the firm is making an overall loss (since fixed costs must be paid either way in the short run). If $P^* < AVC$, the firm cannot even cover the variable cost of production — every unit sold loses money beyond its direct cost, so it is better to produce nothing and lose only the fixed cost.

!!! example "Why 'losing money while producing' can be the right call"
    A restaurant with a \$5,000/month lease (a sunk fixed cost in the short run) finds that at the going price, revenue covers all ingredient and labor costs (variable costs) plus \$2,000 toward the lease. Shutting down would mean losing the full \$5,000 lease payment with zero revenue; staying open loses only \$3,000 (the \$5,000 lease minus the \$2,000 contribution). The restaurant should **stay open**, even though it is losing money overall.

### The Short-Run Supply Curve of a Firm

The competitive firm's short-run supply curve is the portion of its marginal cost curve that lies **at or above the minimum point of AVC**. For any price below that threshold, the firm supplies zero.

$$\text{Firm's short-run supply curve} = MC \text{ curve, for all } P \geq AVC_{\min}$$

!!! mascot-tip "One Number Decides Everything"
    ![Professor Owl sharing a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Facing a shutdown question? You only need two numbers: price and minimum AVC. Skip the full profit calculation — just compare those two and the decision falls out immediately.

---

## 6.5 Short-Run Industry Supply Curve

The **short-run industry (market) supply curve** is obtained by **horizontally summing** the supply curves (the relevant portions of $MC$ above $AVC_{\min}$) of every individual firm in the industry, at each price.

!!! example "Horizontal summation"
    Suppose an industry has 1,000 identical firms, and at a price of \$40, each individual firm supplies 5 units (as in the Section 6.3 example). The industry quantity supplied at $P=\$40$ is $1{,}000 \times 5 = 5{,}000$ units. Repeating this calculation at every price generates the industry supply curve.

| Price | Quantity Supplied per Firm | Number of Firms | Industry Quantity Supplied |
|---|---|---|---|
| \$30 | 3 | 1,000 | 3,000 |
| \$35 | 4 | 1,000 | 4,000 |
| \$40 | 5 | 1,000 | 5,000 |
| \$45 | 6 | 1,000 | 6,000 |

This is exactly the market supply curve introduced in Chapter 2, now derived rigorously from firms' marginal cost curves and profit-maximizing behavior.

---

## 6.6 Short-Run vs. Long-Run Equilibrium

### Short-Run Equilibrium

In the **short run**, the number of firms in the industry is fixed (entry/exit takes time). The market price is determined by the intersection of the (fixed-number-of-firms) short-run industry supply curve and market demand. At this price, individual firms may earn:

- **Positive economic profit** (price exceeds average total cost)
- **Zero economic profit** (price equals average total cost — "normal profit")
- **A loss** (price is below average total cost, but above $AVC_{\min}$, so the firm still produces)

!!! note "Economic profit vs. accounting profit"
    **Economic profit** subtracts *all* costs, including the opportunity cost of the owner's time and capital (implicit costs), from revenue. **Accounting profit** subtracts only explicit (out-of-pocket) costs. A firm can show positive accounting profit while earning zero or negative economic profit — meaning its resources could have earned more being used elsewhere.

### Long-Run Equilibrium

In the **long run**, firms can enter or exit the industry freely (one of the four defining conditions from Section 6.1):

- If firms are earning **positive economic profit**, new firms are attracted into the industry. Entry increases industry supply, shifting the supply curve right, which **lowers the market price** until profit is driven to zero.
- If firms are earning **negative economic profit** (losses), existing firms exit the industry. Exit decreases industry supply, shifting the supply curve left, which **raises the market price** until the remaining firms earn zero economic profit.

This entry-and-exit process continues until price settles exactly at the **minimum point of each firm's long-run average cost curve**, where economic profit is exactly zero.

---

## 6.7 Zero Economic Profit in the Long Run

**Long-run competitive equilibrium** occurs where:

$$P^* = MR = MC = ATC_{\min}$$

At this point, each firm earns exactly **zero economic profit** — meaning it earns a "normal" return just sufficient to keep its resources employed in this industry (no better use of those resources exists elsewhere), but no *excess* return that would attract further entry.

!!! warning "Zero economic profit is not the same as going broke"
    Zero economic profit means the firm is earning exactly the market rate of return on its invested resources — comparable to what the owner could earn in their next-best alternative. It is a perfectly sustainable, "break-even" outcome in the economic sense, not a sign of business failure.

### Worked Example: Long-Run Adjustment

!!! mascot-encourage "Dividing Market by Firm Size, Step by Step"
    ![Professor Owl giving encouragement](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    Finding the long-run number of firms looks like a lot of moving parts at once — demand, ATC minimum, firm output — but it's really just one division at the end. Follow the three steps below in order and it resolves quickly.

Suppose the long-run average cost curve of every (identical) firm in a competitive industry has its minimum at $ATC_{\min} = \$20$ per unit, occurring at an output of 100 units per firm.

**Step 1:** In long-run equilibrium, price must equal \$20 (otherwise entry or exit would still be occurring).

**Step 2:** Suppose market demand at $P=\$20$ is $Q_D = 50{,}000$ units.

**Step 3:** The number of firms in long-run equilibrium is:

$$\text{Number of firms} = \frac{Q_D}{q_{\text{firm}}} = \frac{50{,}000}{100} = 500 \text{ firms}$$

If demand increased, price would temporarily rise above \$20 in the short run (attracting entry), and the number of firms would increase until price returned to \$20 in the new long-run equilibrium.

---

## 6.8 Consumer and Producer Surplus; Allocative Efficiency

Recall from Chapter 2: **consumer surplus** is the area below the demand curve and above the price; **producer surplus** is the area above the supply curve and below the price. Competitive equilibrium (where $S=D$) maximizes **total surplus** (CS + PS).

### Why Competitive Equilibrium Is Allocatively Efficient

**Allocative efficiency** occurs when resources are allocated to produce the combination of goods that society values most, given its resources — formally, when price equals marginal cost ($P = MC$) for every good, so that the value society places on the last unit produced (captured by price, which reflects consumers' willingness to pay) exactly equals the cost of producing it.

In long-run competitive equilibrium, we have shown:

$$P^* = MC = ATC_{\min}$$

Because $P = MC$ at every competitive firm, no reallocation of resources — producing more or less of this good, or shifting resources to another industry — can increase total surplus. This is the formal justification for the informal notion, introduced in Chapter 2, of the "invisible hand": competitive markets, driven purely by self-interested price-taking behavior, achieve the surplus-maximizing, allocatively efficient outcome without any central coordination.

!!! tip "Two distinct efficiency results, now connected"
    Chapter 2 showed that competitive equilibrium maximizes total surplus. This chapter shows *why*, by deriving the supply curve from cost-minimizing, profit-maximizing firms. The $P=MC$ condition is the single thread connecting individual firm behavior to market-wide efficiency.

#### Diagram: Perfectly Competitive Firm Profit Maximizer

<details markdown="1">
<summary>Perfectly Competitive Firm Profit Maximizer</summary>
Type: microsim
**sim-id:** perfect-competition-profit-max<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** determine<br/>
**Learning Objective:** The learner will determine a price-taking firm's profit-maximizing output level and resulting profit or loss, given a market price and the firm's cost schedule, using the P=MC rule.

**Prerequisites:** price taker, marginal revenue, marginal cost, the MR=MC profit-maximization rule, economic profit (Section 6.2–6.3).

**Evidence of Mastery:** For 2 additional challenge prices, the learner determines Q* and the resulting profit using the given cost schedule. Correct when both match exactly. Mastery is 2 of 2 correct.

**Misconceptions:** (1) Choosing the Q with the lowest TC rather than the Q where MC=P. (2) Stopping at the first Q with negative profit instead of continuing to the Q where profit is maximized. (3) Picking the smallest Q among tied profits instead of the largest.

**Instructional Rationale:** Apply-level work requires executing the MC=P rule on new price values, with the base case worked once as a demonstration before scored practice.

**Content:**

The chapter's own cost schedule (Section 6.3):

| Q | TC | MC | TR at \$40 | Profit at \$40 | TR at \$30 | Profit at \$30 | TR at \$45 | Profit at \$45 |
|---|---|---|---|---|---|---|---|---|
| 0 | \$50 | — | \$0 | −\$50 | \$0 | −\$50 | \$0 | −\$50 |
| 1 | \$80 | \$30 | \$40 | −\$40 | \$30 | −\$50 | \$45 | −\$35 |
| 2 | \$105 | \$25 | \$80 | −\$25 | \$60 | −\$45 | \$90 | −\$15 |
| 3 | \$135 | \$30 | \$120 | −\$15 | \$90 | −\$45 | \$135 | \$0 |
| 4 | \$170 | \$35 | \$160 | −\$10 | \$120 | −\$50 | \$180 | \$10 |
| 5 | \$210 | \$40 | \$200 | −\$10 | \$150 | −\$60 | \$225 | \$15 |
| 6 | \$255 | \$45 | \$240 | −\$15 | \$180 | −\$75 | \$270 | \$15 |

At P=\$40: Q*=5, profit=−\$10 (the chapter's own base case). At P=\$30: Q*=3, profit=−\$45. At P=\$45: Q*=6, profit=\$15.

**Provenance:** The TC and MC columns and the P=\$40 base case are the chapter's own "Worked Example" in Section 6.3. The \$30 and \$45 challenges reuse the same TC schedule with TR recomputed at the new price; labeled illustrative.

**Rules:** The profit-maximizing Q* is the largest Q for which MC(Q) ≤ P. Profit(Q) = P×Q − TC(Q). If multiple Q give the same maximum profit, report the largest such Q, matching the chapter's own convention. Market price P: min \$20, max \$50, step \$5, default \$40.

**Learner Activity:**

1. The learner watches the base case (P=\$40) solved: the sim steps through Q=0 to 6, marking profit at each row, and highlights Q*=5 as the largest Q with MC≤P.
2. The learner sets the price to \$30 and types the predicted Q* and profit.
3. The sim checks both values against the table and reveals the correct answer.
4. The learner repeats for price \$45.

**Feedback:** 2 scored challenges, fixed order, two attempts each. Correct: "Correct: Q* = <value>, profit = <value>." Incorrect (first attempt): "Find the largest Q where MC is still at or below the price." After the second wrong attempt, the correct Q* and profit are shown with the row-by-row reasoning. A running count "Challenges correct: n of 2" is shown.

**Starting State:** The base case (P=\$40) is shown fully worked, with Q*=5 highlighted and the −\$10 loss area shaded between TC and TR. The question on screen before the first challenge is "If the market price drops to \$30, what is the new profit-maximizing quantity and profit?"

**Chapter Anchors:** The chapter's Section 6.3 worked example states that at P*=\$40 the firm maximizes profit at Q*=5 with a profit of −\$10; the sim's base-case demonstration reproduces this exactly.
</details>

---

## Key Terms

| Term | Definition |
|---|---|
| **Perfect Competition** | A market structure with many buyers/sellers, a standardized product, free entry/exit, and perfect information |
| **Price Taker** | A firm that must accept the market price because it cannot influence it |
| **Marginal Revenue (MR)** | The additional revenue from selling one more unit; equals price for a competitive firm |
| **MR = MC Rule** | The profit-maximizing condition for any firm: produce where marginal revenue equals marginal cost |
| **Shutdown Rule** | A firm should produce in the short run if $P \geq AVC_{\min}$; otherwise it should shut down |
| **Short-Run Industry Supply Curve** | The horizontal sum of all firms' short-run supply curves (their $MC$ above $AVC_{\min}$) |
| **Economic Profit** | Revenue minus all costs, including implicit opportunity costs |
| **Accounting Profit** | Revenue minus only explicit (out-of-pocket) costs |
| **Long-Run Equilibrium** | The state reached after free entry/exit drives economic profit to zero across the industry |
| **Allocative Efficiency** | The condition where price equals marginal cost, so resources are allocated to their highest-valued use |
| **Consumer Surplus** | The area below the demand curve and above the price |
| **Producer Surplus** | The area above the supply curve and below the price |

---

## Practice Problems

### Problem 1 — Price Taking and Marginal Revenue

A competitive wheat farmer sells wheat at the market price of \$8 per bushel.

**a)** What is the farmer's marginal revenue for the 1st bushel? The 100th bushel?  
**b)** What does the farmer's individual demand curve look like, and why?  
**c)** If the farmer tried to charge \$9 per bushel, what would happen to sales?

??? success "Solution"
    **a)** Marginal revenue is \$8 for every bushel, including the 1st and the 100th — as a price taker, every unit sold earns exactly the market price.

    **b)** The farmer's individual demand curve is **horizontal (perfectly elastic)** at $P=\$8$ — the farmer can sell any quantity at this price, but nothing at a higher price, since buyers can purchase identical wheat elsewhere.

    **c)** Sales would fall to **zero** — buyers would simply purchase wheat from any of the many other farmers selling an identical product at the \$8 market price.

### Problem 2 — MR = MC Rule

A competitive firm faces a market price of \$25. Its marginal cost schedule is:

| $Q$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $MC$ | \$10 | \$15 | \$20 | \$25 | \$30 | \$36 |

**a)** What quantity maximizes the firm's profit?  
**b)** Explain why producing one unit less, or one unit more, would reduce profit.

??? success "Solution"
    **a)** The firm should produce where $P=MR=MC$. At $Q=4$, $MC=\$25=P$. **$Q^*=4$**.

    **b)** Producing the 3rd unit instead of stopping at 4 (i.e., only producing 3) would mean forgoing a unit where $MR(\$25) > MC(\$25$, the 4th unit$)$ — wait, more precisely: at $Q=3$, the next (4th) unit has $MC=\$25=MR$, so producing it adds exactly as much to revenue as to cost (zero net effect, but included since $MC \leq MR$). Producing a 5th unit would cost $MC=\$30 > MR=\$25$ — this unit reduces profit by \$5, so the firm should not produce it. Thus $Q=4$ is optimal: every unit up to 4 has $MC \leq MR$, and the 5th unit would have $MC > MR$.

### Problem 3 — Shutdown Rule

A competitive firm has the following short-run cost data at its profit-maximizing output of 10 units: $ATC = \$18$, $AVC=\$12$, $AFC=\$6$.

**a)** If the market price is \$15, should the firm produce or shut down in the short run? Explain.  
**b)** If the market price is \$10, should the firm produce or shut down? Explain.  
**c)** In case (a), is the firm earning a profit or a loss? How much per unit?

??? success "Solution"
    **a)** **Produce.** Since $P=\$15 > AVC=\$12$, the firm covers all variable costs and contributes \$3 per unit toward fixed costs. Even though $P < ATC$ (a loss), producing is better than shutting down.

    **b)** **Shut down.** Since $P=\$10 < AVC=\$12$, the firm cannot even cover its variable costs; every unit produced loses money beyond the fixed cost it must pay regardless. Producing zero minimizes losses to just the fixed cost.

    **c)** At $P=\$15$ and $ATC=\$18$, the firm earns a **loss of \$3 per unit** (×10 units = \$30 total loss), but this is still better than shutting down, which would mean losing the full fixed cost of $AFC \times Q = \$6 \times 10 = \$60$.

### Problem 4 — Industry Supply Curve

An industry has 200 identical competitive firms. Each individual firm's supply schedule (quantity supplied at each price, from its $MC$ curve above $AVC_{\min}$) is:

| Price | Quantity Supplied per Firm |
|---|---|
| \$10 | 0 (below shutdown price) |
| \$15 | 20 |
| \$20 | 30 |
| \$25 | 40 |

**a)** Construct the short-run industry supply curve.  
**b)** If market demand at $P=\$20$ is 5,000 units, is the market in equilibrium? Explain.

??? success "Solution"
    **a)** Multiply each firm's quantity by 200 firms:

    | Price | Industry Quantity Supplied |
    |---|---|
    | \$10 | 0 |
    | \$15 | 4,000 |
    | \$20 | 6,000 |
    | \$25 | 8,000 |

    **b)** At $P=\$20$, industry supply is 6,000 units, but demand is only 5,000 units — this means there is a **surplus of 1,000 units** at $P=\$20$. The market is **not in equilibrium**; price must fall until quantity demanded rises (and quantity supplied falls) to meet at a lower equilibrium price.

### Problem 5 — Long-Run Equilibrium

Every firm in a competitive industry has identical long-run average costs, with $ATC_{\min} = \$12$ at an output of 50 units per firm. Currently, the market price is \$18, and each firm is producing 60 units.

**a)** Is the industry in long-run equilibrium? Explain.  
**b)** What will happen to the number of firms in the industry over time, and why?  
**c)** What price will prevail once the long run is reached?

??? success "Solution"
    **a)** **No**, the industry is not in long-run equilibrium. Since $P=\$18 > ATC_{\min}=\$12$, firms are earning positive economic profit, which will attract entry.

    **b)** New firms will **enter** the industry, attracted by the positive economic profit. As more firms enter, industry supply shifts right, pushing the market price down.

    **c)** Entry will continue until economic profit is driven to zero, i.e., until price falls to $P = ATC_{\min} = \mathbf{\$12}$.

### Problem 6 — Allocative Efficiency

A competitive market is in long-run equilibrium with $P^* = MC = ATC_{\min} = \$30$.

**a)** Explain why this outcome is allocatively efficient.  
**b)** Suppose a policy forced price down to \$25 (below marginal cost at the equilibrium quantity). Using the concept of consumer and producer surplus, explain why this would reduce total surplus (create a deadweight loss), even though consumers pay a lower price.

??? success "Solution"
    **a)** The outcome is allocatively efficient because $P=MC$: the price consumers are willing to pay for the last unit (reflecting its value to them) exactly equals the marginal cost of producing it (reflecting the value of resources used elsewhere). No reallocation of resources toward or away from this good could increase total surplus.

    **b)** At a forced price of \$25, quantity supplied would fall below the equilibrium quantity (since $P < MC$ at the original equilibrium quantity means producers are no longer willing to supply that much). The reduction in quantity traded means some units that consumers valued more than their cost of production (units where willingness to pay exceeds marginal cost) are no longer produced and exchanged — this lost surplus from forgone mutually beneficial trades is a **deadweight loss**. Even though remaining consumers benefit from a lower price, this transfer is outweighed by the surplus lost from the reduction in quantity traded, so total surplus falls.

!!! mascot-celebration "You've Derived Market Efficiency From Scratch"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You just connected firm-level profit maximization all the way to market-wide allocative efficiency — the same invisible-hand result from Chapter 2, now proven rather than asserted. That's one of the deepest ideas in all of economics!

---

!!! tip "Next Chapter"
    In [Chapter 7: Monopoly](../07-monopoly/index.md), we remove the price-taking assumption entirely and study the opposite extreme — a single seller with market power — to see how the MR = MC rule, pricing, and efficiency outcomes change when a firm can influence price.
