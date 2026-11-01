# Chapter 14: Information Economics

## Learning Objectives

After completing this chapter, you will be able to:

1. Distinguish symmetric from asymmetric information and identify which side of a market holds the informational advantage
2. Explain adverse selection using Akerlof's "market for lemons" and derive its effect on market outcomes
3. Distinguish moral hazard (hidden actions) from adverse selection (hidden information)
4. Explain how signaling can allow informed parties to credibly reveal private information
5. Explain how screening allows uninformed parties to sort informed parties by type
6. Analyze principal-agent problems and the incentive contracts used to mitigate them
7. Apply these tools to real markets: health insurance, used cars, credit, and labor contracts

---

!!! mascot-welcome "When Someone Knows More Than You"
    ![Professor Owl waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Every choice has a trade-off -- but some trades are riskier than others, because one side of the deal knows something the other side doesn't. In this chapter you'll meet the used-car seller who knows their car is a lemon, the insurance applicant who knows their own health better than any insurer, and the clever tools -- signaling, screening, and incentive contracts -- that markets have invented to cope. This is the economics of trust, and of what happens when trust alone isn't enough.

## 14.1 Symmetric vs. Asymmetric Information

The supply-and-demand model of Chapter 2 assumed that buyers and sellers know everything relevant about the good being traded: its quality, the risk involved, the effort behind it. Economists call this **symmetric information** — both sides of a transaction have the same relevant knowledge.

In many real markets, this assumption fails. **Asymmetric information** exists when one party to a transaction knows something relevant that the other party does not. Asymmetric information is not a minor wrinkle — it can prevent mutually beneficial trades from happening at all, and it is one of the central reasons markets fail to reach the efficient outcomes described in Chapter 12.

Economists sort problems of asymmetric information into two broad categories, distinguished by *when* the information gap matters relative to the transaction:

| Problem | Nature of the hidden information | Timing | Example |
|---|---|---|---|
| **Adverse selection** | Hidden *characteristic* (type) | Exists **before** the contract is signed | A used car's owner knows if it's a lemon before selling it |
| **Moral hazard** | Hidden *action* (behavior) | Arises **after** the contract is signed | A driver with insurance drives less carefully after buying the policy |

!!! mascot-thinking "Before or After the Ink Dries"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Here's the one question that sorts every problem in this chapter: did the hidden information exist before the contract was signed, or does the hidden behavior only happen after? Before means adverse selection -- a type that was always there; after means moral hazard -- a choice the contract itself changed. Get the timing right, and the correct tool follows almost automatically.

!!! note "Why this distinction matters"
    Adverse selection is a problem of **selection** — who chooses to participate in a market or contract. Moral hazard is a problem of **incentives** — how a contract changes behavior after it is signed. The policy tools that address each are different: signaling and screening address adverse selection; monitoring and incentive-compatible contracts address moral hazard.

The economists George Akerlof, Michael Spence, and Joseph Stiglitz shared the 2001 Nobel Prize in Economics for developing the theory of markets with asymmetric information — the framework this chapter builds on.

---

## 14.2 Adverse Selection: The Market for Lemons

### Akerlof's Insight

In his famous 1970 paper, George Akerlof asked a deceptively simple question: why are used cars that have barely been driven often sold for so much less than their "true" value? His answer launched an entire field of economics.

!!! mascot-encourage "The Lemons Math Looks Scarier Than It Is"
    ![Professor Owl encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If the back-and-forth of buyers revising their expectations downward feels dizzying at first, you're not alone -- this unraveling logic is genuinely one of the hardest ideas in microeconomics, which is exactly why it won Akerlof a Nobel Prize. Go slowly through each round of the price-quality spiral below, and notice it's really the same simple calculation -- expected value given who actually shows up to sell -- repeated until nothing changes.

Consider a market for used cars. Each seller knows the true quality of their own car; buyers cannot observe quality before purchase — they can only see the *average* quality of cars offered for sale. Suppose there are two types of used cars:

- **High-quality cars ("peaches"):** worth \$10,000 to sellers and \$12,000 to buyers
- **Low-quality cars ("lemons"):** worth \$4,000 to sellers and \$5,000 to buyers

Assume half of all used cars on the market are peaches and half are lemons, and buyers cannot tell which is which at the time of purchase. Because buyers cannot distinguish quality, they will only pay a price based on the **average quality** they expect to receive.

**Buyers' expected value**, if both types are offered for sale in equal proportion:

$$E[\text{Value}] = 0.5(12{,}000) + 0.5(5{,}000) = \$8{,}500$$

At a price of \$8,500, what happens? Owners of **peaches** (worth \$10,000 to them) will **not** sell — \$8,500 is less than what the car is worth to them. Owners of **lemons** (worth \$4,000 to them) are happy to sell at \$8,500. So only lemons come to market.

But if buyers anticipate this, they revise their expectations: if only lemons are sold, buyers should only be willing to pay the value of a lemon.

$$E[\text{Value} \mid \text{only lemons offered}] = \$5{,}000$$

### The Death Spiral

This process can cascade. At \$8,500, only lemons sell. Rational buyers anticipate this and lower their offer to \$5,000 (lemon value). At \$5,000, sellers of lemons (valuing their car at \$4,000) are still willing to sell. The market settles at a price reflecting **only** lemon quality — the peaches are permanently driven out of the market even though peach buyers and peach sellers could have found a mutually beneficial trade (anywhere between \$10,000 and \$12,000) if information had been symmetric.

!!! warning "Market collapse"
    In the most extreme version of this model, adverse selection can cause a market to **disappear entirely** — even though there are gains from trade available to every participant if only quality could be verified. The inefficiency comes not from bad intentions but from the simple fact that buyers cannot distinguish good from bad before purchase.

### A General Formulation

Let a fraction $\lambda$ of sellers have high-quality goods worth $V_H$ to buyers, and $(1-\lambda)$ have low-quality goods worth $V_L$ to buyers, with $V_H > V_L$. If sellers of high quality require a minimum price $S_H$ to sell, and the market-clearing price must reflect average expected quality:

$$P = \lambda V_H + (1-\lambda) V_L$$

The high-quality sellers participate only if $P \geq S_H$. If $S_H > \lambda V_H + (1-\lambda)V_L$, high-quality sellers exit, $\lambda$ falls, and $P$ falls further — a feedback loop that can unravel the market completely.

### Other "Lemons" Markets

Adverse selection extends well beyond used cars:

- **Health insurance:** People who know they are likely to get sick are more eager to buy generous insurance than healthy people are. If insurers cannot distinguish risk types, they must price policies based on the *average* risk of their applicant pool. This can drive healthy, low-risk people out of the market (they find the average-risk price too expensive), raising the average risk of those who remain, which raises prices further — the same unraveling dynamic.
- **Credit markets:** Borrowers know their own likelihood of repayment better than lenders do. If a bank cannot distinguish safe from risky borrowers, it must charge an interest rate reflecting average default risk. This can discourage safe borrowers, leaving a riskier pool — a phenomenon Stiglitz and Weiss (1981) showed can lead banks to **ration credit** (deny loans) rather than simply raise interest rates indefinitely.
- **Labor markets:** Workers know their own skill and work ethic better than employers do at the hiring stage.

---

## 14.3 Moral Hazard and Hidden Actions

### The Problem

**Moral hazard** arises when one party's actions, taken *after* a contract is signed, are not fully observable to the other party, and those actions affect the outcome of the contract. The classic illustration is insurance: once you are insured against a loss, you bear less of the cost of that loss yourself, so you have less incentive to prevent it.

!!! example "Moral hazard illustrations"
    - A driver with full collision coverage may drive less cautiously than one with no insurance (less incentive to avoid accidents, since the insurer bears the cost).
    - A renter who has posted no security deposit may take worse care of the apartment.
    - An employee on a flat salary (not tied to performance) may exert less effort than one paid by the piece.
    - A borrower who is not personally liable for a loan (e.g., behind limited liability) may take on riskier projects with the bank's money.

### Why Moral Hazard Is Different from Adverse Selection

Adverse selection is about **who** shows up to a market (a hidden type that existed before the contract). Moral hazard is about **what people do** once insured, employed, or lent to (a hidden action that occurs after the contract). Both stem from asymmetric information, but the timing and the remedy differ.

### A Simple Model

Suppose a worker can choose high effort ($e_H$) or low effort ($e_L$), where $e_H$ costs the worker a disutility of $c$ but raises the probability of a good outcome (e.g., project success) from $p_L$ to $p_H$ ($p_H > p_L$). If the firm cannot observe effort — only the outcome — and pays a flat wage $w$ regardless of outcome, the worker will always choose $e_L$ (the effort that minimizes cost), because pay does not depend on effort. This is the moral hazard: the firm would prefer high effort, but cannot contract on it directly, only on the (noisy) outcome.

**Incentive-compatible solution:** Pay a wage that depends on the outcome, e.g., $w_{\text{success}} = w_H$ and $w_{\text{failure}} = w_L$, with $w_H > w_L$, chosen so that the expected gain from exerting high effort exceeds its cost $c$:

$$p_H w_H + (1-p_H)w_L - c \; \geq \; p_L w_H + (1-p_L)w_L$$

Rearranging:

$$(p_H - p_L)(w_H - w_L) \geq c$$

This is the **incentive compatibility condition**: the pay gap between success and failure, weighted by how much effort changes the probability of success, must be large enough to cover the cost of effort. This is why many real-world contracts tie pay to performance — commissions, bonuses, stock options, tips, and piece rates are all attempts to solve moral hazard by linking pay to observable outcomes that are correlated with unobservable effort.

!!! mascot-tip "Solving Incentive Compatibility in One Line"
    ![Professor Owl tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    Whenever you're asked for the minimum pay gap that induces high effort, skip straight to $(p_H - p_L)(w_H - w_L) \geq c$ and divide: the minimum gap is just $c$ divided by the change in success probability. You almost never need to set up the full expected-utility comparison from scratch once you recognize the problem as an incentive-compatibility question.

### Mitigating Moral Hazard

| Tool | How it works | Example |
|---|---|---|
| **Deductibles and co-pays** | Insured party bears part of the loss, restoring some incentive to prevent it | Auto and health insurance deductibles |
| **Monitoring** | Reduce the information asymmetry directly | Employer supervision, telematics devices that track driving behavior |
| **Performance pay** | Tie compensation to observable outcomes correlated with effort | Sales commissions, bonuses, stock options |
| **Reputation / repeated interaction** | Future business depends on current behavior | Online seller ratings, repeat customers |
| **Liability rules** | Make the agent bear some cost of bad outcomes | Not allowing full discharge of debt in bankruptcy |

---

## 14.4 Signaling: Letting the Informed Party Speak

When adverse selection threatens to destroy a market, the **informed** party sometimes has an incentive to find a credible way to reveal their private information. This is called **signaling**.

### Spence's Education Model

Michael Spence's classic (1973) model asks: why do employers pay more for workers with college degrees, even in jobs where the specific material learned in college is never used? His answer: a degree can function as a **signal** of underlying (unobservable) ability, *if* it is less costly for high-ability workers to obtain than for low-ability workers.

Suppose there are two types of workers, High ability (H) and Low ability (L), and the cost of acquiring $y$ years of education is $c_H(y)$ for high types and $c_L(y)$ for low types, with $c_H(y) < c_L(y)$ for any $y > 0$ (education is relatively less costly/painful for high-ability workers — they learn faster, find it less unpleasant). Employers cannot observe ability directly but can observe years of education, $y$.

For signaling to work (a "separating equilibrium"), the signal must satisfy two conditions:

1. **High types want to signal:** the wage premium for acquiring education $y^*$ must exceed its cost to a high type.
2. **Low types do NOT want to mimic:** the same wage premium must *not* be worth it for a low type, i.e., it would cost them more than the wage gain.

$$c_L(y^*) > w_H - w_L > c_H(y^*)$$

If such a $y^*$ exists, education can separate the two types in equilibrium even though a college education, in Spence's stylized model, teaches no job-relevant skill at all — its value is purely in being a cost that only high-ability types find worthwhile to incur.

!!! mascot-thinking "A 'Useless' Signal That Says Everything"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Sit with this for a second: in Spence's model, the education itself teaches the worker nothing useful on the job. Its entire value comes from being expensive enough that a low-ability worker wouldn't bother faking it. That's the mental shift signaling asks of you -- a credential's power to inform can come purely from its cost, not from its content.

!!! example "Other signals"
    - **Warranties:** A manufacturer confident in its product's reliability can profitably offer a long warranty (few claims will be filed); a manufacturer of unreliable products cannot afford to, because claims would be too costly. The warranty length signals quality.
    - **Reputation:** An established restaurant with years of good reviews signals quality that a brand-new restaurant cannot yet demonstrate.
    - **Dividends:** A firm that pays a stable dividend signals confidence in its future cash flows, since cutting a dividend later would be costly to its reputation.
    - **Collateral:** Offering more collateral on a loan signals that a borrower genuinely expects to repay (since a borrower planning to default would not want to risk losing valuable collateral).

### Requirements for an Effective Signal

For a signal to credibly convey private information, it generally must be:

- **Costly** — a costless signal could be sent by anyone, so it would convey no information
- **Differentially costly** across types — it must be cheaper for the type it's meant to reveal (otherwise everyone, or no one, would send it)
- **Observable** to the uninformed party

---

## 14.5 Screening: Letting the Uninformed Party Sort

**Screening** is the mirror image of signaling: instead of the informed party revealing information, the **uninformed** party designs a menu of options that induces different types to reveal themselves by the choices they make.

### Insurance Deductibles as a Screening Device

An insurance company cannot observe which applicants are high-risk and which are low-risk. Instead of a single policy, it can offer a **menu**:

| Policy | Premium | Deductible |
|---|---|---|
| Policy A | High premium | Low deductible |
| Policy B | Low premium | High deductible |

High-risk individuals, who expect to file claims, prefer Policy A (low deductible matters more to them, and they're willing to pay the higher premium to avoid a large out-of-pocket cost). Low-risk individuals, who rarely expect to file a claim, prefer Policy B (why pay a high premium for low-deductible protection they are unlikely to use?). By choosing between the two policies, customers **reveal their type** even though the insurer never directly observes risk.

This is an example of a **self-selection constraint**: the menu must be designed so that each type prefers the option intended for them over the option intended for the other type.

!!! mascot-warning "A Menu Isn't Screening Unless It Actually Sorts"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A common mistake is assuming that offering *any* menu of contracts automatically screens customers by type. It doesn't -- if both types end up preferring the same option (as happens in Problem 5 at the end of this chapter), you've learned nothing about who's who. Always check the self-selection constraint directly: does each type's own expected-cost calculation actually favor the option meant for them?

### Job Interviews and Screening

Employers use interviews, tests, probationary periods, and tiered job offers (e.g., offering a lower base salary with a large bonus for proven performers) as screening devices. A candidate's *willingness* to accept a performance-contingent contract can itself reveal information: a candidate confident in their own ability is more willing to accept pay tied to performance than a candidate who is not.

### Screening vs. Signaling — Who Moves First?

| | Who acts first | Who designs the mechanism | Example |
|---|---|---|---|
| **Signaling** | Informed party | Informed party chooses a costly action | Worker chooses how much education to get |
| **Screening** | Uninformed party | Uninformed party designs a menu of contracts | Insurer designs a menu of deductible/premium combinations |

---

## 14.6 Principal-Agent Problems

A **principal-agent problem** arises whenever one party (the **principal**) hires or delegates authority to another party (the **agent**) to act on their behalf, but the agent's interests are not perfectly aligned with the principal's, and the principal cannot perfectly monitor the agent's actions.

$$\text{Principal-Agent Problem} = \text{Misaligned incentives} + \text{Imperfect monitoring}$$

!!! example "Principal-agent relationships"
    | Principal | Agent | Potential conflict |
    |---|---|---|
    | Shareholders | CEO | CEO may prefer prestige projects or perks over maximizing shareholder value |
    | Patient | Doctor | Doctor may recommend more (or less) treatment than is medically optimal, especially under fee-for-service pay |
    | Homeowner | Contractor | Contractor paid hourly has less incentive to finish quickly |
    | Client | Lawyer billing by the hour | Lawyer may have an incentive to prolong a case |
    | Voters | Elected officials | Officials may pursue re-election or personal goals over constituents' interests |

### Solving the Principal-Agent Problem

Principals use several tools, many of which we've already encountered as tools against moral hazard (the principal-agent problem is, formally, a generalization of the moral hazard problem):

1. **Incentive contracts** that tie the agent's pay to outcomes correlated with the principal's goals (stock options for CEOs, commissions for salespeople).
2. **Monitoring** to reduce the information gap (audits, boards of directors, performance reviews).
3. **Bonding** — requiring the agent to post a stake that is forfeited for poor performance (a security deposit, a performance bond).
4. **Competition and reputation** — repeated interactions and outside options discipline agents who cannot be perfectly monitored in any single period.

!!! note "The agency cost tradeoff"
    Perfect incentive alignment is usually impossible (or prohibitively expensive) to achieve, so real-world contracts accept some **agency cost** — the loss in value from imperfect alignment — in exchange for lower-powered, simpler, or less risky incentive schemes. A CEO cannot bear 100% of the risk of the firm's performance (she would demand enormous compensation to accept that risk), so boards settle for incentive contracts that only partially align her pay with shareholder value.

---

## 14.7 Applications

### Health Insurance

Health insurance markets combine **both** adverse selection and moral hazard:

- *Adverse selection:* People who expect to need more care are more likely to buy generous coverage, raising the average cost of the insured pool.
- *Moral hazard:* Once insured, people may consume more healthcare than they would if paying full price out of pocket (since the marginal cost to them is lower).

Policy responses include mandates (requiring everyone, healthy and sick, to buy insurance, preventing the healthy from opting out and causing the death-spiral dynamic of Section 14.2), subsidies, community rating regulations, and cost-sharing tools like deductibles and co-pays (which address moral hazard, per Section 14.3).

### Used Cars

Modern used-car markets have developed institutions specifically to combat the lemons problem: certified pre-owned programs (manufacturer-backed signals of quality), vehicle history reports like Carfax (reducing the information asymmetry directly), warranties (a costly signal, per Section 14.4), and independent mechanic inspections (a buyer-initiated screening device).

### Credit Markets

Lenders screen borrowers using credit scores, collateral requirements, and down payments (all of which are costlier for borrowers who expect to default, making them effective screens). Interest rates that are "too good to be true" can themselves be adversely selected — a lender who simply raised rates to cover the risk of its average borrower might find that doing so drives away its safest borrowers, worsening the pool it's left with, which is part of why credit rationing (denying some loans altogether rather than raising their price) can be the profit-maximizing response for a lender facing asymmetric information.

### Labor Contracts

Employers use probationary periods, performance bonuses, stock vesting schedules, and non-compete or training-repayment clauses to manage both moral hazard (motivating effort once hired) and adverse selection (screening for the right hires before offering a permanent role).

---

## Key Terms

| Term | Definition |
|---|---|
| **Symmetric Information** | Both parties to a transaction have the same relevant knowledge |
| **Asymmetric Information** | One party has relevant knowledge the other lacks |
| **Adverse Selection** | A hidden-characteristic problem arising before a contract, where low-quality participants crowd out high-quality ones |
| **Moral Hazard** | A hidden-action problem arising after a contract, where one party's unobservable behavior changes once insured or incentivized |
| **Market for Lemons** | Akerlof's model showing how adverse selection can drive high-quality goods out of a market |
| **Signaling** | An informed party takes a costly, differentially-costly action to credibly reveal private information |
| **Screening** | An uninformed party designs a menu of options that induces informed parties to reveal their type through self-selection |
| **Separating Equilibrium** | An equilibrium in which different types choose different actions, revealing their type |
| **Principal-Agent Problem** | A conflict of interest between a principal and an agent acting on their behalf, worsened by imperfect monitoring |
| **Incentive Compatibility** | A contract condition ensuring each party's best response is the behavior the contract intends to induce |
| **Agency Cost** | The loss in value arising from imperfect alignment between principal and agent incentives |
| **Credit Rationing** | Denying loans to some borrowers rather than raising interest rates, to avoid worsening adverse selection |

---

## Practice Problems

### Problem 1 — Identifying the Problem Type

For each scenario, state whether it is primarily an example of **adverse selection** or **moral hazard**, and explain why.

**a)** A new homeowner's insurance policyholder stops bothering to lock the back door now that theft is covered.  
**b)** People with a family history of a hereditary disease are especially eager to buy long-term care insurance.  
**c)** A city's taxi medallion buyer, once licensed, drives more recklessly than before (knowing their insurer will cover most damages).  
**d)** Among people who respond to a credit card company's offer of a card with no credit check, a disproportionate share turn out to be high credit-risk.

