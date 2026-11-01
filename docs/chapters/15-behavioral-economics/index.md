# Chapter 15: Behavioral Economics

## Learning Objectives

After completing this chapter, you will be able to:

1. Explain bounded rationality and why it limits the standard model of the perfectly optimizing consumer
2. Identify common heuristics and cognitive biases and describe how they cause systematic decision errors
3. Explain loss aversion and prospect theory, and contrast them with standard expected-utility theory
4. Explain present bias and hyperbolic discounting, and distinguish them from standard exponential discounting
5. Explain framing effects and mental accounting and give examples of each
6. Describe social preferences — fairness, reciprocity, and altruism — and how they depart from pure self-interest
7. Explain nudge theory and libertarian paternalism, and apply these concepts to real policy design

---

!!! mascot-welcome "Meet the Human Behind Homo Economicus"
    ![Professor Owl waving welcome](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    Every choice has a trade-off -- but here's a confession: real people don't always make that trade-off the way the last eleven chapters assumed. This chapter is where we put down the perfectly rational optimizer and pick up the actual, wonderfully quirky human: someone who procrastinates, flinches at losses more than they celebrate equal gains, and can be nudged toward better choices without ever losing their freedom to choose otherwise. Let's see what economics looks like once we let people be people.

## 15.1 Bounded Rationality

The standard economic model developed in Chapters 2 through 11 assumes **homo economicus** — a perfectly rational decision-maker who has stable preferences, processes all available information without error, and chooses the option that maximizes utility. This assumption is powerful because it is tractable: it lets us build clean, predictive models. But it is also, in many situations, descriptively wrong.

**Bounded rationality**, a term coined by Herbert Simon (who won the Nobel Prize in 1978), describes decision-making that is limited by:

- **Limited information** — people cannot costlessly gather and process every relevant fact
- **Limited cognitive capacity** — the brain cannot perform unlimited calculations in real time
- **Limited time** — many decisions must be made quickly

Rather than exhaustively optimizing, Simon argued, people **satisfice** — they search until they find an option that is "good enough," rather than continuing to search for the objectively best one.

!!! mascot-thinking "Good Enough Beats Perfect"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Notice the shift Herbert Simon is asking you to make: instead of a decision-maker who calculates the single best option out of every possibility, picture someone who stops searching the moment they find an option that clears their own "good enough" bar. That's satisficing, and once you start looking for it, you'll see it behind nearly every bias in Section 15.2.

**Behavioral economics** is the subfield that incorporates insights from psychology into economic models, relaxing the assumption of unbounded rationality to build models that better predict actual human behavior. Daniel Kahneman and Vernon Smith shared the 2002 Nobel Prize for pioneering work combining psychological insight with economic analysis (Kahneman) and experimental methods (Smith); Richard Thaler won the 2017 Nobel Prize specifically for his contributions to behavioral economics.

!!! note "Two systems of thinking"
    Kahneman's influential book *Thinking, Fast and Slow* describes two modes of cognition: **System 1** is fast, automatic, intuitive, and emotional. **System 2** is slow, deliberate, analytical, and effortful. Many biases arise because System 1 generates quick answers that System 2 fails to override — even when System 2 "knows better."

---

## 15.2 Heuristics and Cognitive Biases

A **heuristic** is a mental shortcut that simplifies decision-making. Heuristics are often useful — they let us make fast, reasonably good decisions without exhaustive calculation — but they can also produce systematic, predictable errors called **cognitive biases**.

| Heuristic / Bias | Description | Example |
|---|---|---|
| **Availability heuristic** | Judging likelihood by how easily examples come to mind | Overestimating shark attack risk after seeing news coverage, even though car accidents are far more common |
| **Anchoring** | Relying too heavily on an initial piece of information | A \$500 "original price" next to a \$300 "sale price" makes \$300 feel like a bargain, regardless of the item's true value |
| **Representativeness heuristic** | Judging probability by similarity to a stereotype, ignoring base rates | Assuming a quiet, detail-oriented person is more likely to be a librarian than a salesperson, even though salespeople vastly outnumber librarians |
| **Overconfidence** | Overestimating the accuracy of one's own judgments or abilities | Most investors believe they can "beat the market," though most actually underperform a simple index fund |
| **Confirmation bias** | Seeking information that confirms existing beliefs and discounting contrary evidence | An investor who believes a stock will rise reads only bullish analysis |
| **Status quo bias** | A preference for the current state of affairs, even when a change would be beneficial | Employees who stick with a poorly performing default retirement allocation rather than switching |

!!! mascot-tip "A Quick Test for Naming the Bias"
    ![Professor Owl tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    When a question describes a judgment error, ask yourself one quick diagnostic: is it about how easily examples come to mind (availability), an initial number distorting everything after it (anchoring), or a resemblance to a stereotype that ignores the base rate (representativeness)? Naming the mechanism, not just the mistake, is what these problems are actually testing.

!!! example "Anchoring in negotiation"
    In salary negotiations, the first number mentioned tends to "anchor" the rest of the discussion. A job candidate who states a high initial salary expectation often ends up with a higher final offer than one who waits for the employer to name a number first — even though the "fair" value of the job hasn't changed.

These biases matter economically because they lead to **systematic**, not random, departures from the rational-choice predictions of Chapters 2–11 — and systematic errors can be anticipated (and sometimes exploited) by firms, policymakers, and well-informed counterparties.

---

## 15.3 Loss Aversion and Prospect Theory

### Expected Utility Theory (the Standard Model)

The traditional economic model of decision-making under risk, **expected utility theory**, assumes people evaluate a risky choice by its expected utility:

$$EU = \sum_i p_i \, u(W_i)$$

where $p_i$ is the probability of outcome $i$ and $u(W_i)$ is the utility of final wealth $W_i$. Critically, this model evaluates outcomes based on **final wealth levels**, and it is symmetric: a loss of \$100 and a gain of \$100 are judged purely by how they change total wealth.

### Kahneman and Tversky's Challenge

In 1979, Daniel Kahneman and Amos Tversky proposed **prospect theory** as a descriptively more accurate alternative, built on experimental evidence that people systematically violate expected utility theory. Prospect theory has three key features:

1. **Reference dependence:** People evaluate outcomes as **gains or losses relative to a reference point** (often the status quo), not as final wealth levels.
2. **Loss aversion:** Losses loom larger than equivalent gains. Experimentally, losses are felt roughly **twice** as intensely as equivalent gains.
3. **Diminishing sensitivity:** The pain of each additional dollar lost (or pleasure of each additional dollar gained) diminishes the further it is from the reference point — captured by a value function that is concave for gains and convex for losses.

$$\text{Loss Aversion:} \quad |v(-x)| > v(x) \quad \text{for } x > 0$$

A common empirical estimate puts the **loss aversion coefficient** $\lambda \approx 2$, meaning:

$$v(-x) \approx -2 \cdot v(x)$$

!!! mascot-encourage "Prospect Theory Rewards a Second Read"
    ![Professor Owl encouraging](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    If reference dependence, loss aversion, and diminishing sensitivity feel like three new ideas thrown at you at once, that's a fair reaction -- this is widely considered one of the most conceptually demanding topics in the course, which is why it earned Kahneman a Nobel Prize. Work through the value-function example below one piece at a time, and keep asking "gain or loss relative to what?" -- that question alone resolves most of the confusion.

!!! example "The endowment effect"
    Richard Thaler documented that people demand a much higher price to **give up** an item they own (the "selling price") than they are willing to **pay** to acquire the identical item if they don't yet own it (the "buying price"). In one classic experiment, participants given a coffee mug demanded roughly twice as much to sell it as other participants were willing to pay for an identical mug. This is a direct consequence of loss aversion: giving up the mug is coded as a *loss* (which looms large), while not acquiring it is merely coded as a *forgone gain* (which looms smaller).

### A Worked Example: The Value Function

Suppose a simplified prospect-theory value function is:

$$v(x) = \begin{cases} x^{0.5} & \text{if } x \geq 0 \text{ (gain)} \\ -2(-x)^{0.5} & \text{if } x < 0 \text{ (loss)} \end{cases}$$

Consider a gamble: a 50% chance of gaining \$100 and a 50% chance of losing \$100, relative to the current reference point.

**Standard expected-value calculation:** $EV = 0.5(100) + 0.5(-100) = 0$ — a fair gamble.

**Prospect-theory valuation:**

$$v(100) = 100^{0.5} = 10$$

$$v(-100) = -2(100)^{0.5} = -20$$

$$\text{Prospect value} = 0.5(10) + 0.5(-20) = 5 - 10 = -5$$

Even though the gamble is fair in expected-value terms, a loss-averse decision-maker assigns it a **negative** prospect value — and will reject it. This explains a well-documented experimental finding: most people reject fair coin-flip gambles over money, even gambles that a risk-*neutral* expected-utility maximizer should be indifferent to.

!!! mascot-warning "Always Ask: Relative to What?"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A frequent error is plugging final wealth straight into the prospect-theory value function, the way you would with expected utility. Don't -- $v(x)$ only makes sense once you've first found $x$ as a gain or loss *relative to the decision-maker's reference point*, which is usually (but not always) the status quo.

---

## 15.4 Present Bias and Hyperbolic Discounting

### The Standard Model: Exponential Discounting

The standard model of intertemporal choice assumes people discount future utility **exponentially** at a constant rate $\delta$ (or discount rate $r$):

$$U = u(c_0) + \delta \, u(c_1) + \delta^2 u(c_2) + \dots$$

A key feature of exponential discounting is **time consistency**: the relative weight placed on any two moments in time depends only on the *gap* between them, not on when you ask. A person exponentially discounting should make the same relative tradeoff between "20 years from now" and "21 years from now" as between "today" and "tomorrow."

### Hyperbolic Discounting

Experimental evidence shows people are **not** time-consistent. Most people would rather have \$100 today than \$110 tomorrow (a very high implied discount rate over one day), but would rather have \$110 in 31 days than \$100 in 30 days (a much lower implied discount rate over a *different* one-day gap, just further in the future).

This pattern is captured by **hyperbolic discounting**, often modeled with the **quasi-hyperbolic** ($\beta$-$\delta$) form developed by Laibson:

$$U = u(c_0) + \beta \sum_{t=1}^{\infty} \delta^t u(c_t), \qquad 0 < \beta < 1$$

The parameter $\beta$ captures an extra discount applied **only** between the present and the very next period — a "present bias." Between any two *future* periods, discounting follows the standard exponential rate $\delta$.

!!! example "Numerical illustration of present bias"
    Suppose $\delta = 0.95$ (a stable long-run discount factor) and $\beta = 0.7$ (significant present bias).

    - The relative weight on **next year's** utility vs. **this year's**: $\beta\delta = 0.7 \times 0.95 = 0.665$
    - The relative weight on **year 11's** utility vs. **year 10's** (i.e., two future periods, not involving the present): just $\delta = 0.95$

    The implied "discount rate" between today and next year is much steeper (weight falls to 0.665) than the implied discount rate between any two future years (weight falls only to 0.95). This asymmetry — steep discounting only when the present is involved — is exactly what produces the common pattern: "I'll start saving/dieting/exercising **next month**," repeated every month.

!!! mascot-thinking "Same Person, Two Different Clocks"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Here's the eureka moment of hyperbolic discounting: people don't discount the future too much overall -- they apply one, much steeper discount rate only when the present is on one side of the comparison, and the ordinary, gentler rate whenever both moments being compared are in the future. The person planning next month's diet and the person failing to start it are using two different discount rates, three weeks apart.

### Time Inconsistency and Self-Control

Present bias predicts specific, observable behaviors: procrastination, under-saving for retirement, under-investment in health, and demand for commitment devices (such as automatic payroll deductions into a retirement account, or apps that lock a person out of social media) — tools people **voluntarily** use to bind their future selves, because they correctly predict that their future self will also be present-biased in the moment and may act against their own long-run interest.

---

## 15.5 Framing Effects and Mental Accounting

### Framing Effects

A **framing effect** occurs when people's choices are influenced by how options are *described*, even when the underlying substance of the choice is identical. This directly violates the standard assumption that preferences depend only on real outcomes, not on how those outcomes are presented.

!!! example "The Asian disease problem (Tversky and Kahneman, 1981)"
    Participants were told a disease would kill 600 people, and asked to choose between two programs:

    - **Frame A (gain frame):** "Program 1 will save 200 people" vs. "Program 2 has a 1/3 chance of saving all 600 and a 2/3 chance of saving no one." Most people chose Program 1 (risk-averse in the domain of gains).
    - **Frame B (loss frame):** The identical outcomes, described as "Program 1 will result in 400 deaths" vs. "Program 2 has a 1/3 chance that no one dies and a 2/3 chance that all 600 die." Most people chose Program 2 (risk-seeking in the domain of losses) — even though Program 1 in Frame B is mathematically identical to Program 1 in Frame A.

    Simply reframing identical outcomes from "lives saved" to "lives lost" reversed the majority preference — direct evidence that framing, not just substance, drives choice, consistent with prospect theory's loss aversion (people become risk-seeking to avoid a certain loss).

### Mental Accounting

**Mental accounting**, a concept developed by Richard Thaler, describes how people mentally sort money into separate, non-fungible "accounts" (e.g., "rent money," "vacation fund," "fun money"), even though money is, in reality, perfectly fungible — a dollar is a dollar, regardless of its mental label.

!!! example "Mental accounting examples"
    - A household that won't dip into a "vacation fund" to cover an overdue bill, even while carrying high-interest credit card debt — violating the standard prescription to pay off the highest-interest debt first with any available cash.
    - A gambler who treats "house money" (recent winnings) differently from their original stake, taking bigger risks with winnings than they would with their initial \$100.
    - Treating a tax refund as a "windfall" to be spent on a splurge, rather than recognizing it as simply delayed access to money that was always theirs (over-withheld from each paycheck).

---

## 15.6 Social Preferences: Fairness, Reciprocity, and Altruism

Standard economic models often assume agents care only about their own payoff. **Social preferences** describe systematic patterns in which people's choices also depend on the payoffs (or intentions) of others.

### The Ultimatum Game

In the **ultimatum game**, one player (the proposer) suggests how to split a sum of money (say \$10) with a second player (the responder). If the responder accepts, both get the proposed split; if the responder rejects, **both get nothing**.

A purely self-interested responder should accept *any* positive offer (even \$1 is better than \$0). But in experiments worldwide, offers below roughly 20–30% of the pie are frequently **rejected** — responders are willing to sacrifice their own payoff to punish an offer they perceive as unfair. This is evidence of a preference for **fairness**, sometimes modeled as **inequity aversion**: people derive disutility from outcomes they perceive as unequal, even at a cost to themselves.

### Reciprocity and Altruism

- **Positive reciprocity:** Returning kindness with kindness, even without a binding obligation to do so (e.g., tipping well for good service at a restaurant you'll never visit again).
- **Negative reciprocity:** Punishing unfair treatment, even at a personal cost (as in the ultimatum game).
- **Altruism:** Deriving genuine utility from another person's well-being, independent of any expected return (e.g., anonymous charitable giving).

| Game | What it measures | Typical finding vs. pure self-interest prediction |
|---|---|---|
| **Ultimatum Game** | Fairness / willingness to punish unfair offers | Low offers rejected, even though "any offer > \$0" should be accepted |
| **Dictator Game** | Pure altruism (responder has no power to reject) | Dictators typically give 20–30% of the pie, though the self-interested prediction is \$0 |
| **Public Goods Game** | Voluntary cooperation | Contributions start above the free-riding prediction of \$0, though they often erode with repetition |
| **Trust Game** | Trust and reciprocity | Senders send positive amounts; receivers often return a share, more than the self-interested prediction of \$0 |

---

## 15.7 Nudge Theory and Libertarian Paternalism

### Thaler and Sunstein's Framework

In their influential book *Nudge* (2008), Richard Thaler and Cass Sunstein proposed **libertarian paternalism**: the idea that policymakers and institutions ("choice architects") can design environments that steer people toward decisions that make them better off **by their own judgment**, without restricting anyone's freedom of choice.

A **nudge** is any aspect of choice architecture that predictably alters behavior without forbidding any option or significantly changing economic incentives — it works precisely because it exploits the biases described earlier in this chapter (status quo bias, framing effects, present bias) in the decision-maker's own favor.

!!! note "Why nudges work: they exploit the exact biases from Sections 15.2–15.5"
    - **Defaults exploit status quo bias** (15.2): most people stick with whatever option requires no action.
    - **Commitment devices exploit present bias** (15.4): locking in a future choice today avoids being overridden by a present-biased future self.
    - **Framing nudges exploit framing effects** (15.5): the same information, presented differently, produces different choices.

### Classic Nudge Examples

| Nudge | Mechanism | Policy area |
|---|---|---|
| **Automatic enrollment in retirement plans** | Changes the default from opt-in to opt-out; status quo bias means most employees stay enrolled | Retirement savings |
| **"Save More Tomorrow"** (Thaler & Benartzi) | Employees pre-commit to increasing savings rate with future raises, rather than cutting current take-home pay | Retirement savings |
| **Opt-out organ donation** | Switches the default from "must register to donate" to "presumed consent unless opted out" | Organ donation |
| **Cafeteria food placement** | Placing healthy food at eye level and junk food less visibly does not forbid junk food, but changes what is chosen by default | Public health |
| **Simplified/graphic warning labels** | Framing health risks vividly increases their salience relative to abstract numerical risk | Public health (smoking warnings) |

### Retirement Savings: A Worked Illustration

Suppose a firm's 401(k) enrollment rate is only 40% under an **opt-in** design (employees must actively sign up). Under an otherwise identical **opt-out** design (employees are automatically enrolled at a default contribution rate, say 3% of salary, unless they actively choose to leave), enrollment rates in numerous real-world studies jump to **85–90%** or higher. No option was removed — employees in the opt-out design remain completely free to leave the plan — yet the *default* dramatically changes the outcome, precisely because of the status quo bias described in Section 15.2.

!!! warning "Nudges are not always benign"
    The same tools that nudge people toward their own stated long-run interests (as judged by themselves) can also be used by firms to nudge people toward choices that serve the firm's interest instead — such as pre-checked boxes that enroll customers in costly add-ons, or defaults that make it easy to subscribe and hard to cancel ("dark patterns"). Evaluating any nudge requires asking **whose** interest it serves and whether it respects the chooser's own, true preferences.

---

## Key Terms

| Term | Definition |
|---|---|
| **Bounded Rationality** | Decision-making limited by finite information, cognitive capacity, and time |
| **Satisficing** | Choosing an option that is "good enough" rather than exhaustively optimal |
| **Heuristic** | A mental shortcut used to simplify decision-making |
| **Cognitive Bias** | A systematic, predictable deviation from rational judgment produced by a heuristic |
| **Prospect Theory** | Kahneman and Tversky's model of decision-making under risk, based on gains/losses relative to a reference point |
| **Loss Aversion** | Losses are felt more intensely than equivalent gains |
| **Endowment Effect** | People demand more to give up an item they own than they would pay to acquire it |
| **Present Bias** | A disproportionately strong preference for immediate rewards over future ones |
| **Hyperbolic Discounting** | A discounting pattern in which the implied discount rate is higher over near-term intervals than over equally long future intervals |
| **Time Inconsistency** | A pattern in which a person's preferred plan, chosen in advance, differs from what they actually do when the moment arrives |
| **Framing Effect** | A change in choice caused by how options are described, not by any change in actual outcomes |
| **Mental Accounting** | Treating money as divided into separate, non-fungible mental categories |
| **Social Preferences** | Preferences that depend on the payoffs or intentions of others, not just one's own payoff |
| **Inequity Aversion** | Disutility from unequal outcomes, even at a cost to oneself |
| **Nudge** | A choice-architecture feature that predictably alters behavior without forbidding any option or changing incentives |
| **Libertarian Paternalism** | Designing choice environments to help people choose what is best by their own judgment, while preserving freedom of choice |

---

## Practice Problems

### Problem 1 — Identifying Biases

Identify which heuristic or bias best explains each scenario.

**a)** After reading several news stories about plane crashes, a traveler becomes afraid to fly, even though flying is statistically far safer than driving.  
**b)** A car dealer lists a car's "MSRP" as \$35,000 before offering it at a "discounted" \$29,000, even though \$29,000 was the dealer's target price all along.  
**c)** An employee leaves 90% of their 401(k) contributions in the plan's default money-market fund for ten years, despite better-performing options being available and well-documented.  
**d)** A manager assumes a soft-spoken new hire with glasses is more likely to work in accounting than in sales, disregarding how many more salespeople the firm employs overall.

