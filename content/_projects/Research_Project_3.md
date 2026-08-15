---
title: Iris — Adaptive Telemetry & Data Collection Pipeline
subtitle: Dynamic data granularity & intelligent telemetry for resilient clouds
description: Iris is an adaptive telemetry and data collection system that dynamically adjusts sampling rates and data granularity based on network conditions and security threats.
order: 3
active: true
card_image: null
card_title: Iris Telemetry
external_url: "https://issdatacentersecurity.wordpress.com/"
categories:
    - Iris
    - Telemetry
    - Cloud Infrastructure
    - Data Center Security
---

<h4>Project Overview</h4>

Developed in collaboration with **DorukNet**, **Iris** serves as the adaptive telemetry and data ingestion pipeline for resilient data center management. Maintaining fine-grained telemetry across tens of thousands of server nodes creates unsustainable storage and network overhead during quiet periods.

Iris solves this with an adaptive control loop that dynamically scales data collection resolution: during baseline operations it maintains lightweight statistical summaries, and automatically switches to high-fidelity deep packet telemetry upon detecting anomalous flow triggers.

**Project Page:** [issdatacentersecurity.wordpress.com](https://issdatacentersecurity.wordpress.com/)

#### Key Research Areas & Architecture

- **Adaptive Sampling Algorithms**: Threat-aware dynamic adjustments to telemetry resolution.
- **Resource-Constrained Optimization**: Minimizing CPU/memory overhead on host virtual machines and containers.
- **Unified Security Pipeline**: Seamless integration with Flowzen for coordinated detection and response.
- **Real-Time Analytics Integration**: Providing low-latency training and inference datasets for AI anomaly engines.
