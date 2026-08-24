---
title: Scalable Edge Authentication Framework
subtitle: TÜBİTAK 3501 — Blockchain & Cryptographic Accumulator-Backed Distributed Authentication
description: A TÜBİTAK 3501-supported project developing a decentralized, ultra-low latency edge authentication framework utilizing cryptographic accumulators and Hyperledger Sawtooth blockchain coordination.
order: 1
active: true
card_image: null
card_title: Edge Authentication
external_url: "https://issedgeauthentication.wordpress.com/"
categories:
    - Blockchain
    - Edge Security
    - Cryptographic Accumulators
    - IoT Security
---

<div class="project-details">

  <div class="alert alert-info border-primary mb-4 p-3" style="border-left: 4px solid #2563eb; background: #f0f7ff;">
    <strong>Funding Program:</strong> TÜBİTAK (The Scientific and Technological Research Council of Turkey) — 3501 Career Development Program<br>
    <strong>Host Institution:</strong> Intelligence Systems and Security Lab (ISSLab), Department of Software Engineering, Eskişehir Osmangazi University<br>
  </div>

  <h3>Research Motivation</h3>
  <p>
    As the Internet of Things (IoT) expands exponentially and software applications transition to distributed microservices architectures, authentication requirements increase dramatically. Traditional centralized authentication systems (such as legacy Public Key Infrastructures, RADIUS, or central OAuth servers) suffer from severe limitations:
  </p>
  <ul>
    <li><strong>Single Point of Failure:</strong> Central authentication servers create vulnerability targets for DDoS attacks and systemic outages.</li>
    <li><strong>Latency Overhead:</strong> Querying remote cloud-hosted authentication servers causes intolerable latency for real-time edge devices and cyber-physical systems.</li>
    <li><strong>Privacy Risks:</strong> Centralized credential repositories aggregate sensitive telemetry and user access patterns.</li>
  </ul>
  <p>
    The <strong>Scalable Edge Authentication Framework</strong> solves these challenges by combining <strong>distributed blockchain coordination</strong> with <strong>cryptographic accumulators</strong>. This enables distributed edge nodes to independently verify authentication credentials locally with constant-size proofs without querying a central authority.
  </p>

  <hr class="my-4">

  <h3>System Architecture & Technical Innovations</h3>
  <p>
    The framework establishes a distributed verification topology designed specifically for resource-constrained edge computing:
  </p>
  <ul>
    <li><strong>Cryptographic Accumulators:</strong> Utilizes dynamic RSA and Elliptic Curve Cryptography (ECC) accumulators to represent large sets of valid device identities as a single, compact mathematical element. Devices present constant-size (O(1)) membership witnesses that can be verified in microseconds.</li>
    <li><strong>Blockchain-Coordinated Trust:</strong> Hyperledger Sawtooth distributed ledger serves as the immutable coordination layer for accumulator state updates, credential revocations, and cross-domain edge policy synchronization.</li>
    <li><strong>Zero-Knowledge Authentication:</strong> Devices verify membership in authorized access groups without exposing device serial numbers or sensitive identity metadata.</li>
    <li><strong>Lightweight Revocation:</strong> Accumulator state transitions allow near-instantaneous credential revocation across all edge clusters without rebuilding the credential database.</li>
  </ul>

  <hr class="my-4">

  <h3>Embedded Hardware Prototyping & Benchmarks</h3>
  <p>
    To validate feasibility on real-world IoT hardware, the ISS Lab team evaluated cryptographic primitive execution and memory footprints on embedded microcontrollers:
  </p>
  <ul>
    <li><strong>Hardware Testbeds:</strong> STM32F4 series microcontrollers and STM STEVAL-IDB008V2 Bluetooth Low Energy (BLE) evaluation boards.</li>
    <li><strong>Library Benchmarks:</strong> Comparative evaluation of lightweight ECC libraries (micro-ecc, mbedTLS, TinyCrypt) for resource-constrained embedded systems.</li>
  </ul>

  <hr class="my-4">

  <h3>Related Publications</h3>
  <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
  <h5 class="mb-1 font-weight-bold">A Code-Based Universal Cryptographic Accumulator</h5>
  <p class="text-muted mb-2"><em>İlker Özçelik</em></p>
  <p class="mb-2" style="font-size: 0.92rem;">
    2025 9th International Symposium on Multidisciplinary Studies and Innovative Technologies (ISMSIT), IEEE, 2025, pp. 1-5.
  </p>
  <a href="https://doi.org/10.1109/ISMSIT67332.2025.11268188" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm align-self-start">
    <i class="fa fa-external-link mr-1"></i> Read Article (DOI)
  </a>
