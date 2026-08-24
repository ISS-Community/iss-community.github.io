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
    - Data Center Security
    - Network Monitoring
    - Kubernetes
---

<div class="project-details">

  <div class="alert alert-info border-primary mb-4 p-3" style="border-left: 4px solid #2563eb; background: #f0f7ff;">
    <strong>Industry Collaboration:</strong> Intelligence Systems and Security Lab (ISSLab) & DorukNet<br>
    <strong>Project Motto:</strong> <em>"Stay Safe in Cyber World, Protect Your Data!"</em><br>
  </div>

  <h3>Research Motivation</h3>
  <p>
    In high-bandwidth data centers and modern cloud infrastructures, traditional packet-based inspection methods struggle with prohibitive latency and resource overhead. While flow-based approaches like sFlow, NetFlow, and IPFIX provide scalable alternatives, existing open-source monitoring solutions often suffer from severe packet loss and throughput bottlenecks under heavy traffic bursts.
  </p>
  <p>
    The <strong>Flowzen</strong> project was initiated to address these challenges by delivering a resilient, low-latency network telemetry architecture engineered for real-time traffic ingestion, analysis, and automated threat mitigation.
  </p>

  <hr class="my-4">

  <h3>Flowzen Architecture & Technical Innovations</h3>
  <p>
    Flowzen employs a cloud-native, microservices-based streaming pipeline built on Kubernetes to ensure elasticity and multi-protocol flexibility:
  </p>
  <ul>
    <li><strong>Data Ingestion (Producer Layer):</strong> Utilizes multi-threaded concurrency to capture raw sFlow datagrams with minimal overhead and publish them to Apache Kafka.</li>
    <li><strong>Decoupled Streaming Pipeline:</strong> Leverages Apache Kafka as a high-throughput broker to buffer streaming data and prevent consumer bottlenecks.</li>
    <li><strong>Analytics & Storage (Consumer Layer):</strong> Batches processed flow metrics into ClickHouse; a column-oriented database optimized for real-time analytical queries; and tracks system performance via Prometheus and Grafana.</li>
    <li><strong>Elastic Autoscaling:</strong> Integrates Horizontal Pod Autoscaling (HPA) to dynamically scale consumer instances under heavy load.</li>
  </ul>



  <hr class="my-4">

  <h3>Machine Learning \& Graph Intelligence Integration</h3>
  <p>
    To equip Flowzen with proactive anomaly detection capabilities, extensive empirical research was conducted on model efficiency and graph learning in high-throughput environments:
  </p>
  <ul>
    <li><strong>High-Throughput & Low-Latency Inference:</strong> Deep learning models (MLP, 1D-CNN, GRU, LSTM) were optimized using Open Neural Network Exchange (ONNX) conversion and 8-bit integer post-training quantization (PTQ). Benchmarked on datasets such as CIC-DDoS2019, these models achieved sub-microsecond per-sample inference times for IP spoofing and DrDoS/DNS amplification detection with over 99% accuracy.</li>
    <li><strong>Graph Neural Networks (GNNs) for Relational Threat Detection:</strong> By modeling DNS query interactions (TI-16 dataset) as client-domain heterogeneous graphs, models such as HeteroSAGE and HeteroGAE successfully detected centrally managed botnet nodes with up to 95% accuracy and exceptionally high recall.</li>
  </ul>
  <p>
    Ongoing engineering efforts focus on embedding these optimized ONNX engines and GNN models directly into Flowzen's runtime pipeline.
  </p>


    <hr class="my-4">

  <h3>Platform Vision & Extensibility</h3>
  <p>
    Flowzen employs a cloud-native, microservices-based streaming pipeline built on Kubernetes to ensure elasticity and multi-protocol flexibility:
  </p>
  <ul>
    <li><strong>Data Ingestion (Producer Layer):</strong> Utilizes multi-threaded concurrency to capture raw sFlow datagrams with minimal overhead and publish them to Apache Kafka.</li>
    <li><strong>Decoupled Streaming Pipeline:</strong> Leverages Apache Kafka as a high-throughput broker to buffer streaming data and prevent consumer bottlenecks.</li>
    <li><strong>Analytics & Storage (Consumer Layer):</strong> Batches processed flow metrics into ClickHouse; a column-oriented database optimized for real-time analytical queries; and tracks system performance via Prometheus and Grafana.</li>
    <li><strong>Elastic Autoscaling:</strong> Integrates Horizontal Pod Autoscaling (HPA) to dynamically scale consumer instances under heavy load.</li>
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

 </div>
