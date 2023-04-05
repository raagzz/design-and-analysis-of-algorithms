# Personal Loan Prediction using ANN-EA Hybrid Systems
## Introduction
The dataset contains data on 5000 customers including demographic information, the customer's relationship with the bank and the customer response to the last personal loan campaign.
The **GOAL** is to predict the likelihood of a liability customer buying personal loans.
This prediction task will be done using Neural Networks and the optimization of weights, instead of being done by back-propagation (gradient descent method), will be done using:
- Genetic Algorithm
- Cultural Algorithm
- Particle Swarm Optimization
- Ant Colony Optimization

## Neural Network Architecture
- Input Layer = 11
- Hidden Layer = 8
  - Activation Function: ReLU
- Output Layer = 1
  - Activation Function: Sigmoid


## Hyperparameters
Initial Population = 500
- Genetic Algorithm
  - Generations = 20
  - Mating Pool = 20
- Cultural Algorithm
  - Generations = 20
  - Belief Space Trait = Mean of the Weights < 0.4
- Particle Swarm Optimization
  - Generations = 20
  - w = 0.5
  - c1 = -1
  - c2 = 2
- Ant Colony Optimization
  - Flavour = PACO (Singsathid, P & Wetweerapong, Jeerayut. (2018). Solving Continuous Optimization Problems by Ant Colony Optimization with Domain Partitioning Technique. )
https://www.researchgate.net/publication/339325311_Solving_Continuous_Optimization_Problems_by_Ant_Colony_Optimization_with_Domain_Partitioning_Technique
  - Generations = 20
  - rho = 0.05
  - dec = 0.8
  - inc = 0.4
  - delta = 0.2
  
## Accuracy (Training)
- Genetic Algorithm
  - Accuracy: 0.8769358407079646
![image](https://user-images.githubusercontent.com/87406829/230137213-71151b63-b425-4041-a306-cd9d51f3c135.png)

- Cultural Algorithm
  - Accuracy: 0.8975387168141593
![image](https://user-images.githubusercontent.com/87406829/230137172-babf6a0e-d6bb-4ec6-9d3a-a737203e8708.png)

- Particle Swarm Optimization
  - Accuracy: 0.9325221238938053
![image](https://user-images.githubusercontent.com/87406829/230137319-16993cf3-cf84-4276-b0b3-c1141d8da9a5.png)

- Ant Colony Optimization
  - Accuracy: 0.925608407079646
![image](https://user-images.githubusercontent.com/87406829/230137802-0a3410ed-8faf-4b73-bead-c79071f903e2.png)

  
 ## Classification Report (Testing)
- Genetic Algorithm

|             |precision |   recall | f1-score  | support|
|---|---|---|---|---|
|         0.0   |    0.81   |   0.92    | 0.86   |    771|
|         1.0     |  0.94   |   0.84   |   0.89  |    1037|
|    Accuracy|             |          |    0.88  |    1808|

- Cultural Algorithm

|             |precision |   recall | f1-score  | support|
|---|---|---|---|---|
|         0.0   |    0.87  |   0.91    | 0.89  |    840|
|         1.0     |  0.92   |   0.88   |   0.90  |    968|
|    Accuracy|             |          |    0.90  |    1808|

- Particle Swarm Optimization

|             |precision |   recall | f1-score  | support|
|---|---|---|---|---|
|         0.0   |    0.92   |   0.93    | 0.93   |    863|
|         1.0     |  0.94   |   0.92   |   0.93  |    945|
|    Accuracy|             |          |    0.93  |    1808|

- Ant Colony Optimization

|             |precision |   recall | f1-score  | support|
|---|---|---|---|---|
|         0.0   |    0.95   |   0.91    | 0.93   |    915|
|         1.0     |  0.91   |   0.95   |   0.93  |    893|
|    Accuracy|             |          |    0.93  |    1808|



