---
title: Blockchain-Based Efficient Audit Trail Framework
subtitle: Cryptographic Accumulator and Hyperledger Sawtooth-Backed Verifiable Audit Architecture
description: A decentralized, scalable audit trail framework integrating IPFS, Sawtooth distributed ledger, and dynamic RSA cryptographic accumulators to achieve constant-time O(1) audit verification.
order: 4
active: true
card_image: null
card_title: BC Audit Trails
external_url: 
categories:
    - Blockchain
    - Audit Trails
    - Cryptographic Accumulators
    - Decentralized Storage
---

<div class="project-details">

  <div class="alert alert-info border-primary mb-4 p-3" style="border-left: 4px solid #2563eb; background: #f0f7ff;">
    <strong>Research Focus:</strong> Designing a scalable, tamper-proof, and constant-time verification framework for enterprise and financial audit trails by integrating decentralized storage with dynamic cryptographic accumulators.<br>
    <strong>Funding / Collaboration:</strong> Intelligent Systems Security Lab (ISSLab)<br>
    <strong>Academic Supervision and Institutional Context:</strong> Intelligent Systems Security Lab (ISSLab), Eskisehir Osmangazi University (M.Sc. Thesis: Bilal S. T. Alagha; Advisor: Dr. İlker Özçelik).<br>
  </div>

  <h3>Research Motivation</h3>
  <p>
    An audit trail provides a chronological record of system activities, serving as a foundational mechanism for regulatory compliance, fraud detection, and data governance in financial and enterprise systems. However, conventional audit trail systems face critical structural limitations:
  </p>
  <ul>
    <li><strong>Centralized Vulnerability and Single Points of Failure:</strong> Centralized databases are susceptible to operational failures, unauthorized access, and internal tampering, compromising the integrity of audit records.</li>
    <li><strong>High Cost and Latency:</strong> Manual and legacy auditing workflows are labor-intensive, costly, and lack real-time verification capabilities, often allowing financial fraud to remain undetected for long periods. High-profile corporate failures and global occupational fraud losses highlight the urgent need for verifiable audit mechanisms.</li>
    <li><strong>Blockchain Search and Scalability Bottlenecks:</strong> While distributed ledgers provide immutability, retrieving and verifying specific records within growing blockchains becomes computationally expensive. Standard linear traversal incurs severe time delays, while external database indexing introduces synchronization overhead and trust verification issues.</li>
  </ul>
  <p>
    The <strong>Blockchain-Based Efficient Audit Trail Framework</strong> resolves these challenges by narrowing the operational scope from broad search to precise, constant-time verification. By pairing <strong>InterPlanetary File System (IPFS)</strong> off-chain storage with <strong>Hyperledger Sawtooth</strong> coordination and <strong>dynamic RSA cryptographic accumulators</strong>, the architecture allows auditors to verify document inclusion with constant-size mathematical proofs without traversing the blockchain ledger.
  </p>

  <hr class="my-4">

  <h3>System Architecture and Technical Innovations</h3>
  <p>
    The framework establishes a dual on-chain/off-chain topology designed to maintain data confidentiality, storage efficiency, and high-throughput verification:
  </p>
  <ul>
    <li><strong>Dynamic RSA Cryptographic Accumulators:</strong> Represents large sets of document and transaction hashes as a single, fixed-size mathematical accumulator value stored in the global blockchain state. Individual elements are verified in constant O(1) time and space using compact membership witnesses, avoiding full-ledger downloads.</li>
    <li><strong>Decentralized Content Storage (IPFS):</strong> Large audit documents are stored off-chain across an IPFS peer-to-peer network and addressed via cryptographic Content Identifiers (CIDs). This ensures data availability, content addressing, and tamper detection while keeping on-chain transaction payloads lightweight.</li>
    <li><strong>Off-Chain Coordination Layer:</strong> An intermediary off-chain service manages company accounts, maps accumulator state transitions, updates membership witnesses dynamically, and isolates the underlying blockchain from unauthorized access.</li>
    <li><strong>Sawtooth Blockchain Integration:</strong> Utilizes the modular Splinter/Sawtooth distributed ledger platform with custom transaction processors and Practical Byzantine Fault Tolerance (PBFT) consensus to enforce state validation and maintain tamper-proof accumulator histories.</li>
  </ul>

  <hr class="my-4">

  <h3>Experimental Benchmarks and Comparative Evaluation</h3>
  <p>
    The framework was implemented and evaluated on a multi-node testbed running Splinter Community Sawtooth v1.2 with PBFT consensus on Linux Ubuntu (AMD Ryzen 3 processor, 6+ GB RAM). Performance was systematically benchmarked against existing transaction retrieval methods:
  </p>
  <ul>
    <li><strong>Linear Blockchain Traversal:</strong> Requires downloading all block transactions, resulting in linear O(n) download and CPU search times. Memory saturation and swap-space activation occurred after approximately 22,000 transactions, leading to severe performance degradation.</li>
    <li><strong>Platform-Specific Search:</strong> Sawtooth native node queries exhibited unpredictable latency profiles and induced node disconnections under high transaction loads exceeding 20,000 requests.</li>
    <li><strong>Relational Database Indexing:</strong> Relational B-tree structures achieved logarithmic O(log n) search performance but required secondary database synchronization and introduced independent data integrity verification burdens.</li>
    <li><strong>RSA Cryptographic Accumulator Approach:</strong> Achieved strictly constant O(1) computational, communication, and storage complexity during membership verification, demonstrating robust scalability regardless of dataset expansion.</li>
  </ul>

  <hr class="my-4">

  <h3>Core Research Contributions and Practical Implications</h3>
  <ul>
    <li><strong>Constant-Complexity Verification:</strong> Proved that RSA-based dynamic accumulators reduce audit verification complexity to O(1), enabling rapid verification in high-volume enterprise environments.</li>
    <li><strong>Hybrid Architecture Scalability:</strong> Combined decentralized IPFS storage with on-chain accumulator states to eliminate ledger bloat while maintaining end-to-end provenance.</li>
    <li><strong>Cross-Domain Applicability:</strong> Established a verification foundation adaptable to financial recordkeeping, healthcare data audits (EHR), IoT smart metering, and supply chain tracking.</li>
  </ul>

  <hr class="my-4">

  <h3>Related Publications & Academic Presentations</h3>
  <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
    <h5 class="mb-1 font-weight-bold">A Blockchain-Based Efficient Audit Trail Framework</h5>
    <p class="text-muted mb-2"><em>Bilal S. T. Alagha (Author), Dr. İlker Özçelik (Supervisor)</em></p>
    <p class="mb-2" style="font-size: 0.92rem;">
      Master of Science Thesis, Department of Computer Engineering, Eskisehir Osmangazi University Graduate School of Natural and Applied Sciences, December 2024.
    </p>
  </div>

   <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
    <h5 class="mb-1 font-weight-bold">BEATS: Practical Audit Trail in Blockchain Systems</h5>
    <p class="text-muted mb-2"><em>Bilal Alagha, İlker Özçelik</em></p>
    <p class="mb-2" style="font-size: 0.92rem;">
      IEEE Access, 2025, Vol. 13, pp. 38120-38135.
    </p>
    <a href="https://doi.org/10.1109/ACCESS.2025.3582722" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm align-self-start">
      <i class="fa fa-external-link mr-1"></i> Read Article (DOI: 10.1109/ACCESS.2025.3582722)
    </a>
   </div>

   <div class="card p-3 mb-3 bg-light border-0 shadow-sm">
     <h5 class="mb-1 font-weight-bold">An Empirical Evaluation of Blockchain Transaction Search Methods</h5>
     <p class="text-muted mb-2"><em>Bilal Alagha, İlker Özçelik</em></p>
     <p class="mb-2" style="font-size: 0.92rem;">
       Presented at the AVRASYA 11th International Conference on Applied Sciences, 2024.
     </p>
     <div class="d-flex flex-wrap gap-2">
       <a href="https://www.researchgate.net/publication/387930981_AN_EMPIRICAL_EVALUATION_OF_BLOCKCHAIN_TRANSACTION_SEARCH_METHODS" target="_blank" rel="noopener noreferrer" class="btn btn-outline-primary btn-sm mr-2">
         <i class="fa fa-file-text-o mr-1"></i> ResearchGate Publication
       </a>
     </div>
</div>

</div>
