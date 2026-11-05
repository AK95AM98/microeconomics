# Chapter 13: Externalities and Public Goods

## Learning Objectives

After completing this chapter, you will be able to:

1. Distinguish private (internal) costs and benefits from social costs and benefits, and identify the deadweight loss from negative and positive externalities
2. Calculate the efficient output level and the optimal Pigouvian tax or subsidy for a market with an externality
3. State the Coase theorem and work through a private-bargaining example to an efficient outcome
4. Explain how cap-and-trade systems achieve efficient pollution reduction at least cost
5. Define public goods and derive the condition for their efficient provision
6. Explain the free-rider problem using a simple game-theoretic example
7. Compare voting mechanisms for public-goods provision and analyze common-pool resource solutions (quotas, pricing, and property rights)

---

!!! mascot-welcome "Welcome to Market Failure, Part II"
    ![Professor Owl waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Every choice has a trade-off! And that's true for markets too, even when the costs and benefits spill onto people who never agreed to the deal: the fishery downstream of a factory, the neighbor who benefits from your flu shot, everyone who enjoys a fireworks display they didn't pay for. By the end of this chapter, you'll have a toolkit -- Pigouvian taxes, Coasean bargains, cap-and-trade, and public-goods financing -- for nudging private incentives back in line with what's best for society as a whole.

## 13.1 Negative Externalities and Overproduction

### Private vs. Social Cost

When a firm's production imposes costs on third parties, the **private marginal cost (PMC)** that the firm pays diverges from the **social marginal cost (SMC)** borne by society as a whole:

$$SMC = PMC + MEC$$

where $MEC$ is the **marginal external cost** imposed on third parties. Because the firm only considers $PMC$, not $SMC$, when deciding how much to produce, the market supply curve (which reflects $PMC$) lies below the true social cost curve.

!!! mascot-thinking "The Wedge That Breaks Markets"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Notice what's really going on here: the firm's supply curve was never wrong about the firm's own costs -- it's just answering the wrong question. Every externality problem in this chapter boils down to this same wedge between what a decision-maker pays (or receives) and what society as a whole pays (or receives). Once you can spot that wedge, you can predict which direction the market will miss the efficient outcome.

### Finding the Efficient Quantity

The market reaches its (private) equilibrium where private marginal cost equals private marginal benefit ($PMC = PMB$, which for a competitive market is simply $S = D$). But the *efficient* quantity is where **social** marginal cost equals **social** marginal benefit: $SMC = SMB$. Because $SMC > PMC$ with a negative externality, the efficient quantity is always *less than* the market quantity.

!!! example "Worked example: a steel mill polluting a river"
    A steel mill's private marginal cost is $PMC = 2Q$, and demand (= private and social marginal benefit, since there's no externality on the buyer side) is $P = 100 - Q$. The mill's pollution imposes a constant marginal external cost of $MEC = 20$ per unit on a downstream fishery.

    **Market (unregulated) equilibrium:** Set $PMC = PMB$:

    $$2Q = 100 - Q \implies 3Q = 100 \implies Q_{market} = 33.3, \quad P_{market} = \$66.67$$

    **Efficient quantity:** $SMC = PMC + MEC = 2Q + 20$. Set $SMC = SMB$:

    $$2Q + 20 = 100 - Q \implies 3Q = 80 \implies Q_{efficient} = 26.7$$

    The market **overproduces** by $33.3 - 26.7 = 6.6$ units relative to the efficient level.

### Deadweight Loss from a Negative Externality

Every unit produced beyond $Q_{efficient}$ costs society more than it is worth (since $SMC > SMB$ for $Q > Q_{efficient}$). The deadweight loss is the triangle between the $SMC$ and $SMB$ curves, from $Q_{efficient}$ to $Q_{market}$:

$$DWL = \frac{1}{2} \times (Q_{market} - Q_{efficient}) \times MEC = \frac{1}{2} \times 6.6 \times 20 \approx \$66$$

!!! mascot-warning "Efficient Doesn't Mean Zero"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A common trap: assuming the "efficient" response to pollution is to eliminate it entirely. It isn't -- $Q_{efficient}$ in the steel mill example is still a healthy 26.7 units, not zero. The efficient quantity is wherever $SMC = SMB$, and some pollution is efficient as long as the good produced is worth more than the social cost of making it.

---

## 13.2 Positive Externalities and Underproduction

### Private vs. Social Benefit

With a positive externality, the **social marginal benefit (SMB)** exceeds the **private marginal benefit (PMB)**:

$$SMB = PMB + MEB$$

where $MEB$ is the marginal external benefit enjoyed by third parties. Because buyers only consider their own $PMB$, the market demand curve lies below the true social benefit curve, and the market **underproduces** relative to the efficient quantity.

!!! example "Worked example: flu vaccinations"
    Private demand for flu shots is $P = 60 - Q$ (reflecting each individual's own protection), and private marginal cost (= social marginal cost, since there's no externality on the supply side) is $PMC = Q$. Vaccination generates a constant marginal external benefit of $MEB = 10$ per unit (reduced disease transmission to others).

    **Market equilibrium:** $PMB = PMC \implies 60 - Q = Q \implies Q_{market} = 30$.

    **Efficient quantity:** $SMB = PMB + MEB = 60 - Q + 10 = 70 - Q$. Set $SMB = SMC$:

    $$70 - Q = Q \implies Q_{efficient} = 35$$

    The market **underproduces** by $35 - 30 = 5$ units of vaccination relative to the efficient level. The resulting deadweight loss is $\frac{1}{2} \times 5 \times 10 = \$25$.

---

## 13.3 Pigouvian Taxes and Subsidies

### Correcting a Negative Externality: The Pigouvian Tax

A **Pigouvian tax** is a tax set exactly equal to the marginal external cost at the efficient quantity. It forces producers to "internalize" the externality by making their private cost equal to the true social cost.

$$t^* = MEC(Q_{efficient})$$

!!! example "Setting the optimal tax (continuing the steel mill example)"
    From Section 13.1, $MEC = \$20$ per unit (constant), so the optimal Pigouvian tax is simply $t^* = \$20$ per unit.

    With the tax, the firm's effective marginal cost becomes $PMC + t = 2Q + 20$. Setting this equal to demand:

    $$2Q + 20 = 100 - Q \implies Q = 26.7$$

    This exactly reproduces the efficient quantity found in Section 13.1 — the tax has fully corrected the externality. Tax revenue collected is $t^* \times Q_{efficient} = 20 \times 26.7 = \$534$, which can (in principle) be used to compensate the affected downstream fishery or for other public purposes.

