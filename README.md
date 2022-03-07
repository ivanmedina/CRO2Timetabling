# CRO ALGORITHM TO OPTIMIZE TIMETABLES

## Abstract
Timetabling is an exponentially growing combinatorial problem that requires a large number of decisions to be made to generate school schedules that meet all established requirements, it is here where many of the times through specialized algorithms the desired solutions are obtained, however, certain resources such as teachers or classrooms could be better used, and for this we need to analyze a large number of possible solutions.
In the present research, a valid school schedule is taken as an entry, from which we optimize the use of classrooms to take better advantage of them, applying an algorithm that simulates how molecules form in a more favorable molecular structure, reducing their potential energy to the minimum posible. The algorithm is known by the name CRO (Chemical Reaction Optimization), and is known for its effectiveness in solving very difficult combinatorics problems, so it performs successfully on the Timetabling problem.

## Surface of potential energy
![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen1.png)

## Chemical Reactions
a)	Ineffective collision on the wall
b)	 Decomposition
c)	ineffective intermolecular collision
d)	Synthesis

![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen2.png)

### Ineffective collision on the wall
 ![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen3.png)

### ineffective intermolecular collision
 ![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen4.png)
 
### Descomposition operatos
 ![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen5.png)

### Synthesis operator
 ![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen6.png)
 

## Flowchart
![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen7.png)

---

## Implementation

### Timetabling Input

| Inputs | Expression |
| :---: | :---: |
| Days | $$D=\left[D_{0}, D_{1}, D_{2},{ \ldots}, D_{n}\right]$$ |
| Sloats | $$E=\left[E_{0}, E_{1}, E_{2},{ \ldots}, E_{n}\right]$$  |
| Classrooms | $$S=\left[S_{0}, S_{1}, S_{2},{ \ldots}, S_{n}\right]$$  |
| Courses | $$C=\left[C_{0}, C_{1}, C_{2},{ \ldots}, C_{n}\right]$$  |
| Teachers | $$P=\left[P_{0}, P_{1}, P_{2},{ \ldots}, P_{n}\right]$$  |
| Max. courses per Teacher | $$\operatorname{maxCP}=\left[x \mid x \in \mathbf{N}^{*}\right]$$ |
| Max. spaces per day per Course | $$\operatorname{maxEC}=\left[x \mid x \in \mathbf{N}^{*}\right]$$ |


### Expressions of timetabling input data

| Expression | Example |
| :---: | :---: |
| $$D_{x}$$ | 'Monday' |
| $$E_{x}$$ | '7:30-8:20'  |
| $$S_{x}$$ | 'Classroom 1'  |
| $$C_{x}$$ | { $$T_{x}$$, $$h_{c_{x}}$$ }  |
| $$P_{x}$$ | { 'Teacher 1', $$A_{p}$$, $$B_{p}$$ }  |
| Vector availability teacher $$P_{x}$$ | $$A_{p}$$ = [ 1,1,1,1,1,0,1, ..., $$E_{n}$$ ] |
| Vector subjects teacher $$P_{x}$$ | $$B_{p}$$ = [ 1,1,1,1,1,0,1, ..., $$M_{n}$$ ] |
| Hours per week of the course $$C_{x}$$ | $$h_{c_{x}}=\left\{x \mid x \in N^{*}\right\}$$ |


### Timetabling variables

| Variable | Value |
| :---: | :---: |
| $$X_{descp}$$ | { 1  if teacher 'p' teaches course 'c' in classroom 's' at event 'e' on day 'd'; 0 if not } |
| $$G_{des}$$ | { 1 if lounge ‘s’ is busy ‘e’ on day ‘d’ ; 0 if not } |
| $$O_{dep}$$ | { 1 if teacher 'p' teaches on day 'd' during period 'e'; 0 if not } |
| $$W_{dc}$$ | { 1 if course 'c' is taught on day 'd'; 0 if not } |
| $$Y_{cp}$$ | { 1 if teacher 'p' teaches course 'c'; 0 if not } |
| $$V_{cs}$$ | { 1 si el curso ‘c’ es impartido en el salón ‘s’; 0 si no } |
| $$U_{c}$$ | { N first event assigned for each 'c' } |
| $$W_{s}$$ | { 1 if the room 's' is assigned; 0 if not } |
| $$\gamma_{dc}$$ | { 'e' first event for course 'c' on day 'd'; -1 if there are no spaces for 'c' on day 'd' } |
| $$\omega{dc}$$ | { 'e' last event for course 'c' on day 'd'; -1 if there are no spaces for 'c' on day 'd' } |

