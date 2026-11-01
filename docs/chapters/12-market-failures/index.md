# Chapter 12: Market Failures

## Learning Objectives

After completing this chapter, you will be able to:

1. Explain the conditions required for competitive markets to be efficient, and identify when those conditions break down
2. Distinguish negative and positive externalities and explain why each leads markets away from the efficient outcome
3. Define public goods and common-pool resources using the non-excludability and non-rivalry criteria, and explain the free-rider problem and the tragedy of the commons
4. Explain how information asymmetry can cause markets to fail, including adverse selection and moral hazard
5. Explain how market power causes inefficiency distinct from the other sources of market failure
6. Compare taxes, regulation, property rights, and public provision as government responses to market failure
7. Explain the concept of government failure and why government intervention does not automatically fix market failures

---

!!! mascot-welcome "When the Invisible Hand Needs a Nudge"
    ![Professor Owl waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Every choice has a trade-off — and so far this book has mostly shown you markets getting that trade-off right on their own. This chapter is about the cases where they don't: pollution nobody pays for, goods nobody can be excluded from, deals where one side knows something the other doesn't. Understanding exactly *why* a market fails is the first step toward knowing whether — and how — to fix it.

## 12.1 When Do Markets Fail?

Chapter 2 showed that competitive markets, left alone, maximize total surplus — they are **allocatively efficient**. This is sometimes called the **First Welfare Theorem**: under certain conditions, competitive equilibrium is Pareto efficient. But those conditions are demanding, and in the real world they frequently do not hold. A **market failure** occurs whenever the free market, on its own, fails to allocate resources efficiently — that is, whenever the price system does not lead to the surplus-maximizing quantity.

The conditions required for market efficiency — and the ways each can break down — are summarized below. This chapter surveys each category at a broad level; Chapter 13 returns to externalities and public goods in much greater depth.

| Required Condition for Efficiency | What Happens When It Fails | Market Failure Category |
|---|---|---|
| All costs and benefits are borne by buyers and sellers | Costs/benefits spill onto third parties | Externalities |
| Goods are excludable and rival | Goods can be consumed free, or use by one prevents use by others | Public goods / common-pool resources |
| Buyers and sellers have equal, sufficient information | One side knows more than the other | Information asymmetry |
| Many small buyers and sellers, no one with pricing power | A single firm (or few firms) controls price | Market power |

!!! note "Efficiency is the benchmark, not a guarantee"
    None of these conditions is guaranteed to hold. Markets for haircuts, running shoes, and most restaurant meals come close to satisfying all four and function efficiently without intervention. Markets for pollution, lighthouses, vaccines, and used cars do not — and that is precisely where this chapter focuses.

!!! mascot-thinking "Efficiency Was Never Magic — It Was a Checklist"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Here's the mental model for this whole chapter: the First Welfare Theorem holds only when all four conditions in that table hold at once. Every topic between here and Section 12.6 is really just "which line of the checklist failed, and what does that specific failure look like?"

---

## 12.2 Externalities: Negative and Positive

An **externality** exists when a transaction between a buyer and seller imposes costs or benefits on a third party who is not part of that transaction and whose interests are not reflected in the market price.

### Negative Externalities

A **negative externality** imposes a cost on third parties. The classic example is pollution: a factory's private cost of production does not include the cost of the air pollution it imposes on nearby residents. Because the firm does not pay for this cost, its private marginal cost curve lies *below* the true social marginal cost curve, and the market produces **more than the efficient quantity**.

$$\text{Social Marginal Cost} = \text{Private Marginal Cost} + \text{External Cost}$$

### Positive Externalities

A **positive externality** generates a benefit for third parties. Education is a common example: when you get vaccinated or become more educated, you benefit personally, but society also gains (lower disease transmission, a more informed citizenry, higher productivity of coworkers) in ways the market price does not capture. Because the market ignores this external benefit, the market produces **less than the efficient quantity**.

$$\text{Social Marginal Benefit} = \text{Private Marginal Benefit} + \text{External Benefit}$$

!!! example "Everyday externalities"
    - **Negative:** A loud late-night party (noise imposed on neighbors); a factory dumping waste in a river (harm to downstream users); vehicle emissions (climate and health costs borne by everyone).
    - **Positive:** A beekeeper's bees pollinating a neighboring orchard; a homeowner's beautiful garden raising neighborhood property values; getting a flu vaccine (reduces the chance others get sick).

Chapter 13 develops the full graphical and mathematical apparatus — including Pigouvian taxes, the Coase theorem, and cap-and-trade — for correcting externalities. For now, the key takeaway is the *direction* of the distortion: negative externalities cause overproduction, positive externalities cause underproduction, relative to the socially efficient level.

---

## 12.3 Public Goods: Non-Excludable, Non-Rival

Economists classify goods along two independent dimensions:

- **Excludable:** Can the seller prevent people who do not pay from consuming the good?
- **Rival:** Does one person's consumption reduce the amount available for others?

| | Rival | Non-Rival |
|---|---|---|
| **Excludable** | **Private goods** (a sandwich, a haircut) | **Club goods** (cable TV, a gym membership) |
| **Non-Excludable** | **Common-pool resources** (ocean fisheries, groundwater) | **Public goods** (national defense, basic research, lighthouses) |

!!! mascot-tip "Two Yes/No Questions, Four Boxes, No Ambiguity"
    ![Professor Owl with a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Here's a fast way to classify any good on an exam: ask two questions in order. "Can the seller stop a non-payer from using it?" settles excludability. "Does my use leave less for you?" settles rivalry. Two yes/no answers drop you straight into the right box of that table.

A pure **public good** is both **non-excludable** (you cannot stop someone from consuming it even if they do not pay) and **non-rival** (one person's use does not diminish another's). National defense is the textbook example: protecting the country protects every resident, whether or not they paid taxes toward it, and one additional resident being "defended" does not reduce the defense available to anyone else.

Because no one can be excluded from enjoying a public good, private firms generally cannot profitably produce it — people have an incentive to **free ride**, consuming the benefit without paying. This is why public goods are typically funded through taxation and provided by government. Chapter 13 develops the free-rider problem and voting mechanisms for public goods provision in detail.

---

## 12.4 Common-Pool Resources and the Tragedy of the Commons

A **common-pool resource** is rival (one person's use depletes what is available to others) but non-excludable (no one can easily be stopped from using it). Ocean fisheries, groundwater aquifers, and unregulated grazing land are classic examples.

!!! mascot-warning "Same 'Non-Excludable' Label, Opposite Problem"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    Don't let the shared "non-excludable" label fool you into treating public goods and common-pool resources as the same problem. A public good (Section 12.3) is non-rival — my use doesn't reduce yours, so underfunding is the danger, not overuse. A common-pool resource is rival — which is exactly what makes overuse, not underfunding, the central threat here.

The **tragedy of the commons** describes what happens when a resource is open to all: because no individual user bears the full cost of their own extraction (part of that cost — the depleted resource — is spread across all other users), each person has a private incentive to overuse the resource even though collectively everyone would be better off with restraint. The result is systematic overexploitation and, in extreme cases, collapse of the resource.

!!! example "Historical and modern tragedies of the commons"
    - **Atlantic cod fisheries:** Decades of unrestricted fishing collapsed cod stocks off Newfoundland in the early 1990s, devastating an industry that had operated for centuries.
    - **Groundwater aquifers:** Farmers pumping from a shared aquifer have no individual incentive to conserve, since water they leave in the ground may simply be pumped by a neighbor instead.
    - **Traffic congestion:** Each additional driver on a congested highway imposes delay on all other drivers but bears only a small fraction of that cost personally.

Chapter 13 revisits common-pool resources with specific policy tools (catch shares, water rights, congestion pricing).

---

## 12.5 Information Asymmetry

**Information asymmetry** exists when one party to a transaction has more or better information than the other. This can prevent markets from reaching efficient outcomes even when goods are perfectly rival, excludable, and free of externalities.

### Adverse Selection

**Adverse selection** occurs when the party with *less* information ends up disproportionately transacting with the "worse" types from the other side, because information about quality is hidden *before* the transaction. The classic case is George Akerlof's "market for lemons": in a used-car market, sellers know whether their car is reliable or a "lemon," but buyers cannot tell. Buyers, unwilling to pay top price for a car that might be a lemon, offer only an average price — which then drives owners of genuinely good cars out of the market, leaving a disproportionate share of lemons for sale.

### Moral Hazard

**Moral hazard** occurs when one party changes their behavior *after* a transaction in ways the other party cannot observe or verify, because they no longer bear the full consequences of that behavior. A driver with comprehensive insurance may drive somewhat less carefully than an uninsured driver, since the insurer — not the driver — bears most of the cost of an accident.

!!! mascot-thinking "Before the Deal, or After It? That's the Whole Distinction"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Notice that timing is the entire difference between these two ideas: adverse selection is about hidden information *before* the deal is struck (who you're really dealing with), while moral hazard is about hidden behavior *after* the deal is struck (what they do once the incentives change). Ask yourself "before or after the contract?" and you'll never mix the two up again.

!!! tip "Looking ahead"
    Adverse selection and moral hazard, along with signaling and screening as partial solutions, are developed fully in Chapter 14: Information Economics.

---

## 12.6 Market Power as a Source of Failure

Chapters 7–9 showed that monopoly, monopolistic competition, and oligopoly all involve firms with some ability to set price above marginal cost. This **market power** is itself a distinct source of inefficiency, separate from externalities, public goods, or information problems.

A monopolist restricts output below the competitive level to raise price, creating **deadweight loss**: transactions that would make both the firm and some consumers better off simply do not happen, because the monopolist's profit-maximizing quantity is lower than the surplus-maximizing quantity.

$$Q_{monopoly} < Q_{competitive} \implies \text{Deadweight Loss} > 0$$

Unlike externalities, this failure does not require any third party at all — it can occur in a two-party market with no spillovers whatsoever, simply because the seller is not a price-taker. Policy responses include antitrust enforcement, price regulation of natural monopolies, and encouraging entry.

!!! example "Quantifying the deadweight loss from market power"
    A market has demand $P = 100 - Q$ and constant marginal cost $MC = 20$ (the same cost a competitive industry would face).

    **Competitive outcome:** Price-taking firms produce until $P = MC$: $100 - Q = 20 \implies Q_{competitive} = 80$.

    **Monopoly outcome:** A monopolist produces until $MR = MC$. With linear demand $P = 100 - Q$, marginal revenue is $MR = 100 - 2Q$. Setting $MR = MC$:

    $$100 - 2Q = 20 \implies Q_{monopoly} = 40, \qquad P_{monopoly} = 100 - 40 = \$60$$

    The monopolist restricts output from 80 units to 40 units and raises price from \$20 to \$60. The deadweight loss is the triangle between the demand curve and $MC$, between $Q_{monopoly}$ and $Q_{competitive}$:

    $$DWL = \frac{1}{2} \times (Q_{competitive} - Q_{monopoly}) \times (P_{monopoly} - MC) = \frac{1}{2} \times 40 \times 40 = \$800$$

    This \$800 of surplus is destroyed — not transferred to anyone — purely because output is restricted below the efficient level. Chapter 7 develops this result in full.

---

## 12.7 Government Responses to Market Failure

Governments have four broad policy tools for addressing market failures. The right tool depends on which type of failure is present.

| Policy Tool | Best Suited For | Example |
|---|---|---|
| **Taxes (Pigouvian)** | Negative externalities | Carbon tax, cigarette tax |
| **Subsidies** | Positive externalities | Vaccine subsidies, R&D tax credits |
| **Regulation** | Externalities, market power, information gaps | Emissions standards, mandatory product labeling |
| **Property rights** | Common-pool resources | Fishing quotas, tradable water rights |
| **Public provision** | Public goods | National defense, public roads, basic research funding |
| **Antitrust enforcement** | Market power | Breaking up or blocking anticompetitive mergers |

!!! example "Matching the tool to the failure"
    A city with heavy traffic congestion (a common-pool resource problem — roads are rival but hard to exclude people from) might use **congestion pricing** (a form of Pigouvian tax) rather than an R&D subsidy, which would do nothing to address the externality. Conversely, underfunded basic scientific research (a public good with positive externalities) is better addressed through direct public funding than through a tax, since the problem is underprovision, not overprovision.

---

## 12.8 Government Failure

Government intervention is not automatically an improvement over the market outcome. **Government failure** occurs when a policy intended to correct a market failure instead makes outcomes worse, or fails to improve them, due to poor information, political incentives, or unintended side effects.

### Rent-Seeking

**Rent-seeking** is the use of resources to obtain a larger share of existing wealth through the political process, rather than by creating new wealth. Firms may lobby for tariffs, subsidies, or regulations that benefit them specifically, at a cost borne by consumers or taxpayers generally. Because the benefits of rent-seeking are concentrated on a small group (who have a strong incentive to lobby) while the costs are spread across many people (each of whom has little individual incentive to oppose it), rent-seeking policies can persist even when they reduce total surplus.

### Other Sources of Government Failure

- **Imperfect information:** Regulators often know less about industry-specific conditions than the firms they regulate.
- **Principal-agent problems:** Elected officials and bureaucrats may pursue their own re-election or budget-maximizing incentives rather than the public interest.
- **Unintended consequences:** A policy designed to fix one problem may create new distortions elsewhere (e.g., a price ceiling intended to help consumers can create shortages, as seen in Chapter 2's extensions).
- **Regulatory capture:** Regulated industries may come to influence or control the agencies meant to regulate them.

!!! warning "Market failure does not imply government success"
    The existence of a market failure is a *necessary* but not *sufficient* condition for government intervention to improve welfare. Economists compare the costs of the market failure against the costs of likely government failure before recommending intervention — sometimes "do nothing" is still the best available option.

---

## Key Terms

| Term | Definition |
|---|---|
| **Market Failure** | A situation in which the free market fails to allocate resources efficiently |
| **Externality** | A cost or benefit of a transaction that falls on a third party |
| **Negative Externality** | An external cost; leads to market overproduction |
| **Positive Externality** | An external benefit; leads to market underproduction |
| **Excludability** | Whether non-payers can be prevented from consuming a good |
| **Rivalry** | Whether one person's consumption reduces what is available to others |
| **Public Good** | A good that is both non-excludable and non-rival |
| **Common-Pool Resource** | A good that is rival but non-excludable |
| **Tragedy of the Commons** | Overexploitation of a shared resource because no user bears its full cost |
| **Information Asymmetry** | One party to a transaction has more/better information than the other |
| **Adverse Selection** | Hidden information before a transaction skews the market toward "worse" types |
| **Moral Hazard** | Hidden behavior after a transaction changes incentives because consequences are shared |
| **Market Power** | A firm's ability to set price above marginal cost, causing deadweight loss |
| **Pigouvian Tax** | A tax designed to correct a negative externality |
| **Rent-Seeking** | Using resources to capture existing wealth via politics rather than create new wealth |
| **Government Failure** | A policy intervention that fails to improve, or worsens, an inefficient outcome |

---

## Practice Problems

### Problem 1 — Classifying Market Failures

For each scenario, identify the primary type of market failure (externality, public good/common-pool resource, information asymmetry, or market power).

**a)** A pharmaceutical company is the sole producer of a patented life-saving drug and charges a price far above its marginal cost.
**b)** A chemical plant discharges waste into a river used by downstream fishing communities.
**c)** A health insurance applicant knows about a pre-existing condition that the insurer cannot easily verify.
**d)** A small town's fireworks display can be watched by everyone in town, whether or not they contributed to pay for it.

??? success "Solution"
    **a)** **Market power** — a single seller with no competition sets price above marginal cost, independent of any externality or information problem.

    **b)** **Negative externality** — the plant's private cost of production does not include the harm imposed on downstream users.

    **c)** **Information asymmetry (adverse selection)** — the applicant has hidden information about their own risk that the insurer lacks.

    **d)** **Public good** — the fireworks display is non-excludable (anyone in town can watch) and non-rival (one person watching does not reduce what others see), creating a free-rider problem for funding it.

