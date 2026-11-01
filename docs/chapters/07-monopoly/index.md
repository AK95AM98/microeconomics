# Chapter 7: Monopoly

## Learning Objectives

After completing this chapter, you will be able to:

1. Identify the sources of monopoly power and the barriers that sustain it
2. Derive a monopolist's marginal revenue curve from its demand curve
3. Find the profit-maximizing price and quantity for a monopolist
4. Compare monopoly outcomes to perfect competition and quantify the deadweight loss
5. Distinguish first-, second-, and third-degree price discrimination and their welfare effects
6. Explain why natural monopoly arises and how regulators respond to it
7. Describe the goals and tools of antitrust policy

---

!!! mascot-welcome "Meet the Opposite Extreme"
    ![Professor Owl waving hello](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Chapter 6 gave you a firm with zero pricing power. This chapter flips that completely: one seller, full control over price, and a very different set of trade-offs. Every choice has a trade-off, and here you'll see how a monopolist's own pricing choice creates a cost society actually bears.

## 7.1 Sources of Monopoly Power

A **monopoly** is a market with a single seller of a good that has no close substitutes. Unlike the price-taking firms of Chapter 6, a monopolist is a **price maker** — it chooses a point on the market demand curve rather than accepting a price set by the market.

Monopoly power persists only if **barriers to entry** prevent other firms from competing it away. The major sources are:

| Barrier | Description | Example |
|---|---|---|
| **Economies of scale** | Average cost falls over the entire relevant range of output, so one large firm can produce more cheaply than several small ones | Local water utility |
| **Control of a key input** | A firm owns or controls an essential resource | De Beers' historical control of diamond mines |
| **Legal restrictions** | Government grants exclusive rights | Patents, copyrights, broadcast licenses |
| **Network effects** | The good becomes more valuable as more people use it, locking in the largest network | Early social media platforms |
| **Government franchise** | The government designates a single provider | U.S. Postal Service for first-class mail |

!!! example "Patents as a deliberate monopoly"
    A pharmaceutical patent grants the developer the exclusive right to sell a drug for a fixed period (typically 20 years from filing). This is monopoly power created *on purpose* — society trades higher short-run drug prices for the incentive to innovate in the first place.

A firm with the largest market share is not necessarily a monopolist in the economic sense; what matters is the absence of close substitutes and the durability of the barriers protecting its position.

---

## 7.2 The Monopolist's Demand and Marginal Revenue

Because the monopolist is the only seller, the **market demand curve** *is* the firm's demand curve. This is the single most important fact distinguishing monopoly from perfect competition: a competitive firm faces a horizontal (perfectly elastic) demand curve at the market price, but a monopolist faces the entire downward-sloping market demand curve.

This has a crucial consequence: to sell more output, the monopolist must **lower its price on all units sold**, not just the marginal unit. Marginal revenue therefore falls faster than price.

### Deriving Marginal Revenue

Let the monopolist face a linear demand curve:

$$P = a - bQ$$

Total revenue is:

$$TR = P \times Q = (a - bQ)Q = aQ - bQ^2$$

Marginal revenue is the derivative of total revenue with respect to quantity:

$$MR = \frac{d(TR)}{dQ} = a - 2bQ$$

**Key result:** For a linear demand curve $P = a - bQ$, the marginal revenue curve is also linear, has the same vertical intercept $a$, but is **twice as steep** as demand. The $MR$ curve lies below the demand curve at every quantity greater than zero.

### Numerical Example

Suppose demand is $P = 100 - 2Q$, so $MR = 100 - 4Q$.

| $Q$ | $P$ | $TR = P \times Q$ | $MR$ (next unit) |
|---|---|---|---|
| 0 | 100 | 0 | 96 |
| 10 | 80 | 800 | 60 |
| 20 | 60 | 1,200 | 20 |
| 25 | 50 | 1,250 | 0 |
| 30 | 40 | 1,200 | −20 |
| 40 | 20 | 800 | −60 |

Marginal revenue falls twice as fast as price and reaches **zero at $Q = 25$** — exactly where total revenue is maximized. Beyond $Q = 25$, marginal revenue is negative: selling additional units *reduces* total revenue because the price cut needed to sell them outweighs the extra units sold.

!!! note "MR and the elasticity of demand"
    Marginal revenue is positive where demand is elastic ($|\varepsilon_d| > 1$), zero where demand is unit-elastic, and negative where demand is inelastic ($|\varepsilon_d| < 1$). A profit-maximizing monopolist never knowingly operates in the inelastic region of demand, since it could raise price, sell less, and still earn more revenue while incurring lower cost.

!!! mascot-thinking "Why a Monopolist Avoids the Inelastic Region"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    If MR is negative, raising price actually *increases* revenue while cutting output — and lowering output also cuts cost. No rational monopolist would ever knowingly sit where demand is inelastic; it's strictly better to raise price and sell less.

---

## 7.3 Profit Maximization for a Monopolist

Like any firm, a monopolist maximizes profit by choosing the quantity where **marginal revenue equals marginal cost**:

$$MR = MC$$

The key difference from perfect competition is that the monopolist then charges the price given by the **demand curve** at that quantity — not the (lower) marginal cost.

### Steps to Solve

1. Find the demand curve $P(Q)$ and derive $MR(Q)$.
2. Find $MC(Q)$ from the cost function.
3. Set $MR = MC$ and solve for $Q^M$ (the monopoly quantity).
4. Plug $Q^M$ into the demand curve to find $P^M$ (the monopoly price).
5. Compute profit: $\pi = (P^M - ATC(Q^M)) \times Q^M$.

### Worked Example

A monopolist faces demand $P = 100 - 2Q$ and has constant marginal cost $MC = 20$ (so $TC = 20Q$, with no fixed costs in this simplified example).

From Section 7.2, $MR = 100 - 4Q$. Set $MR = MC$:

$$100 - 4Q = 20$$
$$80 = 4Q$$
$$Q^M = 20$$

Price from the demand curve:

$$P^M = 100 - 2(20) = \$60$$

Profit (since $ATC = MC = 20$ at every quantity here):

$$\pi = (P^M - ATC) \times Q^M = (60 - 20) \times 20 = \$800$$

!!! warning "Common mistake"
    Students often set $P = MC$ (the competitive rule) instead of $MR = MC$. A monopolist that set $P = MC$ would be ignoring the fact that producing more requires cutting the price on *all* units, not just the last one. Always find $MR$ first, then read price off the demand curve.

### Monopoly Does Not Guarantee Profit

A monopolist earns **economic profit** only if $P^M > ATC(Q^M)$. If demand is weak relative to costs, a monopolist can still suffer a loss — monopoly power guarantees the absence of competitors, not profitability.

---

## 7.4 Monopoly vs. Competitive Pricing

Compare the monopoly outcome to what would happen if this same market were perfectly competitive, with many small firms whose combined marginal cost curve equals the monopolist's $MC$ curve (i.e., supply is $MC$).

Using the numbers from Section 7.3: under perfect competition, price equals marginal cost along the demand curve:

$$100 - 2Q = 20 \implies Q^C = 40, \quad P^C = \$20$$

| | Perfect Competition | Monopoly |
|---|---|---|
| Price | \$20 | \$60 |
| Quantity | 40 | 20 |
| Outcome | $P = MC$ (efficient) | $P > MC$ (inefficient) |

Relative to the competitive outcome, the monopolist **restricts output and raises price**. This is the defining inefficiency of monopoly: the monopolist refuses to sell units for which willingness to pay exceeds the marginal cost of production, because selling them would require lowering the price on units already sold.

---

## 7.5 Deadweight Loss and Inefficiency

Because the monopolist produces less than the efficient (competitive) quantity, some mutually beneficial trades never happen. The lost total surplus is the **deadweight loss (DWL)** of monopoly.

### Graphical Logic

- **Consumer surplus** shrinks because price is higher and quantity is lower than under competition.
- **Producer surplus (profit)** may rise — the monopolist gains from the higher price on units it does sell, but loses the surplus from units it no longer sells.
- Part of what was consumer surplus under competition is **transferred** to the monopolist as higher profit (this is a transfer, not a loss to society).
- The surplus on units between $Q^M$ and $Q^C$ that are no longer traded is lost entirely — this is the **deadweight loss**.

### Numerical Example (continuing Sections 7.3–7.4)

With $P = 100 - 2Q$ and $MC = 20$: $Q^C = 40$, $Q^M = 20$, $P^M = 60$.

The deadweight loss is the triangle between the demand curve and the $MC$ curve, over the quantity range from $Q^M = 20$ to $Q^C = 40$:

$$DWL = \frac{1}{2} \times (P^M - MC) \times (Q^C - Q^M) = \frac{1}{2} \times (60 - 20) \times (40 - 20)$$

$$DWL = \frac{1}{2} \times 40 \times 20 = \$400$$

!!! example "Interpreting the deadweight loss"
    This \$400 represents the total surplus that would have been created by trading units 21 through 40 — surplus that simply vanishes because the monopolist won't produce them. No one captures this value; it is a pure loss to society, which is why monopoly is called **allocatively inefficient**.

---

## 7.6 Price Discrimination

**Price discrimination** is charging different prices to different customers (or for different units) for reasons unrelated to cost differences. It is a strategy for capturing some of the consumer surplus that uniform pricing leaves on the table — and, counterintuitively, it can *reduce* deadweight loss by expanding output toward the efficient level.

Three conditions must hold for price discrimination to be possible and profitable: (1) the firm must have market power, (2) it must be able to **identify** or **sort** customers by willingness to pay, and (3) it must be able to prevent **resale** (arbitrage) between low-price and high-price customers.

### First-Degree (Personalized) Price Discrimination

The firm charges each customer exactly their willingness to pay. This is the theoretical extreme: the firm captures **all** consumer surplus as profit, and because every unit for which willingness to pay exceeds marginal cost gets sold, output expands to $Q^C$ and the deadweight loss falls to **zero**. All surplus becomes producer surplus — efficient, but with no consumer surplus at all.

!!! note "Real-world approximations"
    Perfect first-degree discrimination is rare, but a car salesperson haggling individually with each buyer, or a university's financial-aid office setting each student's net tuition based on need and merit, approximates it.

### Second-Degree Price Discrimination

The firm offers a **menu** of price-quantity (or price-quality) bundles, and customers self-select the bundle that suits them. The firm doesn't observe willingness to pay directly but infers it from customers' choices.

!!! example "Second-degree discrimination in practice"
    - **Quantity discounts:** Costco's bulk packaging; buy-one-get-one offers.
    - **Versioning:** Airlines selling Basic Economy, Economy, and Business Class seats on the same flight at very different markups over cost.
    - **Software tiers:** "Home," "Pro," and "Enterprise" versions of the same software, with the Pro version artificially limited to be less useful than Enterprise.

### Third-Degree Price Discrimination

The firm sorts customers into **groups** based on an observable characteristic correlated with willingness to pay (age, student status, location, time of purchase) and charges each group a different price.

**Rule for third-degree discrimination:** The firm sets $MR_1 = MR_2 = MC$ across the two (or more) markets. The group with the **less elastic** demand is charged the **higher** price.

!!! mascot-encourage "Two Markets, Same Rule, Twice"
    ![Professor Owl giving encouragement](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    Don't let two demand curves at once feel like double the difficulty — you're just applying MR = MC separately in each market. Solve one market fully before even glancing at the other.

#### Worked Example

A monopolist sells to two markets with demand curves:

$$P_1 = 50 - Q_1 \quad \text{(Market 1: adults)}$$
$$P_2 = 30 - Q_2 \quad \text{(Market 2: students)}$$

Marginal cost is constant at $MC = 10$ in both markets, and resale between markets is impossible.

Marginal revenue in each market: $MR_1 = 50 - 2Q_1$, $MR_2 = 30 - 2Q_2$.

Set each equal to $MC = 10$:

$$50 - 2Q_1 = 10 \implies Q_1 = 20, \quad P_1 = 50 - 20 = \$30$$
$$30 - 2Q_2 = 10 \implies Q_2 = 10, \quad P_2 = 30 - 10 = \$20$$

| Market | Price | Quantity |
|---|---|---|
| Adults (less elastic at any common price) | \$30 | 20 |
| Students (more elastic) | \$20 | 10 |

Students — typically more price-sensitive — pay the lower price, consistent with the rule that the more elastic group gets the discount.

!!! tip "Why 'student discounts' and 'senior discounts' exist"
    Movie theaters and software companies offer discounts to students and seniors not out of charity, but because these groups tend to have more elastic demand (lower income, more substitutes, more free time to shop around). Charging them less while charging full price to less price-sensitive adults raises total profit.

### Welfare Effects of Price Discrimination

| Degree | Consumer Surplus | Producer Surplus | Deadweight Loss |
|---|---|---|---|
| None (uniform price) | Positive | Positive | Positive (as in 7.5) |
| First-degree | Zero | Maximum (= old CS + old DWL) | Zero |
| Second/Third-degree | Reduced, but not zero | Increased | Reduced relative to uniform pricing (generally) |

Price discrimination is therefore ambiguous for consumers as a whole — some pay more, some pay less — but it typically **increases total surplus** relative to uniform monopoly pricing, because it induces the monopolist to serve customers (like price-sensitive students) it would otherwise exclude.

!!! mascot-tip "Three Degrees, One Pattern"
    ![Professor Owl sharing a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Remember them by how much the firm knows: first-degree knows each customer's exact value, second-degree lets customers sort themselves with a menu, third-degree sorts customers by an observable group trait. More information always means more surplus captured.

---

## 7.7 Natural Monopoly and Regulation

A **natural monopoly** arises when a single firm can supply the entire market at lower cost than two or more firms could — typically because very large fixed costs and economies of scale cause average total cost ($ATC$) to decline throughout the relevant range of market demand.

!!! example "Classic natural monopolies"
    - Electricity transmission and distribution
    - Water and sewer utilities
    - Natural gas pipelines

Because duplicating the fixed infrastructure (power lines, pipes) would be wasteful, society typically allows a single regulated firm to operate rather than forcing competition.

### The Regulator's Dilemma

For a natural monopoly, the efficient price ($P = MC$) typically lies **below** average total cost, because large fixed costs pull $ATC$ above $MC$ at every relevant quantity. Setting $P = MC$ (**marginal-cost pricing**) is efficient but forces the firm into a loss, which is unsustainable without a subsidy.

!!! mascot-warning "Efficient Doesn't Mean Sustainable"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    It's tempting to say regulators should always set $P = MC$ since it's efficient. But for a natural monopoly, that price doesn't cover fixed costs — without a subsidy, the firm goes bankrupt and stops providing the service at all.

| Regulatory Rule | Price | Effect |
|---|---|---|
| **Marginal-cost pricing** ($P = MC$) | Lowest, efficient | Firm earns a loss equal to its fixed cost — needs a subsidy to survive |
| **Average-cost pricing** ($P = ATC$) | Higher than MC pricing | Firm breaks even (zero economic profit); some deadweight loss remains, but far less than unregulated monopoly |
| **Rate-of-return regulation** | Set to allow a "fair" return on invested capital | Common in practice; can blunt incentives to cut costs |

Most real-world utility regulation uses **average-cost pricing** as a practical compromise: it lets the firm cover its costs (including a normal return on capital) while keeping price well below the unregulated monopoly price.

---

## 7.8 Antitrust Policy

**Antitrust policy** (called "competition policy" outside the U.S.) refers to laws and government actions aimed at preventing firms from acquiring or abusing monopoly power in ways that harm consumers.

### Key U.S. Antitrust Laws

| Law | Year | Main Provision |
|---|---|---|
| **Sherman Antitrust Act** | 1890 | Outlaws contracts, combinations, and conspiracies that restrain trade; outlaws monopolization |
| **Clayton Act** | 1914 | Prohibits specific practices: price discrimination that harms competition, exclusive dealing, mergers that substantially lessen competition |
| **Federal Trade Commission Act** | 1914 | Created the FTC to enforce antitrust and consumer-protection law |

### Enforcement Tools

- **Blocking mergers** that would substantially reduce competition (reviewed by the FTC and Department of Justice).
- **Breaking up** firms found to be illegally monopolizing a market (e.g., *Standard Oil*, 1911).
- **Prohibiting price-fixing and collusion** among competitors (a per se violation — illegal regardless of its effect on price).
- **Prohibiting predatory pricing** — deliberately pricing below cost to drive out rivals, intending to raise prices later.

!!! note "Monopoly is not illegal; monopolizing is"
    U.S. antitrust law does not punish a firm simply for *becoming* a monopoly through superior products, lower costs, or business acumen. It targets firms that acquire or maintain monopoly power through anticompetitive conduct — exclusionary contracts, predatory pricing, or illegal mergers — rather than through competing on the merits.

---

## Key Terms

| Term | Definition |
|---|---|
| **Monopoly** | A market with a single seller of a good with no close substitutes |
| **Barrier to Entry** | A factor that prevents new firms from entering a market |
| **Natural Monopoly** | A market where one firm can supply the entire market at lower cost than multiple firms |
| **Price Maker** | A firm whose own output decisions affect the market price |
| **Marginal Revenue (MR)** | The change in total revenue from selling one more unit |
| **Monopoly Price/Quantity** | The price and quantity where $MR = MC$ and price is read off the demand curve |
| **Deadweight Loss** | The lost total surplus from producing less than the efficient quantity |
| **Price Discrimination** | Charging different prices to different customers for reasons unrelated to cost |
| **First-Degree Price Discrimination** | Charging each customer exactly their willingness to pay |
| **Second-Degree Price Discrimination** | Offering a menu of price-quantity bundles that customers self-select |
| **Third-Degree Price Discrimination** | Charging different groups of customers different prices based on an observable trait |
| **Arbitrage** | Reselling a good from low-price buyers to high-price buyers, which undermines price discrimination |
| **Marginal-Cost Pricing** | Regulatory rule setting price equal to marginal cost; efficient but may cause losses for a natural monopoly |
| **Average-Cost Pricing** | Regulatory rule setting price equal to average total cost; allows the firm to break even |
| **Antitrust Policy** | Laws and enforcement actions aimed at preventing anticompetitive monopoly power |
| **Sherman Antitrust Act** | 1890 law outlawing restraint of trade and monopolization |

---

## Practice Problems

### Problem 1 — Marginal Revenue

A monopolist faces demand $P = 60 - Q$.

**a)** Write the total revenue function and derive the marginal revenue function.  
**b)** At what quantity does $MR = 0$?  
**c)** Over what range of quantity is demand elastic?

