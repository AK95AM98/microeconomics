# Chapter 5: Production and Costs

## Learning Objectives

After completing this chapter, you will be able to:

1. Describe a production function and distinguish between fixed and variable inputs
2. Calculate and interpret total, marginal, and average product
3. Distinguish between the short run and the long run in production decisions
4. Explain and apply the law of diminishing marginal returns
5. Distinguish fixed costs, variable costs, and total costs, and graph each
6. Calculate average fixed cost, average variable cost, and average total cost
7. Calculate marginal cost and explain its relationship to average costs
8. Explain economies and diseconomies of scale and identify the minimum efficient scale

---

!!! mascot-welcome "From Costs to Curves"
    ![Professor Owl waving hello](../../img/mascot/welcome.png){ class="mascot-admonition-img" }
    We've studied how consumers choose what to buy — now we flip to the other side of the market and ask how firms decide what to produce. Everything here sets up the shutdown and supply decisions coming in Chapter 6, so pay close attention to how marginal cost behaves. Every choice has a trade-off, and for a firm, that trade-off is written into its cost curves.

## 5.1 The Production Function

A **production function** describes the maximum quantity of output a firm can produce from a given combination of inputs, given the current state of technology:

$$Q = f(L, K)$$

where $Q$ is output, $L$ is labor, and $K$ is capital (the two most common inputs in simplified models). A production function is a purely *technological* relationship — it says nothing yet about costs or prices, only about what is physically possible.

!!! example "Inputs across industries"
    - A bakery: labor (bakers), capital (ovens, mixers), and raw materials (flour, sugar)
    - A software firm: labor (engineers), capital (servers, computers)
    - A farm: labor, capital (tractors), and land

---

## 5.2 Total, Marginal, and Average Product

Economists track three related measures of a firm's output as it varies one input (typically labor) while holding others fixed:

| Measure | Definition | Formula |
|---|---|---|
| **Total Product (TP)** | Total output produced by a given quantity of the variable input | $TP = Q$ |
| **Marginal Product (MP)** | The additional output from one more unit of the variable input | $MP_L = \dfrac{\Delta TP}{\Delta L}$ |
| **Average Product (AP)** | Output per unit of the variable input | $AP_L = \dfrac{TP}{L}$ |

!!! example "Production schedule for a food truck"
    | Workers ($L$) | Total Product ($TP$) | Marginal Product ($MP_L$) | Average Product ($AP_L$) |
    |---|---|---|---|
    | 0 | 0 | — | — |
    | 1 | 10 | 10 | 10.0 |
    | 2 | 22 | 12 | 11.0 |
    | 3 | 33 | 11 | 11.0 |
    | 4 | 40 | 7 | 10.0 |
    | 5 | 44 | 4 | 8.8 |
    | 6 | 44 | 0 | 7.3 |
    | 7 | 40 | −4 | 5.7 |

    Marginal product rises at first (workers 1–2, benefiting from specialization in a small kitchen), then falls (diminishing returns as the truck's limited grill space becomes crowded), reaches zero at worker 6 (the truck is at capacity), and turns negative at worker 7 (too many cooks literally get in each other's way, lowering total output).

### The Relationship Between MP and AP

- When $MP_L > AP_L$, average product is **rising** (an above-average worker pulls the average up).
- When $MP_L < AP_L$, average product is **falling** (a below-average worker pulls the average down).
- When $MP_L = AP_L$, average product is at its **maximum**.

This is the same mathematical relationship that governs marginal and average *cost* later in this chapter — marginal always "pulls" average toward it.

!!! mascot-thinking "Marginal Always Pulls the Average"
    ![Professor Owl thinking](../../img/mascot/thinking.png){ class="mascot-admonition-img" }
    Hold onto this pattern — it reappears constantly: whenever a marginal value sits above an average, it pulls that average up; below, it pulls it down. You'll see this exact logic again with marginal and average cost in a few sections.

---

## 5.3 Short Run vs. Long Run

| | Short Run | Long Run |
|---|---|---|
| **Definition** | A period in which at least one input (typically capital/plant size) is fixed | A period long enough that all inputs, including plant size, are variable |
| **Firm's decision** | How much of the variable input (e.g., labor) to use with a fixed plant | What size of plant to build, and how much of every input to use |
| **Flexibility** | Limited — some costs are fixed no matter what output level is chosen | Full — the firm can choose any point on its production function, including exiting entirely |

