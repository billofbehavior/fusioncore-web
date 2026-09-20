---
title: "SBOB specification — v0.0.4"
weight: 20
type: "docs"
draft: false
---

<style>
/* Re-uses the .spec-doc styling from spec-stackprofile-v0.0.1.md.
   Both pages keep their own style block so neither depends on the other. */
.post__inner { max-width: min(1600px, 96vw); }
.spec-doc { max-width: 1460px; margin: 0 auto; line-height: 1.65; color: #0a0a0a; }
.spec-doc p, .spec-doc li, .spec-doc blockquote, .spec-doc .ainote, .spec-doc .proposed, .spec-doc .status, .spec-doc pre { max-width: 980px; }
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
.spec-doc .vendor td:nth-child(n+4), .spec-doc .vendor th:nth-child(n+4) { color: #400049; } .spec-doc .vendor th:nth-child(n+4) { background: #f3e5f5; } .spec-doc .vendor td:nth-child(n+4) code { color: #400049; border-color: #C9A5CF; background: #faf3fb; }
.spec-doc .vendor table { table-layout: fixed; }
.spec-doc .vendor th:nth-child(1), .spec-doc .vendor td:nth-child(1) { width: 12%; }
.spec-doc .vendor th:nth-child(2), .spec-doc .vendor td:nth-child(2) { width: 13%; }
.spec-doc .vendor th:nth-child(3), .spec-doc .vendor td:nth-child(3) { width: 17%; }
.spec-doc .vendor th:nth-child(n+4), .spec-doc .vendor td:nth-child(n+4) { width: 18%; }
.spec-doc .vendor td:nth-child(3) code { font-size: 0.78rem; line-height: 1.45; word-break: break-word; overflow-wrap: anywhere; white-space: normal; display: inline; }
.spec-doc .vendorref { background: #fff5d6; border-bottom: 1px dotted #C3A50D; padding: 0 2px; }
.spec-doc .ainote { background: #f3e5f5; border-left: 4px solid #400049; color: #400049; padding: 0.6rem 0.9rem; margin: 0.8rem 0 1.2rem; font-size: 0.92rem; border-radius: 3px; }
.spec-doc .proposed { color: #b3001b; } .spec-doc .proposed code, .spec-doc .proposed a { color: #b3001b; } .spec-doc div.proposed { border: 1px dashed #b3001b; padding: 0.5rem 0.9rem; margin: 0.8rem 0; border-radius: 4px; background: #fff7f7; }
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
/* Reference-implementation status markers — see the "Reference implementation" note in §1. */
.spec-doc .ri { display: inline-block; font-size: 0.68rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; border-radius: 999px; padding: 0.05em 0.55em; vertical-align: middle; margin: 0 0.15em; white-space: nowrap; }
.spec-doc .ri.defacto  { color: #33447a; background: #eef1fb; border: 1px solid #c2ccec; }
.spec-doc .ri.unmerged { color: #6b3fa0; background: #f4eefc; border: 1px solid #d9c8f0; }
.spec-doc .ri-note { border-left: 4px solid #4A5B8C; background: #f5f7fc; padding: 0.8rem 1.1rem; margin: 1.2rem 0 1.8rem; border-radius: 3px; font-size: 0.92rem; }
.spec-doc .ri-note b { color: #1c2030; }
</style>

<div class="spec-doc" markdown="1">


<dl class="status">
  <dt>Document</dt><dd>Software Bill of Behavior</dd>
  <dt>Version</dt><dd>0.0.4</dd>
  <dt>Stage</dt><dd>Proposed</dd>
</dl>


<details class="toc" open>
  <summary>Contents</summary>
  <ol>
    <li><a href="#abstract">Abstract</a></li>
    <li><a href="#1-introduction">1. Introduction</a></li>
    <li style="margin-left:1.2em"><a href="#1-4-generalized-rules">1.4 Generalized rules: the portable set</a></li>
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
    <li><a href="#8-signatures">8. Signatures</a></li>
    <li><a href="#8-security-considerations">9. Security considerations</a></li>
    <li><a href="#9-open-issues">10. Open issues</a></li>
    <li><a href="#10-references">11. References</a></li>
    <li><a href="#appendix-a-change-log">Appendix A. Change log</a></li>
  </ol>
</details>

## Abstract {#abstract .no-rule}

A **Software Bill of Behavior** (SBOB) is a signed, declarative document that states what a piece of software is **intended to do at runtime** — specifically, which Linux capabilities it requires, which files it expects to open, which child processes it spawns, which network destinations it accepts/establishes.
## 1. Introduction {#1-introduction}

### 1.1 What an SBOB is for {#1-1-purpose}

The SBOB expresses, in machine-readable and human-readable form, the **prescriptive intent** of the software author: the set of behaviors the software is designed to exhibit.


The quality of an SBOB can be judged by:
- its ability to distinguish malicious from intentional behavior
- its transferability (portability) across linux-based systems
- its compatibility with standard gitOps tooling
- its usability by humans (time to first detection)



#### 1.1.1 Kernel vs User-Space: Universal Applicability
The SBOB is designed to make runtime security more achievable, not to replace existing approaches such as the Linux Security Modules.


To serve all application languages, an SBOB is based on the lowest common denominator: the Linux Kernel and for high-compatibility, we will rely on the ABI or other long-term-stable elements.

### 1.2 Relationship to existing standards {#1-2-relationship-to-existing-standards}

| Other artifact | What it covers | Relationship to SBOB |
|---|---|---|
| **SBOM** (CycloneDX, SPDX) | static composition (packages, versions, licences) | complementary — solves the question of `ingredients` |
| **RBOM** (in-toto,rapidford)| execution-aware refinement of SBOM | complementary — solves the question of `reachability` |
| **VEX** | Vendor declared exploitability of a CVE|  complementary — solves the question of `CVE relevance` |
| **`ContainerProfile`** | runtime-observed behavior captured by an in-cluster operator | Raw ingredient, this document shows how to abstract it into an SBOB|
| **Seccomp / AppArmor profile** | kernel-enforced syscall and resource policy | adjacent — an SBoB MAY transpile into a seccomp profile |

### 1.3 Conformance language {#1-3-conformance}

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** in this document are to be interpreted as described in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174) when, and only when, they appear in all capitals.

### 1.4 Generalized rules: the portable set {#1-4-generalized-rules}

<div class="ainote">Tool 1 is the reference implementation. The Tool 2, Tool 3 and Tool 4 columns (purple) were compiled by an AI agent on 2026-09-20 from those projects' public rule files and documentation. They have not been verified against a running installation and may be wrong.</div>

Cell legend: Tool 1 cells abbreviate the rule's CEL predicate, prefixed by its event type; the verbatim expressions are in the shipped rule set (`default-rules.yaml`, chart tag `kubescape-operator-1.41.0-duckling16`). **native** = shipped; **generated** = emitted from the SBOB by tooling; **deny-list** = expressible only as an explicit deny of the observed value; **N/A** = no equivalent found in the indexed sources.

#### 1.4.1 Rules that read the SBOB {#1-4-1-profile-rules}

<div class="vendor" markdown="1">

| Generalized rule | SBOB section | Tool 1 | Tool 2 | Tool 3 | Tool 4 |
|---|---|---|---|---|---|
| **Process execution** | `execs[].path` (key `process-execution`) | `exec`: `!was_executed` | `not proc.exepath in (sbob_execs)` | `process[] {path, action: allow}` | deny-list: `data.pathname!=<path>` |
| **Process arguments** | `execs[].args` (key `process-arguments`) | `exec`: `!was_executed_with_args` | `proc.cmdline regex <pattern>` | N/A | N/A |
| **File access** | `opens[].path` (key `file-access`) | `open`: `!was_path_opened` | `not fd.name pmatch (sbob_opens)` | `file[] {filter, recursive}` monitor list | deny-list: `data.pathname!=<path>` |
| **Domain communication** | `egress[].dnsNames` (key `domain-communication`) | `dns`: `!is_domain_in_egress` | N/A | address group per name, egress allow | N/A |
| **Egress traffic** | `egress[]` (key `egress-traffic`) | `network`: `OUTGOING && !in_egress` | `outbound and not fd.sip in (sbob_egress)` | `egress[] {selector, ports, action: allow}` | deny-list: `security_socket_connect` |
| **Ingress traffic** | `ingress[]` (key `ingress-traffic`) | `network`: `HOST && !in_ingress` | `inbound and not fd.cip in (sbob_ingress)` | `ingress[] {selector, ports, action: allow}` | N/A |

</div>

#### 1.4.2 Signature rules; the SBOB allowlists who may perform them {#1-4-2-signature-rules}

These rules fire without an SBOB. The SBOB section for them is `rulePolicies`: per rule, the processes (`processAllowed`, by `comm`) or the whole container (`containerAllowed`) that are intended to perform the action. The engine implements the detection; the SBOB supplies the exemption.

<div class="vendor" markdown="1">

| Generalized rule | SBOB section | Tool 1 | Tool 2 | Tool 3 | Tool 4 |
|---|---|---|---|---|---|
| **Binary not in container image** | `rulePolicies.binary-not-in-image` | `exec`: `upperlayer && !was_executed` | native `Drop and execute new binary in container` | native zero-drift | N/A |
| **Execution from memory** | `rulePolicies.execution-from-memory` | `exec`: `exepath ~ memfd` | native `Fileless execution via memfd_create` | N/A | native `TRC-105` |
| **Execution from shared memory** | `rulePolicies.execution-from-shared-memory` | `exec`: `exepath ~ /dev/shm` | native `Execution from /dev/shm` | generated: `process[] {path: /dev/shm/*, action: deny}` | N/A |
| **Sensitive file access** | `rulePolicies.sensitive-file-access` | `open`: `path ~ /etc/shadow` | native `Read sensitive file untrusted` | generated: `file[] {filter: /etc/shadow, behavior: block_access}` | N/A |
| **Link over sensitive file** | `rulePolicies.link-over-sensitive-file` | `symlink`/`hardlink`: `oldPath ~ shadow` | native `Create Symlink Over Sensitive Files`, `Create Hardlink Over Sensitive Files` | N/A | N/A |
| **Service-account token access** | `rulePolicies.service-account-token-access` | `open`: `path ~ sa token` | N/A | N/A | native `TRC-108` |
| **Procfs environment read** | `rulePolicies.procfs-environment-read` | `open`: `path ~ /proc/*/environ` | native `Read environment variable from /proc files` | N/A | N/A |
| **Kubernetes API access** | `rulePolicies.kubernetes-api-access` | `exec`/`network`: `kubectl`, API addr | native `Contact K8S API Server From Container` | N/A | N/A |
| **Module load** | `rulePolicies.module-load` | `kmod`: `init_module` | native `Linux Kernel Module Injection Detected` | N/A | native `TRC-1017` |
| **eBPF program load** | `rulePolicies.ebpf-program-load` | `bpf`: `cmd == 5` | native `BPF Program Not Profiled` | N/A | N/A |
| **Namespace change** | `rulePolicies.namespace-change` | `unshare`: `pcomm != runc` | native `Change namespace privileges via unshare` | N/A | N/A |
| **Process tracing** | `rulePolicies.process-tracing` | `ptrace`: `true` | native `PTRACE attached to process`, `PTRACE anti-debug attempt` | N/A | native `TRC-103`, `TRC-102` |
| **Dynamic linker hook** | `rulePolicies.dynamic-linker-hook` | `exec`/`open`: `ld hook` | N/A | N/A | native `TRC-107` |
| **SSH connection** | `rulePolicies.ssh-connection` | `ssh`: `dstPort not in [22]` | native `Disallowed SSH Connection Non Standard Port` | partial: suspicious process `ssh` | N/A |
| **Cgroup release_agent write** | `rulePolicies.cgroup-release-agent-write` | N/A | native `Detect release_agent File Container Escapes` | N/A | native `TRC-1010` |
| **Stdio to socket** | `rulePolicies.stdio-to-socket` | N/A | native `Redirect STDOUT/STDIN to Network Connection in Container` | N/A | native `TRC-101` |

</div>

#### 1.4.3 `rulePolicies` in the SBOB {#1-4-3-rulepolicies}

```yaml
spec:
  rulePolicies:
    file-access:
      processAllowed: [logrotate]
    service-account-token-access:
      containerAllowed: true
    module-load:
      processAllowed: [modprobe]
```


## 2. Conformance {#2-conformance}

A **conformant SBOB document** is a (set of) YAML document(s) that:

1. Has the envelope described in §4.1, with `apiVersion`, `kind`, `metadata`, and `spec` populated.
2. Describes exactly one Pod with all ContainerTypes.
3. Populates at least <span class="field">spec.imageID</span>, plus any of the structural sections (§4.3 through §4.8) that apply.
4. If any field uses a wildcard or pattern, that pattern conforms to §5.
5. Distinguishes absent fields (NULL) from explicit-empty fields (NONE) per §5.4 in its YAML form, even when the underlying language binding collapses the two.

A **conformant verifier**:

1. Matches the SBOB name <span class="ri defacto">using a label</span> on the pod
2. Implements every match step in §6 against every section of §4 that the document populates.
3. Treats absent fields (NULL — non-deterministic, implementation-defined posture) and explicit empty-collection fields (NONE — declared zero-activity, hard violation on first observation) **differently** (§5.4).
4. Reports its NULL-handling posture (deny / log-only / learn-mode) at startup so operators know what their absent-field workloads will encounter.
5. Emits drift events keyed by the generalized rule names of §1.4, carrying the engine-specific rule ID alongside the name.

## 3. Document structure {#3-document-structure}

An SBOB document is a single YAML stream containing one Kubernetes-style resource.


```yaml
kind: ContainerProfile
metadata:
  name: <name-unique-to-environment>   # mandatory; the pod label binds to this value
  namespace: <namespace>
spec:
  architectures: [...]
  imageID: <oci-image-with-digest>
  capabilities:   [...]
  endpoints:      [...]
  execs:          [...]
  opens:          [...]
  ingress:        [...]
  egress:         [...]
  rulePolicies:   { ... }
```

One document describes one container. A pod with several containers carries one `ContainerProfile` per container, each bound by its own label value.

## 4. Schema reference {#4-schema-reference}

### 4.1 Envelope {#4-1-envelope}

| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">apiVersion</span> | string | <span class="req">required</span> | |
| <span class="field">kind</span> | string | <span class="req">required</span> | |
| <span class="field">metadata.name</span> | string | <span class="req">required</span> | A short, stable name for the container. |
| <span class="field">metadata.namespace</span> | string | <span class="req">required</span> | Namespace of the workload the profile binds to. |
| <span class="field">metadata.annotations</span> | map | <span class="opt">optional</span> | |
| <span class="field">spec.architectures</span> | list of strings | <span class="opt">optional</span> | Linux architecture tokens for which this SBOB applies (e.g. `amd64`, `arm64`). |
| <span class="field">spec.imageID</span> | string | <span class="req">required</span> | The OCI image reference, ideally pinned by digest. |
| <span class="field">spec.*</span> | sections | <span class="opt">optional</span> | The behavioural sections listed in §4.2. |

### 4.2 Sections {#4-2-container-entry}

All sections sit directly under `spec`. There is no per-container list; init and ephemeral containers get their own `ContainerProfile` documents.

| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">capabilities</span> | list of strings | <span class="opt">optional</span> | See §4.3. |
| <span class="field">endpoints</span> | list of objects | <span class="opt">optional</span> | See §4.4. |
| <span class="field">execs</span> | list of objects | <span class="opt">optional</span> | See §4.5. |
| <span class="field">opens</span> | list of objects | <span class="opt">optional</span> | See §4.6. |
| <span class="field">ingress</span> | list of objects | <span class="opt">optional</span> | See §4.7. highly recommended|
| <span class="field">egress</span> | list of objects | <span class="opt">optional</span> | See §4.7.  highly recommended|
| <span class="field">rulePolicies</span> | map | <span class="opt">optional</span> | See §4.8. |

### 4.3 capabilities {#4-3-capabilities}

A list of Linux capabilities that the workload is permitted to hold. Each entry MUST be a token from the kernel's [`capabilities(7)`](https://man7.org/linux/man-pages/man7/capabilities.7.html) manual page, in upper-case (e.g. `CAP_NET_BIND_SERVICE`).

```yaml
capabilities: [CAP_SETGID, CAP_SETPCAP, CAP_SETUID]
```

A verifier MUST emit a violation if the live process holds any capability not listed. The absence of the field carries a different meaning from explicit empty (`capabilities: []`) — see §5.4.

### 4.4 endpoints {#4-4-endpoints}

A list of HTTP-level endpoints the workload is expected to expose (<span class="field">direction: inbound</span>) or call (<span class="field">direction: outbound</span>).

| Field | Type | Description |
|---|---|---|---|
| <span class="field">endpoint</span> | string |  Pattern of the form `:<port>/<path>`. Each component supports wildcards per §5. |
| <span class="field">methods</span> | list of strings | HTTP verbs (`GET`, `POST`, …) the endpoint accepts or sends. |
| <span class="field">headers</span> | map or null |  Map of `<header-name>: <expected-value-pattern>`.  |
| <span class="field">direction</span> | enum | `inbound` or `outbound`. |

```yaml
endpoints:
- endpoint: ":0/api/data"   # any port, exact path
  methods: [GET, POST]      
  headers: null             # explicit, no extra headers expected
  direction: outbound
```
<span class="ri defacto">The desired degree of specificity in methods and headers is under debate</span> 

### 4.5 execs {#4-5-execs}

A list of processes that the workload is permitted to spawn (via `execve`).

| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">path</span> | string | <span class="req">required</span> | Absolute filesystem path of the executable. Wildcards per §5. |
| <span class="field">args</span> | list of strings | <span class="opt">optional</span> | Argument vector. Each entry is either a literal token or one of the exec-arg wildcard tokens defined in §5: `⋯` (DynamicIdentifier) matches exactly one argument position in a path, `⋯⋯` (ExecArgsWildcard) matches zero-or-more consecutive arguments. `*` is **not** an argument wildcard — it matches literally inside `args`. A token containing `⋯` is split on `/` and `⋯` MUST equal a whole segment; a prefix that stops mid-segment (`/a/b/elasticsearch⋯`, `--config=⋯`) matches nothing and is rejected by `bobctl validate`. |

```yaml
execs:
- path: /usr/sbin/apache2          # exact installation path
  args: [/usr/sbin/apache2, '⋯⋯']  # anchored argv[0] then any tail
- path: /⋯/apache2                 # relative installation path
  args: [/⋯/apache2, '⋯⋯']         
```




### 4.6 opens {#4-6-opens}

A list of file paths the workload is permitted to open, with the open-flag combinations under which it is permitted to open them.

| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">path</span> | string | <span class="req">required</span> | Filesystem path, absolute. Wildcards per §5: `⋯` (U+22EF, DynamicIdentifier) matches exactly one segment; `*` (WildcardIdentifier) matches zero-or-more segments mid-path and one-or-more segments when trailing.  |
| <span class="field">flags</span> | list of strings | <span class="req">required</span> | Subset of `O_RDONLY`, `O_WRONLY`, `O_RDWR`, `O_CREAT`, `O_TRUNC`, `O_APPEND`, `O_CLOEXEC`, `O_NONBLOCK`, `O_DIRECTORY`, `O_NOFOLLOW`, `O_PATH`. See Kernel documentation |

```yaml
opens:
- flags: [O_RDONLY, O_WRONLY, O_CREAT]
  path: /var/log/apache2/*       # any descendant (1+ segments under, never the bare dir)
- flags: [O_RDONLY]
  path: /etc/resolv.conf         # exact
- flags: [O_RDONLY, O_WRONLY]
  path: /opt/*/vendor/app/node/*  # mid-path * is 0+ segments (§5.1), trailing * is 1+ segments
- flags: [O_RDONLY, O_WRONLY]
  path: /opt/⋯/vendor/app/node/*  # mid-path ⋯ is 1 segments (§5.1), trailing * is 1+ segments
```

### 4.7 egress and ingress {#4-7-egress}

Two parallel lists the workload is permitted to exchange traffic with:

- <span class="field">egress[]</span> — destinations the workload is permitted to **dial** (it initiates the connection)
- <span class="field">ingress[]</span> — peers the workload is permitted to **accept connections from** (the peer initiates)

Both lists carry entries of the same  shape (table below) and are evaluated by symmetric verifier paths.

The two stanzas mirror the Kubernetes [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/) model as closely as the runtime view allows: the same two directions, the same `podSelector` / `namespaceSelector` / `ipBlock` peer vocabulary, and the same `ports[]` shape. An SBOB SHOULD be expressible as a NetworkPolicy and a NetworkPolicy SHOULD be expressible as the observed-intent half of an SBOB, so that a declared profile and an enforced policy can be diffed against one another. Where the two diverge, the divergence is stated: an SBOB additionally carries `dnsNames` (a query name the workload resolved, which NetworkPolicy cannot express) and records observed addresses rather than admission-time selectors.




| Field | Type | Required | Description |
|---|---|---|---|
| <span class="field">identifier</span> | string | <span class="opt">optional</span> | Free-form short name to refer to this entry in `rulePolicies` or in cross-document references. |
| <span class="field">type</span> | enum | <span class="opt">optional</span> | `external` (default) or `internal`. |
| <span class="field">ipAddresses</span> | list of strings | <span class="opt">optional</span> | **New in v0.0.2.** Each entry is one of: an IPv4/IPv6 literal, a CIDR (`10.0.0.0/8`, `2001:db8::/32`), or the `*` sentinel meaning "any IP" (sugar for `0.0.0.0/0`+`::/0`). The verifier matches the live observed IP against each entry per §5.7; an observation that matches ANY entry passes. Empty list `[]` is NONE per §5.4 (no IP traffic intended). |
| <span class="field">dnsNames</span> | list of strings | <span class="opt">optional</span> | Set of DNS names (FQDN form with trailing dot RECOMMENDED) the verifier accepts. Each entry MAY use the wildcard tokens defined in §5.8: leading `*.<suffix>` (RFC 4592, exactly one label), mid `<a>.⋯.<b>` (DynamicIdentifier, exactly one label), or trailing `<prefix>.*` (one or more labels). Strings without these tokens are byte-equality. Replaces the deprecated single `dns` field. |
| <span class="field">podSelector</span> | label selector | <span class="opt">optional</span> | Cluster-internal traffic: matches pods bearing these labels. |
| <span class="field">namespaceSelector</span> | label selector | <span class="opt">optional</span> | Cluster-internal traffic: matches pods in namespaces bearing these labels. |
| <span class="field">ports[]</span> | list of objects | <span class="req">required</span> | Each entry: `name` (`<protocol>-<port>` e.g. `TCP-443`), `protocol` (`TCP`/`UDP`/`SCTP`), `port` (uint16, nullable per §5.4). |

```yaml
spec:
  egress:
  - identifier: stripe-api
    type: external
    ipAddresses: ["162.0.217.171/32"]
    dnsNames: ["*.api.stripe.com."]
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
    ipAddresses: ["10.244.0.0/16"]      # TBD should there be a K8S-SVC-CIDR etc placeholder
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



### 4.8 rulePolicies {#4-8-policybinding}

A map keyed by a **generalized rule name** (§1.4, kebab case) whose value says who is intended to perform that action. It is the SBOB's allowlist for the signature rules of §1.4.2; the rules of §1.4.1 read their own sections and ignore it.

**Key:** the generalized rule name (`namespace-change`, `module-load`, ...). The verifier maps it to its engine rule ID and carries both in the drift event.

**Value:**

| Field | Type | Description |
|---|---|---|
| <span class="field">processAllowed</span> | list of strings | Process `comm` names that ARE intended to perform the action. |
| <span class="field">containerAllowed</span> | bool | `true`: any process in the container may perform the action. `false` is identical to omitting the entry. |

```yaml
rulePolicies:
  namespace-change:
    processAllowed: [runc]         # only runc may unshare
  file-access:
    processAllowed: [logrotate]
```

An entry for a rule the engine does not honour (§1.4.3) has no effect and MUST NOT be treated as a deny.

## 5. Pattern and wildcard semantics {#5-pattern-semantics}

Relevant to abstract exact kernel events into a `semantic` and `portable` description of `intent`.

### 5.1 Path wildcards `*` and `⋯` {#5-1-path-star}

Two wildcard tokens are defined for path components.

**`⋯` (U+22EF) — exactly one segment.** A single Unicode codepoint, NOT three ASCII periods. Matches one full path segment (zero-or-more characters that do not contain `/`). Spelt distinctly to avoid colliding with accidential use of globs.

**`*` (PathWildcard) — variable arity, position-dependent.**

* When `*` appears **mid-path** (i.e. there are more segments after it), it matches **zero or more consecutive segments**.
* When `*` appears **trailing** (last segment of the pattern), it matches **one or more remaining segments** — never zero.

| Pattern | Matches | Does not match |
|---|---|---|
| `/etc/⋯` | `/etc/passwd`, `/etc/hosts` | `/etc/`, `/etc/ssh/sshd_config`, `/etc/ssl/certs/ca.pem` |
| `/etc/*` (trailing) | `/etc/passwd`, `/etc/ssh/sshd_config` | `/etc`, `/etc/` |
| `/a/*/b` (mid) | `/a/b`, `/a/x/b`, `/a/x/y/b` | `/a/x/c` |
| `/a/⋯/b` | `/a/x/b` | `/a/b`, `/a/x/y/b` |





### 5.3 Exec-argument wildcards {#5-3-exec-arg-wildcards}

The `*` and `⋯` tokens of §5.1 are **path** wildcards. An `exec` entry's `args` vector uses

* **`⋯⋯` (WildcardExecs) — zero or more arguments.** Absorbs a run of consecutive argv entries, including none: `[/bin/foo, '⋯⋯']` matches `/bin/foo` with any tail (or none), whereas `[/bin/foo]` matches only the bare invocation with no arguments.

`*` is **not** an argument wildcard — inside `args` it is a literal asterisk.



### 5.4 Absent (NULL) vs explicit-empty (NONE) {#5-4-empty-vs-absent}

TBD





### 5.6 Port wildcards {#5-6-port-wildcard}

Ports appear in two contexts curretly

* **<span class="field">endpoints[].endpoint</span> string** — for http, use the integer 0 to express the intent of `ANY PORT`. `:0/api/data`

* **<span class="field">egress[].ports[].port / ingress[].ports[].port</span>** — an absent `port` (null) means ANY PORT; an omitted `ports` stanza means any port on that peer. A populated `ports[]` matches only its literal (protocol, port) entries. The RFC 6335 numeric-`0` sentinel does NOT apply at this field.



### 5.7 IP address matching {#5-7-ip}

Matches an observed IP against an
<span class="field">ipAddresses[]</span> list using these forms in
order. Each entry is one of:

| Form | Example | Semantics |
|---|---|---|
| **IPv4 / IPv6 literal** | `162.0.217.171`, `2001:db8::1` | Byte-equality on the parsed IP. The textual canonicalisation is the verifier's responsibility (e.g. `2001:db8::1` and `2001:0db8:0000:0000:0000:0000:0000:0001` MUST compare equal). |
| **CIDR** | `10.0.0.0/8`, `2001:db8::/32` | The verifier parses the entry with `net.ParseCIDR` (or equivalent) once and stores the `*net.IPNet`; matches via `IPNet.Contains(observedIP)`. |
| **\*** | `*` | `0.0.0.0/0` (RFC 4632, all IPv4) and `::/0` (RFC 4291, all IPv6). Matches any observed IP. |



### 5.8 DNS name matching {#5-8-network-wildcards}

Matches an observed DNS name (from the workload's own `getaddrinfo` / `res_query` event see §8.2) against the
<span class="field">dnsNames[]</span> 

| Form | Position | Semantics | Example | Matches | Doesn't |
|---|---|---|---|---|---|
| Literal | — | byte-equality after trailing-dot normalisation | `api.stripe.com.` | `api.stripe.com.`, `api.stripe.com` | `v1.api.stripe.com.` |
| `*.<suffix>` | leading | RFC 4592 — **exactly one** label before `<suffix>` | `*.example.com.` | `api.example.com.`, `webhook.example.com.` | `v1.api.example.com.`, `example.com.` (apex), `.example.com.` (empty label) |
| `<a>.⋯.<b>` | mid | DynamicIdentifier — **exactly one** label between `<a>` and `<b>` | `svc.⋯.kubernetes.io.` | `svc.kube-system.kubernetes.io.` | `svc.kubernetes.io.`, `svc.a.b.kubernetes.io.` |
| `<prefix>.*` | trailing | WildcardIdentifier — **one or more** labels after `<prefix>` (never zero) | `mycorp.com.*` | `mycorp.com.api.`, `mycorp.com.api.v1.` | `mycorp.com.` (apex match — zero rejected) |

#### Rationale for the token choices

* **Leading `*` = exactly one label** is RFC 4592
* **Mid-label `*` is non-standard** — bind/coredns reject it, cilium uses regex, Calico has its own glob form. v0.0.2 deliberately uses the project's existing `⋯` token for the mid position, so the wire format never claims RFC 4592 compliance for a non-standard shape and producers' intent is unambiguous.
* **Trailing `*` = one-or-more** matches the path semantic in §5.1 — a trailing `*` MUST consume at least one label, never zero, so `mycorp.com.*` does not silently allow access to the bare apex.



#### Apex matching

`*.example.com.` does NOT match the bare apex `example.com.` — same defensive rule as path-side trailing-`*`. Producers that intend the apex MUST list `example.com.` as a separate `dnsNames` entry. Same rule for `<prefix>.*` trailing form.

#### Empty / `**` rejection

A `dnsNames[i]` containing `**` (recursive wildcard) MUST be rejected

#### List semantics

The verifier matches each observed name against EVERY entry in `dnsNames`; an observation that matches ANY entry passes. Entries are unordered. A NONE list (`dnsNames: []`) per §5.4 means "no DNS traffic intended" — any DNS observation is a hard violation.



## 6. Verifier algorithm {#6-verifier-algorithm}

WIP

<!-- A conformant verifier consumes:

1. A signed SBoB document for the container under check.
2. A live observation stream from a runtime sensor (kubescape node-agent,
   Falco, Tetragon, or equivalent) over a configured window. -->



<!-- For each container in <span class="field">spec.containers[]</span> AND
its own `ingress[]` / `egress[]` (§4.7), same document:

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
   in the same ContainerProfile, route by direction:
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
kind: ContainerProfile
metadata:
  name: payment-app
  namespace: shop
  annotations: {kubescape.io/managed-by: User}
spec:
  imageID: ghcr.io/billofbehavior/payment-app@sha256:f6c18b0...
```



### 7.2 Full example with wildcards {#7-2-full}

```yaml
kind: ContainerProfile
metadata:
  name: payment-app
  namespace: shop
  annotations:
  kubescape.io/managed-by: User
  sbob.io/spec-version: "0.0.4"
spec:
  architectures: [amd64]
  imageID: ghcr.io/billofbehavior/payment-app@sha256:f6c18b0...
  capabilities: [CAP_SETGID, CAP_SETPCAP, CAP_SETUID]
  endpoints:
  - endpoint: ":0/api/data"     # any port, exact path
    methods: [GET, POST]
    headers: null               # explicit no extra headers
    direction: outbound
  execs:
    path: /usr/sbin/apache2                  # intended exact path
  - args: [/usr/sbin/apache2, '⋯⋯']          # zero-or-more trailing args
  - path: /usr/lib/postgresql/⋯/bin/postgres # version number does NOT matter 
    args: ["postgres"]
  - path: /usr/lib/postgresql/16/bin/initdb  # version number DOES matter
    args: ["initdb"]
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
    dnsNames:                          # supersedes the deprecated single dns field
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
      - "svc.⋯.cluster.local."         # leaves NAMESPACE label open to user
    ports:
    - {name: UDP-53, protocol: UDP, port: 53}
  rulePolicies:
    namespace-change:            # §1.4.2 (kubescape R1006, Falco "Change namespace privileges via unshare")
      processAllowed: [runc]     # only runc may unshare
    module-load:                 # §1.4.2 (kubescape R1002, Falco "Linux Kernel Module Injection Detected", Tracee TRC-1017)
      containerAllowed: false    # same as omitting the entry; shown for clarity
```

## 8. Signatures {#8-signatures}

WIP

## 9. Security considerations {#8-security-considerations}
<!-- 
### 8.1 Wildcards as policy weakening {#8-1-wildcard-weakening}



### 8.2 DNS spoofing of egress declarations {#8-2-dns-spoofing}

A verifier that resolves <span class="field">egress[].dnsNames</span> at
verification time would be exposed to local DNS spoofing — a compromised
resolver could shrink-wrap the verifier's accept-set to whatever the
attacker wanted. v0.0.4 verifiers MUST NOT call DNS at evaluation time;
they MUST evaluate DNS-name observations against the
<span class="field">dnsNames</span> list as **string equality on the
observed query name**, taken from the workload's own DNS query event
(typically captured by the runtime sensor at the `getaddrinfo` /
`res_query` boundary). IP-address observations are matched separately
against <span class="field">ipAddress</span> per §5.7. 

### 8.3 Capability surface {#8-3-capability-surface}

-->
## 10. Open issues 

- Generalisation of rules: names and verbs
- Notations for common network-masks such as `{pod_cidr}` to be discoverable/replaceable by bobctl
- Implementation and example of bundling and signing of bundles
- Support for pod-lifecycle
- Guidance on `useful syscalls`

<!-- 1. **Recursive wildcard `**`.** v0.0.3 covers multi-segment matching
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
   listeners and UNIX domain sockets are not addressed in v0.0.3.
5. **Profile composition.** A single SBoB document with multiple
   containers is supported, but the cross-container relationships
   (init / sidecar / main) are not. v0.0.2 may add an `ordering` field.
6. **Negative declarations.** Currently the SBoB declares the *positive*
   set of permitted behaviors. A `denyOpens[]` style negative section is
   under discussion; the trade-off is verifier complexity.
7. **Linter conformance.** A separate linter spec (and a `bobctl lint`
   subcommand) is planned but out of scope here.
8. **Binding-side NULL/NONE preservation.** The <span class="vendorref">kubescape-derived</span> Go
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

## 11. References {#10-references}

* RFC 2119, *Key words for use in RFCs to Indicate Requirement Levels*. <https://www.rfc-editor.org/rfc/rfc2119>
* RFC 8174, *Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words*. <https://www.rfc-editor.org/rfc/rfc8174>
* `capabilities(7)`, Linux manual page. <https://man7.org/linux/man-pages/man7/capabilities.7.html>
* `open(2)`, Linux manual page. <https://man7.org/linux/man-pages/man2/open.2.html>
* RFC 6335, *Internet Assigned Numbers Authority (IANA) Procedures for the Management of the Service Name and Transport Protocol Port Number Registry* — note on port `0`. <https://www.rfc-editor.org/rfc/rfc6335>
* <span class="vendorref">kubescape `ContainerProfile` CRD</span>, schema source. <https://github.com/kubescape/storage>
* SBoB stack-profile extension, draft v0.0.3. [`spec-stackprofile-v0.0.1`](../drafts/spec-stackprofile-v0.0.1/)

## Appendix A. Change log {#appendix-a-change-log}

| Date | Version | Note |
|---|---|---|
| 2026-05-04 | 0.0.1 | Initial draft. |
| 2026-09-20 | 0.0.4 | **Document syntax.** One document per container, flat `spec` (no `containers[]`), `imageID` at top level, `metadata.namespace` plus a provenance annotation, one binding label on the pod. §4.8 renamed `rulePolicies`, keyed by generalized rule name (§1.4), values `processAllowed` / `containerAllowed`. §4.5 whole-segment `⋯` rule stated. §1.4 generalized rules added. §5.6 port semantics stated. §6 reads `ingress[]` / `egress[]` from the same document. |
| 2026-05-16 | 0.0.3 | **Spec ↔ code alignment pass.** §4.1 kind spelling corrected to `NetworkNeighborhood` (American — matches CRD, tooling, CI). §4.2 container-type field removed; replaced with a description of the kubescape PodSpec-style three-list layout (`spec.containers[]` / `spec.initContainers[]` / `spec.ephemeralContainers[]`). §4.4 headers entry sharpened with an explicit TODO about the `json.RawMessage` + `omitempty` binding collapsing NULL/NONE — workaround (`headersIntent` enum or custom unmarshaller) deferred to v0.0.2. §4.5 execs entry gains a TODO about admission-time enforcement of `path` REQUIRED (current CRD tags it `opt` for binding reasons). §4.8 rewritten to match the in-code `rulePolicies` field name + engine-rule-ID key + boolean `containerAllowed` value; the canonical-action-verb registry from Appendix B is retained as a v0.0.2 goal rather than a current normative wire format. §5.6 split into two rules: endpoint-string `:0` wildcard (unchanged), and a new explicit rule that `NetworkNeighbor.ports[].port` uses null-pointer = "any port" (the RFC 6335 numeric-`0` sentinel does NOT apply at this field). §5.3 exec-argument wildcards defined: `⋯⋯` (ExecArgsWildcard) matches zero-or-more args, `⋯` (DynamicIdentifier) exactly one; `*` is opens/path-only and matches literally inside `args`. Removed a non-normative subsection that did not reflect the implementation. |
| 2026-05-10 | 0.0.2 | **Network wildcards landed.** §5.7 IP matching promoted from TODO to normative — `ipAddresses []string` (new plural) accepts IPv4/IPv6 literals, CIDRs (`net.ParseCIDR` + `IPNet.Contains`), and `*` sentinel for any. Singular `ipAddress` deprecated, kept for back-compat. §5.8 DNS matching: leading `*.<suffix>` (RFC 4592, exactly one label), mid `<a>.⋯.<b>` (DynamicIdentifier, exactly one), trailing `<prefix>.*` (one or more, never zero). `**` recursive form rejected — reserved for v0.0.3. §4.7 retitled "egress and ingress" — both directions are first-class, share the same `NetworkNeighbor` shape, and consume the same matcher implementation; example extended with two `ingress[]` entries (CIDR-based LB-probe + selector-based prometheus-scrape). §6.2 algorithm step renamed "network neighbour check" with direction-aware routing (`pktType=='OUTGOING'`→`egress[]`, `pktType=='INCOMING'`→`ingress[]`) and a new `net.ingress_unexpected` drift verb. §7.2 example demonstrates IPv6 CIDR + leading-`*` DNS + mid-`⋯` Kubernetes-service-FQDN form. |
</div>
/spec-doc