??? success "Solution"
    **a)** **Availability heuristic** — vivid, memorable news coverage makes plane crashes seem more probable than they are, relative to the (much more common but less memorable) risk of car accidents.

    **b)** **Anchoring** — the high "MSRP" anchors the buyer's sense of value, making \$29,000 feel like a bargain regardless of the car's actual worth.

    **c)** **Status quo bias** — the employee sticks with the default option rather than actively choosing a better one.

    **d)** **Representativeness heuristic** — the manager judges by resemblance to a stereotype ("accountant-like" appearance) while ignoring the base rate (far more employees are in sales).

### Problem 2 — Prospect Theory Valuation

Using the value function $v(x) = x^{0.5}$ for gains and $v(x) = -2(-x)^{0.5}$ for losses, evaluate the following gamble relative to the current reference point: a 50% chance of gaining \$400 and a 50% chance of losing \$100.

**a)** What is the gamble's expected monetary value?  
**b)** What is its prospect-theory value?  
**c)** Would a prospect-theory decision-maker accept this gamble? Would a risk-neutral expected-value maximizer?

??? success "Solution"
    **a)** $EV = 0.5(400) + 0.5(-100) = 200 - 50 = \$150$. A risk-neutral maximizer would clearly accept, since the expected value is positive.

    **b)** $v(400) = 400^{0.5} = 20$. $v(-100) = -2(100)^{0.5} = -20$.
    
    $$\text{Prospect value} = 0.5(20) + 0.5(-20) = 10 - 10 = 0$$

    **c)** The prospect-theory value is exactly **zero** — a loss-averse decision-maker is indifferent, even though the gamble has a substantially positive expected monetary value (\$150). This illustrates how loss aversion makes favorable gambles look much less attractive once a potential loss is involved, compared to a risk-neutral benchmark that only cares about expected value.

