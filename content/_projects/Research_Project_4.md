---
title: Adversarial Attack Detection & Mitigation
subtitle: Real-Time Mitigation of Adversarial Attacks for Secure AI Systems in Digital Twins
description: A defense-industry supported project designing high-fidelity digital twin simulation environments, Graph Neural Network (GNN) anomaly detectors, and quantized ONNX models to protect critical cyber-physical systems.
order: 3
active: true
card_image: null
card_title: "AI Security"
external_url: 
categories:
    - AI Security
    - Graph Learning
    - Critical Infrastructure
---

<div class="project-details">

  <div class="alert alert-info border-primary mb-4 p-3" style="border-left: 4px solid #2563eb; background: #f0f7ff;">
    <strong>Research Focus:</strong> Intelligent Systems Security & Cyber-Physical Infrastructure Protection<br>
    <strong>Host Institution:</strong> Intelligence Systems and Security Lab (ISSLab), Eskişehir Osmangazi University<br>
    <strong>Research Portal:</strong> <a href="https://esoguiss.wordpress.com/intelligent-systems/" target="_blank" rel="noopener noreferrer">esoguiss.wordpress.com/intelligent-systems/</a>
  </div>

<p>
This project constitutes a core security initiative within a broader Digital Twin ecosystem framework. As Artificial Intelligence (AI) and Deep Learning (DL) models become increasingly vital across critical infrastructures, defense systems, autonomous operations, and industrial networks, their exposure to adversarial threats poses severe risks. Adversarial attacks manipulate input features via imperceptible perturbations to deceive AI models, leading to misclassification, performance degradation, and compromised decision-making.
</p>

<p>
To guarantee the reliability, integrity, and resilience of AI components embedded within the Digital Twin environment, this research focuses on developing a robust, high-generalizability, and real-time framework to detect, explain, and mitigate adversarial attacks targeting deep learning systems.
</p>

  <h3>Executive Summary & Research Motivation</h3>
  <p>
    Mission-critical infrastructures (including power grids, telecommunication cores, transportation networks, and defense communications) require continuous uptime and zero-tolerance for service interruption. As these systems incorporate autonomous decision-making and machine learning components, they become exposed to complex, multi-stage cyber attacks and adversarial manipulation.
  </p>
  <p>
    Deploying untested defensive countermeasures directly onto live infrastructure risks unintended service disruption. The <strong>Digital Twin Based Smart Attack Detection</strong> project addresses this dilemma by pairing live networks with <strong>high-fidelity digital replicas (Digital Twins)</strong>. This allows security operators to simulate attack trajectories, evaluate AI robustness, and test proactive defense countermeasures safely before operational deployment.
  </p>

  <hr class="my-4">

  <h3>Core Technical Innovations & Methodologies</h3>
  
  <h4>1. High-Fidelity Digital Twin Simulation</h4>
  <p>
    Maintains real-time topological and state synchronization between physical network assets and virtual digital replicas. Security analysts can inject synthetic zero-day exploits, analyze attack propagation across virtual network segments, and evaluate automated response playbooks without impacting production traffic.
  </p>

  <h4>2. Graph Neural Networks (GNN) for Botnet Detection</h4>
  <p>
    Traditional intrusion detection inspects isolated packets or single-device flow records. ISS Lab explores graph representation learning to model topological interactions across entire networks, identifying coordinated botnet command-and-control (C2) communication patterns and compromised nodes with high resilience against evasion techniques.
  </p>

  <h4>3. Ultra-Low Latency Inference via Quantized ONNX Models</h4>
  <p>
    To protect resource-constrained edge gateways against volumetric Distributed Reflection Denial of Service (DrDoS) attacks, the team develops integer-quantized (INT8) ONNX deep learning models that achieve microsecond inference latency while matching the classification accuracy of full-precision neural networks.
  </p>

  <h4>4. Adversarial Machine Learning & Robustness Metrics</h4>
  <p>
    Investigates how adversarial perturbations deceive intelligent classifiers and develops formal robustness metrics to guarantee dependability in mission-critical deployments.
  </p>

  <hr class="my-4">

  <h3>Related Publications</h3>

  <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
    <h5 class="mb-1 font-weight-bold">High-Throughput and Low-Latency DrDoS Detection Using Quantized ONNX Models</h5>
    <p class="text-muted mb-2"><em>Salih Eren, Alperen Gültekin, Ömer Özkan, İlker Özçelik</em></p>
    <p class="mb-2" style="font-size: 0.92rem;">
      Symmetry, 2026, 18(7), 1187.
    </p>
    <a href="https://doi.org/10.3390/sym18071187" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm align-self-start">
      <i class="fa fa-external-link mr-1"></i> Read Article (DOI: 10.3390/sym18071187)
    </a>
  </div>

  <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
    <h5 class="mb-1 font-weight-bold">Botnet Node Detection Using Graph Learning</h5>
    <p class="text-muted mb-2"><em>Gizem Karyağdı, İlker Özçelik</em></p>
    <p class="mb-2" style="font-size: 0.92rem;">
      Applied Sciences, 2025, 16(1), 24.
    </p>
    <a href="https://doi.org/10.3390/app16010024" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm align-self-start">
      <i class="fa fa-external-link mr-1"></i> Read Article (DOI: 10.3390/app16010024)
    </a>
  </div>

  <hr class="my-4">

  <h3>Project Seminars & Technical Webcasts</h3>
  <div class="row">
    <div class="col-md-6 mb-3">
      <div class="card h-100 p-3 shadow-sm border">
        <h6 class="font-weight-bold mb-2">Adversarial Attacks on Graph Neural Networks</h6>
        <p class="small text-muted mb-3">Graduate seminar discussing adversarial attack mechanisms on GNNs, perturbation strategies, and defensive graph learning techniques.</p>
        <a href="https://www.youtube.com/watch?v=tXkzQgZWeT8" target="_blank" rel="noopener noreferrer" class="btn btn-danger btn-sm mt-auto">
          <i class="fa fa-youtube-play mr-1"></i> Watch Video on YouTube
        </a>
      </div>
    </div>
    <div class="col-md-6 mb-3">
      <div class="card h-100 p-3 shadow-sm border">
        <h6 class="font-weight-bold mb-2">LLM Security in Enterprise Networks</h6>
        <p class="small text-muted mb-3">Technical presentation analyzing security implications, privacy leak vectors, and defensive hardening for LLM deployments.</p>
        <a href="https://www.youtube.com/watch?v=gYtPo_axz_E" target="_blank" rel="noopener noreferrer" class="btn btn-danger btn-sm mt-auto">
          <i class="fa fa-youtube-play mr-1"></i> Watch Video on YouTube
        </a>
      </div>
    </div>
  </div>

  <hr class="my-4">

  <h3>Resources & External Links</h3>
  <ul>
    <li><strong>Intelligent Systems Research:</strong> <a href="https://esoguiss.wordpress.com/intelligent-systems/" target="_blank" rel="noopener noreferrer">esoguiss.wordpress.com/intelligent-systems/</a></li>
    <li><strong>Next-Generation Networking:</strong> <a href="https://esoguiss.wordpress.com/networking/" target="_blank" rel="noopener noreferrer">esoguiss.wordpress.com/networking/</a></li>
    <li><strong>YouTube Video Archive:</strong> <a href="https://www.youtube.com/@isslab_tr/videos" target="_blank" rel="noopener noreferrer">@isslab_tr</a></li>
  </ul>

</div>
