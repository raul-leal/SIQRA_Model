# SIQRA_Model
Analysis of the SIQRA model for computer virus behavior on networks.

# Introduction
Kermack and McKendrick developed the SIR (Susceptible-Infected-Removed) model for modeling biological viruses in 1920. Since then, many other models have been developed from the original SIR and adapted to model the behavior of computer viruses due to its similarity with biological viruses. One of these models is the SIQRA (Susceptible-Infected-Quarantine-Removed-Antidotal), developed in [3].

<p align="center">
<img src = "https://github.com/user-attachments/assets/5606bbf3-7acf-4619-b64e-ff1daef18187">
</p>

Two SIQRA models were developed for that paper, with Model 2 having a non-linear IQ term. The equations were as follow:

Model 1                                                       | Model 2 | 
--------------------------------------------------------------| ---------- | 
$\dot{S} = -\alpha_{SA} S A - \beta S I + \sigma R + \omega Q,$| $\dot{S} = -\alpha_{SA} S A - \beta S I + \sigma R + \omega Q,$ | 
$\dot{I} = \beta S I - \alpha_{IA} A I - \delta Q I,$  | $\dot{I} = \beta S I - \alpha_{IA} A I - \delta Q I,$  | 
$\dot{Q} = \delta I - \omega Q - \alpha_{QA} Q - \alpha Q,$ | $\dot{Q} = \delta Q I - \omega Q - \alpha_{QA} Q - \alpha Q,$   |
$\dot{R} = \alpha Q - \sigma R, $ | $\dot{R} = \alpha Q - \sigma R, $    |
$\dot{A} = \alpha_{SA} S A + \alpha_{IA} A I + \alpha_{QA} Q A.$|   $\dot{A} = \alpha_{SA} S A + \alpha_{IA} A I + \alpha_{QA} Q A.$ |

This work aimed to test the stability of this model through simulations with a population of 100 nodes.

# Analysis of the SIQRA Model
Firstly, a manual variation of the initial conditions and parameters was done in order to achieve significant changes in the network's behavior. After these checks, a modeling of the SIQRA network was performed, where all parameters varied from 0.1 to 1.0, aiming for a more in-depth analysis of the influence of each parameter on the final state of the SIQRA network. These tests concluded that the network in question is stable for all possible variations if the model used does not include a nonlinear IQ term, and can be safely implemented in real computer networks. For the model with a nonlinear IQ term, the necessity of an initial population of at least one antidote or quarantine node was proven.

<p align="center">
<img src="https://github.com/user-attachments/assets/79e85f04-f4ea-4ac1-baf1-13b637c61526">
<br> The above figure shows an example of parameter variation.
</p>


<p align="center">
<img src = "https://github.com/user-attachments/assets/dcbb0c6a-69ab-412e-919d-f33204bdaa54">
<br>Example of a type 2 network with an initial population of 99 susceptibles and 1 infected tending towards an endemic final state.
</p>



# References
[1] KERMAKC, W.O.; MCKENDRICK, A.G.; A contribution to the mathematical theory of epidemics. _Proceedings of the Royal Society of London. Series A, Containing papers of mathematical and physical character_, 115(772), p. 700-721, 1927.

[2] KERMACK, W.O.; MCKENDRICK, A.G.; Contributions to the mathematical theory of epidemics. II.-The problem of endemicity. _Proceedings of the Royal Society of London. Series A, containing papers of mathematical and physical character_, 138(834), p. 55-83, 1932.

[3] PIQUEIRA, J.R.C.; BATISTELA, C.M.; Considering quarantine in the SIRA malware propagation model. _Mathematical Problemns in Engineering_, 2019, p. 1-8, 2019.
