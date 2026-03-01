
# Calculus II - Homework 03 (Chapter 12.1–12.6)

**Source:** Paul's Online Math Notes – Calculus III Practice Problems

**Website:** [https://tutorial.math.lamar.edu/Classes/CalcIII/CalcIII.aspx](https://tutorial.math.lamar.edu/Classes/CalcIII/CalcIII.aspx)

---

# Topic 1: 12.1 Derivative and Motion (2 Problems)

**Source Section:** [Calculus with Vector Functions (Section 12.7)](https://tutorial.math.lamar.edu/Problems/CalcIII/VectorFcnsCalculus.aspx)

### 📸 Screenshot โจทย์ต้นฉบับ (Problems 4 & 5)

### 📸 Screenshot เฉลยต้นฉบับ Problem 1.1

### 📸 Screenshot เฉลยต้นฉบับ Problem 1.2

---

## Problem 1.1

**Original Problem:** Compute the derivative of the vector function:


$$\vec{r}(t) = (t^3 - 1)\vec{i} + e^{2t}\vec{j} + \cos(t)\vec{k}$$

### Solution

We differentiate each component with respect to $t$:

**Step 1:** Differentiate the $\vec{i}$ component:


$$\frac{d}{dt}(t^3 - 1) = 3t^2$$

**Step 2:** Differentiate the $\vec{j}$ component:


$$\frac{d}{dt}(e^{2t}) = 2e^{2t}$$

**Step 3:** Differentiate the $\vec{k}$ component:


$$\frac{d}{dt}(\cos(t)) = -\sin(t)$$

### Final Answer:

$$\vec{r}'(t) = 3t^2\vec{i} + 2e^{2t}\vec{j} - \sin(t)\vec{k}$$

---

## Problem 1.2

**Original Problem:** Compute the derivative of the vector function:


$$\vec{r}(t) = \left\langle \ln(t^2 + 1), te^{-t}, 4 \right\rangle$$

### Solution

We differentiate each component with respect to $t$:

**Step 1:** Differentiate the first component using the chain rule:


$$\frac{d}{dt}\left[\ln(t^2 + 1)\right] = \frac{2t}{t^2 + 1}$$

**Step 2:** Differentiate the second component using the product rule:


$$\frac{d}{dt}\left[te^{-t}\right] = e^{-t} + t(-e^{-t}) = e^{-t}(1 - t)$$

**Step 3:** Differentiate the third component:


$$\frac{d}{dt}(4) = 0$$

### Final Answer:

$$\vec{r}'(t) = \left\langle \frac{2t}{t^2 + 1}, e^{-t}(1 - t), 0 \right\rangle$$

---

---

# Topic 2: 12.2 Integrals of Vector Function; Projectile Motion (2 Problems)

**Source Section:** [Calculus with Vector Functions (Section 12.7)](https://tutorial.math.lamar.edu/Problems/CalcIII/VectorFcnsCalculus.aspx)

### 📸 Screenshot เฉลยต้นฉบับ Problem 2.1

### 📸 Screenshot เฉลยต้นฉบับ Problem 2.2

---

## Problem 2.1

**Original Problem:** Evaluate:


$$\int \vec{r}(t)dt, \quad \text{where } \vec{r}(t) = t^3\vec{i} - \frac{2t}{t^2+1}\vec{j} + \cos^2(3t)\vec{k}$$

### Solution

We integrate each component separately:

**Step 1:** Integrate the $\vec{i}$ component:


$$\int t^3dt = \frac{t^4}{4}$$

**Step 2:** Integrate the $\vec{j}$ component:


$$\int \frac{2t}{t^2+1}dt$$


Let $u = t^2 + 1$, then $du = 2tdt$:


$$= \int \frac{du}{u} = \ln|u| = \ln(t^2 + 1)$$

**Step 3:** Integrate the $\vec{k}$ component using the identity $\cos^2(\theta) = \frac{1 + \cos(2\theta)}{2}$:


$$\int \cos^2(3t)dt = \int \frac{1 + \cos(6t)}{2}dt = \frac{t}{2} + \frac{\sin(6t)}{12}$$

### Final Answer:

$$\int \vec{r}(t)dt = \frac{t^4}{4}\vec{i} - \ln(t^2+1)\vec{j} + \left(\frac{t}{2} + \frac{\sin(6t)}{12}\right)\vec{k} + \vec{C}$$

where $\vec{C}$ is the vector constant of integration.

---

## Problem 2.2

**Original Problem:** Evaluate:


$$\int_{-1}^{2} \vec{r}(t)dt, \quad \text{where } \vec{r}(t) = \langle 6, 6t^2 - 4t, te^{2t} \rangle$$

### Solution

We integrate each component from $-1$ to $2$:

**Step 1:** Integrate the first component:


$$\int_{-1}^{2} 6dt = 6t\Big|_{-1}^{2} = 6(2) - 6(-1) = 12 + 6 = 18$$

**Step 2:** Integrate the second component:


$$\int_{-1}^{2} (6t^2 - 4t)dt = \left[2t^3 - 2t^2\right]_{-1}^{2}$$

$$= \left(2(8) - 2(4)\right) - \left(2(-1) - 2(1)\right) = (16-8) - (-2-2) = 8 + 4 = 12$$

**Step 3:** Integrate the third component using integration by parts:


$$\int_{-1}^{2} te^{2t}dt$$

Let $u = t$, $dv = e^{2t}dt$, then $du = dt$, $v = \frac{e^{2t}}{2}$:

$$= \frac{te^{2t}}{2}\Bigg|_{-1}^{2} - \int_{-1}^{2} \frac{e^{2t}}{2}dt$$

$$= \frac{te^{2t}}{2}\Bigg|_{-1}^{2} - \frac{e^{2t}}{4}\Bigg|_{-1}^{2}$$

$$= \left(\frac{2e^{4}}{2} - \frac{(-1)e^{-2}}{2}\right) - \left(\frac{e^{4}}{4} - \frac{e^{-2}}{4}\right)$$

$$= \left(e^4 + \frac{e^{-2}}{2}\right) - \left(\frac{e^4}{4} - \frac{e^{-2}}{4}\right)$$

$$= e^4 + \frac{e^{-2}}{2} - \frac{e^4}{4} + \frac{e^{-2}}{4}$$

$$= \frac{3e^4}{4} + \frac{3e^{-2}}{4} = \frac{3}{4}\left(e^4 + e^{-2}\right)$$

### Final Answer:

$$\int_{-1}^{2} \vec{r}(t)dt = \left\langle 18, 12, \frac{3}{4}(e^4 + e^{-2}) \right\rangle$$

---

---

# Topic 3: 12.3 Arc Length in Space (2 Problems)

**Source Section:** [Arc Length with Vector Functions (Section 12.9)](https://tutorial.math.lamar.edu/Problems/CalcIII/VectorArcLength.aspx)

### 📸 Screenshot โจทย์ต้นฉบับ (Problems 1 & 2)

### 📸 Screenshot เฉลยต้นฉบับ Problem 3.1

### 📸 Screenshot เฉลยต้นฉบับ Problem 3.2

---

## Problem 3.1

**Original Problem:** Determine the length of the vector function on the given interval:


$$\vec{r}(t) = (3-4t)\vec{i} + 6t\vec{j} - (9+2t)\vec{k}, \quad -6 \le t \le 8$$

### Solution

**Step 1:** Find $\vec{r}'(t)$:


$$\vec{r}'(t) = -4\vec{i} + 6\vec{j} - 2\vec{k}$$

**Step 2:** Find $||\vec{r}'(t)||$:


$$||\vec{r}'(t)|| = \sqrt{(-4)^2 + 6^2 + (-2)^2} = \sqrt{16 + 36 + 4} = \sqrt{56} = 2\sqrt{14}$$

**Step 3:** Calculate the arc length:


$$L = \int_{-6}^{8} ||\vec{r}'(t)||dt = \int_{-6}^{8} 2\sqrt{14}dt$$

$$L = 2\sqrt{14}\cdot t\Big|_{-6}^{8} = 2\sqrt{14}(8 - (-6)) = 2\sqrt{14}\cdot 14 = 28\sqrt{14}$$

### Final Answer:

$$L = 28\sqrt{14}$$

---

## Problem 3.2

**Original Problem:** Determine the length of the vector function on the given interval:


$$\vec{r}(t) = \left\langle \frac{1}{3}t^3, 4t, \sqrt{2}t^2 \right\rangle, \quad 0 \le t \le 2$$

### Solution

**Step 1:** Find $\vec{r}'(t)$:


$$\vec{r}'(t) = \left\langle t^2, 4, 2\sqrt{2}t \right\rangle$$

**Step 2:** Find $||\vec{r}'(t)||$:


$$||\vec{r}'(t)|| = \sqrt{(t^2)^2 + 4^2 + (2\sqrt{2}t)^2}$$

$$= \sqrt{t^4 + 16 + 8t^2}$$

$$= \sqrt{(t^2 + 4)^2} = t^2 + 4$$

(Note: $t^2 + 4 > 0$ always, so no absolute value needed.)

**Step 3:** Calculate the arc length:


$$L = \int_{0}^{2} (t^2 + 4)dt = \left[\frac{t^3}{3} + 4t\right]_{0}^{2}$$

$$= \frac{8}{3} + 8 = \frac{8}{3} + \frac{24}{3} = \frac{32}{3}$$

### Final Answer:

$$L = \frac{32}{3}$$

---

---

# Topic 4: 12.4 Curvature and Normal Vector of Curve (2 Problems)

**Source Section:** [Curvature (Section 12.10)](https://tutorial.math.lamar.edu/Problems/CalcIII/Curvature.aspx)

### 📸 Screenshot โจทย์ต้นฉบับ (Problems 1 & 2)

### 📸 Screenshot เฉลยต้นฉบับ Problem 4.1

### 📸 Screenshot เฉลยต้นฉบับ Problem 4.2

---

## Problem 4.1

**Original Problem:** Find the curvature for:


$$\vec{r}(t) = \langle \cos(2t), -\sin(2t), 4t \rangle$$

### Solution

The curvature formula is: $\kappa = \frac{||\vec{r}'(t) \times \vec{r}''(t)||}{||\vec{r}'(t)||^3}$

**Step 1:** Find $\vec{r}'(t)$:


$$\vec{r}'(t) = \langle -2\sin(2t), -2\cos(2t), 4 \rangle$$

**Step 2:** Find $||\vec{r}'(t)||$:


$$||\vec{r}'(t)|| = \sqrt{4\sin^2(2t) + 4\cos^2(2t) + 16} = \sqrt{4 + 16} = \sqrt{20} = 2\sqrt{5}$$

**Step 3:** Find $\vec{r}''(t)$:


$$\vec{r}''(t) = \langle -4\cos(2t), 4\sin(2t), 0 \rangle$$

**Step 4:** Compute $\vec{r}'(t) \times \vec{r}''(t)$:


$$\vec{r}' \times \vec{r}'' = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\\\ -2\sin(2t) & -2\cos(2t) & 4 \\\\ -4\cos(2t) & 4\sin(2t) & 0 \end{vmatrix}$$

$$\vec{i}: (-2\cos(2t))(0) - (4)(4\sin(2t)) = -16\sin(2t)$$

$$\vec{j}: -[(-2\sin(2t))(0) - (4)(-4\cos(2t))] = -16\cos(2t)$$

$$\vec{k}: (-2\sin(2t))(4\sin(2t)) - (-2\cos(2t))(-4\cos(2t))$$

$$= -8\sin^2(2t) - 8\cos^2(2t) = -8$$

So: $\vec{r}' \times \vec{r}'' = \langle -16\sin(2t), -16\cos(2t), -8 \rangle$

**Step 5:** Find $||\vec{r}' \times \vec{r}''||$:


$$= \sqrt{256\sin^2(2t) + 256\cos^2(2t) + 64} = \sqrt{256 + 64} = \sqrt{320} = 8\sqrt{5}$$

**Step 6:** Compute curvature:


$$\kappa = \frac{8\sqrt{5}}{(2\sqrt{5})^3} = \frac{8\sqrt{5}}{40\sqrt{5}} = \frac{8}{40} = \frac{1}{5}$$

### Final Answer:

$$\kappa = \frac{1}{5}$$

---

## Problem 4.2

**Original Problem:** Find the curvature for:


$$\vec{r}(t) = \langle 4t, -t^2, 2t^3 \rangle$$

### Solution

**Step 1:** Find $\vec{r}'(t)$:


$$\vec{r}'(t) = \langle 4, -2t, 6t^2 \rangle$$

**Step 2:** Find $||\vec{r}'(t)||$:


$$||\vec{r}'(t)|| = \sqrt{16 + 4t^2 + 36t^4}$$

$$= \sqrt{4(4 + t^2 + 9t^4)} = 2\sqrt{9t^4 + t^2 + 4}$$

**Step 3:** Find $\vec{r}''(t)$:


$$\vec{r}''(t) = \langle 0, -2, 12t \rangle$$

**Step 4:** Compute $\vec{r}'(t) \times \vec{r}''(t)$:


$$\vec{r}' \times \vec{r}'' = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\\\ 4 & -2t & 6t^2 \\\\ 0 & -2 & 12t \end{vmatrix}$$

$$\vec{i}: (-2t)(12t) - (6t^2)(-2) = -24t^2 + 12t^2 = -12t^2$$

$$\vec{j}: -[(4)(12t) - (6t^2)(0)] = -48t$$

$$\vec{k}: (4)(-2) - (-2t)(0) = -8$$

So: $\vec{r}' \times \vec{r}'' = \langle -12t^2, -48t, -8 \rangle$

**Step 5:** Find $||\vec{r}' \times \vec{r}''||$:


$$= \sqrt{144t^4 + 2304t^2 + 64}$$

$$= \sqrt{4(36t^4 + 576t^2 + 16)} = 2\sqrt{36t^4 + 576t^2 + 16}$$

**Step 6:** Compute curvature:


$$\kappa = \frac{2\sqrt{36t^4 + 576t^2 + 16}}{[2\sqrt{9t^4 + t^2 + 4}]^3}$$

$$= \frac{2\sqrt{36t^4 + 576t^2 + 16}}{8(9t^4 + t^2 + 4)^{3/2}}$$

$$= \frac{\sqrt{36t^4 + 576t^2 + 16}}{4(9t^4 + t^2 + 4)^{3/2}}$$

### Final Answer:

$$\kappa(t) = \frac{\sqrt{36t^4 + 576t^2 + 16}}{4(9t^4 + t^2 + 4)^{3/2}}$$

---

---

# Topic 5: 12.5 Tangential and Normal Components of Acceleration (2 Problems)

**Source Section:** [Velocity and Acceleration (Section 12.11)](https://tutorial.math.lamar.edu/Problems/CalcIII/Velocity_Acceleration.aspx)

### 📸 Screenshot โจทย์ต้นฉบับ (Problems 1 & 2)

### 📸 Screenshot เฉลยต้นฉบับ Problem 5.1

### 📸 Screenshot เฉลยต้นฉบับ Problem 5.2 (Lesson Example)

---

## Problem 5.1

**Original Problem:** Determine the tangential and normal components of acceleration for the object whose position is given by:


$$\vec{r}(t) = \langle \cos(2t), -\sin(2t), 4t \rangle$$

### Solution

**Step 1:** Find the velocity vector $\vec{v}(t)$:


$$\vec{v}(t) = \vec{r}'(t) = \langle -2\sin(2t), -2\cos(2t), 4 \rangle$$

**Step 2:** Find the speed $||\vec{v}(t)||$:


$$||\vec{v}(t)|| = \sqrt{4\sin^2(2t) + 4\cos^2(2t) + 16} = \sqrt{4 + 16} = \sqrt{20} = 2\sqrt{5}$$

**Step 3:** Calculate tangential acceleration $a_T$:


$$a_T = \frac{d}{dt}||\vec{v}(t)||$$


Since $||\vec{v}(t)|| = 2\sqrt{5}$ is constant:


$$a_T = 0$$

**Step 4:** Find the acceleration vector $\vec{a}(t)$:


$$\vec{a}(t) = \vec{v}'(t) = \langle -4\cos(2t), 4\sin(2t), 0 \rangle$$

**Step 5:** Find $||\vec{a}(t)||$:


$$||\vec{a}(t)|| = \sqrt{16\cos^2(2t) + 16\sin^2(2t) + 0} = \sqrt{16} = 4$$

**Step 6:** Calculate normal acceleration $a_N$ using $||\vec{a}||^2 = a_T^2 + a_N^2$:


$$a_N = \sqrt{||\vec{a}||^2 - a_T^2} = \sqrt{16 - 0} = 4$$

### Final Answer:

* **Tangential component:** $a_T = 0$
* **Normal component:** $a_N = 4$

---

## Problem 5.2

**Original Problem (Worked Example from Lesson Notes):** An object has acceleration $\vec{a}(t) = \vec{i} + 2\vec{j} + 6t\vec{k}$, initial velocity $\vec{v}(0) = \vec{j} - \vec{k}$, and initial position $\vec{r}(0) = \vec{i} - 2\vec{j} + 3\vec{k}$.

Determine the tangential and normal components of acceleration.

**Source:** [Velocity and Acceleration Lesson Notes — Example 2](https://tutorial.math.lamar.edu/Classes/CalcIII/Velocity_Acceleration.aspx)

### Solution

**Step 1:** First find $\vec{v}(t)$ by integrating $\vec{a}(t)$:


$$\vec{v}(t) = \int \langle 1, 2, 6t \rangle dt = \langle t, 2t, 3t^2 \rangle + \vec{C_1}$$


Apply $\vec{v}(0) = \langle 0, 1, -1 \rangle$: $\vec{C_1} = \langle 0, 1, -1 \rangle$


$$\vec{v}(t) = \langle t, 2t + 1, 3t^2 - 1 \rangle$$

**Step 2:** Find the speed $||\vec{v}(t)||$:


$$||\vec{v}(t)|| = \sqrt{t^2 + (2t+1)^2 + (3t^2-1)^2}$$

$$= \sqrt{t^2 + 4t^2 + 4t + 1 + 9t^4 - 6t^2 + 1}$$

$$= \sqrt{9t^4 - t^2 + 4t + 2}$$

**Step 3:** Calculate $a_T = \frac{\vec{v} \cdot \vec{a}}{||\vec{v}||}$:

$$\vec{v} \cdot \vec{a} = (t)(1) + (2t+1)(2) + (3t^2-1)(6t)$$

$$= t + 4t + 2 + 18t^3 - 6t = 18t^3 - t + 2$$

$$a_T = \frac{18t^3 - t + 2}{\sqrt{9t^4 - t^2 + 4t + 2}}$$

**Step 4:** Compute $\vec{v} \times \vec{a}$ for $a_N$:


$$\vec{v} \times \vec{a} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\\\ t & 2t+1 & 3t^2-1 \\\\ 1 & 2 & 6t \end{vmatrix}$$

$$\vec{i}: (2t+1)(6t) - (3t^2-1)(2) = 12t^2 + 6t - 6t^2 + 2 = 6t^2 + 6t + 2$$

$$\vec{j}: -[(t)(6t) - (3t^2-1)(1)] = -(6t^2 - 3t^2 + 1) = -(3t^2 + 1)$$

$$\vec{k}: (t)(2) - (2t+1)(1) = 2t - 2t - 1 = -1$$

$$\vec{v} \times \vec{a} = \langle 6t^2 + 6t + 2, -(3t^2+1), -1 \rangle$$

**Step 5:** Find $||\vec{v} \times \vec{a}||$:


$$||\vec{v} \times \vec{a}|| = \sqrt{(6t^2+6t+2)^2 + (3t^2+1)^2 + 1}$$

**Step 6:** Calculate $a_N = \frac{||\vec{v} \times \vec{a}||}{||\vec{v}||}$:


$$a_N = \frac{\sqrt{(6t^2+6t+2)^2 + (3t^2+1)^2 + 1}}{\sqrt{9t^4 - t^2 + 4t + 2}}$$

### Final Answer:

$$a_T = \frac{18t^3 - t + 2}{\sqrt{9t^4 - t^2 + 4t + 2}}$$

$$a_N = \frac{\sqrt{(6t^2+6t+2)^2 + (3t^2+1)^2 + 1}}{\sqrt{9t^4 - t^2 + 4t + 2}}$$

---

---

# Topic 6: 12.6 Velocity and Acceleration in Polar Coordinates (2 Problems)

**Source Section:** [Velocity and Acceleration (Section 12.11)](https://tutorial.math.lamar.edu/Problems/CalcIII/Velocity_Acceleration.aspx)

### 📸 Screenshot เฉลยต้นฉบับ Problem 6.1

### 📸 Screenshot เฉลยต้นฉบับ Problem 6.2 (Lesson Example)

---

## Problem 6.1

**Original Problem:** An object's acceleration is given by:


$$\vec{a}(t) = 3t\vec{i} - 4e^{-t}\vec{j} + 12t^2\vec{k}$$


The object's initial velocity is $\vec{v}(0) = \vec{j} - 3\vec{k}$ and the object's initial position is $\vec{r}(0) = -5\vec{i} + 2\vec{j} - 3\vec{k}$.

Determine the object's velocity and position functions.

### Solution

#### Part A: Find $\vec{v}(t)$

We integrate the acceleration:


$$\vec{v}(t) = \int \vec{a}(t)dt = \int \langle 3t, -4e^{-t}, 12t^2 \rangle dt$$

$$\vec{v}(t) = \left\langle \frac{3t^2}{2}, 4e^{-t}, 4t^3 \right\rangle + \vec{C_1}$$

Apply initial condition $\vec{v}(0) = \langle 0, 1, -3 \rangle$:


$$\left\langle 0, 4, 0 \right\rangle + \vec{C_1} = \langle 0, 1, -3 \rangle$$

$$\vec{C_1} = \langle 0, -3, -3 \rangle$$

$$\boxed{\vec{v}(t) = \left\langle \frac{3t^2}{2}, 4e^{-t} - 3, 4t^3 - 3 \right\rangle}$$

#### Part B: Find $\vec{r}(t)$

We integrate the velocity:


$$\vec{r}(t) = \int \vec{v}(t)dt = \int \left\langle \frac{3t^2}{2}, 4e^{-t} - 3, 4t^3 - 3 \right\rangle dt$$

$$\vec{r}(t) = \left\langle \frac{t^3}{2}, -4e^{-t} - 3t, t^4 - 3t \right\rangle + \vec{C_2}$$

Apply initial condition $\vec{r}(0) = \langle -5, 2, -3 \rangle$:


$$\left\langle 0, -4, 0 \right\rangle + \vec{C_2} = \langle -5, 2, -3 \rangle$$

$$\vec{C_2} = \langle -5, 6, -3 \rangle$$

$$\boxed{\vec{r}(t) = \left\langle \frac{t^3}{2} - 5, -4e^{-t} - 3t + 6, t^4 - 3t - 3 \right\rangle}$$

### Final Answer:

$$\vec{v}(t) = \frac{3t^2}{2}\vec{i} + (4e^{-t} - 3)\vec{j} + (4t^3 - 3)\vec{k}$$

$$\vec{r}(t) = \left(\frac{t^3}{2} - 5\right)\vec{i} + (-4e^{-t} - 3t + 6)\vec{j} + (t^4 - 3t - 3)\vec{k}$$

---

## Problem 6.2

**Original Problem (Worked Example from Lesson Notes):** An object has acceleration $\vec{a}(t) = \vec{i} + 2\vec{j} + 6t\vec{k}$, initial velocity $\vec{v}(0) = \vec{j} - \vec{k}$, and initial position $\vec{r}(0) = \vec{i} - 2\vec{j} + 3\vec{k}$.

Determine the object's velocity and position functions.

**Source:** [Velocity and Acceleration Lesson Notes — Example 1](https://tutorial.math.lamar.edu/Classes/CalcIII/Velocity_Acceleration.aspx)

### Solution

#### Part A: Find $\vec{v}(t)$

Integrate the acceleration:


$$\vec{v}(t) = \int \vec{a}(t)dt = \int \langle 1, 2, 6t \rangle dt$$

$$= \langle t, 2t, 3t^2 \rangle + \vec{C_1}$$

Apply $\vec{v}(0) = \langle 0, 1, -1 \rangle$:


$$\langle 0, 0, 0 \rangle + \vec{C_1} = \langle 0, 1, -1 \rangle$$

$$\vec{C_1} = \langle 0, 1, -1 \rangle$$

$$\boxed{\vec{v}(t) = \langle t, 2t + 1, 3t^2 - 1 \rangle}$$

#### Part B: Find $\vec{r}(t)$

Integrate the velocity:


$$\vec{r}(t) = \int \vec{v}(t)dt = \int \langle t, 2t + 1, 3t^2 - 1 \rangle dt$$

$$= \langle \frac{t^2}{2}, t^2 + t, t^3 - t \rangle + \vec{C_2}$$

Apply $\vec{r}(0) = \langle 1, -2, 3 \rangle$:


$$\langle 0, 0, 0 \rangle + \vec{C_2} = \langle 1, -2, 3 \rangle$$

$$\vec{C_2} = \langle 1, -2, 3 \rangle$$

$$\boxed{\vec{r}(t) = \langle \frac{t^2}{2} + 1, t^2 + t - 2, t^3 - t + 3 \rangle}$$

### Final Answer:

$$\vec{v}(t) = t\vec{i} + (2t + 1)\vec{j} + (3t^2 - 1)\vec{k}$$

$$\vec{r}(t) = \left(\frac{t^2}{2} + 1\right)\vec{i} + (t^2 + t - 2)\vec{j} + (t^3 - t + 3)\vec{k}$$

---

---

# Summary Table

| # | Topic | Problem Source URL |
| --- | --- | --- |
| 1.1 | 12.1 Derivative and Motion | [Prob 4](https://tutorial.math.lamar.edu/Problems/CalcIII/VectorFcnsCalculus.aspx) |
| 1.2 | 12.1 Derivative and Motion | [Prob 5](https://tutorial.math.lamar.edu/Problems/CalcIII/VectorFcnsCalculus.aspx) |
| 2.1 | 12.2 Integrals of Vector Function | [Prob 7](https://tutorial.math.lamar.edu/Problems/CalcIII/VectorFcnsCalculus.aspx) |
| 2.2 | 12.2 Integrals of Vector Function | [Prob 8](https://tutorial.math.lamar.edu/Problems/CalcIII/VectorFcnsCalculus.aspx) |
| 3.1 | 12.3 Arc Length in Space | [Prob 1](https://tutorial.math.lamar.edu/Problems/CalcIII/VectorArcLength.aspx) |
| 3.2 | 12.3 Arc Length in Space | [Prob 2](https://tutorial.math.lamar.edu/Problems/CalcIII/VectorArcLength.aspx) |
| 4.1 | 12.4 Curvature and Normal Vector | [Prob 1](https://tutorial.math.lamar.edu/Problems/CalcIII/Curvature.aspx) |
| 4.2 | 12.4 Curvature and Normal Vector | [Prob 2](https://tutorial.math.lamar.edu/Problems/CalcIII/Curvature.aspx) |
| 5.1 | 12.5 Tangential and Normal Accel. | [Prob 2](https://tutorial.math.lamar.edu/Problems/CalcIII/Velocity_Acceleration.aspx) |
| 5.2 | 12.5 Tangential and Normal Accel. | [Lesson Example 2](https://tutorial.math.lamar.edu/Classes/CalcIII/Velocity_Acceleration.aspx) |
| 6.1 | 12.6 Velocity and Acceleration | [Prob 1](https://tutorial.math.lamar.edu/Problems/CalcIII/Velocity_Acceleration.aspx) |
| 6.2 | 12.6 Velocity and Acceleration | [Lesson Example 1](https://tutorial.math.lamar.edu/Classes/CalcIII/Velocity_Acceleration.aspx) |

---