### Restrictions

#### Hard Constraints

| Resrtiction | Description |
| :---: | :---: |
|R1| Courses are scheduled according to the number of hours per week required. |
|R2| Courses assigned to the same teacher must not occur in the same period. |
|R3| A classroom can only attend one course per period.|
|R4| Teachers can only be assigned the subjects they are capable of teaching. |
|R5| Teachers may have a maximum of 4 subjects assigned.|
|R6| The availability of the teacher must be respected|
|R7| Classes must be scheduled in daily sessions of maximum 3. |
|R8| There should be no interruptions in any session of any course. |

#### Soft Constraints

| Resrtiction | Description |
| :---: | :---: |
|R9| Each course corresponds to only one classroom. |
|R10| Courses assigned more than one day must start at the same time. |
|R11| There must be at least one day off between sessions of the same course. |
|R12| Assignments should be made in such a way as to take advantage of as many rooms as possible. |

### Base model for restrictions

#### R1
$$\sum_{d=0}^{D_{n}} \sum_{e=0}^{E_{n}} \sum_{s=0}^{S_{n}} \sum_{p=0}^{P_{n}} X_{d e s c p}=\mathrm{H}_{c_{i}} \forall c$$

#### R2
$$\sum_{s=0}^{S_{n}} \sum_{c=0}^{C_{n}} X_{d e s c p} \leq 1 \forall d \forall e \forall p$$

#### Restriction 3
$$\sum_{c=0}^{C_{n}} \sum_{p=0}^{P_{n}} X_{d e s c p} \leq 1 \forall d \forall e \forall s$$

#### R4
$$Y_{c p} \leq B_{c p}$$

#### R5
$$\sum_{c=0}^{C_{n}} Y_{c p} \leq 4 \forall p$$

#### R6
$$\sum_{s=0}^{S_{n}} \sum_{c=0}^{C_{n}} X_{d e s c p} \leq \mathrm{A}_{p e} \forall d \forall e \forall p$$

#### R7
$$\sum_{e=0}^{E_{n}} \sum_{s=0}^{S_{n}} X_{\operatorname{desc} p} \leq 3 \forall d \forall c \forall p$$

#### R8
$$\begin{gathered}
\left(\left(\Omega_{d c}+1\right)-\left(\Gamma_{d c}+1\right)\right)=\sum_{e=\Gamma_{d c}}^{\Omega_{d c}} \sum_{s=0}^{S_{n}} \sum_{p=0}^{P_{n}} X_{d e s c p} \forall d \forall c \\
\mid\left(W_{d c}=1, Y_{c p}=1 \text { y } V_{c s}=1\right)
\end{gathered}$$

#### R9
$$\sum_{s=0}^{S_{n}} V_{c S} \leq 1 \forall c$$

#### R10
$$\sum_{d=0}^{D_{n}} \sum_{s=0}^{S_{n}} \sum_{p=0}^{P_{n}} X_{d U_{c} s c s p}=\sum_{d=0}^{D_{n}} W_{d c} \forall c$$

#### R11
$$W_{d c}+W_{d+1 c} \leq 1 \forall c: d \in\left\{D_{1}, D_{2}, \ldots D_{n-1}\right\}$$

#### R12
$$\mathrm{Z}_{\mathrm{i}}=\sum_{0}^{S_{n}} Q_{S} / \operatorname{Sn}$$
$$Z_{j>Z_{0}}$$

### Objective Function

The value of the objective function is the result of evaluating the constraints, and is expressed through the following equation.

$$F(x)=(R D * C)+R S$$

### Fitness Function

Although the fitness function and the objective function can be considered the same, the objective function will be considered as the function to be optimized and fitness as another function that guides optimization towards maximization or minimization.

$$f(F(x))=1 / F(x)$$

===

## Results

### Instances