??? success "Solution"
    **a)** $TR = PQ = (60-Q)Q = 60Q - Q^2$. $MR = \dfrac{d(TR)}{dQ} = 60 - 2Q$.

    **b)** $MR = 0 \Rightarrow 60 - 2Q = 0 \Rightarrow Q = 30$.

    **c)** Demand is elastic wherever $MR > 0$, i.e., for $Q < 30$. (Demand is unit-elastic at $Q=30$ and inelastic for $Q > 30$.)

### Problem 2 — Profit Maximization

A monopolist faces demand $P = 120 - 2Q$ and has total cost $TC = 10Q + 200$ (so $MC = 10$).

**a)** Find the profit-maximizing quantity and price.  
**b)** Calculate the monopolist's profit.  
**c)** Is this monopolist earning an economic profit, breaking even, or earning a loss?

??? success "Solution"
    **a)** $MR = 120 - 4Q$. Set $MR = MC$: $120 - 4Q = 10 \Rightarrow Q^M = 27.5$. Then $P^M = 120 - 2(27.5) = \$65$.

    **b)** $TR = 65 \times 27.5 = \$1{,}787.50$. $TC = 10(27.5) + 200 = 275 + 200 = \$475$. Profit $= 1{,}787.50 - 475 = \$1{,}312.50$.

    **c)** The firm earns a positive **economic profit** of \$1,312.50, since $TR > TC$.