### Problem 3 — Hyperbolic Discounting

Using the quasi-hyperbolic model with $\beta = 0.6$ and $\delta = 0.9$, compare the discount factor applied between:

**a)** This year and next year.  
**b)** Year 5 and year 6 (two future periods, neither of which is the present).  
**c)** Explain, using your answers, why a person might plan to start saving next year but then fail to do so when next year arrives.

??? success "Solution"
    **a)** Between the present and next year, the discount factor is $\beta\delta = 0.6 \times 0.9 = 0.54$.

    **b)** Between two future years, only the standard exponential discount factor applies: $\delta = 0.9$.

    **c)** When planning **today** about saving in "year 5 vs. year 6" (both future), the person uses the mild discount factor $\delta = 0.9$ and judges the tradeoff as roughly fair, so they plan to start saving later. But when "year 5" actually **arrives and becomes the present**, the comparison is now between the present (year 5) and the near future (year 6) — and the much steeper factor $\beta\delta = 0.54$ applies. The near-term temptation to spend now looms much larger than it did when viewed from a distance, so the person again postpones saving. This is the mechanism behind "I'll start next month," repeated indefinitely.

### Problem 4 — Framing Effects

A hospital is deciding how to describe the outcome of a surgery to patients. Survival rate and mortality rate convey the identical statistical information.