| Id | Days | Sloats | Classrooms | Courses | Hours x Course | Teachers | MaxCP | MaxEC | 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 |  1 |  1  | 1  |  1  | 1 | 1  | 1 | 1 |
| 2 |  2 |  2  | 2  |  2  | 2 | 2  | 2 | 2 |
| 3 |  5 |  6  | 10 |  6  | 6 | 6  | 1 | 3 |
| 4 |  5 |  6  | 10 |  6  | 6 | 3  | 2 | 3 |
| 5 |  5 |  6  | 10 | 10  | 6 | 10 | 2 | 3 |
| 6 |  5 |  6  | 20 | 20  | 6 | 20 | 2 | 3 |
| 7 |  5 | 12  |20  | 20  | 6 | 20 | 2 | 3 |
| 8 |  5 | 12  |30  | 30  | 6 | 30 | 4 | 3 |
| 9 |  5 | 16  |40  | 40  | 6 | 40 | 4 | 3 |
| 10 | 5 | 16  |50  | 50  | 6 | 50 | 4 | 3 |

### Instance parameters

| Id | Initial KE | KELossRate | Colision | Alfa | Beta |Max Iteratrions |  Population Size | 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | 
| 1 | 10% | 0.00011  | 0.3  | 10 |  0.00001    | 50000  | 500  | 
| 2 | 10% | 0.00011  | 0.3  | 10 |  0.00001    | 50000  | 500  | 
| 3 | 10% | 0.00011  | 0.3  | 10 |  0.00001    | 50000  | 500  | 
| 4 | 20% | 0.2  |     0.5  | 10 |  0.005      | 50000  | 500  | 
| 5 | 20% | 0.2  |     0.7  | 10 |  0.005      | 5000   | 250  | 
| 6 | 20% | 0.2  |     0.7  | 10 |  0.005      | 5000   | 250  | 
| 7 | 33% | 0.3  |     0.8  | 10 |  0.00005    | 500    | 60  | 
| 8 | 15% | 0.1  |     0.8  | 100 | 0.00005    | 50000  | 100  | 
| 9 | 5% |  0.2  |     0.85 | 100 | 0.00005    | 5000   | 100  | 
| 10 | 5% | 0.05  |    0.9  | 20 |  0.00000025 | 500    | 20  | 

### Execution times

| Id | Time | 
| :---: | :---: |
| 1 |   0 s. |
| 2 |   44 s. |
| 3 |   5 m. |
| 4 |   8 m. |
| 5 |   42 m. |
| 6 |   81 m. |
| 7 |   1.9 h. |
| 8 |   2.7 h. |
| 9 |   3 h. |
| 10 |  3.8 h. |

### Final results

| Id | f(F(x)) | Z | f(F(x))' | Z' | Molecule Number | 
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 |  0.000125 | 1.00 | 0.000125 |          1.00   |  - |
| 2 |  0.000125 | 1.00 | 0.000123 |          1   |     149 |
| 3 |  0.000125 | 0.60 | 0.000123 |          0.8   |   150 |
| 4 |  0.00012499 | 0.29 | 0.00012344 |      0.5   |   500 |
| 5 |  0.00012499 | 0.5 | 0.00012334 |       0.7   |   248 |
| 6 |  0.0001249921 | 0.5 | 0.0001249906 |   0.55   |  109 |
| 7 |  0.0001249921 | 0.5 | 0.0001249906 |   0.55   |  41 |
| 8 |  0.0001249921 | 0.5 | 0.0001249915 |   0.5   |   40 |
| 9 |  0.0001249921 | 0.5 | 0.0001249917 |   0.525   | 78 |
| 10 | 0.0001249921 | 0.5 | 0.0001249918 |   0.5   |   9 |

### Optimization analysis

![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen8.png)
![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen9.png)

## Example
![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen10.png)
![imagen1.png](https://raw.githubusercontent.com/ivanmedina/CRO2Timetabling/main/assets/Imagen11.png)

$$P=\left[P_{0}, P_{1}, P_{2},{ \ldots}, P_{n}\right]$$ 

## Conclusion

The current research is satisfactorily concluded, whose purpose is to demonstrate that it is possible to achieve better solutions to the timetabling problem with the CRO algorithm,
than with a heuristic algorithm. CRO's metaheuristic techniques have good results in problems that require exploring a very large solution space.
Optimization is better and faster appreciated in medium difficulty instances, of 20 courses or less, at least with current resources and techniques applied for implementation.

The process of energy redistribution, with the use of the correct operators, is highly effective to test most possible combinations to solve very large problems exponentially,
also the application of the 4 possible events that simulate chemical reactions, where 2 of them are responsible for intensification and the other 2 for diversification,
successfully perform the task of avoiding stagnation.