!!! mascot-tip "A Shortcut for Spotting the Right Tax"
    ![Professor Owl tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Here's a time-saver for any Pigouvian tax problem: if $MEC$ is already stated as a constant (like the \$20 here), you don't need to re-derive $Q_{efficient}$ to find $t^*$ -- the optimal tax is just that constant. You only need to solve for $Q_{efficient}$ when you're asked to verify the tax restores it, or when $MEC$ itself varies with $Q$.

### Correcting a Positive Externality: The Pigouvian Subsidy

Symmetrically, a **Pigouvian subsidy** set equal to the marginal external benefit induces the efficient, higher quantity when there is underproduction.

$$s^* = MEB(Q_{efficient})$$

!!! example "Setting the optimal subsidy (continuing the vaccination example)"
    From Section 13.2, $MEB = \$10$ per unit, so $s^* = \$10$. With the subsidy, buyers face an effective price $P - s$, so their willingness to pay a market price rises, shifting effective demand up. Supplying $PMC = Q$ against effective demand $PMB + s = 60 - Q + 10 = 70 - Q$:

    $$70 - Q = Q \implies Q = 35$$

    This matches the efficient quantity exactly — the subsidy corrects the underproduction.

### General Formula

$$\boxed{t^* \text{ or } s^* = \text{Marginal External Cost or Benefit, evaluated at } Q_{efficient}}$$

!!! warning "The tax/subsidy must target the externality, not the transaction"
    A Pigouvian tax is not simply "a tax on a harmful-looking good" — its *size* must be calibrated to the actual marginal external cost. A tax set too high overcorrects (causing underproduction, a new deadweight loss); set too low, it undercorrects.

---

!!! mascot-encourage "Yes, This One Trips Everyone Up"
    ![Professor Owl encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If the Coase theorem feels slippery on a first read, that's completely normal -- it's one of the most counterintuitive results in this course. The trick is to stop asking "who's at fault?" and start asking "is there a trade both sides would accept?" Work through the numbers in both bargaining directions below, slowly, and the logic will click into place.

## 13.4 The Coase Theorem and Private Bargaining

### Statement of the Theorem

Taxes and subsidies require the government to measure the externality and intervene. The economist Ronald Coase argued that under certain conditions, externalities can instead be resolved **privately**, without government action at all.

**The Coase Theorem:** If property rights are clearly defined, transaction costs are low, and bargaining is possible, private parties can negotiate their way to the economically efficient outcome regardless of who initially holds the legal right.

The key insight is that the party suffering the externality and the party causing it can bargain: whichever arrangement produces more total surplus will be reached, because any surplus left on the table creates room for a mutually beneficial deal.

### Worked Numerical Example

A factory's production generates noise that annoys a neighboring resident. The factory earns \$500/week in profit from its current activity. The noise is worth \$300/week to the resident to eliminate (i.e., the resident would be willing to pay up to \$300/week to make the factory quiet, or alternatively, suffers \$300/week of harm from the noise).

**Case A: The resident has the legal right to quiet (the factory must get consent to make noise).**

The factory can offer to pay the resident for the right to continue operating noisily. Since the factory earns \$500/week — more than the resident's \$300/week cost of enduring the noise — a bargain exists: the factory offers, say, \$350/week to the resident, who accepts (better than \$0, and the factory still nets \$500 − \$350 = \$150 profit, better than shutting down). The factory **continues operating**, which is efficient because its value ($500) exceeds the harm it causes ($300).

**Case B: The factory has the legal right to make noise (no consent needed).**

The resident could try to pay the factory to stop. But the resident would only be willing to pay up to \$300/week, while the factory would need at least \$500/week to be compensated for stopping. No price exists that makes both sides better off, so **no deal happens** — the factory continues operating.

!!! note "The efficient outcome is the same either way"
    In both cases, the factory continues operating — the economically efficient outcome, since its value (\$500) exceeds the harm (\$300). The assignment of the legal right only changes *who pays whom*, not *what happens*: with resident's rights, the factory pays the resident; with factory's rights, no payment occurs. This is the heart of the Coase theorem — efficiency does not depend on the initial allocation of rights, as long as bargaining is costless.

### Why the Coase Theorem Often Fails in Practice

Coasean bargaining breaks down when:

- **Transaction costs are high** — negotiating and enforcing an agreement (lawyers, monitoring) may itself be costly.
- **Many parties are affected** — a factory's pollution may affect thousands of people, making coordinated bargaining prohibitively difficult (a free-rider problem among the victims, discussed in Section 13.8).
- **Property rights are unclear or unenforceable** — if it's unclear who legally "owns" clean air, there is nothing to bargain over.

!!! example "Why air pollution is rarely solved by Coasean bargaining"
    A coal plant's air pollution affects an entire city of residents. Even if the plant has a clearly assigned legal right to pollute, organizing hundreds of thousands of residents to collectively negotiate and pay the plant to reduce emissions is essentially impossible — the transaction costs of coordinating that many people swamp any potential gains. This is precisely why externalities affecting large, diffuse groups are usually handled through Pigouvian taxes or regulation (Section 13.3) rather than private bargaining.

---

## 13.5 Cap-and-Trade Systems

### How Cap-and-Trade Works

A **cap-and-trade system** is a market-based alternative to a Pigouvian tax for correcting a negative externality. The government sets a **cap** — a maximum total quantity of pollution (emissions permits) — and issues (or auctions) permits up to that cap. Firms are then free to **trade** permits among themselves.

### Why Trading Achieves Efficiency at Least Cost

Firms differ in how costly it is for them to reduce emissions (their **marginal abatement cost**). A firm with a *low* cost of reducing emissions will find it cheaper to cut its own pollution and sell its spare permits than to keep polluting; a firm with a *high* cost of reducing emissions will prefer to buy permits rather than cut back. Trading continues until every firm's marginal cost of abatement is equalized to the market permit price $p^*$:

$$MAC_1 = MAC_2 = \cdots = MAC_n = p^*$$

This achieves the *overall* emissions target (set by the cap) at the lowest possible total cost — exactly the same total abatement is achieved as a uniform Pigouvian tax of $p^*$ per unit would achieve, but the cap guarantees the *quantity* of pollution directly, whereas the tax guarantees the *price* directly.

!!! example "Cap-and-trade numerical example"
    Two firms each currently emit 100 tons of pollution. Firm A's marginal abatement cost is $MAC_A = 2x$ (where $x$ is tons abated); Firm B's is $MAC_B = 8x$. The regulator caps total emissions at 150 tons, requiring 50 tons of total abatement, and issues 150 permits.

    Efficient abatement requires $MAC_A = MAC_B$ at the margin:

    $$2x_A = 8x_B, \quad x_A + x_B = 50$$

    Substituting $x_A = 4x_B$: $4x_B + x_B = 50 \implies x_B = 10, \; x_A = 40$.

    Firm A (which can abate cheaply) does most of the abatement (40 tons), while Firm B (which finds abatement expensive) does little (10 tons) and instead buys permits from Firm A. The market-clearing permit price equalizes marginal costs: $p^* = MAC_A(40) = 2(40) = \$80 = MAC_B(10) = 8(10) = \$80$. Total abatement cost is minimized compared to, say, requiring both firms to cut emissions by 25 tons each.

---

## 13.6 Public Goods: Definition and the Efficient Provision Condition

### Recap: Non-Excludable and Non-Rival

As introduced in Chapter 12, a **public good** is both non-excludable and non-rival. Classic examples include national defense, lighthouses, basic scientific research, and public fireworks displays.

### The Samuelson Condition

Because a public good is non-rival, *everyone* who values it can simultaneously enjoy the same unit — so the efficient quantity is found by **summing** each person's marginal benefit (vertically adding demand curves), not by the usual horizontal summation used for private goods.

$$\text{Efficient Quantity: } \sum_{i=1}^{n} MB_i = MC$$

This is often called the **Samuelson condition** for public goods, in contrast to the private-good efficiency condition $MB_i = MC$ for each individual.

!!! mascot-thinking "Why You Add, Not Choose"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    This is the moment this chapter asks you to unlearn a habit from earlier chapters: for a private good, you add up quantities at a given price (horizontal summation); for a public good, where everyone consumes the same unit simultaneously, you add up what each person is willing to pay for that unit instead (vertical summation). Same word, "add," but a completely different operation -- mixing them up is the single most common Samuelson-condition mistake.

!!! example "Worked example: a neighborhood fireworks display"
    Three neighbors value a fireworks display as follows: Neighbor 1's marginal benefit is $MB_1 = 30 - Q$, Neighbor 2's is $MB_2 = 20 - Q$, Neighbor 3's is $MB_3 = 10 - Q$ (where $Q$ is display size/intensity). The marginal cost of a bigger display is $MC = 2Q$.

    Because fireworks are non-rival, sum the marginal benefits vertically:

    $$\sum MB_i = (30 - Q) + (20 - Q) + (10 - Q) = 60 - 3Q$$

    Set $\sum MB_i = MC$:

    $$60 - 3Q = 2Q \implies 60 = 5Q \implies Q^* = 12$$

    The efficient display size is $Q^* = 12$ — far larger than what any single neighbor would privately fund alone (Neighbor 1 alone would set $MB_1 = MC \implies 30 - Q = 2Q \implies Q = 10$, and Neighbors 2 and 3 would fund even less, or nothing, on their own).

---

## 13.7 The Free-Rider Problem

### Why Public Goods Are Underprovided

Because a public good is non-excludable, no individual can be forced to pay for it, and each person has an incentive to **free ride**: let others pay for the good while still enjoying its benefits. If everyone free rides, the good may not get funded at all, even though its total social value exceeds its cost.

### A Simple Game-Theoretic Example

Suppose two neighbors are each deciding whether to **Contribute** \$60 toward a \$100 streetlight that benefits both of them equally (each values the streetlight at \$80 if it is built, regardless of who paid). The streetlight gets built if at least one neighbor contributes \$60 (the other contributing \$40 to cover the rest) — but to keep this simple, suppose the light is built if and only if **both** contribute \$50 each, totaling the required \$100.

| | Neighbor 2: Contribute (\$50) | Neighbor 2: Free Ride (\$0) |
|---|---|---|
| **Neighbor 1: Contribute (\$50)** | Light built. Each nets $80 - 50 = \$30$ | Light not built. N1 nets $-\$50$, N2 nets \$0 |
| **Neighbor 1: Free Ride (\$0)** | Light not built. N1 nets \$0, N2 nets $-\$50$ | Light not built. Both net \$0 |

This is a **prisoner's dilemma** structure (Chapter 10): mutual contribution ($30, $30) is better for both than mutual free-riding ($0, $0), but each neighbor's individually dominant strategy is to free ride — if the other contributes, free riding yields \$80 (full benefit, no cost) which is better than \$30; if the other free rides, contributing alone yields $-\$50$, which is worse than \$0. The dominant strategy for both is **Free Ride**, so the Nash equilibrium is (Free Ride, Free Ride) — the light does not get built, even though building it ($30 + $30 = $60 net total surplus) is better than not building it ($0 total).

!!! warning "The free-rider problem is exactly why public goods need government provision"
    Private, voluntary contribution systematically underprovides public goods for the same reason underlying every prisoner's dilemma: individually rational behavior produces a collectively inefficient outcome. This is the central economic argument for financing public goods through compulsory taxation rather than voluntary donation.

---

## 13.8 Providing Public Goods: Voting and Public Choice

Because public goods are typically funded through government rather than markets, **how** government decides how much to provide becomes an economic question in its own right — the field of **public choice** theory.

### Majority Voting and the Median Voter

Under simple majority rule with a single issue (e.g., "how large should the public park budget be?"), and if voters' preferences are *single-peaked* (each voter has one preferred amount, and support falls off as proposals move further from it in either direction), the **median voter theorem** predicts that the outcome of majority voting will match the preference of the **median voter** — the voter exactly in the middle of the preference distribution.

!!! example "Median voter theorem in action"
    Five town residents have the following preferred annual park budgets: \$10,000, \$30,000, \$50,000, \$70,000, \$200,000. Under pairwise majority voting between any two proposals, the \$50,000 proposal (the median) will defeat any other proposal, because it can always attract support from the voters on the side closer to it. The outcome converges to the median voter's preferred amount, regardless of the mean (which here is \$72,000) — a very wealthy or very frugal outlier does not dominate the outcome the way it would in a market purchase decision.

### Limitations

Majority voting can still produce inefficient outcomes relative to the Samuelson condition (Section 13.6) — the median voter's preferred quantity generally does not equal the surplus-maximizing quantity, because voting does not weight preferences by intensity (a voter who cares passionately gets the same one vote as someone who barely cares). This is one reason public-goods provision remains a persistently debated area of policy.

---

## 13.9 Common-Pool Resources: Fisheries, Groundwater, and Congestion

Chapter 12 introduced the tragedy of the commons; here we examine concrete policy tools used to prevent it.

| Resource | Problem | Policy Tool | How It Works |
|---|---|---|---|
| **Ocean fisheries** | Overfishing collapses fish stocks | Individual Transferable Quotas (ITQs) | Each fisher is allocated a tradable share of the total allowable catch, creating a property right that rewards conservation |
| **Groundwater aquifers** | Over-pumping depletes the water table | Water rights / pumping permits | Usage rights are defined and limited, often tradable, so users bear the cost of their own extraction |
| **Road congestion** | Each driver imposes delay on others | Congestion pricing | Tolls that rise with congestion force drivers to internalize the delay they impose on others, similar to a Pigouvian tax |

!!! example "Congestion pricing as a Pigouvian tax on a common-pool resource"
    A congested highway lets 10,000 cars through per hour for free, but average delay rises sharply with each additional car — a cost each driver imposes on every other driver but does not personally pay. A congestion toll of \$8 during peak hours, calibrated to the marginal external delay cost each driver imposes, reduces traffic to the efficient volume, exactly paralleling the Pigouvian tax logic of Section 13.3 applied to a common-pool resource instead of ordinary pollution.

The common thread across all three tools is the same insight from Section 13.4's Coase theorem and Section 13.3's Pigouvian taxes: **assigning well-defined, enforceable property rights (or their price equivalent) forces users to internalize the costs they impose on others**, converting a tragedy-of-the-commons problem into one where private incentives align with social efficiency.

#### Diagram: Pigouvian Tax Explorer

<details markdown="1">
<summary>Pigouvian Tax Explorer</summary>
Type: microsim
**sim-id:** pigouvian-tax-explorer<br/>
**Library:** p5.js<br/>
**Status:** Specified<br/>
**Bloom Level:** Apply<br/>
**Bloom Verb:** calculate<br/>
**Learning Objective:** The learner will calculate the per-unit Pigouvian tax that restores the socially efficient quantity, given the chapter's private marginal cost, demand, and marginal external cost values.

**Prerequisites:** private marginal cost, social marginal cost, marginal external cost, Pigouvian tax (Sections 13.1, 13.3).

**Evidence of Mastery:** For 1 additional challenge, the learner computes the efficient quantity, the optimal tax, and the resulting tax revenue. Correct within ±0.5 units / ±\$1 for each of the 3 values. Mastery requires all 3 correct.

**Misconceptions:** (1) Believing the tax should equal the full social marginal cost rather than just the external-cost wedge. (2) Forgetting that the unregulated market quantity does not depend on MEC at all, since the firm ignores the externality by definition. (3) Computing tax revenue using the market quantity instead of the efficient quantity actually traded once the tax is imposed.

**Instructional Rationale:** An Apply-level task needs the learner to execute the chapter's own three-step procedure (find the market quantity, find the efficient quantity, set tax=MEC) on a new MEC value, reusing the exact method the chapter demonstrates.

**Content:**

The chapter's own steel-mill example (Sections 13.1, 13.3): private marginal cost PMC=2Q, demand (=social marginal benefit) P=100−Q, marginal external cost MEC=\$20/unit (constant).

| MEC | Market Q (PMC=demand) | Efficient Q (SMC=demand) | Optimal tax t* | Tax revenue |
|---|---|---|---|---|
| \$20 (base case) | 33.3 | 26.7 | \$20 | \$534 |
| \$30 (challenge) | 33.3 | 23.3 | \$30 | \$700 |

**Provenance:** From the chapter's own "Worked example: a steel mill polluting a river" (Section 13.1) and "Setting the optimal tax" (Section 13.3). The MEC=\$30 challenge is an illustrative extension using the same PMC and demand curves.

**Rules:** Market equilibrium: PMC = demand → 2Q = 100−Q. Efficient quantity: social marginal cost (PMC+MEC) = demand → 2Q+MEC = 100−Q. Optimal tax t* = MEC, since MEC is constant here (the chapter's own shortcut). Tax revenue = t* × efficient quantity. Marginal external cost MEC: min \$10, max \$40, step \$5, default \$20.

**Learner Activity:**

1. The learner watches the base case (MEC=\$20) solved step by step, reproducing the chapter's own numbers: market Q=33.3, efficient Q=26.7, t*=\$20, revenue=\$534.
2. The learner sets MEC to \$30 and types the efficient quantity, the optimal tax, and the tax revenue.
3. The sim checks all three values and shows the shifted PMC+t line intersecting demand at the new efficient quantity.

**Feedback:** 1 scored challenge (3 sub-values), two attempts. Correct: "Correct: efficient Q ≈ 23.3, t* = \$30, revenue ≈ \$700." Incorrect (first attempt): "Recompute social marginal cost as PMC + MEC, then set it equal to demand; the tax equals MEC directly since MEC is constant here." After the second wrong attempt, the full worked solution is shown. A result "Challenge correct: yes/no" is shown.

**Starting State:** MEC is set to \$20, with PMC, demand, and the social-marginal-cost line all plotted, market Q=33.3 and efficient Q=26.7 both marked, and the optimal tax t*=\$20 stated. The question on screen is "If the marginal external cost were \$30 instead of \$20, what tax restores efficiency — and how much revenue would it raise?"

**Chapter Anchors:** The chapter's Sections 13.1 and 13.3 state market Q=33.3, efficient Q=26.7, t*=\$20, and tax revenue=\$534 for PMC=2Q, demand=100−Q, MEC=\$20; the sim's base-case demonstration reproduces all four values exactly.
</details>

---

## Key Terms

| Term | Definition |
|---|---|
| **Social Marginal Cost (SMC)** | Private marginal cost plus the marginal external cost |
| **Social Marginal Benefit (SMB)** | Private marginal benefit plus the marginal external benefit |
| **Marginal External Cost (MEC)** | The cost of one more unit of production imposed on third parties |
| **Marginal External Benefit (MEB)** | The benefit of one more unit of consumption enjoyed by third parties |
| **Pigouvian Tax** | A per-unit tax equal to the marginal external cost, correcting a negative externality |
| **Pigouvian Subsidy** | A per-unit subsidy equal to the marginal external benefit, correcting a positive externality |
| **Coase Theorem** | With clear property rights, low transaction costs, and bargaining, private parties reach the efficient outcome regardless of who holds the rights |
| **Cap-and-Trade** | A system capping total pollution and allowing firms to trade permits, equalizing marginal abatement costs |
| **Marginal Abatement Cost (MAC)** | The cost of reducing pollution by one more unit |
| **Samuelson Condition** | Efficient public-goods provision requires the *sum* of individual marginal benefits to equal marginal cost |
| **Free-Rider Problem** | The incentive to let others pay for a non-excludable good while still enjoying its benefits |
| **Median Voter Theorem** | Majority voting on a single issue with single-peaked preferences yields the median voter's preferred outcome |
| **Individual Transferable Quota (ITQ)** | A tradable property right to harvest a fixed share of a common-pool resource |
| **Congestion Pricing** | A toll that rises with congestion, forcing drivers to internalize the delay they impose on others |

---

## Practice Problems

### Problem 1 — Pigouvian Tax for a Negative Externality

A paper mill has private marginal cost $PMC = 3Q$ and faces demand $P = 150 - 2Q$. Each unit of paper produced imposes a constant marginal external cost of $MEC = \$15$ on a downstream community (water pollution).

**a)** Find the market (unregulated) equilibrium quantity.
**b)** Find the socially efficient quantity.
**c)** Find the optimal Pigouvian tax, and verify that it induces the efficient quantity.
**d)** Calculate the deadweight loss of the unregulated market outcome.