!!! note "The short run is a planning horizon, not a fixed calendar length"
    "Short run" does not mean "a few weeks." It means *before* the firm can adjust its fixed inputs. For a nuclear power plant, the short run might be a decade (construction time for a new plant); for a food truck, the short run might be a few months (time to buy a second truck).

---

## 5.4 The Law of Diminishing Marginal Returns

**The Law of Diminishing Marginal Returns:** As more units of a variable input are added to a fixed amount of other inputs, the marginal product of the variable input eventually declines.

This law does **not** say that marginal product is always falling — it explicitly allows for marginal product to rise initially, as in the food truck example (workers 1 and 2 benefit from specialization). The law only requires that, *eventually*, each additional unit of the variable input adds less output than the previous one, because the input is being combined with a progressively smaller share of the fixed input.

!!! example "Why diminishing returns set in"
    One cook in a kitchen with ten burners is understaffed — adding a second cook roughly doubles output. But once ten cooks are using ten burners, an eleventh cook has no burner to use and can only marginally help (fetching ingredients, cleaning), with the twelfth and beyond contributing almost nothing, or even getting in the way.

This law is the production-side mirror of the law of diminishing marginal utility from Chapter 4, and it is the fundamental reason why short-run marginal cost curves eventually slope upward, as the next sections show.

---

## 5.5 Fixed, Variable, and Total Costs

| Cost Type | Definition | Behavior as Output Rises |
|---|---|---|
| **Fixed Cost (FC)** | Costs that do not vary with the quantity of output produced | Constant |
| **Variable Cost (VC)** | Costs that change with the quantity of output produced | Rises with output |
| **Total Cost (TC)** | The sum of fixed and variable costs | $TC = FC + VC$ |

!!! example "Fixed and variable costs for a food truck"
    - **Fixed costs:** Truck lease (\$2,000/month), permit fees — paid regardless of how many tacos are sold.
    - **Variable costs:** Ingredients, hourly wages, propane — rise directly with the number of tacos made.

!!! mascot-warning "Fixed Cost Is Not the Same as Sunk Cost"
    ![Professor Owl warning](../../img/mascot/warning.png){ class="mascot-admonition-img" }
    A fixed cost (like the truck lease) still has to be paid going forward and can sometimes be avoided by shutting down entirely — a true sunk cost, from Chapter 1, is money already spent that no decision can get back.

### Cost Schedule Example

| Output ($Q$) | $FC$ | $VC$ | $TC$ |
|---|---|---|---|
| 0 | \$100 | \$0 | \$100 |
| 1 | \$100 | \$50 | \$150 |
| 2 | \$100 | \$90 | \$190 |
| 3 | \$100 | \$120 | \$220 |
| 4 | \$100 | \$160 | \$260 |
| 5 | \$100 | \$220 | \$320 |

Notice that $FC$ stays at \$100 throughout, while $VC$ and therefore $TC$ rise with output.

---

## 5.6 Average Costs

| Measure | Formula | Interpretation |
|---|---|---|
| **Average Fixed Cost (AFC)** | $AFC = FC/Q$ | Fixed cost per unit; always falling as $Q$ rises ("spreading the overhead") |
| **Average Variable Cost (AVC)** | $AVC = VC/Q$ | Variable cost per unit; typically U-shaped |
| **Average Total Cost (ATC)** | $ATC = TC/Q = AFC + AVC$ | Total cost per unit; U-shaped |

Using the schedule from Section 5.5:

| $Q$ | $AFC$ | $AVC$ | $ATC$ |
|---|---|---|---|
| 1 | \$100.00 | \$50.00 | \$150.00 |
| 2 | \$50.00 | \$45.00 | \$95.00 |
| 3 | \$33.33 | \$40.00 | \$73.33 |
| 4 | \$25.00 | \$40.00 | \$65.00 |
| 5 | \$20.00 | \$44.00 | \$64.00 |

$AFC$ falls continuously (\$100.00 → \$20.00) as fixed costs are spread over more units. $AVC$ falls, then rises, as the firm first benefits from and then suffers from diminishing marginal returns. $ATC$ follows a U-shape, reaching its lowest point (around $Q=5$ here) where the two forces balance.

!!! mascot-tip "AFC Always Falls — No Exceptions"
    ![Professor Owl sharing a tip](../../img/mascot/tip.png){ class="mascot-admonition-img" }
    You can always sanity-check an AFC column: it should shrink every single time output rises, since a fixed dollar amount is being divided by a growing number. If your AFC ever rises, recheck your arithmetic.

