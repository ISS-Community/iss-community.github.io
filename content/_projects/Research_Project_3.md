---
title: Advanced Black-Box Adversarial Attack for Machine Learning Models
subtitle: Hybrid Generative Adversarial Attack
description: A PyTorch-based adversarial framework integrating Genetic Algorithms and Multi-Objective Evolutionary Algorithms with Generative Adversarial Networks to evaluate machine learning robustness against black-box adversarial attack.
order: 5
active: true
card_image: null
card_title: Adversarial Attack
permalink: /projects/black-box-adversarial-attack/
status: ongoing
external_url: 
categories:
    - Adversarial Attack
    - Black-Box Attack
    - Generative Adversarial Networks
    - Evolutionary Computation
    - Network Security
---

<div class="project-details">

  <div class="alert alert-info border-primary mb-4 p-3" style="border-left: 4px solid #2563eb; background: #f0f7ff;">
    <strong>Research Focus:</strong> Developing a hybrid optimization framework integrating Generative Adversarial Networks, Genetic Algorithms, and Multi-Objective Evolutionary Algorithms for effective and stealthy adversarial perturbation generation.<br>
    <strong>Funding / Collaboration:</strong> Intelligent Systems Security Lab (ISSLab)<br>
    <strong>Academic Supervision and Institutional Context:</strong> Intelligent Systems Security Lab (ISSLab), Eskisehir Osmangazi University (M.Sc. Thesis: Aybüke Kılıç; Advisor: Dr. İlker Özçelik).<br>
  </div>

  <h3>Research Motivation</h3>
  <p>
    Machine learning (ML) models are extensively deployed across critical cybersecurity applications, including Network Intrusion Detection Systems (NIDS), malware classification, and automated threat monitoring. Despite their high empirical accuracy, these models exhibit profound vulnerability to adversarial attacks: carefully crafted, imperceptible perturbations designed to induce misclassification while evading operational detection.
  </p>
  <p>
    Existing adversarial sample generation methodologies face significant architectural and practical limitations:
  </p>
  <ul>
    <li><strong>Gradient Dependency and Black-Box Constraints:</strong> Classical gradient-based techniques (such as FGSM, PGD, and Carlini-Wagner) require full white-box access to target model gradients, rendering them ineffective in realistic black-box deployment environments where only query outputs are accessible.</li>
    <li><strong>Susceptibility to Local Optima:</strong> Gradient-descent optimization trajectories frequently converge to sub-optimal local extrema, limiting the diversity and potency of generated adversarial vectors.</li>
    <li><strong>Training Instabilities in Standard GANs:</strong> While Generative Adversarial Networks (GANs) offer a generative alternative, standard gradient-trained GANs suffer from mode collapse, vanishing gradients, and training divergence.</li>
    <li><strong>Stealth versus Efficacy Trade-Off:</strong> Generating perturbations that maximize classification error while strictly adhering to geometric distance constraints (such as L2 norm boundaries) requires multi-faceted optimization across competing objectives.</li>
  </ul>
  <p>
    To resolve these challenges, this research introduces an advanced adversarial architecture combining <strong>Generative Adversarial Networks (GANs)</strong> with <strong>Evolutionary Computation (EC)</strong>. By integrating global population search mechanics with gradient-based local convergence, the framework synthesizes highly potent adversarial perturbations under strict stealth constraints.
  </p>

  <hr class="my-4">

  <h3>System Architecture & Technical Innovations</h3>
  <p>
    The architecture establishes a two-phase hybrid optimization pipeline implemented in PyTorch with CUDA GPU acceleration:
  </p>
  <ul>
    <li><strong>Two-Phase Hybrid Optimization Pipeline:</strong> The network executes an initial Phase 1 consisting of initial Adam optimization to establish baseline representation learning, followed by Phase 2 comprising 50 generations of hybrid evolutionary optimization.</li>
    <li><strong>GA-Driven Generator Optimization:</strong> The generator network is evolved via Genetic Algorithms (GA). This population-based global search navigates complex loss landscapes and prevents premature convergence.</li>
    <li><strong>MOEA-Guided Discriminator Evolution:</strong> The discriminator network is optimized using the Non-dominated Sorting Genetic Algorithm II (NSGA-II). It concurrently evaluates Pareto-optimal trade-offs across attack effectiveness, perturbation diversity, and stealth scoring.</li>
    <li><strong>Standardized Evolutionary Operators:</strong> To guarantee experimental reproducibility, the framework applies uniform crossover, Gaussian mutation, tournament selection, and elitist replacement.</li>
    <li><strong>Strict L2 Norm Bounding:</strong> Perturbations are strictly constrained to an L2 norm upper bound of epsilon = 0.1, ensuring generated network traffic modifications remain statistically imperceptible and preserve feature integrity.</li>
  </ul>

  <hr class="my-4">

  <h3>Experimental Setup & Benchmarks</h3>
  <p>
    The framework was systematically evaluated on the UNSW-NB15 network intrusion dataset, comprising 257,673 network traffic records (175,341 training and 82,332 testing samples) across 10 distinct attack categories (Normal, Generic, Exploits, Fuzzers, DoS, Reconnaissance, Analysis, Backdoor, Shellcode, and Worms). Categorical attributes were processed via One-Hot Encoding and numerical features via StandardScaler, producing a 195-dimensional input space.
  </p>
  <p>
    Adversarial perturbations were evaluated against a reference Random Forest classifier (100 decision trees) trained on the UNSW-NB15 feature distribution.
  </p>

  <ul>
    <li><strong>Superior Attack Potency:</strong> The proposed hybrid approach degraded classifier accuracy from 64.43% down to 34.61%, achieving an absolute accuracy drop of 29.82%. This represents a 633% increase in attack effectiveness over the standard Adam-optimized GAN baseline.</li>
    <li><strong>Rigorous Perturbation Control:</strong> Across all evaluated configurations, average L2 norm perturbation magnitudes remained exactly at the target constraint threshold (0.100), proving that enhanced attack success was driven by structural perturbation quality rather than increased noise volume.</li>
    <li><strong>GPU Acceleration Benefits:</strong> Deploying PyTorch tensor operations with CUDA 11.8 on dedicated GPU hardware reduced population evaluation runtimes from over 24 hours (CPU-bound) to practical operational timeframes.</li>
  </ul>

  <hr class="my-4">

  <h3>Security Implications & Red Team Applications</h3>
  <p>
    The empirical results have substantial implications for machine learning security and cybersecurity operations:
  </p>
  <ul>
    <li><strong>Proactive Red Teaming:</strong> The hybrid GAN framework serves as an automated Red Team utility, discovering latent architectural vulnerabilities in machine learning classifiers prior to production deployment.</li>
    <li><strong>Blue Team Defense Enhancement:</strong> Generating diverse, Pareto-optimal adversarial distributions provides critical training telemetry for developing resilient Blue Team countermeasures, including robust adversarial training and anomaly detection filters.</li>
    <li><strong>Cross-Domain Applicability:</strong> The gradient-free evolutionary generator architecture establishes a reliable paradigm for black-box vulnerability assessments in complex, multi-modal cyber-physical systems.</li>
  </ul>

  <hr class="my-4">

  <h3>Related Publications & Academic Presentations</h3>
  <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
    <h5 class="mb-1 font-weight-bold">Advanced Adversarial Attack Architecture for Machine Learning Models</h5>
    <p class="text-muted mb-2"><em>Aybüke Kılıç (Author), Dr. İlker Özçelik (Supervisor)</em></p>
    <p class="mb-2" style="font-size: 0.92rem;">
      Master of Science Thesis, Department of Computer Engineering, Eskisehir Osmangazi University Graduate School of Natural and Applied Sciences, August 2025.
    </p>
  </div>

  <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
    <h5 class="mb-1 font-weight-bold">Enhancing Minority Class Detection in Intrusion Detection Systems Using GAN-Based Data Augmentation: A Heuristic Study</h5>
    <p class="text-muted mb-2"><em>Aybüke Kılıç, İlker Özçelik</em></p>
    <p class="mb-2" style="font-size: 0.92rem;">
      Published in 2025.
    </p>
  </div>
</div>