??? success "Solution"
    **a)** Set $PMC = P$: $3Q = 150 - 2Q \implies 5Q = 150 \implies Q_{market} = 30$.

    **b)** $SMC = 3Q + 15$. Set $SMC = P$: $3Q + 15 = 150 - 2Q \implies 5Q = 135 \implies Q_{efficient} = 27$.

    **c)** $t^* = MEC = \$15$. With the tax, firms face $PMC + t = 3Q + 15$, and setting this equal to demand reproduces exactly $Q = 27$ from part (b) — confirmed.

    **d)** $DWL = \frac{1}{2} \times (30 - 27) \times 15 = \frac{1}{2} \times 3 \times 15 = \$22.50$.

### Problem 2 — Pigouvian Subsidy for a Positive Externality

Private demand for a job-training program is $P = 80 - Q$, and marginal cost is $MC = Q$. Each unit of training generates a marginal external benefit of $MEB = \$20$ (employers and the broader economy benefit from a more skilled workforce).

**a)** Find the market equilibrium quantity.
**b)** Find the efficient quantity.
**c)** Find the optimal per-unit subsidy.

??? success "Solution"
    **a)** $80 - Q = Q \implies Q_{market} = 40$.

    **b)** $SMB = 80 - Q + 20 = 100 - Q$. Set $100 - Q = Q \implies Q_{efficient} = 50$.

    **c)** $s^* = MEB = \$20$. The subsidy raises effective demand to $100 - Q$, which (as shown in part b) yields $Q = 50$, confirming the efficient outcome.