??? success "Solution"
    **a)** **Moral hazard** — the hidden *action* (not locking the door) changes after the contract is signed.

    **b)** **Adverse selection** — the hidden *characteristic* (family health risk) exists before the contract and affects who chooses to buy insurance.

    **c)** **Moral hazard** — insurance changes behavior (less caution) after coverage begins.

    **d)** **Adverse selection** — the self-selected applicant pool (those willing to respond to a no-credit-check offer) is skewed toward a hidden pre-existing characteristic: being unable to pass a credit check elsewhere.

### Problem 2 — The Lemons Model

In a used laptop market, high-quality laptops ("good") are worth \$800 to buyers and \$600 to sellers. Low-quality laptops ("bad") are worth \$300 to buyers and \$200 to sellers. Half of all laptops offered for sale are good and half are bad, and buyers cannot distinguish them before purchase.

**a)** What price would buyers be willing to pay if they expect an equal mix of good and bad laptops?  
**b)** At that price, will owners of good laptops sell? Will owners of bad laptops sell?  
**c)** What happens to the market as a result? What is the final equilibrium price?

??? success "Solution"
    **a)** Expected value $= 0.5(800) + 0.5(300) = \$550$.

    **b)** Owners of good laptops value theirs at \$600, which **exceeds** \$550 — they will **not** sell at this price. Owners of bad laptops value theirs at \$200, which is **below** \$550 — they are happy to sell.

    **c)** Since only bad laptops end up for sale, rational buyers revise their expectations downward to the value of a bad laptop only: \$300. The market **unravels** — good laptops are driven out entirely, and the equilibrium price settles at **\$300**, reflecting only low-quality laptops. (Buyers of bad laptops are willing to pay up to \$300, and sellers of bad laptops will accept anything above \$200, so trade in low-quality laptops continues at a price between \$200 and \$300 — here taken at the buyer's willingness to pay, \$300, for simplicity.)

### Problem 3 — Incentive Compatibility

A firm wants a worker to exert high effort. High effort raises the probability of a successful project from $p_L = 0.4$ to $p_H = 0.7$. The worker's disutility of high effort (relative to low effort) is $c = \$9{,}000$. The firm pays $w_H$ if the project succeeds and $w_L$ if it fails.

**a)** Write the incentive compatibility condition that ensures the worker chooses high effort.  
**b)** If $w_L = \$40{,}000$, what is the minimum $w_H$ that satisfies incentive compatibility?