### Problem 3 — Deadweight Loss

Demand is $P = 200 - Q$ and marginal cost is constant at $MC = 40$ (no fixed costs).

**a)** Find the competitive price and quantity.  
**b)** Find the monopoly price and quantity.  
**c)** Calculate the deadweight loss from monopoly.

??? success "Solution"
    **a)** Competitive: $P = MC \Rightarrow 200 - Q = 40 \Rightarrow Q^C = 160$, $P^C = 40$.

    **b)** Monopoly: $MR = 200 - 2Q$. Set $MR = MC$: $200 - 2Q = 40 \Rightarrow Q^M = 80$. $P^M = 200 - 80 = \$120$.

    **c)** $DWL = \frac{1}{2} \times (P^M - MC) \times (Q^C - Q^M) = \frac{1}{2} \times (120-40) \times (160-80) = \frac{1}{2} \times 80 \times 80 = \$3{,}200$.

### Problem 4 — Third-Degree Price Discrimination

An airline sells tickets to business travelers and leisure travelers on the same flight. Demand curves are:

$$P_B = 800 - 2Q_B \quad \text{(business)}$$
$$P_L = 400 - 2Q_L \quad \text{(leisure)}$$

Marginal cost per seat is constant at $MC = 100$, and the airline can prevent resale (tickets are non-transferable).