### Problem 3 — The Coase Theorem

A dry cleaner's machine vents fumes that bother a bookstore next door. Operating the machine is worth \$400/week to the dry cleaner. The fumes cost the bookstore \$250/week in lost business (customers avoid the smell).

**a)** Suppose the bookstore has the legal right to clean air. Will the dry cleaner continue to operate? Describe a possible bargain.
**b)** Suppose instead the dry cleaner has the legal right to operate without restriction. Will the dry cleaner continue to operate?
**c)** Is the outcome efficient in both cases? Explain why or why not.
**d)** Now suppose operating the machine is only worth \$200/week to the dry cleaner (less than the \$250/week harm). Redo parts (a) and (b).

??? success "Solution"
    **a)** The dry cleaner can offer to pay the bookstore for the right to operate. Since \$400 > \$250, a bargain exists (e.g., the dry cleaner pays the bookstore \$280/week): the bookstore is better off than with \$0, and the dry cleaner still nets \$400 − \$280 = \$120, better than shutting down. **The dry cleaner continues operating.**

    **b)** The bookstore could try to pay the dry cleaner to stop, but would only pay up to \$250, while the dry cleaner needs at least \$400 to accept. No deal is possible. **The dry cleaner continues operating** (since it has the right to, and no one pays it to stop).

    **c)** Yes, efficient in both cases — the dry cleaner's operation generates \$400 of value against only \$250 of harm, so continued operation maximizes total surplus regardless of who holds the legal right. This illustrates the Coase theorem: the assignment of property rights affects *who pays whom*, not the efficient *outcome*.

    **d)** Now the machine is worth only \$200, less than the \$250 harm. **(a)** With the bookstore holding the right: the dry cleaner cannot offer enough (its maximum willingness to pay is \$200, less than the bookstore's \$250 minimum to accept), so no deal is struck — **the dry cleaner stops operating**. **(b)** With the dry cleaner holding the right: the bookstore can now profitably pay the dry cleaner to stop (the bookstore is willing to pay up to \$250, more than the \$200 needed to compensate the dry cleaner for lost value) — e.g., bookstore pays \$220, **the dry cleaner stops operating**. In both cases the efficient outcome (stop operating, since harm \$250 > value \$200) is reached.

### Problem 4 — Public Goods and the Samuelson Condition

Four households are considering funding a shared community garden. Their marginal benefits are $MB_1 = 40 - 2Q$, $MB_2 = 30 - 2Q$, $MB_3 = 20 - 2Q$, $MB_4 = 10 - 2Q$. The marginal cost of expanding the garden is $MC = 5Q$.

**a)** Write the condition for efficient provision of this public good.
**b)** Solve for the efficient size $Q^*$.
**c)** If only Household 1 funded the garden alone, what size would they choose? Compare to $Q^*$ and explain the discrepancy.

