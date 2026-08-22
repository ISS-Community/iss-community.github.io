---
title: ISS — DorukNet Data Center Security (Flowzen & Iris)
subtitle: Cloud-Native High-Throughput Network Monitoring & Adaptive Telemetry Pipelines
description: An industry-collaboration project with DorukNet developing Flowzen for real-time traffic monitoring and Iris for adaptive telemetry collection to protect data center infrastructures.
order: 2
active: true
card_image: null
card_title: Data Center Security
external_url: "https://issdatacentersecurity.wordpress.com/"
categories:
    - Flowzen
    - Iris
    - Data Center Security
    - Network Monitoring
    - Kubernetes
---

<div class="project-details">

  <div class="alert alert-info border-primary mb-4 p-3" style="border-left: 4px solid #2563eb; background: #f0f7ff;">
    <strong>Industry Collaboration:</strong> Intelligence Systems and Security Lab (ISSLab) & DorukNet<br>
    <strong>Project Motto:</strong> <em>"Stay Safe in Cyber World, Protect Your Data!"</em><br>
    <strong>Project Website:</strong> <a href="https://issdatacentersecurity.wordpress.com/" target="_blank" rel="noopener noreferrer">issdatacentersecurity.wordpress.com</a>
  </div>

  <h3>Executive Summary & Collaboration Background</h3>
  <p>
    Modern cloud and data center networks face surging bandwidth demands and increasingly sophisticated cyber attacks, including volumetric DrDoS floods, stealthy port scans, and multi-vector spoofing incidents. Conventional network monitoring solutions create significant processing bottlenecks, causing packet loss and blind spots during critical incident response windows.
  </p>
  <p>
    In collaboration with <strong>DorukNet</strong>, the ISS Lab developed a unified defense and telemetry ecosystem comprising two complementary, cloud-native technologies:
  </p>
  <ul>
    <li><strong>Flowzen:</strong> A modular, high-throughput network monitoring and flow analysis platform designed for wire-speed packet inspection.</li>
    <li><strong>Iris:</strong> An adaptive telemetry collection engine dynamically adjusting sampling rates and data granularity based on network threat conditions.</li>
  </ul>

  <hr class="my-4">

  <h3>Flowzen Platform Architecture & Capabilities</h3>
  <p>
    Flowzen addresses the core challenges of scalability and resilience in modern high-bandwidth data center environments:
  </p>
  <ul>
    <li><strong>Real-Time Stream Analytics:</strong> Captures and processes raw packet streams with zero-copy ring buffers, aggregating flow metrics into actionable cybersecurity features with sub-millisecond latency.</li>
    <li><strong>Kubernetes Horizontal Pod Autoscaling (HPA):</strong> The platform dynamically monitors CPU utilization, queue depth, and incoming packet rates. When traffic surges occur, Kubernetes automatically spins up worker pods to distribute ingestion loads.</li>
    <li><strong>Drastic Packet Loss Reduction:</strong> In rigorous benchmark tests simulating large-scale DrDoS and volumetric packet bursts, Flowzen reduced packet loss from <strong>52% down to 2.5%</strong>, ensuring comprehensive visibility even during heavy adversarial congestion.</li>
    <li><strong>Multi-Environment Deployment:</strong> Designed for seamless operation across on-premises bare-metal, hybrid cloud, and multi-tenant data center environments.</li>
  </ul>

  <hr class="my-4">

  <h3>Iris Adaptive Telemetry Pipeline</h3>
  <p>
    To prevent telemetry storage exhaustion while capturing fine-grained attack data:
  </p>
  <ul>
    <li><strong>Dynamic Sampling Rates:</strong> Iris automatically shifts from coarse baseline sampling during normal operational states to ultra-high-resolution, full-packet capture when security anomalies or threshold triggers occur.</li>
    <li><strong>Feature Extraction Pipeline:</strong> Feeds downstream machine learning classifiers (including deep learning IP spoofing detectors and quantized ONNX models) with pre-processed, standardized telemetry vectors.</li>
  </ul>

  <hr class="my-4">

  <h3>Related Publications & Academic Presentations</h3>
  
  <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
    <h5 class="mb-1 font-weight-bold">Flowzen: Modular and Scalable Network Monitoring Platform</h5>
    <p class="text-muted mb-2"><em>Furkan Çetin, Alperen Gültekin, İsmet Kaan Çekiş, Mustafa Özgür, İlker Özçelik</em></p>
    <p class="mb-2" style="font-size: 0.92rem;">
      Presented at the 18th International Conference on Information Security and Cryptology (ISCTURKIYE 2025), Information and Communication Technologies Authority (BTK), Ankara. Published in IEEE Xplore.
    </p>
    <div class="d-flex flex-wrap gap-2">
      <a href="https://lnkd.in/dyp5rjQ2" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm mr-2">
        <i class="fa fa-file-text-o mr-1"></i> IEEE Xplore Paper
      </a>
      <a href="https://www.linkedin.com/posts/ozcelikilker_btk-iaovsctaesrkiye-flowzen-activity-7394380988484665344-IFJS" target="_blank" rel="noopener noreferrer" class="btn btn-outline-dark btn-sm">
        <i class="fa fa-linkedin mr-1"></i> LinkedIn Announcement
      </a>
    </div>
  </div>

  <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
    <h5 class="mb-1 font-weight-bold">IP Spoofing Detection Using Deep Learning</h5>
    <p class="text-muted mb-2"><em>İsmet Kaan Çekiş, Buğra Ayrancı, Fatma Nur Salman, İlker Özçelik</em></p>
    <p class="mb-2" style="font-size: 0.92rem;">
      Applied Sciences, 2025, 15(17), 9508.
    </p>
    <a href="https://doi.org/10.3390/app15179508" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm align-self-start">
      <i class="fa fa-external-link mr-1"></i> Read Article (DOI: 10.3390/app15179508)
    </a>
  </div>

  <hr class="my-4">

  <h3>Project Videos & Technical Seminars</h3>
  <div class="row">
    <div class="col-md-6 mb-3">
      <div class="card h-100 p-3 shadow-sm border">
        <h6 class="font-weight-bold mb-2">Flowzen Traffic Monitoring & HPA Autoscaling Demo</h6>
        <p class="small text-muted mb-3">Demonstration of high-speed packet ingestion, automated worker pod scaling, and real-time anomaly detection under heavy traffic loads.</p>
        <a href="https://www.youtube.com/@isslab_tr/videos" target="_blank" rel="noopener noreferrer" class="btn btn-danger btn-sm mt-auto">
          <i class="fa fa-youtube-play mr-1"></i> Watch Video on YouTube
        </a>
      </div>
    </div>
    <div class="col-md-6 mb-3">
      <div class="card h-100 p-3 shadow-sm border">
        <h6 class="font-weight-bold mb-2">SDN & Data Center Security Seminars</h6>
        <p class="small text-muted mb-3">Research presentations on software-defined networking, large-scale data center defense, and high-throughput telemetry pipelines.</p>
        <a href="https://www.youtube.com/@isslab_tr/videos" target="_blank" rel="noopener noreferrer" class="btn btn-danger btn-sm mt-auto">
          <i class="fa fa-youtube-play mr-1"></i> Watch Video on YouTube
        </a>
      </div>
    </div>
  </div>

  <hr class="my-4">

  <h3>Resources & External Links</h3>
  <ul>
    <li><strong>Project Website:</strong> <a href="https://issdatacentersecurity.wordpress.com/" target="_blank" rel="noopener noreferrer">issdatacentersecurity.wordpress.com</a></li>
    <li><strong>Industry Partner:</strong> <a href="https://www.doruk.net.tr/" target="_blank" rel="noopener noreferrer">DorukNet (doruk.net.tr)</a></li>
    <li><strong>ISSLab Blog:</strong> <a href="https://esoguisslab.wordpress.com/" target="_blank" rel="noopener noreferrer">esoguisslab.wordpress.com</a></li>
  </ul>

</div>
