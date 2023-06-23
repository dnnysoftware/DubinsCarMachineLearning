<a name="readme-top"></a>

[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><<a href="#installation">Installation</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![MY SECURITY CAMERA DEMO](img/demo-screenshot.png)

This Project is supposed to simulate Dubin's car which is used in fields of robotics and control theory in which the algorithm tries to find the path from a start position of the "car" to an end position in a parking lot while avoiding walls. This implementation uses reinforcement learning with genetic algorithms to find generations that approach the goal state and reduce cost doing so. Each generation has randomly generated control vectors and calcuates differential equations with respect to time intervals to find the most ideal next state.

Control Vector u(t) = [γ β]^T:
* γ: heading rate (rad/s)
* β: acceleration (ft/s^2)

State Vector s(t) = [x y a v]^T:
* x: x-position (ft)
* y: y-position (ft)
* a: heading angle (rad)
* v: velocity (ft/s)

ODEs: 
* 𝑥̇ = 𝑣 cos 𝛼 
* 𝑦̇ = 𝑣 sin 𝛼 
* 𝛼̇ = γ
* 𝑣̇ = 𝛽
* 𝐬k+1 =𝐬k + 𝛥t(𝐟(𝐬k,𝐮k,𝑡k))

At Runtime: 
* User has default or updated configurations in config.yaml read
* Generates inital random control vectors population from configuration constraints
* 2D plot is generated showing updated positions of best state in a generation
* Genetic algorithm runs where it converts binary control values to decimal, then uses ODEs (differential equations) to find the next state from the provided control vector, after picks the state with the lowest cost to the next generation and repeats.
* When cost is less than the cost tolerance found in the configuration constraints then a report is generated of the viable control and state vectors and corresponding graphs are shown of each variable with respect to time.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Languages:
* Python
* Shell Script
* YAML

Libraries:
* numpy
* matplotlib
* random
* time
* yaml

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started


### Installation

1.

<p align="right">(<a href="#readme-top">back to top</a>)</p>