### Problem 2 — Excludability and Rivalry

Classify each good into one of the four categories (private good, club good, common-pool resource, public good) based on excludability and rivalry, and justify your answer.

**a)** A Netflix subscription
**b)** Open-ocean tuna stocks
**c)** A slice of pizza
**d)** Street lighting on a public road

??? success "Solution"
    **a)** **Club good** — excludable (you need a paid subscription), non-rival (your friend watching doesn't reduce your access).

    **b)** **Common-pool resource** — non-excludable (hard to stop anyone from fishing international waters), rival (fish caught by one boat are unavailable to others).

    **c)** **Private good** — excludable (the seller can refuse to give it to you without payment) and rival (once you eat it, no one else can).

    **d)** **Public good** — non-excludable (anyone walking the street benefits from the light) and non-rival (one pedestrian benefiting doesn't reduce the light available to another).

### Problem 3 — Matching Policy to Failure

For each market failure below, recommend the most appropriate government response from Section 12.7 (tax, subsidy, regulation, property rights, public provision, or antitrust) and briefly justify your choice.

**a)** Overfishing in a shared coastal fishery.
**b)** A factory emitting air pollution with no regulation.
**c)** Underfunded basic scientific research with broad social spillover benefits.
**d)** A proposed merger between the only two firms in a local cable market.