---

## 5.7 Marginal Cost

**Marginal cost (MC)** is the additional cost of producing one more unit of output:

$$MC = \frac{\Delta TC}{\Delta Q} = \frac{\Delta VC}{\Delta Q}$$

(Since fixed costs don't change with output, the change in total cost equals the change in variable cost.)

| $Q$ | $TC$ | $MC$ |
|---|---|---|
| 0 | \$100 | — |
| 1 | \$150 | \$50 |
| 2 | \$190 | \$40 |
| 3 | \$220 | \$30 |
| 4 | \$260 | \$40 |
| 5 | \$320 | \$60 |

Marginal cost falls initially (as the firm benefits from increasing marginal returns to its variable input), reaches a minimum, and then rises (as diminishing marginal returns set in) — the same U-shape, driven by the same underlying production relationship, as marginal product's inverse.

### The MC-ATC and MC-AVC Relationship

Just as marginal product "pulls" average product (Section 5.2), marginal cost "pulls" the average cost curves:

- When $MC < ATC$ (or $AVC$), the average is **falling**.
- When $MC > ATC$ (or $AVC$), the average is **rising**.
- $MC$ crosses $ATC$ and $AVC$ at their respective **minimum points**.

!!! tip "Why MC always crosses ATC at ATC's minimum"
    This is a purely mathematical property of averages and margins: if the next unit costs less than the current average, it pulls the average down; if it costs more, it pulls the average up. The average can only be at a minimum (neither rising nor falling) when the marginal value exactly equals it.

!!! mascot-encourage "Derivatives Make This Faster, Not Harder"
    ![Professor Owl giving encouragement](../../img/mascot/encouraging.png){ class="mascot-admonition-img" }
    Deriving MC and ATC from a cost function can feel like a lot of new notation at once. Take it one step at a time: differentiate TC for MC, divide TC by Q for ATC, then set them equal — the algebra below walks through exactly that.

### Worked Example: Deriving Costs from a Cost Function

Suppose a firm's total cost function is $TC(Q) = 200 + 10Q + 2Q^2$.

**Step 1: Identify fixed and variable cost.**

$$FC = 200 \qquad VC(Q) = 10Q + 2Q^2$$

**Step 2: Derive marginal cost.**

$$MC(Q) = \frac{d(TC)}{dQ} = 10 + 4Q$$

**Step 3: Derive average total cost.**

$$ATC(Q) = \frac{TC}{Q} = \frac{200}{Q} + 10 + 2Q$$

**Step 4: Find the output that minimizes ATC**, by setting $MC = ATC$:

$$10 + 4Q = \frac{200}{Q} + 10 + 2Q$$

$$2Q = \frac{200}{Q}$$

$$2Q^2 = 200 \implies Q^2 = 100 \implies Q^* = 10$$

At $Q=10$: $ATC = \dfrac{200}{10} + 10 + 2(10) = 20+10+20 = \$50$, and $MC = 10+4(10) = \$50$. The curves intersect exactly at $ATC$'s minimum, confirming the relationship above.

---

## 5.8 Long-Run Average Cost and Economies of Scale

In the long run, a firm can choose its plant size. The **long-run average cost (LRAC) curve** is the envelope of all the short-run average total cost curves available to the firm at different plant sizes — at each output level, it shows the lowest possible average cost achievable by choosing the best plant size for that output.

| Region of LRAC | Name | Cause |
|---|---|---|
| **Downward-sloping** | **Economies of scale** | Average cost falls as output rises — specialization of labor, bulk-purchasing discounts, more efficient large-scale equipment, spreading fixed costs (like R&D) over more units |
| **Flat (bottom)** | **Constant returns to scale** | Average cost is roughly unchanged as output rises over this range |
| **Upward-sloping** | **Diseconomies of scale** | Average cost rises as output rises — coordination and communication problems, bureaucracy, and management difficulties in very large organizations |

!!! example "Economies of scale in practice"
    Amazon's enormous distribution network allows it to negotiate better shipping rates and spread the cost of its technology infrastructure across billions of transactions, lowering its average cost per package far below what a small retailer could achieve.

!!! example "Diseconomies of scale in practice"
    A restaurant chain that grows too quickly may struggle to maintain food quality and consistent management across hundreds of new locations, with layers of corporate bureaucracy slowing decisions and raising average costs per location.

---

## 5.9 Minimum Efficient Scale

The **minimum efficient scale (MES)** is the lowest level of output at which a firm achieves all available economies of scale — that is, the smallest output level at which the LRAC curve reaches its minimum point (or the start of its flat region).

The size of the minimum efficient scale relative to the size of the overall market helps determine the structure of an industry:

- If MES is **small** relative to market demand, many firms can operate efficiently — the industry tends toward many competitors (e.g., restaurants, hair salons).
- If MES is **large** relative to market demand, only a few firms can operate at an efficient scale — the industry tends toward few large firms or even a natural monopoly (e.g., electric utilities, semiconductor fabrication).

!!! note "Preview: market structure"
    Minimum efficient scale is one of the key concepts that will reappear in Chapters 6 through 9 when we study how the number and size of firms in an industry — perfect competition, monopoly, monopolistic competition, and oligopoly — depend partly on the shape of the long-run average cost curve.

---

## Key Terms

| Term | Definition |
|---|---|
| **Production Function** | The relationship showing the maximum output obtainable from given quantities of inputs |
| **Total Product (TP)** | Total output produced by a given quantity of the variable input |
| **Marginal Product (MP)** | The additional output from one more unit of a variable input |
| **Average Product (AP)** | Output per unit of the variable input |
| **Law of Diminishing Marginal Returns** | Marginal product of a variable input eventually declines as more of it is added to a fixed input |
| **Fixed Cost (FC)** | Costs that do not vary with the quantity of output |
| **Variable Cost (VC)** | Costs that vary with the quantity of output |
| **Total Cost (TC)** | $FC + VC$ |
| **Average Fixed Cost (AFC)** | $FC/Q$ |
| **Average Variable Cost (AVC)** | $VC/Q$ |
| **Average Total Cost (ATC)** | $TC/Q$ |
| **Marginal Cost (MC)** | The additional cost of producing one more unit of output |
| **Long-Run Average Cost (LRAC)** | The lowest average cost achievable at each output level when plant size is variable |
| **Economies of Scale** | Average cost falls as output rises |
| **Diseconomies of Scale** | Average cost rises as output rises |
| **Minimum Efficient Scale (MES)** | The smallest output level at which all available economies of scale are achieved |

---

## Practice Problems

### Problem 1 — Total, Marginal, and Average Product

A firm's production schedule is:

| Labor ($L$) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Total Product | 0 | 15 | 34 | 48 | 58 | 63 |

**a)** Calculate the marginal product of each worker.  
**b)** Calculate the average product of each quantity of labor.  
**c)** At what point does marginal product start declining? Is this consistent with the law of diminishing marginal returns?