??? success "Solution"
    **a)** The incentive compatibility condition is:
    
    $$(p_H - p_L)(w_H - w_L) \geq c$$
    
    $$(0.7 - 0.4)(w_H - w_L) \geq 9{,}000$$
    
    $$0.3(w_H - w_L) \geq 9{,}000 \implies w_H - w_L \geq 30{,}000$$

    **b)** With $w_L = \$40{,}000$:
    
    $$w_H \geq 40{,}000 + 30{,}000 = \$70{,}000$$
    
    The firm must pay at least **\$70,000** on success (versus \$40,000 on failure) to make high effort worthwhile for the worker.

### Problem 4 — Signaling Condition

Suppose a high-ability worker's cost of obtaining $y$ years of education is $c_H(y) = 5{,}000y$, and a low-ability worker's cost is $c_L(y) = 15{,}000y$. Firms pay $w_L = \$40{,}000$ to workers with no credentials and $w_H = \$70{,}000$ to workers with a credential of $y^* $ years, if that credential is believed to signal high ability.

**a)** What is the maximum $y^*$ (in years) such that high-ability workers still find it worthwhile to acquire the credential?  
**b)** What is the minimum $y^*$ such that low-ability workers do NOT want to acquire the credential?  
**c)** Does a separating equilibrium exist? If so, over what range of $y^*$?