**a)** Frame A: "This surgery has a 90% survival rate." Frame B: "This surgery has a 10% mortality rate." Are these statistically different? Explain why patient choices might differ anyway.  
**b)** Give one additional real-world example (not from the chapter) where framing identical information differently would likely change people's choices.

??? success "Solution"
    **a)** The two frames are **statistically identical** — both describe outcomes where 90 out of 100 patients survive and 10 do not. However, research on framing effects shows patients (and even physicians) rate the surgery as more favorable under the "90% survival" frame than the "10% mortality" frame, because the word "mortality" draws attention to the loss domain, triggering loss-averse reactions even though no new information has been conveyed.

    **b)** Example answers will vary; a strong answer identifies identical information framed as a gain versus a loss and explains the likely behavioral effect. For example: describing a gas station's cash discount as "5% off for paying cash" (a gain frame) generates a more positive reaction than describing the identical price difference as "a 5% surcharge for paying by card" (a loss frame), even though the dollar amounts are the same.

### Problem 5 — Designing a Nudge

A university wants to increase the share of students who sign up to be organ donors when renewing their student ID, without banning or restricting anyone's choice.

**a)** Propose a specific nudge based on the concepts in Section 15.7, and explain which bias or heuristic it exploits.  
**b)** Explain why this intervention counts as "libertarian paternalism" rather than ordinary paternalism (such as mandating organ donation).  
**c)** Describe one ethical concern a critic might raise about this nudge.

