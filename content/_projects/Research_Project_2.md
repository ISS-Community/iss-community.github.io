---
title: Flowzen — Modular & Scalable Network Monitoring Platform
subtitle: Real-time traffic monitoring & autoscaling stream analytics
description: Flowzen is a modular, high-throughput network monitoring platform utilizing streaming architectures and Horizontal Pod Autoscaling (HPA) to analyze high-speed enterprise traffic and detect cyber attacks.
order: 2
active: true
card_image: null
card_title: Flowzen Platform
external_url: "https://issdatacentersecurity.wordpress.com/"
categories:
    - Flowzen
    - Network Monitoring
    - Stream Analytics
    - Data Center Security
---

<h4>Project Overview</h4>

Developed within the **ISS — DorukNet Data Center Security Project**, **Flowzen** is a modern, modular, and cloud-native network traffic monitoring platform designed for high-bandwidth data center environments. Traditional monitoring tools often suffer from high latency and severe packet loss under sudden traffic bursts.

Flowzen overcomes these limitations by coupling a real-time streaming pipeline with **Kubernetes Horizontal Pod Autoscaling (HPA)**. In stress tests and live data center deployments, Flowzen drastically reduced packet loss from 52% to 2.5% under high-volume volumetric attacks while providing microsecond flow-level visibility.

**Project Page:** [issdatacentersecurity.wordpress.com](https://issdatacentersecurity.wordpress.com/)

#### Key Research Areas & Architecture

- **High-Throughput Packet Processing**: Zero-copy packet capture and wire-speed flow aggregation.
- **Horizontal Pod Autoscaling (HPA)**: Dynamic worker scaling based on real-time traffic volume and CPU utilization.
- **Stream Analytics**: Real-time feature extraction for machine learning and anomaly detection models.
- **Attack Detection Integration**: Native feeds to DrDoS, Botnet, and IP spoofing classifiers.

#### Key Publications

- Çetin F., Gültekin A., Çekiş İ. K., Özgür M., Özçelik İ., *"Flowzen: Modular and Scalable Network Monitoring Platform"*, 18th International Conference on Information Security and Cryptology (ISCTurkiye), 2025.