??? success "Solution"
    **a)** $MP_1=15, MP_2=19, MP_3=14, MP_4=10, MP_5=5$.

    **b)** $AP_1=15.0, AP_2=17.0, AP_3=16.0, AP_4=14.5, AP_5=12.6$.

    **c)** Marginal product rises from worker 1 to worker 2 (15→19), then declines continuously from worker 2 onward (19→14→10→5). This is consistent with diminishing marginal returns: increasing returns initially (specialization benefits), then diminishing returns as more labor is combined with the fixed capital.

### Problem 2 — Fixed, Variable, and Total Cost

A firm has fixed costs of \$500. Its variable costs are given below:

| $Q$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| $VC$ | \$0 | \$200 | \$360 | \$480 | \$640 |

**a)** Calculate total cost at each output level.  
**b)** Calculate marginal cost at each output level.  
**c)** Calculate average total cost at $Q=4$.

??? success "Solution"
    **a)** $TC = FC+VC$: $TC_0=\$500, TC_1=\$700, TC_2=\$860, TC_3=\$980, TC_4=\$1{,}140$.

    **b)** $MC_1 = 700-500=\$200$; $MC_2=860-700=\$160$; $MC_3=980-860=\$120$; $MC_4=1140-980=\$160$.

    **c)** $ATC_4 = TC_4/Q = 1140/4 = \$285$.

### Problem 3 — Deriving Costs Algebraically

A firm's total cost function is $TC(Q) = 300 + 20Q + Q^2$.

**a)** Identify fixed cost and derive the variable cost function.  
**b)** Derive the marginal cost function.  
**c)** Derive the average total cost function.  
**d)** Find the output level that minimizes ATC.