??? success "Solution"
    **a)** Change the ID renewal form's organ donor question from an opt-in checkbox ("Check here to become an organ donor") to an opt-out default ("You will be registered as an organ donor unless you check here to decline"). This exploits **status quo bias** (Section 15.2): most students will leave the default unchanged, regardless of which way it points, simply because it requires no action.

    **b)** It is libertarian because no option is removed — any student who prefers not to donate can still opt out freely, at no cost beyond checking a box. It is paternalistic in that the university is deliberately setting the default in the direction it judges to be, on balance, better for students and for society (more donors, more lives saved), rather than remaining neutral.

    **c)** A critic might argue that opt-out defaults for something as significant and personal as organ donation could register people as donors who, with more deliberate thought, would have preferred not to be — raising a concern about whether the "choice" reflects genuine informed consent or simply inattention. (Other reasonable ethical concerns, such as fairness, transparency about the default, or whether vulnerable populations are disproportionately affected, are also acceptable.)

---

!!! mascot-celebration "You've Rebuilt the Rational Model, Flaws and All"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    From bounded rationality to prospect theory to nudges, you've just learned why real decisions deviate from the textbook optimum in predictable, exploitable ways -- and why that predictability is itself what makes behavioral economics a science rather than just a list of quirks. You're ready for the final chapter, where we put the standard rational model back to work on one of its biggest success stories: international trade.

---

!!! tip "Next Chapter"
    In [Chapter 16: International Trade](../16-international-trade/index.md), we return to the standard rational-choice framework to study why countries trade, who gains and who loses, and how trade policy shapes those outcomes — closing out the course.
