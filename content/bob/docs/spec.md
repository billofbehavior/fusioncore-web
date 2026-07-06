---
title: "SBoB specification — v0.0.1"
weight: 20
type: "docs"
draft: false
---

<style>
/* Re-uses the .spec-doc styling from spec-stackprofile-v0.0.1.md.
   Both pages keep their own style block so neither depends on the other. */
.spec-doc { max-width: 880px; margin: 0 auto; line-height: 1.65; color: #0a0a0a; }
.spec-doc h2 { font-size: 1.55rem; margin: 2.4rem 0 0.6rem; padding-top: 0.8rem; border-top: 1px solid #e6e2d6; letter-spacing: -0.01em; }
.spec-doc h3 { font-size: 1.18rem; margin: 1.8rem 0 0.4rem; color: #0a0a0a; }
.spec-doc h4 { font-size: 1rem; margin: 1.2rem 0 0.3rem; font-weight: 700; color: #2a2a2a; }
.spec-doc h2:first-child, .spec-doc h2.no-rule { border-top: 0; padding-top: 0; }
.spec-doc p, .spec-doc li { font-size: 0.98rem; }
.spec-doc strong { color: #0a0a0a; }
.spec-doc code { background: #f6f4ee; padding: 0.08em 0.36em; border-radius: 3px; font-size: 0.92em; color: #0a0a0a; border: 1px solid #ece6d2; }
.spec-doc pre  { background: #0a0a0a; color: #f4f4f4; padding: 1rem 1.1rem; border-radius: 6px; overflow-x: auto; font-size: 0.86rem; line-height: 1.55; }
.spec-doc pre code { background: transparent; border: 0; padding: 0; color: inherit; font-size: inherit; }
.spec-doc table { width: 100%; border-collapse: collapse; margin: 1rem 0 1.4rem; font-size: 0.92rem; }
.spec-doc th, .spec-doc td { text-align: left; padding: 0.55rem 0.7rem; border-bottom: 1px solid #e6e2d6; vertical-align: top; }
.spec-doc th { background: #faf8f1; font-weight: 700; color: #1c2030; border-bottom: 2px solid #C3A50D; }
.spec-doc tr:hover td { background: #fcfbf6; }
.spec-doc blockquote { border-left: 3px solid #C3A50D; background: #fff5d6; padding: 0.7rem 1rem; margin: 1rem 0; color: #2a2a2a; }
.spec-doc blockquote.warn { border-left-color: #D43F5B; background: #fdecef; }
.spec-doc blockquote p:last-child { margin-bottom: 0; }
.spec-doc .status {
  display: grid; grid-template-columns: max-content 1fr; gap: 0.4rem 1.1rem;
  background: #faf8f1; border-left: 4px solid #C3A50D; padding: 0.9rem 1.1rem;
  margin: 0 0 1.6rem; font-size: 0.92rem; border-radius: 3px;
}
.spec-doc .status dt { font-weight: 700; color: #6a4f00; }
.spec-doc .status dd { margin: 0; }
.spec-doc .toc { background: #faf8f1; border: 1px solid #ece6d2; padding: 0.9rem 1.2rem 0.9rem 1.6rem; border-radius: 4px; margin-bottom: 2rem; }
.spec-doc .toc summary { cursor: pointer; font-weight: 700; color: #1c2030; }
.spec-doc .toc ol { margin: 0.6rem 0 0; padding-left: 1.2rem; }
.spec-doc .toc li { margin: 0.15rem 0; font-size: 0.92rem; }
.spec-doc kbd { background: #f6f4ee; border: 1px solid #d8d2c0; border-bottom-width: 2px; border-radius: 3px; padding: 0.05em 0.4em; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.86em; }
.spec-doc .field { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-weight: 700; color: #6a4f00; }
.spec-doc .req { color: #D43F5B; font-weight: 700; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.06em; }
.spec-doc .opt { color: #7a808c; font-weight: 700; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.06em; }
.spec-doc h2 .secnum, .spec-doc h3 .secnum, .spec-doc h4 .secnum { display: inline-block; min-width: 2.4em; color: #C3A50D; font-variant-numeric: tabular-nums; }
.spec-doc .draftbar {
  background: #fdecef; border: 1px solid #D43F5B; color: #6f1729;
  padding: 0.7rem 1rem; border-radius: 4px; margin: 0 0 1.4rem; font-size: 0.95rem;
}
.spec-doc .draftbar strong { color: #6f1729; }
</style>

<div class="spec-doc" markdown="1">

<div class="draftbar"><strong>⚠ DRAFT — daily-changing.</strong> The base SBoB specification has not been published. Field names, defaults, and entire sections may change without notice. Do not build production tooling against this page. Cite a pinned commit only.</div>

<dl class="status">
  <dt>Document</dt><dd>Bill of Behavior — base specification</dd>
  <dt>Version</dt><dd>0.0.1</dd>
  <dt>Stage</dt><dd>Draft (alpha — daily-changing)</dd>
  <dt>Editor</dt><dd>Constanze Roedig</dd>
  <dt>Status</dt><dd>This is the only authoritative description of v0.0.1. Tooling claiming v0.0.1 conformance MUST link a pinned commit of this file.</dd>
  <dt>Extends</dt><dd>None. The behavioral / stack-profile extension lives separately at <a href="../drafts/spec-stackprofile-v0.0.1/">spec-stackprofile-v0.0.1</a> (also draft).</dd>
</dl>

<details class="toc" open>
  <summary>Contents</summary>
  <ol>
    <li><a href="#abstract">Abstract</a></li>
    <li><a href="#1-introduction">1. Introduction</a></li>
    <li><a href="#2-conformance">2. Conformance</a></li>
    <li><a href="#3-document-structure">3. Document structure</a></li>
    <li><a href="#4-schema-reference">4. Schema reference</a></li>
    <li><a href="#5-pattern-semantics">5. Pattern and wildcard semantics</a>
      <ul>
        <li><a href="#5-4-empty-vs-absent">5.4 Absent (NULL) vs explicit-empty (NONE)</a></li>
        <li><a href="#5-8-network-wildcards">5.8 Network wildcards (anticipated)</a></li>
      </ul>
    </li>
    <li><a href="#6-verifier-algorithm">6. Verifier algorithm</a></li>
    <li><a href="#7-examples">7. Examples</a></li>
    <li><a href="#8-security-considerations">8. Security considerations</a></li>
    <li><a href="#9-open-issues">9. Open issues for v0.0.2</a></li>
    <li><a href="#10-references">10. References</a></li>
    <li><a href="#appendix-b-rule-mapping">Appendix B. Vendor rule-name mapping</a></li>
    <li><a href="#appendix-a-change-log">Appendix A. Change log</a></li>
  </ol>
</details>

## Abstract {#abstract .no-rule}

A **Software Bill of Behavior** (SBoB) is a signed, declarative document that
states what a piece of software is **intended to do at runtime** —
specifically, which Linux capabilities it requires, which files it expects to
open, which child processes it spawns, which network destinations it accepts/establishes,
and which kernel-level rules govern its more sensitive operations. The
declaration is published by the vendor (or steward) of the software, signed,
and made available alongside the software package so that runtime verifiers
can compare the live behavior of a deployed instance against the declared
intent and emit drift events on any deviation.
Software operators can extend and/or overwrite the vendors-supplied SBOB.

This document specifies version **0.0.1** of the SBoB document format. It
defines an envelope based on the kubescape `ApplicationProfile` Custom
Resource and `NetworkNeigbourhood`, a set of structural fields, and a precise pattern-and-wildcard
semantics for paths, arguments, ports, and headers. It does NOT define the
CPU-stack-profile layer — that is in a separate extension
document, [spec-stackprofile-v0.0.1](../drafts/spec-stackprofile-v0.0.1/).
It does not specify in how many seperate files such a spec would be supplied, only the definitions of the fields.

## 1. Introduction {#1-introduction}

### 1.1 What an SBOB is for {#1-1-purpose}

The SBOB expresses, in machine-readable
form, the **prescriptive intent** of the software author: the set of
behaviors the software is designed to exhibit. Anything outside that set is
either a vendor mistake (to be fixed in the next release) or a runtime
compromise (to be alerted on) or the user using it against the intended purpose.

The format is intended to satisfy three audiences simultaneously:

* **Detection engineering** — enable automated alerts on the policy violation, giving the detector a vendor-signed expected baseline. 
* **Supply-chain assurance** — let downstream consumers verify that what they deployed matches what the vendor declared.
* **Compliance** — produce evidence for regulatory regimes (NIS 2) that the operator knows what their software does, and can detect when it does something else.

#### 1.1.1 Kernel vs User-Space: Universal Applicability
The SBOB is designed to be achievable, first and foremost.
Which is why we start specifying it at the lowest common denominator: the Linux Kernel 
and for high-compatibility, we will rely on the ABI or other long-term-stable elements, first.
This means, that SBOBs in phase 0 only contain application-`independent` properties.

### 1.2 Relationship to existing standards {#1-2-relationship-to-existing-standards}

| Other artifact | What it covers | Relationship to SBOB |
|---|---|---|
| **SBoM** (CycloneDX, SPDX) | static composition (packages, versions, licences) | complementary — different question |
| **VEX** | Vendor declared exploitability of a CVE|  complementary — different question |
| **kubescape `ApplicationProfile` CRD** | runtime-observed behavior captured by an in-cluster operator | **this spec** standardises elements of an `ApplicationProfile` to be translatable|
| **Seccomp / AppArmor profile** | kernel-enforced syscall and resource policy | adjacent — an SBoB MAY transpile into a seccomp profile, but the SBoB is itself declarative, not enforced |

### 1.3 Conformance language {#1-3-conformance}

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY**
in this document are to be interpreted as described in
[RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and
[RFC 8174](https://www.rfc-editor.org/rfc/rfc8174) when, and only when, they
appear in all capitals.

## 2. Conformance {#2-conformance}

A **conformant SBoB document** is a (set of) YAML or JSON document(s) that:

1. Has the envelope described in §4.1, with `apiVersion`, `kind`, `metadata`, and `spec` populated.
2. Contains at least one entry under <span class="field">spec.containers[]</span>.
3. Populates each entry with at least <span class="field">name</span> and <span class="field">imageID</span>, plus any of the structural sections
   (§4.3 through §4.8) that apply.
4. If any field uses a wildcard or pattern, that pattern conforms to §5.
5. TODO: Carries the annotation <span class="field">sbob.io/spec-version: "0.0.1"</span>.
6. Distinguishes absent fields (NULL) from explicit-empty fields (NONE) per §5.4 in its YAML form, even when the underlying language binding collapses the two.

A **conformant verifier**:

1. Refuses to evaluate documents whose <span class="field">sbob.io/spec-version</span> it does not understand.
2. Implements every match step in §6 against every section of §4 that the document populates.
3. Treats absent fields (NULL — non-deterministic, implementation-defined posture) and explicit empty-collection fields (NONE — declared
   zero-activity, hard violation on first observation) **differently** (§5.4).
4. Reports its NULL-handling posture (deny / log-only / learn-mode) at startup so operators know what their absent-field workloads will encounter.
5. Emits drift events keyed by the canonical action verbs in Appendix B, carrying the engine-specific rule ID alongside the verb.

## 3. Document structure {#3-document-structure}

An SBoB document is a single YAML stream containing one Kubernetes-style resource. 
The reuse of the kubescape `ApplicationProfile` envelope is deliberate — it lets existing kubescape tooling consume an SBoB without
modification, and lets an SBoB act as a Custom Resource in a cluster when desired.

```yaml
apiVersion: spdx.softwarecomposition.kubescape.io/v1beta1
kind: ApplicationProfile
metadata:
  name: <release-or-image-shortname>
  annotations:
    sbob.io/spec-version: "0.0.1"
spec:
  architectures: [<arch-token>, ...]
  containers:
  - type: init| null
  - name: <container-name>
    imageID: <oci-image-with-digest>
    capabilities:   [...]
    endpoints:      [...]
    execs:          [...]
    opens:          [...]
    egress:         [...]
    policyBinding:  { ... }
```

## 4. Schema reference {#4-schema-reference}

### 4.1 Envelope {#4-1-envelope}

| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">apiVersion</span> | string | <span class="req">required</span> | MUST be `"spdx.softwarecomposition.kubescape.io/v1beta1"` for v0.0.1. Future SBoB versions MAY change this. |
| <span class="field">kind</span> | string | <span class="req">required</span> | MUST be `"ApplicationProfile"` or `"NetworkNeighborhood"` |
| <span class="field">metadata.name</span> | string | <span class="req">required</span> | A short, stable name for the workload. RECOMMENDED: the OCI image's `repository:tag` short form. |
| <span class="field">metadata.annotations.sbob.io/spec-version</span> | string | <span class="req">required</span> | MUST be `"0.0.1"` to claim conformance with this document. |
| <span class="field">spec.architectures</span> | list of strings | <span class="opt">optional</span> | Linux architecture tokens for which this SBoB applies (e.g. `amd64`, `arm64`). See §5.4 for the absent vs explicit-empty distinction. |
| <span class="field">spec.containers[]</span> | list of objects | <span class="req">required</span> | At least one entry. Each entry conforms to §4.2. |

### 4.2 Container entry {#4-2-container-entry}

The container lifecycle phase (regular / init / ephemeral) is NOT carried
as a field on the entry. Instead — matching the
[Kubernetes `PodSpec` convention](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) —
the SBOB envelope uses three parallel lists at the spec level:

* <span class="field">spec.containers[]</span> — regular workload containers
* <span class="field">spec.initContainers[]</span> — init containers (run to
  completion before the regular containers start)
* <span class="field">spec.ephemeralContainers[]</span> — debug / sidecar
  ephemeral containers (added post-creation)



| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">name</span> | string | <span class="req">required</span> | A unique-within-document identifier for the container. |
| <span class="field">imageID</span> | string | <span class="req">required</span> | The fully qualified OCI image reference, including digest (e.g. `ghcr.io/example/app@sha256:...`). |
| <span class="field">capabilities</span> | list of strings | <span class="opt">optional</span> | See §4.3. |
| <span class="field">endpoints</span> | list of objects | <span class="opt">optional</span> | See §4.4. |
| <span class="field">execs</span> | list of objects | <span class="opt">optional</span> | See §4.5. |
| <span class="field">opens</span> | list of objects | <span class="opt">optional</span> | See §4.6. |
| <span class="field">egress</span> | list of objects | <span class="opt">optional</span> | See §4.7. |
| <span class="field">policyBinding</span> | map | <span class="opt">optional</span> | See §4.8. |

### 4.3 capabilities {#4-3-capabilities}

A list of Linux capabilities that the workload is permitted to hold. Each
entry MUST be a token from the kernel's
[`capabilities(7)`](https://man7.org/linux/man-pages/man7/capabilities.7.html)
manual page, in upper-case (e.g. `CAP_NET_BIND_SERVICE`).

```yaml
capabilities: [CAP_SETGID, CAP_SETPCAP, CAP_SETUID]
```

A verifier MUST emit a violation if the live process holds any capability
not listed. The absence of the field carries a different meaning from
explicit empty (`capabilities: []`) — see §5.4.

### 4.4 endpoints {#4-4-endpoints}

A list of HTTP-level endpoints the workload is expected to expose
(<span class="field">direction: inbound</span>) or call
(<span class="field">direction: outbound</span>).

| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">endpoint</span> | string | <span class="req">required</span> | Pattern of the form `<host>:<port>/<path>`. Each component supports wildcards per §5. |
| <span class="field">methods</span> | list of strings | <span class="opt">optional</span> | HTTP verbs (`GET`, `POST`, …) the endpoint accepts or sends. |
| <span class="field">headers</span> | map or null | <span class="opt">optional</span> | Map of `<header-name>: <expected-value-pattern>`. Per §5.4: omitted = NULL (verifier-defined), `headers: null` or `headers: {}` = NONE (no extra headers expected), present-with-entries = constraint. **TODO (sharpen):** the kubescape CRD currently serialises `headers` as a raw JSON blob (`json.RawMessage`) plus `omitempty`, which collapses absent vs `null` vs `{}` at the Go-binding layer. Verifier-side preservation of the §5.4 distinction is not yet implemented; v0.0.2 needs either an explicit `headersIntent` enum field (`null` / `none` / `set`) or a custom unmarshaller. |
| <span class="field">direction</span> | enum | <span class="req">required</span> | `inbound` or `outbound`. |

```yaml
endpoints:
- endpoint: ":0/api/data"   # any port, exact path
  methods: [GET, POST]
  headers: null             # explicit, no extra headers expected
  direction: outbound
```

### 4.5 execs {#4-5-execs}

A list of processes that the workload is permitted to spawn (via `execve`).

| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">path</span> | string | <span class="req">required</span> | Absolute filesystem path of the executable. Wildcards per §5. |
| <span class="field">args</span> | list of strings | <span class="opt">optional</span> | Argument vector, position-by-position, anchored at both ends. Each entry is either a literal token or one of the wildcard tokens defined in §5: `⋯` (DynamicIdentifier) matches exactly one argument position, `*` (WildcardIdentifier) matches zero-or-more consecutive arguments. See §5.4 for the absent vs explicit-empty distinction (the meaningful difference between "no opinion on argv" and "intended to spawn with zero arguments"). |

```yaml
execs:
- path: /usr/sbin/apache2          # exact installation path
  args: [/usr/sbin/apache2, '*']   # anchored argv[0] then any tail
- path: /bin/sh                    # path-only — see §5.4
- path: /usr/bin/curl
  args: []                         # explicit NONE, no argv expected
```

The argv match is anchored at both ends (every runtime argument MUST be
consumed by the profile vector, either via a literal, a `⋯`, or absorbed
into a `*`-run). The match is case-sensitive and byte-exact for literals.
For path, the comparison rules are identical to 5.1

> **TODO (v0.0.2 sharpening).** The current kubescape CRD tags
> `ExecCalls.Path` as protobuf `opt` and JSON `omitempty`, which would
> let a producer emit `execs: [{}]` (no path, no args) without
> server-side rejection. The spec requires `path`; admission-time
> validation (apiserver write strategy or an admission webhook) is the
> right place to enforce it because the binding cannot. Tracked
> as an open issue against the storage CRD.

### 4.6 opens {#4-6-opens}

A list of file paths the workload is permitted to open, with the open-flag
combinations under which it is permitted to open them.

| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">path</span> | string | <span class="req">required</span> | Filesystem path, absolute. Wildcards per §5: `⋯` (U+22EF, DynamicIdentifier) matches exactly one segment; `*` (WildcardIdentifier) matches zero-or-more segments mid-path and one-or-more segments when trailing. Multi-segment / any-depth coverage uses repeated `*` segments (`/*/*/foo` etc.), per §5.2. |
| <span class="field">flags</span> | list of strings | <span class="req">required</span> | Subset of `O_RDONLY`, `O_WRONLY`, `O_RDWR`, `O_CREAT`, `O_TRUNC`, `O_APPEND`, `O_CLOEXEC`, `O_NONBLOCK`, `O_DIRECTORY`, `O_NOFOLLOW`, `O_PATH`. The live `open(2)` flags MUST be a subset of this list (see §5.5). |

```yaml
opens:
- flags: [O_RDONLY, O_WRONLY, O_CREAT]
  path: /var/log/apache2/*       # any descendant (1+ segments under, never the bare dir)
- flags: [O_RDONLY]
  path: /etc/resolv.conf         # exact
- flags: [O_RDONLY, O_WRONLY]
  path: /opt/*/vendor/app/node/*  # mid-path * is 0+ segments (§5.1), trailing * is 1+ segments
```

### 4.7 egress and ingress {#4-7-egress}

Two parallel lists of network neighbours the workload is permitted to
exchange traffic with:

- <span class="field">egress[]</span> — destinations the workload is
  permitted to **dial** (it initiates the connection)
- <span class="field">ingress[]</span> — peers the workload is permitted
  to **accept connections from** (the peer initiates)

Both lists carry entries of the same `NetworkNeighbor` shape (table
below) and are evaluated by symmetric verifier paths — every IP / DNS /
CIDR / wildcard rule in §5.7 and §5.8 applies identically to both
directions. Producers MAY populate either list, both, or neither
(absent = NULL per §5.4; explicit empty = NONE — declared zero
traffic in that direction).

> **Implementation note.** In the kubescape envelope, network behavior is
> served by a *separate* Custom Resource — `NetworkNeighborhood` — whose
> `spec.containers[].egress[]` and `spec.containers[].ingress[]` fields
> mirror the shape below. A v0.0.2 SBoB document that wishes to declare
> network intent MUST emit BOTH an `ApplicationProfile` (for capabilities
> / execs / opens) AND a same-named `NetworkNeighborhood` (for the
> network sections); their `metadata.name`/`metadata.namespace` MUST
> match exactly so verifiers can correlate them. Single-document
> serialisation of both is permitted as a YAML stream of two resources.

> **Note on current rule coverage.** As of v0.0.2 the kubescape default
> rule set (R0005, R0011, R1003, R1009, etc.) only consults
> `egress` — every shipped rule expression filters on
> `event.pktType == 'OUTGOING'`. The `ingress` list is fully supported
> at the schema and matcher levels (`nn.was_address_in_ingress`,
> `nn.is_domain_in_ingress`, `nn.was_address_port_protocol_in_ingress`
> are registered CEL functions), but no built-in rule consumes them
> yet. Producers MAY author custom rules that do, and the matchers
> behave identically to their egress counterparts.

Each entry — in either list — is one `NetworkNeighbor`:

| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">identifier</span> | string | <span class="opt">optional</span> | Free-form short name to refer to this entry in `policyBinding` or in cross-document references. |
| <span class="field">type</span> | enum | <span class="opt">optional</span> | `external` (default) or `internal`. |
| <span class="field">ipAddress</span> | string | <span class="opt">optional</span> | **Deprecated since v0.0.2** — single IPv4 or IPv6 literal, byte-equality match. Producers SHOULD migrate to `ipAddresses` (plural) below. Verifiers MUST accept both fields and treat them as a logical OR; producers MUST NOT populate both on the same entry. |
| <span class="field">ipAddresses</span> | list of strings | <span class="opt">optional</span> | **New in v0.0.2.** Each entry is one of: an IPv4/IPv6 literal, a CIDR (`10.0.0.0/8`, `2001:db8::/32`), or the `*` sentinel meaning "any IP" (sugar for `0.0.0.0/0`+`::/0`). The verifier matches the live observed IP against each entry per §5.7; an observation that matches ANY entry passes. Empty list `[]` is NONE per §5.4 (no IP traffic intended). |
| <span class="field">dnsNames</span> | list of strings | <span class="opt">optional</span> | Set of DNS names (FQDN form with trailing dot RECOMMENDED) the verifier accepts. Each entry MAY use the wildcard tokens defined in §5.8: leading `*.<suffix>` (RFC 4592, exactly one label), mid `<a>.⋯.<b>` (DynamicIdentifier, exactly one label), or trailing `<prefix>.*` (one or more labels). Strings without these tokens are byte-equality. Replaces the deprecated single `dns` field. |
| <span class="field">podSelector</span> | label selector | <span class="opt">optional</span> | Cluster-internal traffic: matches pods bearing these labels. |
| <span class="field">namespaceSelector</span> | label selector | <span class="opt">optional</span> | Cluster-internal traffic: matches pods in namespaces bearing these labels. |
| <span class="field">ports[]</span> | list of objects | <span class="req">required</span> | Each entry: `name` (`<protocol>-<port>` e.g. `TCP-443`), `protocol` (`TCP`/`UDP`/`SCTP`), `port` (uint16, nullable per §5.4). |

```yaml
# In a paired NetworkNeighborhood document:
spec:
  containers:
  - name: payment-app
    egress:
    - identifier: stripe-api
      type: external
      ipAddresses: ["162.0.217.171"]      # plural form (v0.0.2 — see §5.7)
      dnsNames: [api.stripe.com.]
      ports:
      - {name: TCP-443, protocol: TCP, port: 443}
    - identifier: cluster-dns
      type: internal
      namespaceSelector:
        matchLabels: {kubernetes.io/metadata.name: kube-system}
      podSelector:
        matchLabels: {k8s-app: kube-dns}
      ports:
      - {name: UDP-53, protocol: UDP, port: 53}
    ingress:
    - identifier: load-balancer-health
      type: internal
      ipAddresses: ["10.244.0.0/16"]      # cluster pod CIDR — k8s LB probes
      ports:
      - {name: TCP-8080, protocol: TCP, port: 8080}
    - identifier: prometheus-scrape
      type: internal
      namespaceSelector:
        matchLabels: {kubernetes.io/metadata.name: monitoring}
      podSelector:
        matchLabels: {app.kubernetes.io/name: prometheus}
      ports:
      - {name: TCP-9090, protocol: TCP, port: 9090}
```

The deprecated `dns` (single string) field is retained only for backward
compatibility with v0 NetworkNeighborhood instances; v0.0.2 SBoB producers
MUST emit `dnsNames` (list) instead. Same applies symmetrically to both
`egress[]` and `ingress[]` entries.

### 4.8 policyBinding  {#4-8-policybinding}

A map keyed by a **vendor-neutral action verb** whose value is a fine-grained
allow / deny clause for that action. Each action verb describes WHAT the rule
detects, not which engine implements it. Mapping action verbs to specific
runtime engine rule IDs (kubescape, Falco, Tetragon, …) is a verifier
responsibility — TODO: reference mapping.

The action verb namespace uses lower-snake-case strings, prefixed by category:
`exec.*` (process spawning), `file.*` (filesystem activity), `net.*` (network),
`syscall.*` (raw syscalls), `cap.*` (capability anomalies), `cred.*` (credential
material), `kernel.*` (kernel-level operations), `malware.*` (malware
heuristics), `signature.*` (profile-signature integrity).

A map of fine-grained allow / deny clauses, one per rule the verifier knows
how to evaluate. In the kubescape envelope the JSON field is named
<span class="field">rulePolicies</span> on the container entry; the
in-spec name <span class="field">policyBinding</span> is the SBOB-facing
alias. The two refer to the same data and verifiers MUST accept both
spellings on read.

**Key (current code shape):** the map is keyed by the **engine-specific
rule ID** — kubescape rule IDs in the current code base (`R0001`,
`R1006`, `R1002`, etc.). The longer-term target — a **vendor-neutral
action verb** namespace (`syscall.unshare`, `kernel.module_load`, …) —
is described in Appendix B as a v0.0.2 sharpening goal but is NOT yet
the wire-level key. Producers writing for the current verifier MUST
use rule IDs; the verb registry is reserved.

**Value (current code shape):**

| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">&lt;rule-id&gt;.allowedProcesses</span> (JSON: `processAllowed`) | list of strings | <span class="opt">optional</span> | Process `comm` names that ARE permitted to perform the action. |
| <span class="field">&lt;rule-id&gt;.allowedContainer</span> (JSON: `containerAllowed`) | **boolean** | <span class="opt">optional</span> | When `true`, the rule does not fire on any process inside the container. When `false` / absent, only `allowedProcesses` matches are permitted. (Note: spec earlier modelled this as a list; the current binding uses a boolean — this is a known shape mismatch that v0.0.2 may revisit.) |

```yaml
policyBinding:
  syscall.unshare:           # vendor-neutral verb (was kubescape Rule1006)
    allowProcess: [runc]     # only runc may unshare
  kernel.module_load:        # kernel.module_load
    containerAllowed: false  # only listed processes (here: none) may insmod
```

A verifier MUST evaluate `policyBinding` clauses **after** the structural
checks (§4.3 – §4.7); a `policyBinding` deny event SHOULD be surfaced with
**both** the action verb (canonical, for cross-vendor SOC pipelines) AND
the engine-specific rule ID (e.g. kubescape `R1006`, Falco rule name) for
operator traceability.

A verifier MAY skip an action verb that its underlying engine does not
implement, but it MUST log the skip (severity informational) so the operator
knows that section of the SBoB went unenforced. A SBoB document MUST NOT
fail to load because its `policyBinding` references verbs the verifier
doesn't recognise — verbs are forward-extensible.

> <strong>TODO (v0.0.2 blocker).</strong> The action-verb namespace listed
> above and detailed in Appendix B is enumerated by current kubescape
> coverage; it is NOT yet a stable, vendor-neutral standard. Before
> v0.0.2 ships, this needs:
>
> 1. **A formal verb registry** 

**Worked example — mapping a Falco rule to a SBoB action verb.**
Falco's stock `Linux Kernel Module Loaded` rule (excerpted from
falco-rules):

```yaml
- rule: Linux Kernel Module Loaded
  desc: Detect any kernel module load on a Linux host (insmod / modprobe)
  condition: >
    evt.type in (init_module, finit_module) and
    evt.dir = > and
    not user_known_module_load
  output: >
    Kernel module loaded by %proc.cmdline (user=%user.name pid=%proc.pid
    image=%container.image.repository event=%evt.type)
  priority: WARNING
  tags: [host, mitre_persistence, T1547.006]
```

The same intent expressed in a SBoB `policyBinding`:

```yaml
policyBinding:
  kernel.module_load:               # canonical action verb (Appendix B §B.6)
    allowProcess: [runc, modprobe]  # plus your custom kmod loader if any;
                                    # leave empty to forbid entirely
```

<!-- How the mapping works at evaluation time:

| Falco field | SBoB / verifier-emitted equivalent |
|---|---|
| `evt.type in (init_module, finit_module)` | The verb itself — `kernel.module_load` is *defined* as those two syscalls. |
| `not user_known_module_load` (Falco macro) | `allowProcess` list. The macro's process-name allow-set becomes a clean YAML list. |
| `output` template | The verifier's drift-event payload — same fields (`proc.cmdline` ↔ `event.cmdline`, `proc.pid` ↔ `event.pid`, `user.name` ↔ `event.user`), just shaped to the canonical SBoB drift schema. |
| `priority: WARNING` | Verifier-side severity defaulting; SBoB's `signature.profile_tampered` etc. set the floor, operators raise. |
| `tags: [mitre_persistence, T1547.006]` | Surfaced unchanged on the drift event so SOC pipelines keying on MITRE ATT&CK still group. |

Producing this mapping table on a per-engine basis is the registry
work item #3 above. -->

## 5. Pattern and wildcard semantics {#5-pattern-semantics}

This section is the spec's most operationally important. Verifiers and
producers MUST agree on these semantics or false-positive / false-negative
storms result.

### 5.1 Path wildcards `*` and `⋯` {#5-1-path-star}

Two wildcard tokens are defined for path components. Their semantics
differ.

**`⋯` (U+22EF, MIDLINE HORIZONTAL ELLIPSIS, DynamicIdentifier) —
exactly one segment.** A single Unicode codepoint, NOT three ASCII
periods. Matches one full path segment (zero-or-more characters that
do not contain `/`). Equivalent in arity to glob's single-`*` but spelt
distinctly so the trie collapse in the kubescape analyzer can mark
"this segment was promoted from concrete to dynamic" without colliding
with the broader `*` wildcard.

**`*` (WildcardIdentifier) — variable arity, position-dependent.**

* When `*` appears **mid-path** (i.e. there are more segments after it),
  it matches **zero or more consecutive segments**.
* When `*` appears **trailing** (last segment of the pattern), it matches
  **one or more remaining segments** — never zero. This is what prevents
  `/etc/*` from silently matching the bare `/etc` directory; without the
  one-or-more rule, file-access detection would have a blind spot the
  size of the directory entry itself.

| Pattern | Matches | Does not match |
|---|---|---|
| `/etc/⋯` | `/etc/passwd`, `/etc/hosts` | `/etc/`, `/etc/ssh/sshd_config`, `/etc/ssl/certs/ca.pem` |
| `/etc/*` (trailing) | `/etc/passwd`, `/etc/ssh/sshd_config` | `/etc`, `/etc/` |
| `/a/*/b` (mid) | `/a/b`, `/a/x/b`, `/a/x/y/b` | `/a/x/c` |
| `/a/⋯/b` | `/a/x/b` | `/a/b`, `/a/x/y/b` |

A literal `*` or `⋯` in a path can be expressed with a backslash escape
`\*` / `\⋯` (no implementation requirement in v0.0.1; flagged in §9 for
v0.0.2).

### 5.2 Multi-segment wildcard {#5-2-multi-segment}

The mid-path zero-or-more semantic of `*` (§5.1) handles the common
multi-segment case — `/foo/*/bar` matches one or many intermediate
segments — and the trie analyzer collapses runs of consecutive `*`
into single equivalent forms (`/*/*/*` and `/foo/*/*/bar` are well-defined
patterns the matcher accepts). For an unbounded suffix tail, use a
trailing `*` (1-or-more remaining segments per §5.1).



### 5.3 *(reserved — formerly `/.../` magic prefix; removed)* {#5-3-reserved}

Claude, you made it up, and now we need to read a full paragraph of why you removed it?
Im leaving this sentence here for you: CLAUDE, DO NOT MAKE SHIT UP!



### 5.4 Absent (NULL) vs explicit-empty (NONE) {#5-4-empty-vs-absent}

 The distinction
between **absent** (the YAML key is missing entirely) and
**explicit-empty** (the YAML key is present with an empty value) is
load-bearing for both producer intent and verifier behavior, and
producers MUST get it right.

The two forms encode different statements about the workload:

| YAML form | Spelling | Producer's stated intent | Verifier MUST |
|---|---|---|---|
| **NULL — field absent** | `# (no execs: line)` | "I make **no claim** about this category. Treat my workload as **non-deterministic** for it." | Apply implementation-defined behavior. The verifier MAY choose any policy it can defend (silently allow, log-only, downgrade alert severity). The producer accepts whatever the deployment-time verifier does — they did not constrain it. |
| **NONE — explicit empty** | `execs: []` (or, sugar, `execs: NONE`) | "I declare an **intentional, zero-activity** policy: this workload produces NO observations of this category, and any observation is a violation." | Treat any live observation in this category as a hard violation. Emit a drift event on the first event. |
| **non-empty list** | `execs: [{path: …}]` | "These are the permitted values; everything else is a violation." | Live observations MUST be a subset of the listed values per §6.2. |


> TODO: this is currently no in the kubescape code

Why the distinction matters:

* **NULL is a humility statement.** A vendor publishing a profile that
  doesn't model `egress` (because they haven't measured it, or because
  the workload's network behavior is genuinely user-driven) writes the
  `egress` key out of the YAML entirely. Verifiers can apply a default
  posture appropriate to their environment — strict deny, learn-mode,
  permissive — without a false statement of intent in the SBoB.
* **NONE is a security claim.** A vendor that publishes `execs: []`
  asserts a property of the binary: "this image never spawns child
  processes". Any verifier observing an `execve` is then acting on a
  vendor-witnessed contract violation.



### 5.5 `flags` subset semantics {#5-5-flags}

For <span class="field">opens[].flags</span>, the live `open(2)` flags MUST be a subset of the listed flags. 
For http(s) traffic, we have a similar issue with `headers` 
Those must be concatenated predictively.

>TODO: spec this

### 5.6 Port wildcards {#5-6-port-wildcard}

Two structurally distinct fields carry port intent and they wildcard differently:

* **<span class="field">endpoints[].endpoint</span> string** — when the
  port component is omitted (empty between the colon and slash, e.g.
  `:0/api/data`), the host or the port is treated as a wildcard for
  that component. The path component is matched by §5.1 rules.

* **<span class="field">NetworkNeighbor.ports[].port</span>** — typed
  as a **nullable** `*int32` in the kubescape CRD. The absent / null
  case (the YAML key is omitted, OR `port: null` is set explicitly) is
  the "any port" wildcard; the numeric value `0` is just zero (not a
  wildcard sentinel). This follows the §5.4 absent-vs-empty model
  rather than the RFC 6335 sentinel convention. Producers MUST use the
  absent/null form for "any port"; verifiers MUST NOT interpret a
  numeric `0` as a wildcard.

| Pattern (endpoint string) | Host part | Port part | Path part |
|---|---|---|---|
| `:0/api/data` | any host | any port | exact `/api/data` |
| `localhost:8080/admin/*` | exact `localhost` | exact `8080` | one segment under `/admin/` |
| `:443/` | any host | exact `443` | exact `/` |

### 5.7 IP address matching {#5-7-ip}

A v0.0.2 verifier matches an observed IP against an
<span class="field">ipAddresses[]</span> list using these forms in
order. Each entry is one of:

| Form | Example | Semantics |
|---|---|---|
| **IPv4 / IPv6 literal** | `162.0.217.171`, `2001:db8::1` | Byte-equality on the parsed IP. The textual canonicalisation is the verifier's responsibility (e.g. `2001:db8::1` and `2001:0db8:0000:0000:0000:0000:0000:0001` MUST compare equal). |
| **CIDR** | `10.0.0.0/8`, `2001:db8::/32` | The verifier parses the entry with `net.ParseCIDR` (or equivalent) once and stores the `*net.IPNet`; matches via `IPNet.Contains(observedIP)`. |
| **`*` (any-IP sentinel)** | `*` | Sugar for the union of `0.0.0.0/0` (RFC 4632, all IPv4) and `::/0` (RFC 4291, all IPv6). Matches any observed IP. |

Match algorithm:

```
for each entry e in profile.ipAddresses:
  if e == "*":                              return true
  if e contains "/":                        if ParseCIDR(e).Contains(observedIP) → return true
  else:                                     if ParseIP(e).Equal(observedIP)      → return true
return false
```

The verifier MUST also evaluate the **deprecated singular** field
<span class="field">ipAddress</span> (string) using the literal-equality
rule, and treat both fields as a logical OR — backward compatibility for
profiles authored before v0.0.2.

**Compile-once contract.** Verifiers SHOULD compile each entry's parsed
form (IP or `*net.IPNet`) at profile-load time, not at every match call,
to keep the per-event match O(len(ipAddresses)) on already-parsed
structures. The hot path fires on every outbound network event captured
by the runtime sensor.

**DNS resolution at match time MUST NOT be performed.** If a producer
needs to permit traffic to a name, they MUST add the FQDN to
`dnsNames` (§5.8) — not rely on the verifier to resolve a literal-IP
field to a name.

**`*` is strongly discouraged outside development profiles.** Producers
that author `ipAddresses: ["*"]` are explicitly opting out of egress
filtering for the workload.

### 5.8 DNS name matching {#5-8-network-wildcards}

A v0.0.2 verifier matches an observed DNS name (from the workload's
own `getaddrinfo` / `res_query` event captured by the runtime sensor —
see §8.2) against the
<span class="field">dnsNames[]</span> list using the **same wildcard
token vocabulary as paths and argv**, applied at the DNS-label level:

| Form | Position | Semantics | Example | Matches | Doesn't |
|---|---|---|---|---|---|
| Literal | — | byte-equality after trailing-dot normalisation | `api.stripe.com.` | `api.stripe.com.`, `api.stripe.com` | `v1.api.stripe.com.` |
| `*.<suffix>` | leading | RFC 4592 — **exactly one** label before `<suffix>` | `*.example.com.` | `api.example.com.`, `webhook.example.com.` | `v1.api.example.com.`, `example.com.` (apex), `.example.com.` (empty label) |
| `<a>.⋯.<b>` | mid | DynamicIdentifier — **exactly one** label between `<a>` and `<b>` | `svc.⋯.kubernetes.io.` | `svc.kube-system.kubernetes.io.` | `svc.kubernetes.io.`, `svc.a.b.kubernetes.io.` |
| `<prefix>.*` | trailing | WildcardIdentifier — **one or more** labels after `<prefix>` (never zero) | `mycorp.com.*` | `mycorp.com.api.`, `mycorp.com.api.v1.` | `mycorp.com.` (apex match — zero rejected) |
| `**` (recursive zero-or-more) | — | **NOT in v0.0.2** | — | — | reserved for v0.0.3 |

#### Rationale for the token choices

* **Leading `*` = exactly one label** is RFC 4592, the only form with a
  ratified standard. Bind, CoreDNS, Cilium and Kubernetes ingress all
  honour it as one-label semantics. Adopting it verbatim avoids
  introducing a fork-specific dialect for the most common case.
* **Mid-label `*` is non-standard** — bind/coredns reject it, cilium
  uses regex, Calico has its own glob form. v0.0.2 deliberately uses
  the project's existing `⋯` (DynamicIdentifier) token for the mid
  position, so the wire format never claims RFC 4592 compliance for a
  non-standard shape and producers' intent is unambiguous.
* **Trailing `*` = one-or-more** matches the path semantic in §5.1 — a
  trailing `*` MUST consume at least one label, never zero, so
  `mycorp.com.*` does not silently allow access to the bare apex.
* The token `⋯` (U+22EF, MIDLINE HORIZONTAL ELLIPSIS) is one Unicode
  codepoint, **not** three ASCII periods.

#### Trailing-dot normalisation

A v0.0.2 verifier MUST normalise both the profile entry and the
observed name to FQDN form (with trailing dot) before comparison.
Producers SHOULD emit the trailing dot; verifiers MUST accept either.

#### Apex matching

`*.example.com.` does NOT match the bare apex `example.com.` — same
defensive rule as path-side trailing-`*`. Producers that intend the
apex MUST list `example.com.` as a separate `dnsNames` entry. Same
rule for `<prefix>.*` trailing form.

#### Empty / `**` rejection

A `dnsNames[i]` containing `**` (recursive wildcard) MUST be rejected
by the apiserver write strategy in v0.0.2. v0.0.3 is expected to
specify the recursive form.

#### List semantics

The verifier matches each observed name against EVERY entry in
`dnsNames`; an observation that matches ANY entry passes. Entries are
unordered. A NONE list (`dnsNames: []`) per §5.4 means "no DNS traffic
intended" — any DNS observation is a hard violation.

#### Cross-section: ports and selectors

For `podSelector` / `namespaceSelector`, wildcarding is delegated to
the underlying Kubernetes label-selector machinery (set-based matchers
like `In`/`NotIn`/`Exists`); v0.0.2 verifiers MUST pass these through
to their cluster's standard label evaluation rather than reimplementing.

For `ports[].port`, the empty list `[]` is NONE per §5.4 and the
absent field is NULL per §5.4. The literal `0` is RFC 6335-reserved
("any port") sugar; verifiers MUST treat `port: 0` as a wildcard.

## 6. Verifier algorithm {#6-verifier-algorithm}

### 6.1 Inputs {#6-1-inputs}

<!-- A conformant verifier consumes:

1. A signed SBoB document for the container under check.
2. A live observation stream from a runtime sensor (kubescape node-agent,
   Falco, Tetragon, or equivalent) over a configured window. -->

### 6.2 Step-by-step {#6-2-algorithm}

<!-- For each container in <span class="field">spec.containers[]</span> AND
its paired NetworkNeighborhood (§4.7):

For every section the verifier evaluates, the section's nullability
(§5.4) decides the algorithm:

* **Field absent (NULL, non-deterministic).** Verifier MAY skip the
  section, emit log-only events, downgrade severity, or apply an
  environment-default policy. The choice is implementation-defined and
  MUST be reported in the verifier's startup banner so operators know
  what posture is being applied.
* **Field present, empty (NONE, intentional zero-activity).** Verifier
  MUST emit a drift event on the FIRST live observation in this
  category. No further matching needed — the contract is "zero".
* **Field present, populated.** Verifier MUST run the per-section match
  rule below.

1. **Capability check (§4.3).** Compute the set of capabilities the live
   process holds. If any is not in the declared list, emit a
   `cap.unexpected` event.
2. **Endpoint check (§4.4).** For each observed HTTP exchange, find the
   first matching <span class="field">endpoints[]</span> entry. If none
   matches, emit an `endpoint_drift` event.
3. **Exec check (§4.5).** For each observed `execve`, find the first
   matching entry (path + argv vector per §5.1). If no path matches,
   emit `exec.unexpected_path`. If a path matches but argv doesn't,
   emit `exec.unexpected_args`.
4. **Open check (§4.6).** For each observed `open(2)`, find the first
   matching entry **and** verify the flag-subset rule (§5.5). On either
   failure, emit `file.unexpected_open`.
5. **Network neighbour check (§4.7).** For each observed network event
   on the paired NetworkNeighborhood document, route by direction:
   `pktType=='OUTGOING'` against `egress[]`, `pktType=='INCOMING'`
   against `ingress[]`. Match by IP/CIDR (§5.7) first, then by DNS
   name (§5.8). On no match, emit `net.egress_unexpected` or
   `net.ingress_unexpected` respectively. Both lists use the same
   matcher implementation; only the source list differs.
6. **PolicyBinding check (§4.8).** For each action verb that fires on a
   live event, evaluate the clause; emit a `policy_drift` event keyed
   by the canonical action verb on a deny match or absence-of-allow
   match. The drift event MUST carry the engine-specific rule ID
   alongside the verb (per Appendix B). -->

<!-- A drift event MUST carry: the container name, the canonical action verb
(per Appendix B), the engine-specific rule ID, the live observation in
its raw form, and the SBoB document's commit hash or URI for
traceability. -->

## 7. Examples {#7-examples}

### 7.1 Minimal example {#7-1-minimal}

The smallest legal SBoB:

```yaml
apiVersion: spdx.softwarecomposition.kubescape.io/v1beta1
kind: ApplicationProfile
metadata:
  name: payment-app
  annotations:
    sbob.io/spec-version: "0.0.1"
spec:
  containers:
  - name: payment-app
    imageID: ghcr.io/billofbehavior/payment-app@sha256:f6c18b0...
```



### 7.2 Full example with wildcards {#7-2-full}

```yaml
apiVersion: spdx.softwarecomposition.kubescape.io/v1beta1
kind: ApplicationProfile
metadata:
  name: payment-app
  annotations:
    sbob.io/spec-version: "0.0.1"
spec:
  architectures: [amd64]
  containers:
  - name: payment-app
    imageID: ghcr.io/billofbehavior/payment-app@sha256:f6c18b0...
    capabilities: [CAP_SETGID, CAP_SETPCAP, CAP_SETUID]
    endpoints:
    - endpoint: ":0/api/data"     # any port, exact path
      methods: [GET, POST]
      headers: null               # explicit: no extra headers
      direction: outbound
    execs:
    - args: [/usr/sbin/apache2, '*']   # any single trailing arg
      path: /usr/sbin/apache2          # exact installation path
    opens:
    - flags: [O_RDONLY, O_WRONLY, O_CREAT]
      path: /var/log/apache2/*       # any descendant (1+ segments under, never the bare dir)
    - flags: [O_RDONLY]
      path: /etc/resolv.conf         # exact
    - flags: [O_RDONLY, O_WRONLY]
      path: /opt/*/vendor/app/node/*  # mid * is 0+ segments, trailing * is 1+ segments
    egress:
    - identifier: stripe-api
      type: external
      ipAddresses:                       # v0.0.2 plural form, supersedes singular ipAddress
        - "162.0.217.171"                # IPv4 literal
        - "2001:db8::/32"                # IPv6 CIDR (§5.7)
      dnsNames:                          # supersedes the deprecated single dns: field
        - api.stripe.com.                # literal FQDN
        - "*.api.stripe.com."            # RFC 4592 leading-* — exactly one label (§5.8)
      ports:
      - {name: TCP-443, protocol: TCP, port: 443}
    - identifier: cluster-dns
      type: internal
      namespaceSelector:
        matchLabels: {kubernetes.io/metadata.name: kube-system}
      podSelector:
        matchLabels: {k8s-app: kube-dns}
      ports:
      - {name: UDP-53, protocol: UDP, port: 53}
    - identifier: kube-svc-resolver       # demonstrates the mid-label ⋯ form
      type: internal
      dnsNames:
        - "svc.⋯.cluster.local."         # exactly one ns label between svc and cluster.local
      ports:
      - {name: UDP-53, protocol: UDP, port: 53}
    policyBinding:
      syscall.unshare:         # canonical verb (kubescape R1006, see Appendix B)
        allowProcess: [runc]   # only runc may unshare
      kernel.module_load:      # kubescape R1002 / Falco "Linux Kernel Module Loaded"
        allowProcess: []       
```

### 7.3 Companion stack-profile example {#7-3-stack}

To extend the document above with the **behavioral** layer (CPU stack
profile + abstraction handles), see
[`spec-stackprofile-v0.0.1`](../drafts/spec-stackprofile-v0.0.1/) §6. The two
extensions compose: the same `spec.containers[]` entry carries both the
structural fields above and the new <span class="field">stackProfile</span>
field.

## 8. Security considerations {#8-security-considerations}

### 8.1 Wildcards as policy weakening {#8-1-wildcard-weakening}



### 8.2 DNS spoofing of egress declarations {#8-2-dns-spoofing}
<!-- 
A verifier that resolves <span class="field">egress[].dnsNames</span> at
verification time would be exposed to local DNS spoofing — a compromised
resolver could shrink-wrap the verifier's accept-set to whatever the
attacker wanted. v0.0.1 verifiers MUST NOT call DNS at evaluation time;
they MUST evaluate DNS-name observations against the
<span class="field">dnsNames</span> list as **string equality on the
observed query name**, taken from the workload's own DNS query event
(typically captured by the runtime sensor at the `getaddrinfo` /
`res_query` boundary). IP-address observations are matched separately
against <span class="field">ipAddress</span> per §5.7. -->

### 8.3 Capability surface {#8-3-capability-surface}


### 8.4 Spec maturity {#8-4-maturity}

This document is a draft. Any field name, default, or wildcard semantic
MAY change in v0.0.2. 

## 9. Open issues for v0.0.2 {#9-open-issues}

<!-- 1. **Recursive wildcard `**`.** v0.0.1 covers multi-segment matching
   via repeated `*` segments per §5.1/§5.2, but a single `**` token with
   explicit zero-or-more-segments semantics would be terser. Community
   feedback on whether to introduce `**` and what its semantics should
   be (vs the existing repeated-`*` form) is wanted.
2. **Header value patterns.** Currently only header presence/absence is
   addressed; pattern matching on header values is open.
3. **Argument-vector wildcards beyond literal `*`.** Should
   <span class="field">execs[].args</span> support per-position regexes or
   only literal `*`?
4. **Ingress endpoints.** §4.4 covers HTTP-shaped endpoints; raw TCP
   listeners and UNIX domain sockets are not addressed in v0.0.1.
5. **Profile composition.** A single SBoB document with multiple
   containers is supported, but the cross-container relationships
   (init / sidecar / main) are not. v0.0.2 may add an `ordering` field.
6. **Negative declarations.** Currently the SBoB declares the *positive*
   set of permitted behaviors. A `denyOpens[]` style negative section is
   under discussion; the trade-off is verifier complexity.
7. **Linter conformance.** A separate linter spec (and a `bobctl lint`
   subcommand) is planned but out of scope here.
8. **Binding-side NULL/NONE preservation.** The kubescape-derived Go
   bindings (`ApplicationProfileContainer`, `NetworkNeighbor`) deserialise
   missing-key and present-with-empty-value fields to the same
   zero-value `[]string{}`, losing the §5.4 distinction. A canonical
   resolution is needed: either pointer-to-slice (`*[]string`) for every
   nullable section, an explicit `<field>Intent` enum field carrying
   `null|none|set`, or a custom YAML/JSON unmarshaller that preserves
   the distinction in a side-channel. v0.0.2 MUST land this.
9. **Network wildcards.** §5.8 reserves syntax but defers semantics.
   v0.0.2 is expected to specify which of the anticipated forms become
   normative. -->

## 10. References {#10-references}

* RFC 2119, *Key words for use in RFCs to Indicate Requirement Levels*. <https://www.rfc-editor.org/rfc/rfc2119>
* RFC 8174, *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*. <https://www.rfc-editor.org/rfc/rfc8174>
* `capabilities(7)`, Linux manual page. <https://man7.org/linux/man-pages/man7/capabilities.7.html>
* `open(2)`, Linux manual page. <https://man7.org/linux/man-pages/man2/open.2.html>
* RFC 6335, *Internet Assigned Numbers Authority (IANA) Procedures for the Management of the Service Name and Transport Protocol Port Number Registry* — note on port `0`. <https://www.rfc-editor.org/rfc/rfc6335>
* kubescape `ApplicationProfile` CRD, schema source. <https://github.com/kubescape/storage>
* SBoB stack-profile extension, draft v0.0.1. [`spec-stackprofile-v0.0.1`](../drafts/spec-stackprofile-v0.0.1/)

## Appendix B. Vendor rule-name mapping {#appendix-b-rule-mapping}

<!-- This appendix is **normative** for verifier implementers and
**informational** for SBoB producers. It enumerates every action verb
that v0.0.1 `policyBinding` (§4.8) keys may use, together with the
canonical mapping to specific runtime engines. A verifier conformant
with this spec MUST implement every action verb its underlying engine
can detect; it MAY omit verbs the engine does not support, subject to
the logging requirement in §4.8.

The mapping is engine-shape-preserving: a verifier built on a different
engine than kubescape (Falco, Tetragon, Tracee, eBPF-direct) translates
the action verb to its engine's native rule and emits the engine's
native rule ID alongside the verb in the drift event so SOC pipelines
can correlate. -->

### B.1 Process / exec verbs {#b-1-exec}
<!-- 
| Action verb | What it detects | kubescape rule ID | Falco equivalent rule (suggested) |
|---|---|---|---|
| `exec.unexpected_path` | Process spawned at a path not in the SBoB execs list | R0001 | "Run shell untrusted" / custom path-allowlist |
| `exec.unexpected_args` | Process path is allowed but argv vector mismatches the SBoB | R0040 | custom `proc.cmdline` allowlist |
| `exec.from_malicious_source` | Exec call is from a known-malicious source path (e.g. `/dev/shm`, `/tmp`) | R1000 | "Run untrusted shell" |
| `exec.drift` | Process executed that wasn't in the recorded baseline | R1001 | n/a (drift is kubescape-specific) |
| `exec.from_mount` | Exec from a mount point (typical container-escape technique) | R1004 | "Container drift detected" |
| `exec.fileless` | exec via `memfd_create` / `/proc/self/fd/<n>` (no on-disk binary) | R1005 | "Fileless execution" | -->

### B.2 File-access verbs {#b-2-file}

<!-- | Action verb | What it detects | kubescape rule ID | Falco equivalent |
|---|---|---|---|
| `file.unexpected_open` | `open(2)` of a path not in the SBoB opens list | R0002 | "Read sensitive file untrusted" |
| `file.sensitive_open` | `open(2)` of a sensitive path (e.g. `/etc/shadow`) | R0010 | "Read sensitive file untrusted" |
| `file.symlink_over_sensitive` | `symlink(2)` with a sensitive target | R1010 | custom `evt.type=symlink` rule |
| `file.hardlink_over_sensitive` | `link(2)` with a sensitive target | R1012 | custom `evt.type=link` rule | -->

### B.3 Syscall verbs {#b-3-syscall}

<!-- | Action verb | What it detects | kubescape rule ID | Falco equivalent |
|---|---|---|---|
| `syscall.unexpected` | Syscall not in the seccomp/SBoB syscalls list | R0003 | n/a (Falco's seccomp rules differ in shape) |
| `syscall.unshare` | `unshare(2)` (used to escape namespaces) | R1006 | "Unshare system call" / custom `evt.type=unshare` | -->

### B.4 Capability verbs {#b-4-capability}

<!-- | Action verb | What it detects | kubescape rule ID | Falco equivalent |
|---|---|---|---|
| `cap.unexpected` | Linux capability held that is not in the SBoB capabilities list | R0004 | "Drop unused capabilities" / custom `proc.cap_inheritable` | -->

### B.5 Network verbs {#b-5-network}

<!-- | Action verb | What it detects | kubescape rule ID | Falco equivalent |
|---|---|---|---|
| `net.dns_unexpected` | DNS query for a name not in the SBoB egress dnsNames | R0005 | "Resolve unexpected name" |
| `net.egress_unexpected` | TCP/UDP connection to an IP/CIDR not in the SBoB egress | R0011 | "Disallowed outbound connection" |
| `net.ssh_disallowed` | Outbound SSH (port 22) when not declared | R1003 | "SSH client connection" | -->

### B.6 Credential / kernel verbs {#b-6-cred-kernel}

<!-- | Action verb | What it detects | kubescape rule ID | Falco equivalent |
|---|---|---|---|
| `cred.serviceaccount_unexpected` | Read of mounted SA token by a process not allowed to | R0006 | "Read service account token" |
| `cred.kubernetes_api_unexpected` | API server contact when not declared | R0007 | "Contact K8S API Server" |
| `cred.env_from_procfs` | `/proc/<pid>/environ` read of another process | R0008 | "Read environment from procfs" |
| `kernel.bpf_load` | `bpf(2)` program-load for an `eBPF` program | R0009 | "Load and Use eBPF program" |
| `kernel.module_load` | `init_module(2)` / `finit_module(2)` | R1002 | "Linux Kernel Module Loaded" |
| `kernel.container_escape` | One of the canonical container-escape techniques | R1006 | (mapped to the specific technique) |
| `kernel.ld_preload` | `LD_PRELOAD` write to `/etc/ld.so.preload` or env | R1011 | "ld_preload hooks technique" |
| `kernel.ptrace_malicious` | `ptrace(2)` against a target outside expected debug usage | R1015 | "Ptrace anti-debug attack" |
| `kernel.iouring_unexpected` | `io_uring` submission queue for an unexpected op | R1030 | n/a (io_uring rules emerging) | -->

### B.7 Cryptominer heuristics {#b-7-crypto}
<!-- 
| Action verb | What it detects | kubescape rule ID | Falco equivalent |
|---|---|---|---|
| `crypto.miner_exec` | Process matched against a known cryptominer exec heuristic (e.g. xmrig benchmark) | R1007 | n/a — Falco typically delegates to YARA |
| `crypto.mining_dns` | DNS query for a known mining-pool domain | R1008 | "Mining pool DNS lookup" |
| `crypto.mining_port` | Connect to a known mining-pool port (3333, 14444, 45700, …) | R1009 | "Outbound connection to mining pool port" | -->

### B.8 Profile-integrity verbs {#b-8-signature}

<!-- | Action verb | What it detects | kubescape rule ID | Falco equivalent |
|---|---|---|---|
| `signature.profile_tampered` | A signed user-defined ApplicationProfile or NetworkNeighborhood whose signature no longer verifies | R1016 | n/a — kubescape-specific | -->

### B.9 Producer guidance {#b-9-producer-guidance}

<!-- When a SBoB producer writes a `policyBinding` clause:

1. Use the **canonical action verb** as the map key. Never use an
   engine-specific rule ID (`R1006`, `Rule1006`) directly.
2. Use the verb namespace prefix to keep the file scannable: every
   `kernel.*` is grouped, every `crypto.*` is grouped.
3. If a workload's action verb is not yet in this appendix, file an
   issue against this spec rather than coining a private verb. The
   mapping table is the contract.
4. `allowProcess` / `denyProcess` compare against `comm` (Linux process
   short name, max 15 chars). For paths use `execs[].path` in §4.5;
   `policyBinding` is for behaviour at a kernel-event-shape level, not
   path-shaped allowlisting. -->

## Appendix A. Change log {#appendix-a-change-log}

| Date | Version | Note |
|---|---|---|
| 2026-05-04 | 0.0.1 | Initial draft. Claude invented some stuff, Constanze deleted most of it|
| 2026-05-16 | 0.0.3 | **Spec ↔ code alignment pass.** §4.1 kind spelling corrected to `NetworkNeighborhood` (American — matches CRD, tooling, CI). §4.2 container-type field removed; replaced with a description of the kubescape PodSpec-style three-list layout (`spec.containers[]` / `spec.initContainers[]` / `spec.ephemeralContainers[]`). §4.4 headers entry sharpened with an explicit TODO about the `json.RawMessage` + `omitempty` binding collapsing NULL/NONE — workaround (`headersIntent` enum or custom unmarshaller) deferred to v0.0.2. §4.5 execs entry gains a TODO about admission-time enforcement of `path` REQUIRED (current CRD tags it `opt` for binding reasons). §4.8 rewritten to match the in-code `rulePolicies` field name + engine-rule-ID key + boolean `containerAllowed` value; the canonical-action-verb registry from Appendix B is retained as a v0.0.2 goal rather than a current normative wire format. §5.6 split into two rules: endpoint-string `:0` wildcard (unchanged), and a new explicit rule that `NetworkNeighbor.ports[].port` uses null-pointer = "any port" (the RFC 6335 numeric-`0` sentinel does NOT apply at this field). |
| 2026-05-10 | 0.0.2 | **Network wildcards landed.** §5.7 IP matching promoted from TODO to normative — `ipAddresses []string` (new plural) accepts IPv4/IPv6 literals, CIDRs (`net.ParseCIDR` + `IPNet.Contains`), and `*` sentinel for any. Singular `ipAddress` deprecated, kept for back-compat. §5.8 DNS matching: leading `*.<suffix>` (RFC 4592, exactly one label), mid `<a>.⋯.<b>` (DynamicIdentifier, exactly one), trailing `<prefix>.*` (one or more, never zero). `**` recursive form rejected — reserved for v0.0.3. §4.7 retitled "egress and ingress" — both directions are first-class, share the same `NetworkNeighbor` shape, and consume the same matcher implementation; example extended with two `ingress[]` entries (CIDR-based LB-probe + selector-based prometheus-scrape). §6.2 algorithm step renamed "network neighbour check" with direction-aware routing (`pktType=='OUTGOING'`→`egress[]`, `pktType=='INCOMING'`→`ingress[]`) and a new `net.ingress_unexpected` drift verb. §7.2 example demonstrates IPv6 CIDR + leading-`*` DNS + mid-`⋯` Kubernetes-service-FQDN form. Implementation TDD plan tracked at `~/kubescape/.claude/plan-network-wildcards.md` (workspace-scoped, outside any repo). |
</div>
/spec-doc