**a)** Find the profit-maximizing price and quantity in each segment.  
**b)** Which group pays more, and why does this make economic sense?

??? success "Solution"
    **a)** Business: $MR_B = 800 - 4Q_B$. Set equal to $MC$: $800 - 4Q_B = 100 \Rightarrow Q_B = 175$, $P_B = 800 - 2(175) = \$450$.

    Leisure: $MR_L = 400 - 4Q_L$. Set equal to $MC$: $400 - 4Q_L = 100 \Rightarrow Q_L = 75$, $P_L = 400 - 2(75) = \$250$.

    **b)** Business travelers pay more (\$450 vs. \$250). Business demand is less elastic — business travelers typically have inflexible schedules and employer-paid tickets, so they are less price-sensitive. The airline exploits this by charging them a higher markup over marginal cost.

### Problem 5 — Natural Monopoly Regulation

A water utility faces market demand $P = 22 - Q$ and has total cost $TC = 35 + 10Q$ (so $MC = 10$ and fixed cost is \$35).

**a)** Find the price and quantity under unregulated monopoly.  
**b)** Find the price and quantity under marginal-cost-pricing regulation ($P = MC$). What is the utility's profit at this price?  
**c)** Find the price and quantity under average-cost-pricing regulation ($P = ATC$), choosing the solution with the larger quantity. Confirm the firm earns zero economic profit there.