??? success "Solution"
    **a)** **Property rights** (e.g., individual transferable fishing quotas) — assigning each fisher an enforceable share of the total allowable catch gives them a private incentive to conserve the resource's long-run value, directly addressing the common-pool resource problem.

    **b)** **Pigouvian tax or regulation** (e.g., an emissions tax or an emissions cap) — forces the factory to internalize the external cost of its pollution, or legally limits the externality directly.

    **c)** **Subsidy or public provision** — since the social benefit of research exceeds the private benefit captured by the researcher, the government should subsidize or directly fund research to increase it toward the efficient level.

    **d)** **Antitrust enforcement** (block or restrict the merger) — combining the only two firms would create a monopoly, which would restrict output and raise prices; antitrust review protects against this specific type of market-power failure.

### Problem 4 — Government Failure

A city government, concerned about a shortage of affordable housing (which it attributes to market failure), imposes strict rent control, capping rents well below the market-clearing level.

**a)** Is a shortage of affordable housing, by itself, necessarily evidence of a market failure? Explain.
**b)** Using the supply-and-demand framework from Chapter 2, predict the effect of the rent cap on the quantity of housing supplied and demanded.
**c)** Explain how this policy could be an example of government failure.

??? success "Solution"
    **a)** Not necessarily. High rents might simply reflect high demand relative to a scarce resource (land in a desirable location) rather than any failure of the market mechanism itself — the market may be functioning efficiently even though the equilibrium price is high. A true market failure would require, e.g., an externality, information problem, or market power specific to the housing market (such as zoning-driven monopoly power among developers).

    **b)** A rent cap set below the equilibrium rent creates a **shortage**: quantity demanded exceeds quantity supplied at the capped price, exactly as in Chapter 2's price-ceiling analysis. Landlords have less incentive to maintain or build new rental housing, and more renters want apartments than are available.

    **c)** This is a textbook case of government failure: a policy intended to make housing more "affordable" instead reduces the quantity supplied, worsens the shortage, and can lead to under-maintenance of existing units and inefficient allocation of apartments (e.g., to those with longest tenure rather than greatest need) — the intervention makes the underlying problem worse rather than correcting a genuine market failure.