</div>
  
  <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
    <h5 class="mb-1 font-weight-bold">Edge Authentication Using a Cryptographic Accumulator</h5>
    <p class="text-muted mb-2"><em>İsmet Kaan Çekiş, Armağan Toros, Volkan Yiğit, İlker Özçelik</em></p>
    <p class="mb-2" style="font-size: 0.92rem;">
    2025 9th International Symposium on Multidisciplinary Studies and Innovative Technologies (ISMSIT), IEEE, 2025, pp. 1-5.
    </p>
    <a href="https://doi.org/10.1109/ISMSIT67332.2025.11268018" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm align-self-start">
    <i class="fa fa-external-link mr-1"></i> Read Article (IEEE Xplore)
    </a>
    </div>  

    <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
  <h5 class="mb-1 font-weight-bold">Performance Evaluation of ECC Based Cryptographic Accumulator on Resource-Constrained Platform</h5>
      <p class="text-muted mb-2"><em>Armağan Toros, İsmet Kaan Çekiş, Kübra Korkmaz, İlker Özçelik</em></p>
      <p class="mb-2" style="font-size: 0.92rem;">
    2024 Innovations in Intelligent Systems and Applications Conference (ASYU), IEEE, 2024, pp. 1-6.
      </p>
      <a href="https://doi.org/10.1109/ASYU62119.2024.10757120" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm align-self-start">
    <i class="fa fa-external-link mr-1"></i> Read Article (DOI: 10.1109/ASYU62119.2024.10757120)
      </a>
    </div>
  
  <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
    <h5 class="mb-1 font-weight-bold">Performance Comparison of ECC Libraries for IoT Devices</h5>
    <p class="text-muted mb-2"><em>İsmet Kaan Çekiş, Armağan Toros, Nimet Apaydın, İlker Özçelik</em></p>
    <p class="mb-2" style="font-size: 0.92rem;">
      Eskişehir Technical University Journal of Science and Technology A - Applied Sciences and Engineering, 2024, 25(2), pp. 278-288.
    </p>
    <a href="https://doi.org/10.18038/estubtda.1427488" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm align-self-start">
      <i class="fa fa-external-link mr-1"></i> Read Article (DOI: 10.18038/estubtda.1427488)
    </a>
  </div>

  <hr class="my-4">

  <h3>Project Video Archive & Tutorials</h3>
  <p class="text-muted">Direct video tutorials and technical presentations produced under this project:</p>

  <div class="row">
    <div class="col-md-4 mb-3">
      <div class="card h-100 p-3 shadow-sm border">
        <h6 class="font-weight-bold mb-2">ECC Cryptographic Accumulator Library</h6>
        <p class="small text-muted mb-3">Usage of the elliptic curve cryptography accumulator repository, proof generation, and verification.</p>
        <a href="https://www.youtube.com/watch?v=xUDw_yeY8DY" target="_blank" rel="noopener noreferrer" class="btn btn-danger btn-sm mt-auto">
          <i class="fa fa-youtube-play mr-1"></i> Watch Video
        </a>
      </div>
    </div>
    <div class="col-md-4 mb-3">
      <div class="card h-100 p-3 shadow-sm border">
        <h6 class="font-weight-bold mb-2">STM Project Creation & Programming</h6>
        <p class="small text-muted mb-3">STM development kit setup, firmware compilation, and embedded security flashing.</p>
        <a href="https://www.youtube.com/watch?v=a1_-ycF26PE" target="_blank" rel="noopener noreferrer" class="btn btn-danger btn-sm mt-auto">
          <i class="fa fa-youtube-play mr-1"></i> Watch Video
        </a>
      </div>
    </div>
    <div class="col-md-4 mb-3">
      <div class="card h-100 p-3 shadow-sm border">
        <h6 class="font-weight-bold mb-2">STM STEVAL-IDB008V2 Setup</h6>
        <p class="small text-muted mb-3">IDE and toolchain installation tutorial for BLE embedded evaluation boards.</p>
        <a href="https://www.youtube.com/watch?v=ywydD5wqOeU" target="_blank" rel="noopener noreferrer" class="btn btn-danger btn-sm mt-auto">
          <i class="fa fa-youtube-play mr-1"></i> Watch Video
        </a>
      </div>
    </div>
  </div>

</div>