??? success "Solution"
    **a)** $FC = 300$; $VC(Q) = 20Q + Q^2$.

    **b)** $MC(Q) = \dfrac{d(TC)}{dQ} = 20 + 2Q$.

    **c)** $ATC(Q) = \dfrac{300}{Q} + 20 + Q$.

    **d)** Set $MC = ATC$: $20+2Q = \dfrac{300}{Q}+20+Q \implies Q = \dfrac{300}{Q} \implies Q^2 = 300 \implies Q^* \approx 17.3$.

    At $Q^* \approx 17.3$: $ATC = \dfrac{300}{17.3} + 20 + 17.3 \approx 17.3+20+17.3 = \$54.6$, matching $MC = 20+2(17.3) \approx \$54.6$. ✓

### Problem 4 — Short Run vs. Long Run

For each scenario, state whether the firm is operating in the short run or the long run, and explain.

**a)** An airline adds two extra flights per day using its existing fleet of planes.  
**b)** A chip manufacturer breaks ground on a new \$10 billion fabrication plant.  
**c)** A coffee shop hires one additional barista for the morning rush.

??? success "Solution"
    **a)** **Short run** — the airline is adjusting a variable input (flight schedules/crew usage) while its fixed input (the fleet of planes/number of planes owned) is unchanged.

    **b)** **Long run** — building an entirely new plant is a change in the firm's fixed input (capital/plant size itself), which by definition only happens in the long run.

    **c)** **Short run** — the coffee shop is adjusting its variable input (labor) while its fixed input (the shop's physical space and equipment) remains the same.

### Problem 5 — Economies of Scale

A firm observes the following long-run average costs at different plant sizes:

| Output (units/day) | 100 | 500 | 1,000 | 2,000 | 3,000 |
|---|---|---|---|---|---|
| LRAC ($/unit) | \$40 | \$25 | \$18 | \$18 | \$22 |

**a)** Over what range of output does the firm experience economies of scale?  
**b)** Over what range does it experience constant returns to scale?  
**c)** Over what range does it experience diseconomies of scale?  
**d)** What is the approximate minimum efficient scale?

??? success "Solution"
    **a)** **Economies of scale** from 100 to 1,000 units/day — LRAC falls continuously (\$40 → \$25 → \$18).

    **b)** **Constant returns to scale** from 1,000 to 2,000 units/day — LRAC stays flat at \$18.

    **c)** **Diseconomies of scale** from 2,000 to 3,000 units/day — LRAC rises (\$18 → \$22).

    **d)** The minimum efficient scale is approximately **1,000 units/day** — the smallest output level at which LRAC first reaches its minimum (\$18).

### Problem 6 — MC and ATC Relationship

A firm's marginal cost and average total cost at various output levels are given:

| $Q$ | 10 | 20 | 30 | 40 |
|---|---|---|---|---|
| $MC$ | \$15 | \$20 | \$25 | \$35 |
| $ATC$ | \$25 | \$22 | \$22 | \$24 |

**a)** Between $Q=10$ and $Q=20$, is ATC rising or falling? Explain using the MC-ATC relationship.  
**b)** Between $Q=30$ and $Q=40$, is ATC rising or falling? Explain.  
**c)** Approximately where does ATC reach its minimum?

??? success "Solution"
    **a)** Between $Q=10$ and $Q=20$, $MC$ (\$15–\$20) is **below** $ATC$ (\$25–\$22), so $ATC$ is **falling** — a below-average marginal cost pulls the average down.

    **b)** Between $Q=30$ and $Q=40$, $MC$ (\$25–\$35) is **above** $ATC$ (\$22–\$24), so $ATC$ is **rising** — an above-average marginal cost pulls the average up.

    **c)** $ATC$ reaches its minimum **around $Q=30$**, where $MC$ (\$25) is closest to equaling $ATC$ (\$22), the transition point between $ATC$ falling and rising.

!!! mascot-celebration "You Can Now Read Any Cost Curve"
    ![Professor Owl celebrating](../../img/mascot/celebration.png){ class="mascot-admonition-img" }
    From a bare production schedule, you can now build every cost curve a firm has — fixed, variable, average, and marginal — and explain exactly why each one bends the way it does. That's the foundation for everything about firm behavior still to come!

---

!!! tip "Next Chapter"
    In [Chapter 6: Perfect Competition](../06-perfect-competition/index.md), we combine the cost curves developed here with market price-taking behavior to derive a firm's profit-maximizing output and the industry supply curve first introduced in Chapter 2.