### Problem 5 — Market Power and Deadweight Loss

A city grants an exclusive franchise to a single cable provider. Market demand for cable service is $P = 80 - Q$, and the constant marginal cost of providing service is $MC = 20$.

**a)** Find the quantity and price that would prevail if the market were competitive ($P = MC$).
**b)** Find the monopolist's profit-maximizing quantity and price (recall $MR = 80 - 2Q$ for linear demand $P = 80 - Q$).
**c)** Calculate the deadweight loss created by the exclusive franchise.
**d)** Suppose a lobbying firm could spend up to the entire gain in monopoly profit to keep the franchise exclusive. Relate this to the concept of rent-seeking from Section 12.8.

??? success "Solution"
    **a)** $80 - Q = 20 \implies Q_{competitive} = 60, \; P_{competitive} = \$20$.

    **b)** Set $MR = MC$: $80 - 2Q = 20 \implies Q_{monopoly} = 30, \; P_{monopoly} = 80 - 30 = \$50$.

    **c)** $DWL = \frac{1}{2} \times (60 - 30) \times (50 - 20) = \frac{1}{2} \times 30 \times 30 = \$450$.

    **d)** The monopolist's profit from the franchise is $(P_{monopoly} - MC) \times Q_{monopoly} = (50-20) \times 30 = \$900$ above the competitive (zero-profit) benchmark. Because this \$900 is a prize created purely by restricting entry, the firm (or a lobbyist acting for it) has an incentive to spend resources — up to nearly \$900 — on lobbying to preserve the exclusive franchise. Those lobbying expenditures produce no new goods or services; they are pure **rent-seeking**, and the resources spent on them are a *further* social loss layered on top of the original \$450 deadweight loss from restricted output.

---

!!! mascot-celebration "You Can Now Diagnose Why a Market Is Failing"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    Externalities, public goods, information asymmetry, market power, and even the ways government intervention can backfire — you worked through every major category economists use to explain why markets don't always deliver efficient outcomes on their own. That diagnostic skill is exactly what Chapter 13 builds on, going deep on the tools that fix externalities and fund public goods.

!!! tip "Next Chapter"
    In [Chapter 13: Externalities and Public Goods](../13-externalities-and-public-goods/index.md), we return to externalities and public goods in much greater depth — deriving the Pigouvian tax mathematically, working through the Coase theorem, and analyzing cap-and-trade and public-goods voting mechanisms.