??? success "Solution"
    **a)** $MR = 22 - 2Q$. Set $MR = MC$: $22 - 2Q = 10 \Rightarrow Q^M = 6$, $P^M = 22 - 6 = \$16$.

    **b)** Marginal-cost pricing: $P = MC = \$10$. From demand, $10 = 22 - Q \Rightarrow Q = 12$. Profit $= TR - TC = (10)(12) - [35 + 10(12)] = 120 - 155 = -\$35$ — a loss exactly equal to the fixed cost, since price covers only marginal cost and nothing toward fixed cost.

    **c)** Average-cost pricing requires $P = ATC = \dfrac{35}{Q} + 10$. Set this equal to the demand price $22 - Q$:

    $$22 - Q = \frac{35}{Q} + 10$$
    $$12Q - Q^2 = 35$$
    $$Q^2 - 12Q + 35 = 0$$
    $$(Q-5)(Q-7) = 0 \implies Q = 5 \text{ or } Q = 7$$

    Taking the larger root, $Q = 7$: $P = 22 - 7 = \$15$. Check: $ATC = 35/7 + 10 = 5 + 10 = \$15 = P$. ✓ Profit $= (15)(7) - [35 + 10(7)] = 105 - 105 = \$0$ — the firm exactly breaks even.

    Comparing all three regimes: price rises from \$10 (marginal-cost) to \$15 (average-cost) to \$16 (unregulated monopoly), while quantity falls from 12 to 7 to 6. Average-cost regulation lands between the efficient outcome and the unregulated monopoly outcome — it sacrifices some efficiency to keep the utility financially viable without a subsidy.

!!! mascot-celebration "You Understand Market Power"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    You can now find a monopolist's price and quantity, measure the deadweight loss it creates, and explain why price discrimination can actually make a market *more* efficient. That's a genuinely sophisticated set of tools!

---

!!! tip "Next Chapter"
    In [Chapter 8: Monopolistic Competition](../08-monopolistic-competition/index.md), we study markets that blend elements of both competition and monopoly — many firms, but each with a slightly differentiated product and some pricing power of its own.