??? success "Solution"
    **a)** High types signal only if the wage gain exceeds the cost: $70{,}000 - 40{,}000 \geq 5{,}000y^* \implies y^* \leq 6$.

    **b)** Low types do NOT want to mimic only if the cost to them exceeds the gain: $15{,}000y^* > 30{,}000 \implies y^* > 2$.

    **c)** Yes — a separating equilibrium exists for any $y^*$ strictly between **2 and 6 years** of education. At such a $y^*$, high-ability workers find it worth acquiring the credential, and low-ability workers find it too costly to mimic, so education correctly separates the two types.

### Problem 5 — Screening Menu

An insurance company cannot tell high-risk from low-risk drivers. It offers two policies:

- **Policy A:** Premium = \$1,200/year, Deductible = \$100
- **Policy B:** Premium = \$600/year, Deductible = \$1,000

A high-risk driver expects to file a claim with probability 0.3 per year; a low-risk driver with probability 0.05 per year. (Assume each driver picks the policy that minimizes their *expected total annual cost* = premium + expected deductible paid.)

**a)** Compute each driver type's expected total cost under each policy.  
**b)** Which policy does each type choose? Does the menu successfully screen the two types?

??? success "Solution"
    **a)** Expected total cost = Premium + (probability of claim × deductible).

    High-risk driver:
    - Policy A: $1{,}200 + 0.3(100) = 1{,}200 + 30 = \$1{,}230$
    - Policy B: $600 + 0.3(1{,}000) = 600 + 300 = \$900$

    Low-risk driver:
    - Policy A: $1{,}200 + 0.05(100) = 1{,}200 + 5 = \$1{,}205$
    - Policy B: $600 + 0.05(1{,}000) = 600 + 50 = \$650$

    **b)** Both types have a lower expected cost under Policy B in this example (\$900 < \$1,230 for high-risk; \$650 < \$1,205 for low-risk), so **both types would choose Policy B** — the menu as given does **not** successfully screen the two types. (In a properly designed screening menu, Policy A's premium would need to be low enough, relative to its low deductible, that high-risk drivers — who expect to pay the deductible more often — prefer it, while low-risk drivers still prefer Policy B's low premium. This problem illustrates that designing an incentive-compatible menu requires carefully balancing the premium-deductible tradeoff against each type's claim probability.)

---

!!! mascot-celebration "You Can Now See the Invisible"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    That's adverse selection, moral hazard, signaling, screening, and the principal-agent problem -- five ideas that explain why insurance markets, used car lots, and employment contracts look the way they do, all handled. You've learned to spot the hidden information markets can't see directly, which is half the battle of being a sharper reader of real-world contracts for the rest of your life.

---

!!! tip "Next Chapter"
    In [Chapter 15: Behavioral Economics](../15-behavioral-economics/index.md), we relax the assumption that people are perfectly rational optimizers, and explore how real psychological biases — loss aversion, present bias, and framing effects — shape economic decisions.