??? success "Solution"
    **a)** Since the garden is non-rival, sum marginal benefits vertically and set equal to marginal cost: $\sum MB_i = MC$.

    **b)** $\sum MB_i = (40 - 2Q) + (30 - 2Q) + (20 - 2Q) + (10 - 2Q) = 100 - 8Q$. Set $100 - 8Q = 5Q \implies 100 = 13Q \implies Q^* \approx 7.69$.

    **c)** Alone, Household 1 sets $MB_1 = MC$: $40 - 2Q = 5Q \implies 40 = 7Q \implies Q = 5.71$. This is well below the efficient $Q^* \approx 7.69$, because Household 1 ignores the benefits the garden provides to Households 2, 3, and 4 — a textbook illustration of why voluntary private provision underprovides public goods relative to the socially efficient quantity.

### Problem 5 — The Free-Rider Game

Two roommates are deciding whether to clean their shared apartment. Cleaning costs each roommate 2 hours of effort (valued at \$20/hour, so \$40 of cost) if they do it. A clean apartment is worth \$50 to each roommate, regardless of who cleaned it. If at least one roommate cleans, the apartment is clean; if neither cleans, it stays dirty (worth \$0 to both).

**a)** Construct the payoff matrix for (Clean, Don't Clean) for both roommates.
**b)** Find the Nash equilibrium (or equilibria).
**c)** Is the outcome efficient? What does this illustrate about public goods?

??? success "Solution"
    **a)** Payoffs (Roommate 1, Roommate 2), net of cleaning cost where applicable:

    | | R2: Clean | R2: Don't Clean |
    |---|---|---|
    | **R1: Clean** | $(50-40, 50-40) = (10, 10)$ | $(50-40, 50) = (10, 50)$ |
    | **R1: Don't Clean** | $(50, 50-40) = (50, 10)$ | $(0, 0)$ |

    **b)** Each roommate's best response is to let the *other* clean: if R2 cleans, R1 prefers Don't Clean (50 > 10); if R2 doesn't clean, R1 prefers Clean (10 > 0)... wait — check carefully: if R2 doesn't clean, R1 comparing Clean (10) vs. Don't Clean (0) prefers **Clean**. So there is no single dominant strategy here; instead there are **two pure-strategy Nash equilibria**: (Clean, Don't Clean) and (Don't Clean, Clean) — in each, exactly one roommate free rides on the other's cleaning, earning \$50 while the cleaner earns only \$10. (Note: unlike the streetlight example in Section 13.7, here a single contributor suffices to provide the good, so this is a "volunteer" coordination game rather than a strict prisoner's dilemma.)

    **c)** Both equilibria are efficient in the sense that the apartment does get cleaned (total surplus $10 + 50 = 60$ far exceeds the $(0,0)$ outcome), but they are *inequitable* — one roommate free rides entirely while the other bears the full cost. This illustrates that even when a public good does get provided, free-riding incentives can create an unfair distribution of who bears the cost, and in larger groups (more than two) or with higher cleaning costs relative to the benefit, this type of game can easily collapse to the inefficient (Don't Clean, Don't Clean) outcome instead, just as in the streetlight example.

---

!!! mascot-celebration "You've Tamed Market Failure"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Take a moment -- you just worked through Pigouvian taxes, the Coase theorem, cap-and-trade, the Samuelson condition, and the free-rider problem, five of the trickiest ideas in microeconomics, and came out able to solve all of them numerically. Every choice has a trade-off, and now you know how to find the one society as a whole should make, even when markets alone won't get us there.

---

!!! tip "Next Chapter"
    In [Chapter 14: Information Economics](../14-information-economics/index.md), we examine how asymmetric information — introduced briefly in Chapter 12 — shapes markets for insurance, used cars, labor, and credit, and what tools (signaling, screening, and contracts) can mitigate adverse selection and moral hazard.
